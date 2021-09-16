#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users,mail
from google.appengine.api import urlfetch
import logging
import math
import datetime
from datetime import timedelta
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

#Use of lambda
#succ = lambda n: lambda f: lambda x: f(n(f)(x))

def BulkSMSHandler():

    from mysms import MessageSchedule, Messages, SMSContacts, Groups, SMSAccount, SMSPortalVodacom,DeliveryReport, SMSPortalBudget, ClickSendSMSPortal
    from myTwilio import MyTwilioPortal
    from accounts import Accounts
    Today = datetime.datetime.now()
    thisDate = Today.date()
    thisTime = Today.time()

    findRequest = MessageSchedule.query(MessageSchedule.strStatus == "Scheduled",
                                        MessageSchedule.strStartDate == thisDate,
                                        MessageSchedule.strStartTime >= thisTime)
    thisMessageScheduleList = findRequest.fetch()

    if len(thisMessageScheduleList) > 0:
        logging.info("There are messages scheduled")

    for thisSchedule in thisMessageScheduleList:
        findRequest = Messages.query(Messages.strMessageID == thisSchedule.strMessageID,
                                     Messages.strSubmitted == False)
        thisMessageList = findRequest.fetch()

        if len(thisMessageList) > 0:
            thisMessage = thisMessageList[0]
        else:
            thisMessage = Messages()

        findRequest = Groups.query(Groups.strGroupID == thisMessage.strGroupID)
        thisGroupList = findRequest.fetch()

        if len(thisGroupList) > 0:
            thisGroup = thisGroupList[0]
        else:
            thisGroup = Groups()

        findRequest = SMSAccount.query(SMSAccount.strOrganizationID == thisGroup.strOrganizationID)
        thisSMSAccountList = findRequest.fetch()

        if len(thisSMSAccountList) > 0:
            thisSMSAccount = thisSMSAccountList[0]

        else:
            thisSMSAccount = SMSAccount()
            thisSMSAccount.writeOrganizationID(strinput=thisGroup.strOrganizationID)
            thisSMSAccount.put()

        findRequest = SMSContacts.query(SMSContacts.strGroupID == thisMessage.strGroupID)
        thisContactsList = findRequest.fetch()

        ReceipientList = []
        for thisContact in thisContactsList:
            if not (thisContact.strCellNumber == None):
                ReceipientList.append(thisContact.strCellNumber)

        if thisSchedule.strNotifyOnStart == True:
            findRequest = Accounts.query(Accounts.uid == thisSchedule.uid)
            thisAccountsList = findRequest.fetch()

            if len(thisAccountsList) > 0:
                thisAccounts = thisAccountsList[0]
                if thisAccounts.cell in ReceipientList:
                    pass
                else:
                    ReceipientList.append(thisAccounts.cell)

        if thisSMSAccount.strTotalSMS >= len(ReceipientList):
            if thisSMSAccount.strUsePortal == "Vodacom":
                findRequest = SMSPortalVodacom.query()
                thisVodaList = findRequest.fetch()

                if len(thisVodaList) > 0:
                    thisVoda = thisVodaList[0]
                else:
                    thisVoda = SMSPortalVodacom()
                    thisVoda.put()

                if thisVoda.CronSendMessages(strCellNumberList=ReceipientList,
                                             strMessage=thisMessage.strMessage,
                                             strAccountID=thisSMSAccount.strOrganizationID):
                    thisSchedule.writeStatus(strinput="Completed")
                    thisSchedule.put()
                    thisMessage.writeDateSubmitted(strinput=thisDate)
                    thisMessage.writeTimeSubmitted(strinput=thisTime)
                    thisMessage.writeSubmitted(strinput=True)
                    thisMessage.put()
                    for StrCell in ReceipientList:
                        thisDeliveryReport = DeliveryReport()
                        thisDeliveryReport.writeMessageID(strinput=thisMessage.strMessageID)
                        thisDeliveryReport.writeGroupID(strinput=thisMessage.strGroupID)
                        thisDeliveryReport.writeOrganizationID(strinput=thisSMSAccount.strOrganizationID)
                        thisDeliveryReport.writeReference(strinput="voda")
                        thisDeliveryReport.writeCell(strinput=StrCell)
                        thisDeliveryReport.writeDate(strinput=thisDate)
                        thisDeliveryReport.writeTime(strinput=thisTime)
                        thisDeliveryReport.writeDelivered(strinput=True)
                        thisDeliveryReport.put()
                    logging.info("Bulk SMS Schedule executed")

            elif thisSMSAccount.strUsePortal == "Budget":
                findRequest = SMSPortalBudget.query()
                thisBudgetPortalList = findRequest.fetch()

                if len(thisBudgetPortalList) > 0:
                    thisPortal = thisBudgetPortalList[0]

                    strTotalDelivered = 0

                    for thisContact in ReceipientList:
                        ref = thisPortal.SendMessage(strMessage=thisMessage.strMessage,
                                                     strMessageID=thisMessage.strMessageID, strCell=thisContact)
                        ref = ref.strip()
                        if (ref != None) and (ref != ""):
                            thisDeliveryReport = DeliveryReport()
                            thisDeliveryReport.writeMessageID(strinput=thisMessage.strMessageID)
                            thisDeliveryReport.writeGroupID(strinput=thisMessage.strGroupID)
                            thisDeliveryReport.writeOrganizationID(strinput=thisSMSAccount.strOrganizationID)
                            thisDeliveryReport.writeReference(strinput=ref)
                            thisDeliveryReport.writeCell(strinput=thisContact)
                            thisDeliveryReport.writeDate(strinput=thisDate)
                            thisDeliveryReport.writeTime(strinput=thisTime)
                            thisDeliveryReport.writeDelivered(strinput=True)
                            thisDeliveryReport.put()
                            strTotalDelivered += 1

                    thisSchedule.put()
                    thisMessage.writeDateSubmitted(strinput=thisDate)
                    thisMessage.writeTimeSubmitted(strinput=thisTime)
                    thisMessage.writeSubmitted(strinput=True)
                    thisMessage.put()

                    thisSMSAccount.writeTotalSMS(strinput=(thisSMSAccount.strTotalSMS - strTotalDelivered))
                    thisSMSAccount.put()

            elif thisSMSAccount.strUsePortal == "ClickSend":
                findRequest = ClickSendSMSPortal.query()
                thisClickSendPortalList = findRequest.fetch()
                if len(thisClickSendPortalList) > 0:
                    thisClickSend = thisClickSendPortalList[0]
                else:
                    thisClickSend = ClickSendSMSPortal()

                strTotalDelivered = 0

                for thisContact in ReceipientList:
                    ref = thisClickSend.SendSMS(strCell=thisContact, strMessage=thisMessage.strMessage)

                    if (ref != None):
                        thisDeliveryReport = DeliveryReport()
                        thisDeliveryReport.writeMessageID(strinput=thisMessage.strMessageID)
                        thisDeliveryReport.writeGroupID(strinput=thisMessage.strGroupID)
                        thisDeliveryReport.writeOrganizationID(strinput=thisSMSAccount.strOrganizationID)
                        thisDeliveryReport.writeReference(strinput=ref)
                        thisDeliveryReport.writeCell(strinput=thisContact)
                        thisDeliveryReport.writeDate(strinput=thisDate)
                        thisDeliveryReport.writeTime(strinput=thisTime)
                        thisDeliveryReport.writeDelivered(strinput=True)
                        thisDeliveryReport.put()
                        strTotalDelivered += 1

                thisSchedule.put()
                thisMessage.writeDateSubmitted(strinput=thisDate)
                thisMessage.writeTimeSubmitted(strinput=thisTime)
                thisMessage.writeSubmitted(strinput=True)
                thisMessage.put()

                thisSMSAccount.writeTotalSMS(strinput=(thisSMSAccount.strTotalSMS - strTotalDelivered))
                thisSMSAccount.put()

            elif thisSMSAccount.strUsePortal == "Twilio":
                findRequest = MyTwilioPortal.query()
                thisTwilioList = findRequest.fetch()

                if len(thisTwilioList) > 0:
                    thisTwilio = thisTwilioList[0]
                else:
                    thisTwilio = MyTwilioPortal()

                strTotalDelivered = 0

                for thisContact in ReceipientList:
                    ref = thisTwilio.sendSMS(strTo=thisContact, strFrom=thisTwilio.strMySMSNumber,
                                             strMessage=thisMessage.strMessage)

                    if (ref != None):
                        thisDeliveryReport = DeliveryReport()
                        thisDeliveryReport.writeMessageID(strinput=thisMessage.strMessageID)
                        thisDeliveryReport.writeGroupID(strinput=thisMessage.strGroupID)
                        thisDeliveryReport.writeOrganizationID(strinput=thisSMSAccount.strOrganizationID)
                        thisDeliveryReport.writeReference(strinput=ref)
                        thisDeliveryReport.writeCell(strinput=thisContact)
                        thisDeliveryReport.writeDate(strinput=thisDate)
                        thisDeliveryReport.writeTime(strinput=thisTime)
                        thisDeliveryReport.writeDelivered(strinput=True)
                        thisDeliveryReport.put()
                        strTotalDelivered += 1

                thisSchedule.put()
                thisMessage.writeDateSubmitted(strinput=thisDate)
                thisMessage.writeTimeSubmitted(strinput=thisTime)
                thisMessage.writeSubmitted(strinput=True)
                thisMessage.put()

                thisSMSAccount.writeTotalSMS(strinput=(thisSMSAccount.strTotalSMS - strTotalDelivered))
                thisSMSAccount.put()


def BulkEmailHandler():
    pass


def SystemStatusHandler():
    pass


def AdvertContactsHandler():

    from advertise import OurContacts
    from mysms import SMSContacts
    from surveys import SurveyContacts

    findRequest = SMSContacts.query()
    thisSMSContactsList = findRequest.fetch()

    for thisSMSContact in thisSMSContactsList:
        findRequest = OurContacts.query(OurContacts.cell == thisSMSContact.strCellNumber)
        thisOurContactsList = findRequest.fetch()

        if len(thisOurContactsList) > 0:
            pass
        else:
            thisOurContact = OurContacts()
            thisOurContact.writeSurname(strinput=thisSMSContact.surname)
            thisOurContact.writeNames(strinput=thisSMSContact.names)
            thisOurContact.writeCell(strinput=thisSMSContact.strCellNumber)
            thisOurContact.writeEmail(strinput="example@example.com")
            thisOurContact.writeOurContactID(strinput=thisOurContact.CreateContactID())
            thisOurContact.put()

    # TODO-NOTE this might be a problem when there is too much contacts on the database in which case we might
    # TODO- have to do this separately

    findRequest = SurveyContacts.query()
    thiSurveyContactList = findRequest.fetch()

    for thisContact in thiSurveyContactList:

        findRequest = OurContacts.query(OurContacts.cell == thisContact.cell)
        thisOurContactsList = findRequest.fetch()

        if len(thisOurContactsList) > 0:
            pass
        else:
            thisOurContact = OurContacts()
            thisOurContact.writeNames(strinput=thisContact.strName)
            thisOurContact.writeSurname(strinput=thisContact.surname)
            thisOurContact.writeCell(strinput=thisContact.cell)
            thisOurContact.writeEmail(strinput="example@example.com")
            thisOurContact.writeOurContactID(strinput=thisOurContact.CreateContactID())
            thisOurContact.put()


def SendAdvertsHandler():

    from advertise import OurContacts, Advert, Stats, SentReport, Orders
    from mysms import SMSPortalBudget

    vstrThisDate = datetime.datetime.now()
    strThisDate = vstrThisDate.date()
    strThisTime = datetime.time(hour=vstrThisDate.hour, minute=vstrThisDate.minute, second=vstrThisDate.second)
    findRequest = Orders.query(Orders.strRunOrder == True, Orders.strFullyPaid == True,
                               Orders.strOrderStartDate == strThisDate, Orders.strOrderStartTime >= strThisTime)
    thisOrdersList = findRequest.fetch()

    findRequest = OurContacts.query()
    thisOurContactList = findRequest.fetch()

    findRequest = SMSPortalBudget.query()
    thisPortalBudgetList = findRequest.fetch()
    if len(thisPortalBudgetList) > 0:
        thisPortalBudget = thisPortalBudgetList[0]
    else:
        thisPortalBudget = SMSPortalBudget()
    i = 0
    j = 0
    for thisOrder in thisOrdersList:
        findRequest = Advert.query(Advert.advert_id == thisOrder.advert_id)
        thisAdvertList = findRequest.fetch()
        if len(thisAdvertList) > 0:
            thisAdvert = thisAdvertList[0]
            for i in range(thisOrder.strTotalSMS):
                if i < len(thisOurContactList):
                    try:
                        thisContact = thisOurContactList[i]
                        ref = thisPortalBudget.SendCronMessage(strMessage=thisAdvert.advert,
                                                               strCell=thisContact.cell)
                        thisSentReport = SentReport()
                        thisSentReport.writeCell(strinput=thisContact.cell)
                        thisSentReport.writeOrderID(strinput=thisOrder.order_id)
                        thisSentReport.writeAdvertID(strinput=thisOrder.advert_id)
                        # thisSentReport.writeMessageStatus(strinput=thisPortalBudget.CheckMessageStatusByCell(cell=thisContact.cell))
                        # Check The Message status of all sent messages through a separate function
                        thisSentReport.writeAdvertSent(strinput=True)
                        thisSentReport.writeMessageReference(strinput=ref)
                        vstrThisDate = datetime.datetime.now()
                        strThisDate = vstrThisDate.date()
                        strThisTime = datetime.time(hour=vstrThisDate.hour, minute=vstrThisDate.minute,
                                                    second=vstrThisDate.second)
                        thisSentReport.writeDateSent(strinput=strThisDate)
                        thisSentReport.writeTimeSent(strinput=strThisTime)
                        thisSentReport.put()
                    except:
                        pass
                else:
                    j += 1

            thisOrder.writeRunOrder(strinput=False)
            thisOrder.writeOrderCompleted(strinput=True)
            thisOrder.put()

            thisAdvert.writeAdvertStatus(strinput="Completed")
            thisAdvert.put()
            thisStats = Stats()
            thisStats.writeAdvertID(strinput=thisAdvert.advert_id)
            thisStats.writeOrderID(strinput=thisOrder.order_id)
            thisStats.writeTotalSent(strinput=i - j)
            thisStats.writeTotalRemaining(strinput=j)
            thisStats.put()

    if i > 500:
        thisPortalBudget.SendCronMessage(strMessage="Sent Adverts to : " + str(i) + " Clients",
                                         strCell="0790471559")
        thisPortalBudget.SendCronMessage(strMessage="Non Delivered Adverts Total : " + str(i),
                                         strCell="0790471559")

    thisPortalBudget.writeAvailableCredit(strinput=thisPortalBudget.CheckCredits())
    thisPortalBudget.put()


def SendAdvertCreditHandler():

    from advertise import OurContacts, Advert, Stats, SentReport, Orders
    from mysms import SMSPortalBudget, SMSPortalVodacom,ClickSendSMSPortal
    from myTwilio import MyTwilioPortal
    import random

    findRequest = OurContacts.query()
    thisOurContactList = findRequest.fetch()


    findRequest = SMSPortalBudget.query()
    thisPortalBudgetList = findRequest.fetch()

    if len(thisPortalBudgetList) > 0:
        thisPortalBudget = thisPortalBudgetList[0]
    else:
        thisPortalBudget = SMSPortalBudget()

    findRequest = SMSPortalVodacom.query()
    thisPortalVodacomList = findRequest.fetch()
    if len(thisPortalVodacomList) > 0:
        thisPortalVodacom = thisPortalVodacomList[0]
    else:
        thisPortalVodacom = SMSPortalVodacom()

    findRequest = ClickSendSMSPortal.query()
    thisClickSendPortalList = findRequest.fetch()

    if len(thisClickSendPortalList) > 0:
        thisClickSendPortal = thisClickSendPortalList[0]
    else:
        thisClickSendPortal = ClickSendSMSPortal()

    findRequest = MyTwilioPortal.query()
    thisTwilioPortalList = findRequest.fetch()

    if len(thisTwilioPortalList) > 0:
        thisTwilioPortal = thisTwilioPortalList[0]
    else:
        thisTwilioPortal = MyTwilioPortal()



    vstrThisDate = datetime.datetime.now()
    strThisDate = vstrThisDate.date()
    strThisTime = datetime.time(hour=vstrThisDate.hour, minute=vstrThisDate.minute, second=vstrThisDate.second)

    # TODO- Note that sending advert might have to be enabled
    # TODO- Please be aware that even if an advert ran its course and the user does not reply
    # TODO- and there is still credits available then the advert might run again the next day

    # TODO- if ran from credit and assigned credit is greator than 1 and scheduled for a previous date then schedule for the next date
    findRequest = Advert.query(Advert.assigned_credit > 0, Advert.run_from_credit == True, Advert.start_date == strThisDate)
    thisAdvertList = findRequest.fetch()

    for thisAdvert in thisAdvertList:
        i = 0
        strStartingCredit = thisAdvert.assigned_credit
        sentList = []

        while ((thisAdvert.assigned_credit > 0) and (i < len(thisOurContactList))):
            try:

                thisContact = random.choice(thisOurContactList)
                if not(thisContact.cell in sentList):
                    try:
                        if thisAdvert.use_portal == "Budget":
                            ref = thisPortalBudget.SendCronMessage(strMessage=thisAdvert.advert, strCell=thisContact.cell)
                            sentList.append(thisContact.cell)
                        elif thisAdvert.use_portal == "ClickSend":
                            ref = thisClickSendPortal.SendSMS(strCell=thisContact.cell, strMessage=thisAdvert.advert)
                            sentList.append(thisContact.cell)

                        elif thisAdvert.use_portal == "Twilio":
                            ref = thisTwilioPortal.sendSMS(strTo=thisContact.cell, strFrom=thisTwilioPortal.strMySMSNumber, strMessage=thisAdvert.advert)
                            sentList.append(thisContact.cell)
                        elif  thisAdvert.use_portal == "Vodacom":
                            sentList.append(thisContact.cell)
                        else:
                            ref = thisPortalBudget.SendCronMessage(strMessage=thisAdvert.advert, strCell=thisContact.cell)
                            sentList.append(thisContact.cell)
                    except:
                        ref = None


                    if ref != None:
                        thisSentReport = SentReport()
                        thisSentReport.writeCell(strinput=thisContact.cell)
                        thisSentReport.writeAdvertID(strinput=thisAdvert.advert_id)
                        # thisSentReport.writeMessageStatus(strinput=thisPortalBudget.CheckMessageStatusByCell(cell=thisContact.cell))
                        # Check The Message status of all sent messages through a separate function
                        thisSentReport.writeAdvertSent(strinput=True)
                        thisSentReport.writeMessageReference(strinput=ref)
                        vstrThisDate = datetime.datetime.now()
                        strThisDate = vstrThisDate.date()
                        strThisTime = datetime.time(hour=vstrThisDate.hour, minute=vstrThisDate.minute,
                                                    second=vstrThisDate.second)
                        thisSentReport.writeDateSent(strinput=strThisDate)
                        thisSentReport.writeTimeSent(strinput=strThisTime)
                        thisSentReport.put()
                        i += 1
                        thisAdvert.assigned_credit = thisAdvert.assigned_credit - 1
                    else:
                        pass
                else:
                    pass
            except:
                i += 1
                thisAdvert.assigned_credit = thisAdvert.assigned_credit - 1

        if thisAdvert.use_portal == "Vodacom":
            thisPortalVodacom.SendAdvert(strCellNumberList=sentList, strMessage=thisAdvert.advert)


        if thisAdvert.assigned_credit <= 0:
            thisAdvert.run_from_credit = False
        thisAdvert.put()

        thisStats = Stats()
        thisStats.writeAdvertID(strinput=thisAdvert.advert_id)
        thisStats.writeTotalSent(strinput=i)
        thisStats.writeTotalRemaining(strinput=(strStartingCredit - i))
        thisStats.put()


def RescheduleAdverts():

    from advertise import Advert
    vstrThisDate = datetime.datetime.now()
    strThisDate = vstrThisDate.date()

    findRequest = Advert.query(Advert.run_from_credit == True, Advert.start_date < strThisDate)
    thisAdvertList = findRequest.fetch()

    vstrThisDate = datetime.datetime.now()
    vstrThisDate += datetime.timedelta(hours=24)
    strThisDate = vstrThisDate.date()

    for thisAdvert in thisAdvertList:
        thisAdvert.writeStartDate(strinput=strThisDate)
        if thisAdvert.assigned_credit > 0:
            thisAdvert.run_from_credit = True
            thisAdvert.writeAdvertStatus(strinput="Running")
        thisAdvert.put()


def BulkMessageStatus():
    """
        Misleading this is for advertising status messages for mainly the budget portal other
        portals have their own call back URLS for sending status messages
    :return:
    """

    from advertise import SentReport
    from mysms import SMSPortalBudget,ClickSendSMSPortal
    from myTwilio import MyTwilioPortal


    vstrThisDate = datetime.datetime.now()
    strThisDate = vstrThisDate.date()
    vstrThisDate -= datetime.timedelta(minutes=10)
    strThisTime = datetime.time(hour=vstrThisDate.hour, minute=vstrThisDate.minute, second=vstrThisDate.second)

    #SENT Report is for adverts Delivery Report is for Bulk SMS,
    findRequest = SentReport.query(SentReport.report_done == False, SentReport.date_sent == strThisDate,
                                   SentReport.time_sent <= strThisTime)
    thisSentReportList = findRequest.fetch()

    thisBudgetPortal = SMSPortalBudget()
    thisTwilioPortal = MyTwilioPortal()
    thisClickSendPortal = ClickSendSMSPortal()

    for thisReport in thisSentReportList:
        if thisReport.portal_used == "Budget":
            thisReport.writeMessageStatus(strinput=thisBudgetPortal.CheckMessageStatus(strRef=thisReport.reference, strCell=thisReport.cell))
            thisReport.writeReportDone(strinput=True)
            thisReport.put()
        elif thisReport.portal_used == "Twilio":
            logging.info("Twilio uses it own callback URL to send status messages")
            pass
        elif thisReport.portal_used == "ClickSend":
            logging.info("Click Send also has its own callback URL for status messages")
        else:
            logging.info("Vodacom does not have a call back and a way to get responses has to be investigated")
            pass



def CheckAdvertsResponses():

    from advertise import SentReport, Responses
    from mysms import SMSPortalBudget

    vstrThisDate = datetime.datetime.now()
    strThisDate = vstrThisDate.date()
    vstrThisDate -= datetime.timedelta(
        minutes=30)  # 30 Minutes therefore is the maximum time for responses to be checked
    strIgnoreDate = vstrThisDate
    # TODO- decrease the number of days if too many resources starts being used
    strIgnoreDate -= datetime.timedelta(days=1)  # if 3 days passes without getting responses then it skips them
    strThisTime = datetime.time(hour=vstrThisDate.hour, minute=vstrThisDate.minute, second=vstrThisDate.second)
    strIgnoreDate = strIgnoreDate.date()

    # TODO- Consider using this method in all response handlers
    findRequest = SentReport.query(SentReport.report_done == True, SentReport.response_checked == False,
                                   SentReport.date_sent == strThisDate)
    thisSentReportList = findRequest.fetch()

    thisPortal = SMSPortalBudget()
    for thisReport in thisSentReportList:
        #TODO- Check the portal used to send the message in order to correctly obtain the response for the message

        try:
            strResponse = thisPortal.CheckSpecificReply(strRef=thisReport.reference)
            if not (strResponse == None):
                ThisResponse = Responses() #This is a response for adverts only
                ThisResponse.writeResponse(strinput=strResponse)
                ThisResponse.writeAdvertID(strinput=thisReport.advert_id)
                ThisResponse.writeReference(strinput=ThisResponse.CreateReference())
                ThisResponse.writeCell(strinput=thisReport.cell)

                vstrThisDate = datetime.datetime.now()
                strThisDate = vstrThisDate.date()
                strThisTime = datetime.time(hour=vstrThisDate.hour, minute=vstrThisDate.minute,
                                            second=vstrThisDate.second)
                ThisResponse.writeDateReceived(strinput=strThisDate)
                ThisResponse.writeTimeReceived(strinput=strThisTime)

                thisReport.writeResponseChecked(strinput=True)
                thisReport.put()
                ThisResponse.put()
        except:
            pass

    # Fixing older responses
    findRequest = SentReport.query(SentReport.report_done == True, SentReport.response_checked == False,
                                   SentReport.date_sent >= strIgnoreDate)
    thisSentReportList = findRequest.fetch()
    thisPortal = SMSPortalBudget()
    for thisReport in thisSentReportList:
        strResponse = thisPortal.CheckSpecificReply(strRef=thisReport.reference)
        if not (strResponse == None):
            ThisResponse = Responses()
            ThisResponse.writeResponse(strinput=strResponse)
            ThisResponse.writeAdvertID(strinput=thisReport.advert_id)
            ThisResponse.writeReference(strinput=ThisResponse.CreateReference())
            ThisResponse.writeCell(strinput=thisReport.cell)
            vstrThisDate = datetime.datetime.now()
            strThisDate = vstrThisDate.date()
            strThisTime = datetime.time(hour=vstrThisDate.hour, minute=vstrThisDate.minute,
                                        second=vstrThisDate.second)
            ThisResponse.writeDateReceived(strinput=strThisDate)
            ThisResponse.writeTimeReceived(strinput=strThisTime)

            thisReport.writeResponseChecked(strinput=True)
            thisReport.put()
            ThisResponse.put()

    # Making sure response older than ignore date will never be cheked again
    findRequest = SentReport.query(SentReport.report_done == True, SentReport.response_checked == False,
                                   SentReport.date_sent < strIgnoreDate)
    thisSentReportList = findRequest.fetch()
    for thisReport in thisSentReportList:
        thisReport.writeResponseChecked(strinput=True)
        thisReport.put()


def GetContactsFromPartners():

    from advertise import OurContacts
    from myapi import PartnerSites,strDefaultWhiteList
    import json
    findRequest = PartnerSites.query(PartnerSites.strServiceName == "Contacts")
    thisPartnerSiteList = findRequest.fetch()

    if len(thisPartnerSiteList) == 0:
        for site in strDefaultWhiteList:
            thisPartner = PartnerSites()
            thisPartner.writeAPIKey(strinput=os.environ.get(os.environ.get('BIM_INTERNAL_API')))
            thisPartner.writeAPISecret(strinput=os.environ.get(os.environ.get('BIM_INTERNAL_SECRET')))
            thisPartner.writeServiceName(strinput="Contacts")
            thisPartner.writeURL(strinput=site)
            thisPartner.put()

        findRequest = PartnerSites.query(PartnerSites.strServiceName == "Contacts")
        thisPartnerSiteList = findRequest.fetch()



    findRequest = OurContacts.query()
    thisContactList = findRequest.fetch()
    numList = []
    for thisContact in thisContactList:
        numList.append(thisContact.cell)


    for thisPartner in thisPartnerSiteList:
        try:
            strReturnData = thisPartner.FetchContactsJSONList()
            if strReturnData != thisPartner.strNoDataCode:
                json_objects =  json.load(strReturnData)
                for contact in json_objects:
                        cell = contact['cell']
                        email = contact['email']
                        names = contact['names']
                        surname = contact['surname']

                        if cell in numList:
                            pass
                        else:
                            thisContact = OurContacts()
                            thisContact.writeCell(strinput=cell)
                            thisContact.writeEmail(strinput=email)
                            thisContact.writeNames(strinput=names)
                            thisContact.writeSurname(strinput=surname)
                            thisContact.writeOurContactID(strinput=thisContact.CreateContactID())
                            thisContact.put()
                            numList.append(cell)
            else:
                pass
        except:
            pass




def CheckBulkSMSResponses():

    from mysms import Messages, SMSPortalBudget, DeliveryReport
    vstrThisDate = datetime.datetime.now()
    strThisDate = vstrThisDate.date()
    strThisTime = datetime.time(hour=vstrThisDate.hour, minute=vstrThisDate.minute, second=vstrThisDate.second)

    # # TODO-This is a code fix
    # findRequest = DeliveryReport.query()
    # thisDeliveyReportsList = findRequest.fetch()
    #
    # for normalize in thisDeliveyReportsList:
    #     if normalize.reference == None:
    #         normalize.reference = "11111"
    #     normalize.put()
    #
    # # TODO-Code Fix ended here

    findRequest = DeliveryReport.query(DeliveryReport.strDate <= strThisDate,
                                       DeliveryReport.strResponseReceived == False,
                                       DeliveryReport.strLimitReached == False)
    thisDeliveryList = findRequest.fetch()

    thisPortal = SMSPortalBudget()
    for thisDelivery in thisDeliveryList:
        if not (thisDelivery.reference == "11111"):
            strResponse = thisPortal.CheckSpecificReply(strRef=thisDelivery.reference)

            if not (strResponse == None):
                strResponse = strResponse.strip()
                thisDelivery.writeResponse(strinput=strResponse)
                thisDelivery.writeDateResponse(strinput=strThisDate)
                thisDelivery.writeTimeResponse(strinput=strThisTime)
                thisDelivery.writeResponseReceived(strinput=True)
                thisDelivery.put()
                # TODO-Note that in order for the response module to work successfully all the time the message id field must contain the reference of the message
                # TODO- On Bulk SMS Message Module Responses can be loaded there for each bulk SMS Module
            else:
                try:
                    thisDelivery.strResponseCounter += 1
                    if thisDelivery.strResponseCheckLimit == thisDelivery.strResponseCounter:
                        thisDelivery.strLimitReached = True

                except:
                    pass
                thisDelivery.put()

        else:
            strResponse = "11111"
            thisDelivery.writeResponse(strinput=strResponse)
            thisDelivery.writeDateResponse(strinput=strThisDate)
            thisDelivery.writeTimeResponse(strinput=strThisTime)
            thisDelivery.writeResponseReceived(strinput=True)
            thisDelivery.put()


def ScheduledSendSurveys():

    from surveys import SurveyOrders, SurveySchedules, SurveyContacts, Surveys, MultiChoiceSurveys, GeneralQuestionsSurvey, MultiChoiceSurveyAnswers, SurveyTracker
    from accounts import Accounts, Organization
    from mysms import SMSPortalBudget

    vstrThisDateTime = datetime.datetime.now()
    strThisDate = vstrThisDateTime.date()
    strThisTime = datetime.time(hour=vstrThisDateTime.hour, minute=vstrThisDateTime.minute,
                                second=vstrThisDateTime.second)

    findRequest = SurveyOrders.query(SurveyOrders.strRunOrder == True,
                                     SurveyOrders.strOrderStartDate == strThisDate,
                                     SurveyOrders.strOrderStartTime >= strThisTime)
    thisSurveyOrdersList = findRequest.fetch()

    findRequest = SMSPortalBudget.query()
    thisPortalList = findRequest.fetch()

    if len(thisPortalList) > 0:
        thisPortal = thisPortalList[0]
    else:
        thisPortal = SMSPortalBudget()

    logging.info("Just the beginning.....")
    logging.info("Schedules found : " + str(len(thisSurveyOrdersList)))

    for thisOrder in thisSurveyOrdersList:
        logging.info("Schedule found")

        findRequest = Accounts.query(Accounts.uid == thisOrder.uid)
        thisAccountList = findRequest.fetch()
        if len(thisAccountList) > 0:
            thisAccount = thisAccountList[0]
            findRequest = Organization.query(Organization.strOrganizationID == thisAccount.organization_id)
            thisOrgList = findRequest.fetch()
            if len(thisOrgList) > 0:
                thisOrg = thisOrgList[0]

            if not (thisAccount.cell == None):
                # TODO- Fix up the message formatting
                strMessage = "Your Survey Schedule : " + " Started Running at : " + str(
                    strThisDate) + " " + str(strThisTime)
                strRef = thisPortal.SendCronMessage(strMessage=strMessage, strCell=thisAccount.cell)
                logging.info("Just Sent the notification message : " + strRef)
            else:
                strMessage = "Your Survey Schedule : " + " Started Running at : " + str(
                    strThisDate) + " " + str(strThisTime)
                strRef = thisPortal.SendCronMessage(strMessage=strMessage, strCell=thisOrg.cell)
                logging.info("Just Sent the notification message : " + strRef)

            findRequest = SurveySchedules.query(SurveySchedules.strScheduleID == thisOrder.strScheduleID)
            thisScheduleList = findRequest.fetch()

            if len(thisScheduleList) > 0:
                thisSchedule = thisScheduleList[0]
            else:
                thisSchedule = SurveySchedules()

            findRequest = SurveyContacts.query(SurveyContacts.strListID == thisSchedule.strListID)
            thisContactList = findRequest.fetch()

            findRequest = Surveys.query(Surveys.strSurveyID == thisSchedule.strSurveyID)
            thisSurveyList = findRequest.fetch()

            if len(thisSurveyList) > 0:
                thisSurvey = thisSurveyList[0]

                if thisSurvey.strSurveyType == "multichoice":
                    findRequest = MultiChoiceSurveys.query(
                        MultiChoiceSurveys.strSurveyID == thisSurvey.strSurveyID).order(+MultiChoiceSurveys.strDateCreated)
                    thisSurveyQuestionList = findRequest.fetch()

                    for thisContact in thisContactList:
                        findRequest = SurveyTracker.query(SurveyTracker.strCell == thisContact.cell,
                                                          SurveyTracker.strSurveyID == thisSurvey.strSurveyID)
                        thisTrackerList = findRequest.fetch()
                        if len(thisTrackerList) > 0:
                            thisTracker = thisTrackerList[0]
                            i = 0
                            thisSurveyQuestion = thisSurveyQuestionList[i]
                            while not (
                                        thisTracker.strCurrentQuestionID == thisSurveyQuestion.strQuestionID) and (
                                        i < len(thisSurveyQuestionList)):
                                i += 1
                                thisSurveyQuestion = thisSurveyQuestionList[i]
                            i += 1
                            if i < len(thisSurveyQuestionList):

                                thisSurveyQuestion = thisSurveyQuestionList[i]

                            else:
                                thisSurveyQuestion = None
                                thisTracker.writeIsLastQuestion(strinput=True)
                        else:
                            thisSurveyQuestion = thisSurveyQuestionList[0]
                            thisTracker = SurveyTracker()
                            thisTracker.writeSurveyID(strinput=thisSurvey.strSurveyID)
                            thisTracker.writeCurrentQuestionID(strinput=thisSurveyQuestion.strQuestionID)
                            thisTracker.writeCell(strinput=thisContact.cell)

                            # TODO- Send Survey Intro duction
                            strMessage = thisOrg.strOrganizationName + "%0A" + "Invites you to participate in a survey. %0A Respond with option numbers on each question. %0A For example if the right answer is option 1. the respond by tapping one and send in your keypad"
                            thisPortal.SendCronMessage(strMessage=strMessage, strCell=thisContact.cell)

                        vstrThisDateTime = datetime.datetime.now()
                        strThisDate = vstrThisDateTime.date()
                        strThisTime = datetime.time(hour=vstrThisDateTime.hour, minute=vstrThisDateTime.minute,
                                                    second=vstrThisDateTime.second)

                        thisTracker.writeDate(strinput=strThisDate)
                        thisTracker.writeTime(strinput=strThisTime)

                        if not (thisTracker.strIsLastQuestion):
                            thisTracker.writeCurrentQuestionID(strinput=thisSurveyQuestion.strQuestionID)
                        else:
                            pass

                        thisTracker.put()

                        findRequest = SMSPortalBudget.query()
                        thisPortalList = findRequest.fetch()

                        if len(thisPortalList) > 0:
                            thisPortal = thisPortalList[0]
                        else:
                            thisPortal = SMSPortalBudget()

                        if not (thisSurveyQuestion == None):
                            strMessage = thisSurveyQuestion.strQuestion
                            strOptions = "%0A"
                            if not (thisSurveyQuestion.strChoiceOne == "undefined"):
                                strOptions += "1. " + thisSurveyQuestion.strChoiceOne + "%0A"
                            if not (thisSurveyQuestion.strChoiceTwo == "undefined"):
                                strOptions += "2. " + thisSurveyQuestion.strChoiceTwo + "%0A"
                            if not (thisSurveyQuestion.strChoiceThree == "undefined"):
                                strOptions += "3. " + thisSurveyQuestion.strChoiceThree + "%0A"
                            if not (thisSurveyQuestion.strChoiceFour == "undefined"):
                                strOptions += "4. " + thisSurveyQuestion.strChoiceFour + "%0A"

                            strMessage = strMessage + strOptions

                            strRef = thisPortal.SendCronMessage(strMessage=strMessage,
                                                                strCell=thisContact.cell)
                            thisAnswers = MultiChoiceSurveyAnswers()
                            thisAnswers.writeCell(strinput=thisContact.cell)
                            thisAnswers.writeNames(strinput=thisContact.strName)
                            thisAnswers.writeSurname(strinput=thisContact.surname)
                            thisAnswers.writeRef(strinput=strRef)
                            thisAnswers.writeSurveyID(strinput=thisSurvey.strSurveyID)
                            thisAnswers.writeQuestionID(strinput=thisSurveyQuestion.strQuestionID)
                            thisAnswers.writeQuestion(strinput=strMessage)
                            thisAnswers.writeOptionNumber(strinput=0)
                            # Note that option number zero mean the contact has not responded
                            thisAnswers.put()
                            #

                            # TODO- Send the present question, note down the present reference for obtaining responses

                            pass  # TODO- Finish up with the survey tracker, but first i have to implement the survey answer module

            thisOrder.writeRunOrder(strinput=False)
            thisOrder.writeOrderCompleted(strinput=True)
            thisOrder.put()


def SurveysResponses():
    """
    :return:
    """
    from surveys import SurveyTracker, MultiChoiceSurveyAnswers, SurveyContacts, MultiChoiceSurveys
    from mysms import SMSPortalBudget, SMSAccount
    findRequest = SurveyTracker.query(SurveyTracker.strResponseReceived == False,
                                      SurveyTracker.strClientParticipation == True,
                                      SurveyTracker.strRunTimes <= 10)
    thisSurveyTrackerList = findRequest.fetch()
    findRequest = SMSPortalBudget.query()
    thisPortalList = findRequest.fetch()
    if len(thisPortalList) > 0:
        thisPortal = thisPortalList[0]
    else:
        thisPortal = SMSPortalBudget()

    for thisTracker in thisSurveyTrackerList:
        if thisTracker.reference != None:
            reply = thisPortal.CheckSpecificReply(strRef=thisTracker.reference)
        else:
            reply = None
        if not (reply == None) and not ("error" in reply):
            thisSurveyAnswer = MultiChoiceSurveyAnswers()
            thisSurveyAnswer.writeCell(thisTracker.cell)
            thisSurveyAnswer.writeSurveyID(strinput=thisTracker.strSurveyID)
            thisSurveyAnswer.writeQuestionID(strinput=thisTracker.strCurrentQuestionID)
            reply = str(reply)
            reply = reply.strip()
            # TODO- Other reply parameters not saved ...Lots of work still needs to be done to finish up surveys
            thisSurveyAnswer.writeOptionNumber(strinput=reply)
            thisSurveyAnswer.writeRef(strinput=thisTracker.reference)

            findRequest = SurveyContacts.query(SurveyContacts.strCell == thisTracker.cell)
            thisContactList = findRequest.fetch()
            if len(thisContactList) > 0:
                thisContact = thisContactList[0]

                thisSurveyAnswer.writeNames(strinput=thisContact.strName)
                thisSurveyAnswer.writeSurname(strinput=thisContact.surname)

            findRequest = MultiChoiceSurveys.query(
                MultiChoiceSurveys.strQuestionID == thisTracker.strCurrentQuestionID)
            thisQuestionsList = findRequest.fetch()

            if len(thisQuestionsList) > 0:
                thisQuestion = thisQuestionsList[0]
                thisSurveyAnswer.writeQuestion(strinput=thisQuestion.strQuestion)

            # TODO - please create a Query to obtain names and surname of the person being surveyed
            # TODO- also run a query to obtain the actual Question the client is answering on the survey
            thisSurveyAnswer.put()


def BulkSMSStatus():

    from mysms import DeliveryReport, SMSPortalBudget, SMSAccount

    vstrThisDate = datetime.datetime.now()
    strThisDate = vstrThisDate.date()
    vstrThisDate -= datetime.timedelta(
        minutes=15)  # The only status that will be checked is those with a delivery report created on the last run
    strThisTime = datetime.time(hour=vstrThisDate.hour, minute=vstrThisDate.minute, second=vstrThisDate.second)

    findRequest = DeliveryReport.query(DeliveryReport.strSendingStatus == "NoStatus",
                                       DeliveryReport.strDate == strThisDate,
                                       DeliveryReport.strTime <= strThisTime)
    thisReportList = findRequest.fetch()

    findRequest = SMSPortalBudget.query()
    thisBudgetList = findRequest.fetch()
    if len(thisBudgetList) > 0:
        thisPortal = thisBudgetList[0]
    else:
        thisPortal = SMSPortalBudget()

    for thisReport in thisReportList:

        # TODO - There could be a timing issue with this task so it should process reports that are at least three minutes old
        #TODO - Check which Portal was used to send the message and act appropriately
        strStatus = thisPortal.CheckMessageStatus(strRef=thisReport.reference, strCell=thisReport.cell)

        if not (strStatus == None):
            thisReport.writeSendingStatus(strinput=strStatus)
            thisReport.put()
            strStatus = str(strStatus)
            if "UNDELIVERED" in strStatus:  # TODO-Note that we have to verify that the status code is actually undelivered for this

                findRequest = SMSAccount.query(SMSAccount.strOrganizationID == thisReport.organization_id)
                thisSMSAccountList = findRequest.fetch()
                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]
                    thisSMSAccount.writeTotalSMS(strinput=str(thisSMSAccount.strTotalSMS + 1))
                    thisSMSAccount.put()
                    # TODO- Consider creating a retry function here, it should take in all the messages that are suppose
                    # TODO- to be retried and feed them in
                    # TODO- a retry list, another task handler must handle the retry messages, if the retry
                    # TODO- function is successfull it should subtract the credit from the user again
                else:
                    pass
            else:
                pass
        else:
            pass


            # TODO- if message was not sent then process


def FaxToEmailOrganizer():
    """
        Access available Email Addresses clean up emails that are not being used anymore
        recreate at least 100 new emails if the unused new emails are lower than 100

    :return:
    """
    from myfax import AvailableEmailEndPoints

    findRequest = AvailableEmailEndPoints.query(AvailableEmailEndPoints.strAssigned == False)
    thisAvailableEmailsList = findRequest.fetch()

    if len(thisAvailableEmailsList) < 100:
        for i in range(100):
            ThisEndPoint = AvailableEmailEndPoints()
            ThisEndPoint.writeEmailReference(strinput=ThisEndPoint.CreateEmailReference())
            vstrEmailAddress = ThisEndPoint.CreateEmailAddress()
            findRequest = AvailableEmailEndPoints.query(
                AvailableEmailEndPoints.strEmailAddress == vstrEmailAddress)
            thisDuplicateList = findRequest.fetch()
            if len(thisDuplicateList) == 0:
                ThisEndPoint.writeEmailAddress(strinput=vstrEmailAddress)
                ThisEndPoint.put()
            else:
                pass


def SendSurveysCredits():
    from surveys import Surveys
    from mysms import SMSAccount,SMSPortalBudget,ClickSendSMSPortal,SMSPortalVodacom
    from advertise import OurContacts

    pass
    #TODO- Finish up sending surveys this is very important





class TasksRouterHandler(webapp2.RequestHandler):


    def get(self):

        URL = self.request.url
        strURLlist = URL.split("/")

        strFunction = strURLlist[4]

        if strFunction == "bulk-sms":
            logging.info("sending scheduled bulk sms runs every ten minutes")
            BulkSMSHandler()

        elif strFunction == "bulk-email":
            logging.info("sending scheduled bulk emails runs every ten minutes")
            BulkEmailHandler()

        elif strFunction == "system-notifications":
            logging.info("send management system notifications runs every 6 hours")
            SystemStatusHandler()


        elif strFunction == "advert-contacts":
            logging.info("build advertising contacts database runs every 12 hours")
            AdvertContactsHandler()

        elif strFunction == "send-adverts":
            logging.info("send scheduled advertising runs every 10 minutes")
            # SendAdvertsHandler() Deprecated TODO investigate how to repurpose this utility to enable sending adverts in chunks

        elif strFunction == "send-credit-adverts":
            logging.info("send adverts using the new credit allocation system runs every 3 hours")
            SendAdvertCreditHandler()

        elif strFunction == "reschedule-adverts":
            logging.info("reschedule adverts based on run status every 4 hours")
            RescheduleAdverts()


        elif strFunction == "check-status":
            logging.info("check bulk messages sms every 15 minutes")
            BulkMessageStatus()


        elif strFunction == "check-adverts-responses":
            logging.info("check adverts responses every 5 minutes")
            CheckAdvertsResponses()

        elif strFunction == "get-partner-contacts":
            logging.info("go through all the partner sites and obtain new contacts")
            GetContactsFromPartners()


        elif strFunction == "check-bulk-sms-responses":
            logging.info("check bulk sms responses every 5 minutes")
            CheckBulkSMSResponses()

        elif strFunction == "schedule-surveys-send":
            logging.info("running scheduled surveys runs every 10 minutes")
            ScheduledSendSurveys()

        elif strFunction == "multi-choice-survey-responses":
            logging.info("check surveys responses runs every 15 minutes")
            SurveysResponses()

        elif strFunction == "check-bulk-sms-status":
            logging.info("bulk sms message status runs every 15 minutes")
            BulkSMSStatus()

        elif strFunction == "organize-fax-to-email":
            logging.info("manage and allocate fax to email resources runs every 60 minutes")
            FaxToEmailOrganizer()

        elif strFunction == "send-credit-surveys":
            logging.info("send scheduled surveys from payment allocator every 15 minutes")
            SendSurveysCredits()

        else:
            pass

    #TODO- Reduce tasks urls using /tasks/.* and then call the right task for each task this will allow the app ro run thousands of cron jobs
    #TODO- My Tasks can also call functions through an API to complete each task.

app = webapp2.WSGIApplication([
    ('/tasks/.*', TasksRouterHandler)

], debug=True)

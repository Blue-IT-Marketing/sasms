=-#!/usr/bin/env python
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


import os
import jinja2
import datetime
from google.cloud import ndb

from userRights import UserRights
from accounts import Accounts
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
import logging
#from twilio.rest import Client
#TODO- Add Twilio to send SMS Also
from xml.etree import ElementTree


class Groups(ndb.Model):

    uid = ndb.StringProperty()
    organization_id = ndb.StringProperty()

    group_id = ndb.StringProperty()
    group_name = ndb.StringProperty()
    description = ndb.StringProperty()

    total_numbers = ndb.IntegerProperty(default=0)


    def writeUserID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.uid = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOrganizationID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.organization_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeGroupID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.group_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeGroupName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.group_name = strinput
                return True
            else:
                return False
        except:
            return False
    def writeGroupDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.description = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateGroupID(self):
        import string,random
        try:
            strGroupID = "SMS"
            for i in range(32):
                strGroupID += random.SystemRandom().choice(string.digits + string.ascii_lowercase)
            return strGroupID
        except:
            return None
    def writeTotalNumbers(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.total_numbers = int(strinput)
                return True
            else:
                return False
        except:
            return False

class SMSContacts(ndb.Model):
    uid = ndb.StringProperty()
    cell_number = ndb.StringProperty()
    email = ndb.StringProperty() #TODO intergrate email with the rest of the contacts
    names = ndb.StringProperty()
    surname = ndb.StringProperty()

    group_id = ndb.StringProperty()

    def writeUserID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.uid = strinput
                return True
            else:
                return False
        except:
            return False
    def writeGroupID(self,strinput):
        try:
            strinput = str(strinput)

            if strinput != None:
                self.group_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCellNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.cell_number = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNames(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.names = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurname(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.surname = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEmail(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.email = strinput
                return True
            else:
                return False
        except:
            return False

class Messages(ndb.Model):

    group_id = ndb.StringProperty()
    message_id = ndb.StringProperty() # Also as reference number for the message



    message = ndb.StringProperty()
    response = ndb.StringProperty() #Message Response
    response_received = ndb.BooleanProperty(default=False)
    date_response = ndb.DateProperty()
    time_response = ndb.TimeProperty()

    submitted = ndb.BooleanProperty(default=False)
    date_submitted = ndb.DateProperty()
    time_submitted = ndb.TimeProperty()
    date_created = ndb.DateProperty(auto_now_add=True)
    time_created = ndb.TimeProperty(auto_now_add=True)

    sent_with_portal = ndb.StringProperty(default="Budget") # Vodacom/ Twilio / ClickSend
    #TODO- make sure every outgoing message indicates which portal it was sent with


    def writeSentWithPortal(self,strinput):
        try:
            strinput = str(strinput)
            strinput = strinput.capitalize()
            if strinput in ["Budget", "Vodacom", "Twilio", "ClickSend"]:
                self.sent_with_portal = strinput
                return True
            else:
                return False
        except:
            return False

    def writeGroupID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.group_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMessageID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.message_id = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateMessageID(self):
        import random,string
        try:
            strMessageID = ""
            for i in range(32):
                strMessageID += random.SystemRandom().choice(string.digits + string.ascii_lowercase)
            return strMessageID

        except:
            return None
    def writeMessage(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.message = strinput
                return True
            else:
                return False

        except:
            return False

    def writeSubmitted(self,strinput):
        try:
            if strinput in [True,False]:
                self.submitted = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateSubmitted(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.date_submitted = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeSubmitted(self,strinput):
        try:
            if strinput != None:
                self.time_submitted = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeCreated(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.time_created = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateCreated(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.date_created = strinput
                return True
            else:
                return False
        except:
            return False

class MessageSchedule(ndb.Model):

    uid = ndb.StringProperty()
    message_id = ndb.StringProperty()

    start_date = ndb.DateProperty()
    start_time = ndb.TimeProperty()
    end_date = ndb.DateProperty()
    end_time = ndb.TimeProperty()

    status = ndb.StringProperty(default="Scheduled") # Running , Completed

    notify_on_start = ndb.BooleanProperty(default=True)
    notify_on_end = ndb.BooleanProperty(default=True)

    def writeUserID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.uid = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMessageID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.message_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStartDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.start_date = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStartTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.start_time = strinput
                return True
            else:
                return False

        except:
            return False

    def writeEndTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.end_time = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEndDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.end_date = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStatus(self,strinput):
        try:
            strinput = str(strinput)

            if strinput in ['Scheduled','Running','Completed']:
                self.status = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNotifyOnStart(self,strinput):
        try:
            if strinput in [True,False]:
                self.notify_on_start = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNotifyonEnd(self,strinput):
        try:
            if strinput in [True,False]:
                self.notify_on_end = strinput
                return True
            else:
                return False
        except:
            return False

class DeliveryReport(ndb.Model):

    message_id = ndb.StringProperty()

    reference = ndb.StringProperty(default="11111") #TODO- Make sure that you never ever ever use messageid as a reference code

    sending_status = ndb.StringProperty(default="NoStatus") # Delivered, Not Delivered

    #TODO-Enable all message kinds to fetch the delivery status for each message sent,
    #TODO- resolve the response message conflict its both in message and also in delivery message this must be resolved

    group_id = ndb.StringProperty()
    organization_id = ndb.StringProperty()
    cell = ndb.StringProperty()

    response = ndb.StringProperty()
    date_response = ndb.DateProperty()
    time_response = ndb.TimeProperty()
    response_received = ndb.BooleanProperty(default=False)
    response_counter = ndb.IntegerProperty(default=0)
    response_check_limit = ndb.IntegerProperty(default=10)

    limit_reached = ndb.BooleanProperty(default=False)

    delivered = ndb.BooleanProperty(default=False)

    date_created = ndb.DateProperty()
    time_created = ndb.TimeProperty()


    def WriteResponseCounter(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.response_counter = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeResponseCounterLimit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.response_check_limit = int(strinput)
                return True
            else:
                return False
        except:
            return False



    def writeSendingStatus(self,strinput):
        try:

            strinput = str(strinput)
            if strinput != None:
                self.sending_status = strinput
                return True
            else:
                return False
        except:
            return False

    def writeResponse(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.response = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateResponse(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.date_response = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeResponse(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.time_response = strinput
                return True
            else:
                return False
        except:
            return False
    def writeResponseReceived(self,strinput):
        try:
            if strinput in [True,False]:
                self.response_received = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMessageID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.message_id = strinput
                return True
            else:
                return False

        except:
            return False
    def writeOrganizationID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.organization_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeGroupID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.group_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.cell = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDelivered(self,strinput):
        try:
            if strinput in [True,False]:
                self.delivered = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDate(self,strinput):
        try:
            if strinput != None:
                self.date_created = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTime(self,strinput):
        try:
            if strinput != None:
                self.time_created = strinput
                return True
            else:
                return False
        except:
            return False
    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.reference = strinput
                return True
            else:
                return False
        except:
            return False

class SMSAccount(ndb.Model):

    organization_id = ndb.StringProperty()
    credit_amount = ndb.FloatProperty(default=0)
    cost_per_sms = ndb.FloatProperty(default=35)
    total_sms = ndb.IntegerProperty(default=10)

    date_created = ndb.DateProperty(auto_now_add=True)
    time_created = ndb.TimeProperty(auto_now_add=True)

    use_portal = ndb.StringProperty(default="Budget") # Budget, Vodacom, ClickSend, Twilio

    deposit_reference = ndb.StringProperty(default="mobjustice budget")

    suspended = ndb.BooleanProperty(default=False)

    #TODO intergrate the proforma invoice payment system to the messaging module

    def writeOrganizationID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.organization_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCreditAmount(self,strinput):
        try:
            if isinstance(strinput,float) or isinstance(strinput,int):
                self.credit_amount = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCostPerSMS(self,strinput):
        try:
            if isinstance(strinput,float) or isinstance(strinput,int):
                self.cost_per_sms = strinput
                return True
            else:
                return False
        except:
            return False
    def CalculateTotalSMS(self):
        try:
            strTotalSMS = (self.credit_amount * 100) // self.cost_per_sms
            return str(strTotalSMS)
        except:
            return None
    def writeTotalSMS(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.total_sms = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeDateCredited(self,strinput):
        try:

            if isinstance(strinput,datetime.date):
                self.date_created = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeCredited(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.time_created = strinput
                return True
            else:
                return False
        except:
            return False
    def writeUsePortal(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.use_portal = strinput
                return True
            else:
                return False
        except:
            return False
    def AddTotalSMS(self,strinput):
        try:
            strinput = str(strinput)

            if strinput.isdigit():
                self.total_sms += int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeDepositReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.deposit_reference = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateDepositReference(self):
        try:
            strDepositeReference = "mobjustice budget"
            return strDepositeReference
        except:
            return None
    def WriteSuspend(self,strinput):
        try:
            if strinput in [True,False]:
                self.suspended = strinput
                return True
            else:
                return False
        except:
            return False

class SMSPortalVodacom(ndb.Model):
    """
        When using the CSV file format send the file as an attachment
    """
    sender_address = ndb.StringProperty(default=os.environ.get('PORTAL_VODACOM_SENDER_EMAIL'))
    email_address = ndb.StringProperty(default=os.environ.get('PORTAL_VODACOM_EMAIL'))
    csv_email = ndb.StringProperty(default=os.environ.get('PORTAL_VODACOM_CSV_EMAIL'))
    sms_size_limit = ndb.IntegerProperty(default=600)
    available_credit = ndb.IntegerProperty(default=67)
    buy_rate = ndb.IntegerProperty(default=32)
    sell_rate = ndb.IntegerProperty(default=35)
    profit = ndb.ComputedProperty(lambda self: self.sell_rate - self.buy_rate)
    portal_address = ndb.StringProperty(default="https://vodacommessaging.co.za")
    system_credit = ndb.IntegerProperty(default=0)
    portal_login = ndb.StringProperty(default=os.environ.get('PORTAL_VODACOM_LOGIN'))
    portal_password = ndb.StringProperty(default=os.environ.get('PORTAL_VODACOM_PASSWORD'))


    def writeSenderAddress(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.sender_address = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCSVEmail(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.csv_email = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEmailAddress(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.email_address = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSMSSixeLimit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 160):
                self.sms_size_limit = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeAvailableCredit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 0):
                self.available_credit = int(strinput)
                return True
            else:
                return False

        except:
            return False
    def writeSellRate(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= self.buy_rate):
                self.sell_rate = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeBuyRate(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 0):
                self.buy_rate = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeSystemCredit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 0):
                self.system_credit = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writePortaLogin(self,strinput):
        try:
            strinput = str(strinput)
            if (strinput == None):
                self.portal_login = strinput
                return True
            else:
                return False
        except:
            return False
    def writePassword(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.portal_password = strinput
                return True
            else:
                return False
        except:
            return False
    def writePortalAddress(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.portal_address = strinput
                return True
            else:
                return False
        except:
            return False
    def SendMessages(self,strCellNumberList,strMessage):
        from myemail import SendEmail
        try:
            strSubject = ""
            strInvalid = False
            if isinstance(strCellNumberList,list):
                for strCell in strCellNumberList:
                    if strSubject == "":
                        strSubject = strCell
                    else:
                        strSubject = strSubject + " " + strCell

            elif "," in strCellNumberList:
                strCellNumberList = strCellNumberList.split(",")
                for strCell in strCellNumberList:
                    if strSubject == "":
                        strSubject = strCell
                    else:
                        strSubject = strSubject + " " + strCell
            else:
                strInvalid = True


            #def SendEmail(strFrom,strTo,subject,body,strTextType,strAttachFileContent=None,strAttachFileName=None):
            if SendEmail(strFrom=self.sender_address, strTo=self.email_address, strSubject=strSubject, strBody=strMessage, strTextType="text/plain"):
                try:
                    self.writeAvailableCredit(strinput=str(self.available_credit - len(strCellNumberList)))
                    self.put()
                except:
                    pass
                return True
            else:
                return False


        except:
            return False

    def CronSendMessages(self,strCellNumberList,strMessage,strAccountID):
        from myemail import SendEmail
        try:

            strSubject = ""
            strInvalid = False
            if isinstance(strCellNumberList,list):
                for strCell in strCellNumberList:
                    if strSubject == "":
                        strSubject = strCell
                    else:
                        strSubject = strSubject + " " + strCell

            elif "," in strCellNumberList:
                strCellNumberList = strCellNumberList.split(",")
                for strCell in strCellNumberList:
                    if strSubject == "":
                        strSubject = strCell
                    else:
                        strSubject = strSubject + " " + strCell
            else:
                strInvalid = True

            if not(strInvalid):

                findRequest = SMSAccount.query(SMSAccount.organization_id == strAccountID)
                thisSMSAccountList = findRequest.fetch()

                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]
                else:
                    thisSMSAccount = SMSAccount()
                    thisSMSAccount.writeOrganizationID(strinput=strAccountID)
                    thisSMSAccount.put()


                if thisSMSAccount.total_sms >= len(strCellNumberList):

                    #def SendEmail(strFrom,strTo,subject,body,strTextType,strAttachFileContent=None,strAttachFileName=None):
                    if SendEmail(strFrom=self.sender_address, strTo=self.email_address, strSubject=strSubject, strBody=strMessage, strTextType="text/plain"):

                        thisSMSAccount.writeTotalSMS(strinput=str(thisSMSAccount.total_sms - len(strCellNumberList)))
                        thisSMSAccount.put()
                        self.writeAvailableCredit(strinput=str(self.available_credit - len(strCellNumberList)))
                        self.put()
                        return True
                    else:
                        return False
                else:
                    logging.info("This False")
                    return False
            else:
                logging.info("This Falsity")
                return False

        except:
            logging.info("Bad Exception")
            return False

    def SendAdvert(self,strCellNumberList,strMessage):
        """
            Can also Send Surveys
        :param strCellNumberList:
        :param strMessage:
        :return:
        """
        from myemail import SendEmail
        try:
            strSubject = ""
            strInvalid = False
            if isinstance(strCellNumberList,list):
                for strCell in strCellNumberList:
                    if strSubject == "":
                        strSubject = strCell
                    else:
                        strSubject = strSubject + " " + strCell

            elif "," in strCellNumberList:
                strCellNumberList = strCellNumberList.split(",")
                for strCell in strCellNumberList:
                    if strSubject == "":
                        strSubject = strCell
                    else:
                        strSubject = strSubject + " " + strCell
            else:
                strInvalid = True


            if SendEmail(strFrom=self.sender_address, strTo=self.email_address, strSubject=strSubject, strBody=strMessage, strTextType="text/plain"):
                return True
            else:
                return False
        except:
            return False


class SMSPortalBudget(ndb.Model):

    rest_send_api = ndb.StringProperty(default="https://www.budgetmessaging.com/sendsms.ashx")
    rest_status_api = ndb.StringProperty(default="https://www.budgetmessaging.com/smsstatus.ashx")
    rest_replies_api = ndb.StringProperty(default="https://www.budgetmessaging.com/smsreply.ashx")
    rest_credits_api = ndb.StringProperty(default="https://www.budgetmessaging.com/credits.ashx")
    login_name = ndb.StringProperty(default=os.environ.get('PORTAL_BUDGET_LOGIN'))
    password = ndb.StringProperty(default=os.environ.get('PORTAL_BUDGET_PASSWORD'))
    portal_address = ndb.StringProperty(default="https://www.budgetmessaging.com")

    sms_size_limit = ndb.IntegerProperty(default=150)
    available_credit = ndb.FloatProperty(default=0)
    sell_rate = ndb.IntegerProperty(default=35)
    advert_sell_rate = ndb.IntegerProperty(default=30)
    buy_rate = ndb.IntegerProperty(default=17)
    profit = ndb.ComputedProperty(lambda self: self.sell_rate - self.buy_rate)
    system_credit = ndb.IntegerProperty(default=0)


    def writeSystemCredit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 0):
                self.system_credit = int(strinput)
                return  True
            else:
                return False
        except:
            return False
    def writeBuyRate(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 0):
                self.buy_rate = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeAdvertSellRate(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.advert_sell_rate = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeSendHTTPS(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.rest_api = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStatusHTTPS(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strStatusHTTPS = strinput
                return True
            else:
                return False

        except:
            return False
    def writeRepliesHTTPS(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.rest_replies_api = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCreditHTTPS(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.rest_credits_api = strinput
                return True
            else:
                return False
        except:
            return False
    def writeLoginName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.login_name = strinput
                return True
            else:
                return False
        except:
            return False
    def writePassword(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.password = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSMSSizeLimit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.sms_size_limit = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeAvailableCredit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.available_credit = float(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeSellRate(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.sell_rate = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writePortalAddress(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.portal_address = strinput
                return True
            else:
                return False

        except:
            return False
    def SendMessage(self,strMessage,strMessageID,strCell):
        try:
            strMessage = strMessage + " Optout:Reply STOP"
            form_data = 'user=' + self.login_name + '&password=' + self.password + '&cell=' + strCell + '&msg=' + strMessage + '&ref=' + strMessageID
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.rest_api, payload=form_data, method=urlfetch.POST, headers=headers, validate_certificate=True)
            if (result.status_code >= 200) and (result.status_code < 400) :
                strResult = result.content
                strResult = strResult.replace("ACCEPTED"," ")
                strResult = strResult.strip()
                return strResult
            else:
                return None
        except urlfetch.Error:
            return None

    def SendCronMessage(self,strMessage,strCell):
        try:
            strMessage = strMessage + " Optout:Reply STOP"
            form_data = 'user=' + self.login_name + '&password=' + self.password + '&cell=' + strCell + '&msg=' + strMessage
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.rest_api, payload=form_data, method=urlfetch.POST, headers=headers, validate_certificate=True)
            if (result.status_code >= 200) and (result.status_code < 400):
                strResult = result.content
                strResult = strResult.replace("ACCEPTED", " ")
                strResult = strResult.strip()
                return strResult
            else:
                return None
        except urlfetch.Error:
            return None

    def CheckMessageStatus(self,strRef,strCell):
        try:
            if "ACCEPTED" in strRef:
                strRef = strRef.replace("ACCEPTED","")

            strRef = strRef.strip()
            logging.info(strRef)
            form_data = 'user=' + self.login_name + '&password=' + self.password + '&ref=' + strRef + "_" + strCell
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.strStatusHTTPS, payload=form_data, method=urlfetch.POST, headers=headers,validate_certificate=True)

            if (result.status_code >= 200) and (result.status_code < 400):
                return result.content
            else:
                return None

        except urlfetch.Error:
            return None


    def CheckMessageStatusByDateRange(self,strMessageID,strStartDate,strEndDate):
        """
        format of StartDate = DD/MM/YYYY
        format of EndDate = DD/MM/YYYY
        :param strMessageID:
        :param strStartDate:
        :param strEndDate:
        :return:
        """
        try:
            strSYear = strStartDate.year
            strSMonth = strStartDate.month
            strSDay = strStartDate.day
            strStartDate = strSDay + "/" + strSMonth + "/" + strSYear
            strEYear = strEndDate.year
            strEMonth = strEndDate.month
            strEDay = strEndDate.day
            strEndDate = strEDay + "/" + strEMonth + "/" + strEYear

            form_data = '&user=' + self.login_name + '&password=' + self.password + '&ref=' + strMessageID + '&startdate=' + strStartDate + '&enddate=' + strEndDate
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.strStatusHTTPS, payload=form_data, method=urlfetch.POST, headers=headers,validate_certificate=True)
            if (result.status_code >= 200) and (result.status_code < 400):
                return result.content
            else:
                return None
        except urlfetch.Error:
            return None


    def CheckMessageReplies(self,strStartDate,strEndDate):
        try:
            form_data = '&user=' + self.login_name + '&password=' + self.password + '&startdate=' + strStartDate + '&enddate=' + strEndDate
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.rest_replies_api, payload=form_data, method=urlfetch.POST, headers=headers,
                                    validate_certificate=True)

            if (result.status_code >= 200) and (result.status_code < 400):
                xStatusMessage = ElementTree.fromstring(result.content)
                return xStatusMessage
            else:
                return None

        except urlfetch.Error:
            return None

    def CheckSpecificReply(self,strRef):
        try:
            if "ACCEPTED" in strRef:
                strRef = strRef.replace("ACCEPTED","")
            strRef = strRef.strip()

            logging.info(strRef)
            form_data = 'user=' + self.login_name + '&password=' + self.password + '&ref=' + strRef
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.rest_replies_api, payload=form_data, method=urlfetch.POST, headers=headers,
                                    validate_certificate=True)

            if (result.status_code >= 200) and (result.status_code < 400):
                xStatusMessage = ElementTree.fromstring(result.content)
                strStatusMessage = xStatusMessage.findtext(".//message")
                if not(strStatusMessage == None):
                    return strStatusMessage
                else:
                    return None
            else:
                return None

        except urlfetch.Error:
            logging.exception('Caught exception fetching ' + self.rest_replies_api)


    def CheckCredits(self):
        try:
            form_data = '&user=' + self.login_name + '&password=' + self.password
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.rest_credits_api, payload=form_data, method=urlfetch.POST, headers=headers,
                                    validate_certificate=True)
            if (result.status_code >= 200) and (result.status_code < 400):
                return result.content
            else:
                return None

            logging.info(result.content)

        except urlfetch.Error:
            return None

class ClickSendSMSPortal(ndb.Model):
    """
        Send SMS Example
        https://api-mapper.clicksend.com/http/v2/send.php?method=http&username=mobiusndou@gmail.com&key=DBC95D5A-FB8F-4C12-8857-956557D14A68&to=0790471559&message=you are the boss
    """
    rest_send_api = ndb.StringProperty(default="https://api-mapper.clicksend.com/http/v2/send.php")
    rest_reply_api = ndb.StringProperty(default="https://sa-sms.appspot.com/clicksend/sms/replies")
    rest_reports_api = ndb.StringProperty(default="https://sa-sms.appspot.com/clicksend/sms/reports")
    rest_fax_reports_api = ndb.StringProperty(default="https://sa-sms.appspotmail.com/clicksend/fax/reports")
    email_incoming_fax = ndb.StringProperty(default="incomingfaxes@sa-sms.appspotmail.com")
    strSendFaxEmail = ndb.StringProperty(default="@fax.clicksend.com")
    strAutho = ndb.StringProperty(default=os.environ.get('CLICK_SEND_AUTH'))
    strUserName = ndb.StringProperty(default=os.environ.get('CLICK_SEND_LOGIN'))
    strAPIKey = ndb.StringProperty(default=os.environ.get('CLICK_SEND_API_KEY'))
    strSendFromEmail = ndb.StringProperty(default=os.environ.get('CLICK_SEND_FROM_EMAIL'))


    def SendSMS(self,strCell,strMessage):
        try:
            strMessage = strMessage + " Optout : Reply STOP"

            form_data = "method=http&username=" + self.strUserName + "&key=" + self.strAPIKey + "&to="+strCell+"&message=" + strMessage
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.rest_send_api, payload=form_data, method=urlfetch.POST, headers=headers, validate_certificate=True)
            if (result.status_code >= 200) and (result.status_code < 400):
                return result.content
            else:
                return None
        except urlfetch.Error:
            return None


    def sendFax(self,strFaxNumber,strFaxFileName,strSubject=None,strCoverPage=None):
        """
         auth~{Username}~{API-Key}~{From}
        :param strFaxNumber:
        :param strFaxFileName:
        :return:

        find out how to add attachments from the cloud store
        Store faxes in the cloud store for at least three months

        readfilename from datastore, obtain filedata and send as attachment together with your email
        type is pdf
        if successfull send the file as attachment to fax

        """
        from myemail import SendEmail
        try:
            strFaxToEmail = strFaxNumber + self.strSendFaxEmail
            strFaxFromEmail = self.strSendFromEmail
            strSubject = self.strAutho
            strUserCoverMessage = strSubject + """ <br> """ + strCoverPage
            strBody = """ 
            <h2>Business Communication and Contact Management</h2>
            
            <strong>Bulk &amp; Business Faxing Solution</strong>
            
            For an easy to use faxing solution for your business register @
            <a href="https://sa-sms.appspot.com">https://sa-sms.appspot.com</a>
            
            <strong>Thank You</strong><br>
            <strong>Justice Ndou</strong><br>
            <strong>Blue IT Marketing Pty LTD</strong><br>              
            """ + strUserCoverMessage

            strBucketName = os.environ.get('BUCKET_NAME',app_identity.get_default_gcs_bucket_name())
            strOpenFaxFileName ="/" + strBucketName+"/" + strFaxFileName
            logging.info("opening this file : " + strOpenFaxFileName)
            with cloudstorage.open(strOpenFaxFileName) as cloudstorage_file:
                FaxFileContent = cloudstorage_file.read()
                logging.info("Successfully opened file")
            logging.info("Past file opening stage")

            if SendEmail(strFrom=strFaxFromEmail,strTo=strFaxToEmail,strSubject=strSubject,strBody=strBody,strTextType='text/html',strAttachFileContent=FaxFileContent,strAttachFileName=strFaxFileName):
                logging.info("Email Sent")
                return True
            else:
                return False
        except:
            return False


from firebaseadmin import VerifyAndReturnAccount


class mySMSHandler(webapp2.RequestHandler):
    def get(self):
        #+ '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
        vstrUserID = self.request.get('vstrUserID')
        vstrEmail = self.request.get('vstrEmail')
        vstrAccessToken = self.request.get('vstrAccessToken')

        thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
        if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

            template = template_env.get_template('templates/sms/sms.html')
            context = {}
            self.response.write(template.render(context))

class SMSGroupHandler(webapp2.RequestHandler):
    def get(self):
        from accounts import Organization

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "1":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):
                findRequest = Accounts.query(Accounts.uid == vstrUserID)
                thisAdminList = findRequest.fetch()
                if len(thisAdminList) > 0:
                    thisAdmin = thisAdminList[0]
                else:
                    thisAdmin = Accounts()

                findRequest = Groups.query(Groups.organization_id == thisAdmin.organization_id)
                thisGroupsList = findRequest.fetch()

                template = template_env.get_template('templates/sms/creategroups.html')
                context = {'thisGroupsList':thisGroupsList}
                self.response.write(template.render(context))

        elif vstrChoice == "2":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrGroupName = self.request.get('vstrGroupName')
            vstrGroupDescription = self.request.get('vstrGroupDescription')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):
                findRequest = Accounts.query(Accounts.uid == vstrUserID)
                thisAdminList = findRequest.fetch()

                if len(thisAdminList) > 0:
                    thisAdmin = thisAdminList[0]
                else:
                    thisAdmin = Accounts()


                findRequest = Groups.query(Groups.group_name == vstrGroupName, Groups.organization_id == thisAdmin.organization_id)
                thisGroupList = findRequest.fetch()

                if len(thisGroupList) > 0:
                    thisGroup = thisGroupList[0]
                else:
                    thisGroup = Groups()

                thisGroup.writeOrganizationID(strinput=thisAdmin.organization_id)
                thisGroup.writeGroupName(strinput=vstrGroupName)
                thisGroup.writeGroupDescription(strinput=vstrGroupDescription)
                thisGroup.writeUserID(strinput=vstrUserID)
                thisGroup.writeGroupID(strinput=thisGroup.CreateGroupID())
                thisGroup.put()

                self.response.write('Group Successfully created ')

        elif vstrChoice == "3":
            pass

        elif vstrChoice == "4":
            #+ '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = UserRights.query(UserRights.strUserID == thisMainAccount.uid)
                thisUserRightList = findRequest.fetch()

                if len(thisUserRightList) > 0:
                    thisUserRight = thisUserRightList[0]
                else:
                    thisUserRight = UserRights()

                if thisUserRight.strAdminUser:
                    findRequest = SMSAccount.query(SMSAccount.organization_id == thisMainAccount.organization_id)
                    thisSMSAccountList = findRequest.fetch()

                    if len(thisSMSAccountList) > 0:
                        thisSMSAccount = thisSMSAccountList[0]
                    else:
                        thisSMSAccount = SMSAccount()

                    findRequest = SMSPortalVodacom.query()
                    thisVodacomPortalList = findRequest.fetch()

                    if len(thisVodacomPortalList) > 0:
                        thisVodacomPortal = thisVodacomPortalList[0]

                    else:
                        thisVodacomPortal = SMSPortalVodacom()

                    findRequest = SMSPortalBudget.query()
                    thisBudgetPortalList = findRequest.fetch()

                    if len(thisBudgetPortalList) > 0:
                        thisBudgetPortal = thisBudgetPortalList[0]
                    else:
                        thisBudgetPortal = SMSPortalBudget()

                    template = template_env.get_template('templates/sms/groups/account.html')
                    context = {'thisSMSAccount':thisSMSAccount,'thisVodacomPortal':thisVodacomPortal,'thisBudgetPortal':thisBudgetPortal}
                    self.response.write(template.render(context))


        elif vstrChoice == "5":
            #+ '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                template = template_env.get_template('templates/sms/groups/reports.html')
                context = {}
                self.response.write(template.render(context))

class GroupManagerHandler(webapp2.RequestHandler):
    def get(self):
        URL = self.request.url
        URLlist = URL.split("/")
        strGroupID = URLlist[len(URLlist) - 1]

        #TODO- Highly Important consider securing the access here with a login name and password passed as parameters with the get method
        #TODO- This means this will work as an API
        findRequest = Groups.query(Groups.group_id == strGroupID)
        thisGroupList = findRequest.fetch()

        if len(thisGroupList) > 0:
            thisGroup = thisGroupList[0]
        else:
            thisGroup = Groups()

        template = template_env.get_template('templates/sms/thisGroup.html')
        context = {'thisGroup':thisGroup}
        self.response.write(template.render(context))

    def post(self):


        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                vstrGroupID = self.request.get('vstrGroupID')

                findRequest = SMSContacts.query(SMSContacts.group_id == vstrGroupID)
                thisContactList = findRequest.fetch()

                template = template_env.get_template('templates/sms/groups/upcontacts.html')
                context = {'thisContactList':thisContactList,'vstrGroupID':vstrGroupID}
                self.response.write(template.render(context))

        elif vstrChoice == "1":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrNames = self.request.get('vstrNames')
            vstrSurname = self.request.get('vstrSurname')
            vstrCellNumber = self.request.get('vstrCellNumber')

            URL = self.request.url
            URLlist = URL.split("/")
            vstrGroupID = URLlist[len(URLlist) - 1]

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                findRequest = SMSContacts.query(SMSContacts.group_id == vstrGroupID, SMSContacts.cell_number == vstrCellNumber)
                thisContactList = findRequest.fetch()

                if len(thisContactList) > 0:
                    thisContact = thisContactList[0]
                else:
                    thisContact = SMSContacts()


                thisContact.writeGroupID(strinput=vstrGroupID)
                thisContact.writeUserID(strinput=thisMainAccount.uid)
                thisContact.writeNames(strinput=vstrNames)
                thisContact.writeSurname(strinput=vstrSurname)
                thisContact.writeCellNumber(strinput=vstrCellNumber)

                thisContact.put()

                findRequest = Groups.query(Groups.group_id == vstrGroupID, Groups.organization_id == thisMainAccount.organization_id)
                thisGroupList = findRequest.fetch()

                if len(thisGroupList) > 0:
                    thisGroup = thisGroupList[0]
                else:
                    thisGroup = Groups()

                thisGroup.writeTotalNumbers(strinput=str(thisGroup.total_numbers + 1))
                thisGroup.put()

                self.response.write("Contact Successfully uploaded")

        elif vstrChoice == "2":

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrGroupID = self.request.get('vstrGroupID')

                findRequest = Messages.query(Messages.group_id == vstrGroupID)
                thisMessagesList = findRequest.fetch()

                template = template_env.get_template('templates/sms/groups/createmessage.html')
                context = {'thisMessagesList':thisMessagesList,'vstrGroupID':vstrGroupID}
                self.response.write(template.render(context))

        elif vstrChoice == "3":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrGroupID = self.request.get('vstrGroupID')
                vstrMessage = self.request.get('vstrMessage')

                thisMessage = Messages()
                thisMessage.writeGroupID(strinput=vstrGroupID)
                thisMessage.writeMessageID(strinput=thisMessage.CreateMessageID())
                thisMessage.writeMessage(strinput=vstrMessage)
                thisDate = datetime.datetime.now()
                thisDate = thisDate.date()

                thisTime = datetime.datetime.now()
                thisTime = thisTime.time()
                thisTime = datetime.time(hour=thisTime.hour,minute=thisTime.minute,second=thisTime.second)
                thisMessage.writeDateCreated(strinput=thisDate)
                thisMessage.writeTimeCreated(strinput=thisTime)


                thisMessage.put()
                self.response.write("Message Uploaded successfully")

        elif vstrChoice == "4":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                vstrGroupList = self.request.get('vstrGroupList')

                if len(vstrGroupList) > 0:
                    vstrGroupList = vstrGroupList.split(",")
                else:
                    vstrGroupList = []


                strAssigned = False
                for strGroupID in vstrGroupList:
                    thisSMSContacts = SMSContacts()


                    thisSMSContacts.writeUserID(strinput=thisMainAccount.uid)
                    thisSMSContacts.writeNames(strinput=thisMainAccount.strMemberNames)
                    thisSMSContacts.writeSurname(strinput=thisMainAccount.strMemberSurname)
                    thisSMSContacts.writeCellNumber(strinput=thisMainAccount.cell)
                    thisSMSContacts.writeGroupID(strinput=strGroupID)

                    thisSMSContacts.put()
                    findRequest = Groups.query(Groups.group_id == strGroupID)
                    thisGroupsList = findRequest.fetch()
                    if len(thisGroupsList) > 0:
                        thisGroup = thisGroupsList[0]
                    else:
                        thisGroup = Groups()

                    thisGroup.writeTotalNumbers(strinput=str(thisGroup.total_numbers + 1))
                    thisGroup.put()
                    strAssigned = True

                if not(strAssigned):
                    self.response.write("Church Member not assigned into Groups")
                else:
                    self.response.write("Church Member Subscribed to selected SMS Groups")

        elif vstrChoice == "5":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                vstrGroupID = self.request.get('vstrGroupID')

                findRequest = Groups.query(Groups.group_id == vstrGroupID, Groups.organization_id == thisMainAccount.organization_id)
                thisGroupList = findRequest.fetch()

                if len(thisGroupList) > 0:
                    thisGroup = thisGroupList[0]
                else:
                    thisGroup = Groups()

                findRequest = SMSContacts.query(SMSContacts.group_id == thisGroup.group_id)
                thisSMSContactsList = findRequest.fetch()

                template = template_env.get_template('templates/sms/groups/editGroup.html')
                context = {'thisGroup':thisGroup,'thisSMSContactsList':thisSMSContactsList}
                self.response.write(template.render(context))

        elif vstrChoice == "6":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrGroupID = self.request.get('vstrGroupID')
                vstrGroupName = self.request.get('vstrGroupName')
                vstrGroupDescription = self.request.get('vstrGroupDescription')

                findRequest = Groups.query(Groups.group_id == vstrGroupID)
                thisGroupList = findRequest.fetch()

                if len(thisGroupList) > 0:
                    thisGroup = thisGroupList[0]
                else:
                    thisGroup = Groups()

                thisGroup.writeGroupName(strinput=vstrGroupName)
                thisGroup.writeGroupDescription(strinput=vstrGroupDescription)
                thisGroup.put()

                self.response.write("SMS Group Successfully updated")

        elif vstrChoice == "7":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                vstrGroupID = self.request.get('vstrGroupID')

                findRequest = Groups.query(Groups.group_id == vstrGroupID, Groups.organization_id == thisMainAccount.organization_id)
                thisGroupList = findRequest.fetch()

                if len(thisGroupList) > 0:
                    thisGroup = thisGroupList[0]
                else:
                    thisGroup = Groups()

                template = template_env.get_template('templates/sms/groups/deleteGroup.html')
                context = {'thisGroup':thisGroup}
                self.response.write(template.render(context))

        elif vstrChoice == "8":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')


            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                vstrGroupID = self.request.get('vstrGroupID')


                findRequest = Groups.query(Groups.group_id == vstrGroupID, Groups.organization_id == thisMainAccount.organization_id)
                thisGroupList = findRequest.fetch()

                for thisGroup in thisGroupList:
                    thisGroup.key.delete()

                findRequest = SMSContacts.query(SMSContacts.group_id == vstrGroupID)
                thisContactList = findRequest.fetch()

                for thisContact in thisContactList:
                    thisContact.key.delete()

                self.response.write("SMS Group Successfully Deleted")

        elif vstrChoice == "9":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrGroupID = self.request.get('vstrGroupID')
                vstrContacts = self.request.get('vstrContacts')
                logging.info(vstrContacts)

                vstrContactList = vstrContacts.split("|")

                for vstrContact in vstrContactList :
                    if len(vstrContact) > 10:
                        try:
                            vstrConList = vstrContact.split(",")
                            vstrCell = vstrConList[0]
                            vstrCell = vstrCell.strip()

                            if vstrCell.startswith('0'):
                                pass
                            else:
                                vstrCell = "0" + vstrCell

                            vstrFirstname = vstrConList[1]
                            vstrFirstname = vstrFirstname.strip()
                            vstrSurname = vstrConList[2]
                            vstrSurname = vstrSurname.strip()

                            findRequest = SMSContacts.query(SMSContacts.cell_number == vstrCell, SMSContacts.group_id == vstrGroupID)
                            thisContactList = findRequest.fetch()

                            if len(thisContactList) > 0:
                                thisContact = thisContactList[0]
                            else:
                                thisContact = SMSContacts()

                            thisContact.writeCellNumber(strinput=vstrCell)
                            thisContact.writeGroupID(strinput=vstrGroupID)
                            thisContact.writeNames(strinput=vstrFirstname)
                            thisContact.writeSurname(strinput=vstrSurname)
                            thisContact.writeUserID(strinput=thisMainAccount.uid)
                            thisContact.put()

                            findRequest = Groups.query(Groups.organization_id == thisMainAccount.organization_id, Groups.group_id == vstrGroupID)
                            thisGroupList = findRequest.fetch()

                            if len(thisGroupList) > 0:
                                thisGroup = thisGroupList[0]
                                thisGroup.writeTotalNumbers(strinput=str(thisGroup.total_numbers + 1))
                                thisGroup.put()
                        except:
                            pass


        elif vstrChoice == "10":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrGroupID = self.request.get('vstrGroupID')

                findRequest = DeliveryReport.query(DeliveryReport.group_id == vstrGroupID)
                thisDeliveryReportList = findRequest.fetch()

                template  =template_env.get_template('templates/sms/groups/groupreports.html')
                context = {'thisDeliveryReportList':thisDeliveryReportList}
                self.response.write(template.render(context))

        elif vstrChoice == "11":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrGroupID = self.request.get('vstrGroupID')
                vstrRemoveCell = self.request.get('vstrRemoveCell')

                findRequest = SMSContacts.query(SMSContacts.group_id == vstrGroupID, SMSContacts.cell_number == vstrRemoveCell)
                thisSMSContactsList = findRequest.fetch()

                for thisContact in thisSMSContactsList:
                    thisContact.key.delete()
                self.response.write("Successfully delete contact")

class thisSMSManagerHandler(webapp2.RequestHandler):
    def get(self):


        URL = self.request.url
        URLlist = URL.split("/")
        vstrMessageID = URLlist[len(URLlist) - 1]

        findRequest = Messages.query(Messages.message_id == vstrMessageID)
        thisMessageList = findRequest.fetch()

        if len(thisMessageList) > 0:
            thisMessage = thisMessageList[0]
        else:
            thisMessage = Messages()


        findRequest = Groups.query(Groups.group_id == thisMessage.group_id)
        thisGroupList = findRequest.fetch()

        if len(thisGroupList) > 0:
            thisGroup = thisGroupList[0]
        else:
            thisGroup = Groups()

        template = template_env.get_template('templates/sms/groups/thisMessage.html')
        context = {'thisMessage':thisMessage,'thisGroup':thisGroup}
        self.response.write(template.render(context))

    def post(self):

        from accounts import Organization,Accounts
        from myemail import SendEmail
        from myTwilio import MyTwilioPortal
        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                vstrMessageID = self.request.get('vstrMessageID')
                vstrGroupID = self.request.get('vstrGroupID')

                findRequest = Messages.query(Messages.message_id == vstrMessageID, Messages.group_id == vstrGroupID)
                thisMessageList = findRequest.fetch()

                if len(thisMessageList) > 0:
                    thisMessage = thisMessageList[0]
                else:
                    thisMessage  = Messages()

                template = template_env.get_template('templates/sms/groups/message/editsms.html')
                context = {'thisMessage':thisMessage,'vstrMessageID':vstrMessageID,'vstrGroupID':vstrGroupID}
                self.response.write(template.render(context))

        elif vstrChoice == "1":
            #TODO- Make sure to get the login details here
            vstrGroupID = self.request.get('vstrGroupID')
            vstrMessageID = self.request.get('vstrMessageID')
            vstrMessage = self.request.get('vstrMessage')

            findRequest = Messages.query(Messages.message_id == vstrMessageID, Messages.group_id == vstrGroupID)
            thisMessageList = findRequest.fetch()

            if len(thisMessageList) > 0:
                thisMessage = thisMessageList[0]
            else:
                thisMessage  = Messages()

            thisMessage.writeMessage(strinput=vstrMessage)
            thisMessage.put()
            self.response.write("Successfully updated Message")

        elif vstrChoice == "2":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrGroupID = self.request.get('vstrGroupID')
                vstrMessageID = self.request.get('vstrMessageID')

                findRequest = MessageSchedule.query(MessageSchedule.message_id == vstrMessageID)
                thisMessageScheduleList = findRequest.fetch()

                if len(thisMessageScheduleList) > 0:
                    thisMessageSchedule = thisMessageScheduleList[0]
                else:
                    thisMessageSchedule = MessageSchedule()



                template = template_env.get_template('templates/sms/groups/message/schedule.html')
                context = {'thisMessageSchedule':thisMessageSchedule,'vstrGroupID':vstrGroupID,'vstrMessageID':vstrMessageID}
                self.response.write(template.render(context))

        elif vstrChoice == "3":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrGroupID = self.request.get('vstrGroupID')
                vstrMessageID = self.request.get('vstrMessageID')
                vstrScheduleTime = self.request.get('vstrScheduleTime')
                vstrNotifyOnStart = self.request.get('vstrNotifyOnStart')
                vstrNotifyOnEnd = self.request.get('vstrNotifyOnEnd')


                findRequest = MessageSchedule.query(MessageSchedule.message_id == vstrMessageID)
                thisMessageScheduleList = findRequest.fetch()

                if len(thisMessageScheduleList) > 0:
                    thisMessageSchedule = thisMessageScheduleList[0]
                else:
                    thisMessageSchedule = MessageSchedule()
                try:
                    logging.info("THIS IS WHAT I AM GETTING : " + vstrScheduleTime)
                    vstrScheduleTime = vstrScheduleTime.split("-")
                    vstrBeginDateTime = vstrScheduleTime[0]
                    vstrEndDateTime = vstrScheduleTime[1]

                    vstrBeginDateTime = vstrBeginDateTime.strip()
                    vstrEndDateTime = vstrEndDateTime.strip()

                    vstrBeginDateTimeList = vstrBeginDateTime.split(" ")
                    vstrEndDateTimeList = vstrEndDateTime.split(" ")

                    vstrBeginDate = vstrBeginDateTimeList[0]
                    vstrBeginTime = vstrBeginDateTimeList[1]

                    vstrEndDate = vstrEndDateTimeList[0]
                    vstrEndTime = vstrEndDateTimeList[1]

                    vstrBeginDateList = vstrBeginDate.split("/")
                    vstrBeginTimeList = vstrBeginTime.split(":")

                    vstrBeginDay = vstrBeginDateList[1]
                    vstrBeginMonth = vstrBeginDateList[0]
                    vstrBeginYear = vstrBeginDateList[2]
                    vstrBeginHour = vstrBeginTimeList[0]
                    vstrBeginMinute = vstrBeginTimeList[1]
                    vstrBeginSecond = 0

                    vstrEndDateList = vstrEndDate.split("/")
                    vstrEndTimeList = vstrEndTime.split(":")

                    vstrEndDay = vstrEndDateList[1]
                    vstrEndMonth = vstrEndDateList[0]
                    vstrEndYear = vstrEndDateList[2]
                    vstrEndHour = vstrEndTimeList[0]
                    vstrEndMinute = vstrEndTimeList[1]
                    vstrEndSecond = 0

                    vstrBeginDate = datetime.date(year=int(vstrBeginYear),month=int(vstrBeginMonth),day=int(vstrBeginDay))
                    vstrBeginTime = datetime.time(hour=int(vstrBeginHour),minute=int(vstrBeginMinute),second=vstrBeginSecond)
                    vstrEndDate = datetime.date(year=int(vstrEndYear),month=int(vstrEndMonth),day=int(vstrEndDay))
                    vstrEndTime = datetime.time(hour=int(vstrEndHour),minute=int(vstrEndMinute),second=int(vstrEndSecond))
                except:
                    strToday = datetime.datetime.now()
                    strThisDate = strToday.date()
                    strThisTime = strToday.time()
                    vstrEndTime = strThisTime


                    strThisTime += datetime.timedelta(minutes=15)
                    vstrBeginDate = strThisDate
                    vstrBeginTime = strThisTime
                    vstrEndDate = strThisDate
                    vstrEndTime += datetime.timedelta(minutes=135)

                thisMessageSchedule.writeMessageID(strinput=vstrMessageID)
                thisMessageSchedule.writeStartDate(strinput=vstrBeginDate)
                thisMessageSchedule.writeStartTime(strinput=vstrBeginTime)
                thisMessageSchedule.writeEndDate(strinput=vstrEndDate)
                thisMessageSchedule.writeEndTime(strinput=vstrEndTime)
                if vstrNotifyOnStart == "Yes":
                    thisMessageSchedule.writeNotifyOnStart(strinput=True)
                else:
                    thisMessageSchedule.writeNotifyOnStart(strinput=False)

                if vstrNotifyOnEnd == "No":
                    thisMessageSchedule.writeNotifyonEnd(strinput=True)
                else:
                    thisMessageSchedule.writeNotifyonEnd(strinput=False)

                thisMessageSchedule.writeUserID(strinput=vstrUserID)

                thisMessageSchedule.put()

                self.response.write("Successfully created Schedule")
        elif vstrChoice == "4":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrGroupID = self.request.get('vstrGroupID')
                vstrMessageID = self.request.get('vstrMessageID')

                findRequest = Messages.query(Messages.message_id == vstrMessageID, Messages.group_id == vstrGroupID)
                thisMessagesList = findRequest.fetch()
                if len(thisMessagesList) > 0:
                    thisMessage = thisMessagesList[0]
                else:
                    thisMessage = Messages()

                findRequest = Groups.query(Groups.group_id == vstrGroupID)
                thisGroupList = findRequest.fetch()

                if len(thisGroupList) > 0:
                    thisGroup = thisGroupList[0]
                else:
                    thisGroup = Groups()

                findRequest = SMSContacts.query(SMSContacts.group_id == vstrGroupID)
                thisSMSContactsList = findRequest.fetch()

                findRequest = SMSAccount.query(SMSAccount.organization_id == thisGroup.organization_id)
                thisSMSAccountList = findRequest.fetch()
                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]
                else:
                    thisSMSAccount = SMSAccount()


                template = template_env.get_template('templates/sms/groups/message/sendSMS.html')
                context = {'thisMessage':thisMessage,'thisGroup':thisGroup,'thisSMSContactsList':thisSMSContactsList,'thisSMSAccount':thisSMSAccount}
                self.response.write(template.render(context))

        elif vstrChoice == "5":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                vstrGroupID = self.request.get('vstrGroupID')
                vstrMessageID = self.request.get('vstrMessageID')


                findRequest = Messages.query(Messages.message_id == vstrMessageID, Messages.group_id == vstrGroupID)
                thisMessagesList = findRequest.fetch()
                if len(thisMessagesList) > 0:
                    thisMessage = thisMessagesList[0]
                else:
                    thisMessage = Messages()

                findRequest = Groups.query(Groups.group_id == vstrGroupID)
                thisGroupList = findRequest.fetch()

                if len(thisGroupList) > 0:
                    thisGroup = thisGroupList[0]
                else:
                    thisGroup = Groups()


                findRequest = SMSContacts.query(SMSContacts.group_id == vstrGroupID)
                thisSMSContactsList = findRequest.fetch()

                findRequest = SMSAccount.query(SMSAccount.organization_id == thisGroup.organization_id)
                thisSMSAccountList = findRequest.fetch()
                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]
                else:
                    thisSMSAccount = SMSAccount()


                findRequest = Organization.query(Organization.strVerified == True, Organization.strOrganizationID == thisSMSAccount.organization_id)
                thisOrgList = findRequest.fetch()

                if len(thisOrgList) > 0:
                    if thisSMSAccount.use_portal == "Vodacom":

                        findRequest = SMSPortalVodacom.query()
                        thisPortalList = findRequest.fetch()

                        if len(thisPortalList) > 0:
                            thisPortal = thisPortalList[0]
                        else:
                            thisPortal = SMSPortalVodacom()

                        i = 0
                        self.response.write("""
                        <table id="SentTable" class="table table-bordered table-striped"><thead>
                                <tr>
                                    <td>Names</td>
                                    <td>Surname</td>
                                    <td>Cell</td>
                                    <td>Status</td>
                                </tr>
                            </thead>
                            <tbody>
                        """)
                        while (thisSMSAccount.total_sms > 0) and (i < len(thisSMSContactsList)):
                            thisContact = thisSMSContactsList[i]

                            thisMessage = SendEmail(strFrom=thisPortal.sender_address, strTo=thisPortal.email_address, strSubject=thisContact.cell_number, strBody=thisMessage.message, strTextType="text/plain")
                            if thisMessage == True:
                                self.response.write(""" <tr> <td> """ + thisContact.names + """</td><td> """ + thisContact.surname + """</td><td>""" + thisContact.cell_number + """</td><td> <span class="label label-success">Sent</span> </td></tr>""")
                                i = i + 1

                                thisPortal.available_credit = thisPortal.available_credit - 1
                                thisDeliveryReport = DeliveryReport()
                                thisDeliveryReport.writeGroupID(thisGroup.group_id)
                                thisDeliveryReport.writeOrganizationID(strinput=thisSMSAccount.organization_id)
                                thisDeliveryReport.writeCell(thisContact.cell_number)
                                thisDeliveryReport.writeDelivered(strinput=True)
                                thisDate = datetime.datetime.now()
                                strThisDate = thisDate.date()
                                strThisTime = thisDate.time()
                                strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,second=strThisTime.second)
                                thisDeliveryReport.writeDate(strinput=strThisDate)
                                thisDeliveryReport.writeTime(strinput=strThisTime)
                                thisDeliveryReport.writeMessageID(strinput=thisMessage.message_id)
                                thisDeliveryReport.put()

                            else:
                                pass

                        self.response.write("""</tbody><tfoot><tr>
                                <tr>
                                    <td>Names</td>
                                    <td>Surname</td>
                                    <td>Cell</td>
                                    <td>Status</td>
                                </tr>
                                </tfoot>
                                </table>
                        """)
                        thisPortal.put()
                        i = i + 1
                        thisSMSAccount.total_sms = thisSMSAccount.total_sms - (i)
                        thisSMSAccount.put()
                        thisMessage.writeSubmitted(strinput=True)

                        thisDate = datetime.datetime.now()
                        strThisDate = thisDate.date()
                        strThisTime = thisDate.time()
                        strThisTime = datetime.time(hour=strThisTime.hour,minute=strThisTime.minute,second=strThisTime.second)
                        thisMessage.writeDateSubmitted(strinput=strThisDate)
                        thisMessage.writeTimeSubmitted(strinput=strThisTime)
                        thisMessage.put()
                    elif thisSMSAccount.use_portal == "Budget":
                        findRequest = SMSPortalBudget.query()
                        thisBudgetPortalList = findRequest.fetch()

                        if len(thisBudgetPortalList) > 0:
                            thisBudgetPortal = thisBudgetPortalList[0]
                        else:
                            thisBudgetPortal = SMSPortalBudget()

                        i = 0
                        self.response.write("""
                        <table id="SentTable" class="table table-bordered table-striped">
                            <thead>
                                <tr>
                                    <td>Names</td>
                                    <td>Surname</td>
                                    <td>Cell</td>
                                    <td>Status</td>
                                </tr>
                            </thead>
                            <tbody>
                        """)
                        while (thisSMSAccount.total_sms > 0) and (i < len(thisSMSContactsList)):
                            try:
                                thisContact = thisSMSContactsList[i]
                                thisDate = datetime.datetime.now()
                                thisDate = thisDate.date()

                                result = thisBudgetPortal.SendCronMessage(strMessage=thisMessage.message, strCell=thisContact.cell_number)
                                if result == None:
                                    isSent = False
                                    self.response.write("""<tr> <td> """ + thisContact.names + """</td><td> """ + thisContact.surname + """</td><td>""" + thisContact.cell_number + """</td><td> <span class="label label-danger">Not Sent</span> </td></tr>""")
                                else:
                                    isSent = True
                                    logging.info("THIS IS THE RETURNED RESULT : " + str(result))
                                    self.response.write("""<tr> <td> """ + thisContact.names + """</td><td> """ + thisContact.surname + """</td><td>""" + thisContact.cell_number + """</td><td> <span class="label label-success">Sent</span> </td></tr>""")

                                if isSent:
                                    i = i + 1
                                    thisBudgetPortal.available_credit = thisBudgetPortal.available_credit - 1
                                    thisDeliveryReport = DeliveryReport()
                                    thisDeliveryReport.writeGroupID(thisGroup.group_id)
                                    thisDeliveryReport.writeOrganizationID(strinput=thisSMSAccount.organization_id)
                                    thisDeliveryReport.writeCell(thisContact.cell_number)
                                    thisDeliveryReport.writeDelivered(strinput=True)
                                    thisDate = datetime.datetime.now()
                                    strThisDate = thisDate.date()
                                    strThisTime = thisDate.time()
                                    strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,
                                                                second=strThisTime.second)
                                    thisDeliveryReport.writeDate(strinput=strThisDate)
                                    thisDeliveryReport.writeTime(strinput=strThisTime)
                                    thisDeliveryReport.writeMessageID(strinput=thisMessage.message_id)
                                    thisDeliveryReport.writeReference(strinput=result)
                                    thisDeliveryReport.put()
                                else:
                                    i = i + 1
                                    #thisBudgetPortal.available_credit = thisBudgetPortal.available_credit - 1
                                    thisDeliveryReport = DeliveryReport()
                                    thisDeliveryReport.writeGroupID(thisGroup.group_id)
                                    thisDeliveryReport.writeOrganizationID(strinput=thisSMSAccount.organization_id)
                                    thisDeliveryReport.writeCell(thisContact.cell_number)
                                    thisDeliveryReport.writeDelivered(strinput=False)
                                    thisDate = datetime.datetime.now()
                                    strThisDate = thisDate.date()
                                    strThisTime = thisDate.time()
                                    strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,
                                                                second=strThisTime.second)
                                    thisDeliveryReport.writeDate(strinput=strThisDate)
                                    thisDeliveryReport.writeTime(strinput=strThisTime)
                                    thisDeliveryReport.writeMessageID(strinput=thisMessage.message_id)
                                    thisDeliveryReport.put()
                                thisSMSAccount.total_sms = thisSMSAccount.total_sms - 1
                            except:
                                thisSMSAccount.total_sms = thisSMSAccount.total_sms - 1
                                i = i + 1

                        thisSMSAccount.put()

                        self.response.write("""</tbody><tfoot><tr>
                                <tr>
                                    <td>Names</td>
                                    <td>Surname</td>
                                    <td>Cell</td>
                                    <td>Status</td>
                                </tr>
                                </tfoot>
                                </table>
                        """)
                        thisBudgetPortal.put()
                        i = i + 1
                        thisMessage.writeSubmitted(strinput=True)

                        thisDate = datetime.datetime.now()
                        strThisDate = thisDate.date()
                        strThisTime = thisDate.time()
                        strThisTime = datetime.time(hour=strThisTime.hour,minute=strThisTime.minute,second=strThisTime.second)
                        thisMessage.writeDateSubmitted(strinput=strThisDate)
                        thisMessage.writeTimeSubmitted(strinput=strThisTime)
                        thisMessage.put()

                    elif thisSMSAccount.use_portal == "ClickSend":
                        findRequest = ClickSendSMSPortal.query()
                        thisClickSendSMSList = findRequest.fetch()

                        if len(thisClickSendSMSList) > 0:
                            thisClickSendSMS = thisClickSendSMSList[0]
                        else:
                            thisClickSendSMS = ClickSendSMSPortal()


                        i = 0
                        self.response.write("""
                        <table id="SentTable" class="table table-bordered table-striped">
                            <thead>
                                <tr>
                                    <td>Names</td>
                                    <td>Surname</td>
                                    <td>Cell</td>
                                    <td>Status</td>
                                </tr>
                            </thead>
                            <tbody>
                        """)
                        while (thisSMSAccount.total_sms > 0) and (i < len(thisSMSContactsList)):
                            try:
                                thisContact = thisSMSContactsList[i]
                                thisDate = datetime.datetime.now()
                                thisDate = thisDate.date()

                                result = thisClickSendSMS.SendSMS(strCell=thisContact.cell_number, strMessage=thisMessage.message)

                                if result == None:
                                    isSent = False
                                    self.response.write(
                                        """<tr> <td> """ + thisContact.names + """</td><td> """ + thisContact.surname + """</td><td>""" + thisContact.cell_number + """</td><td> <span class="label label-danger">Not Sent</span> </td></tr>""")
                                else:
                                    isSent = True
                                    logging.info("THIS IS THE RETURNED RESULT : " + str(result))
                                    self.response.write("""<tr> <td> """ + thisContact.names + """</td><td> """ + thisContact.surname + """</td><td>""" + thisContact.cell_number + """</td><td> <span class="label label-success">Sent</span> </td></tr>""")

                                if isSent:
                                    i = i + 1

                                    thisDeliveryReport = DeliveryReport()
                                    thisDeliveryReport.writeGroupID(thisGroup.group_id)
                                    thisDeliveryReport.writeOrganizationID(strinput=thisSMSAccount.organization_id)
                                    thisDeliveryReport.writeCell(thisContact.cell_number)
                                    thisDeliveryReport.writeDelivered(strinput=True)
                                    thisDate = datetime.datetime.now()
                                    strThisDate = thisDate.date()
                                    strThisTime = thisDate.time()
                                    strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,
                                                                second=strThisTime.second)
                                    thisDeliveryReport.writeDate(strinput=strThisDate)
                                    thisDeliveryReport.writeTime(strinput=strThisTime)
                                    thisDeliveryReport.writeMessageID(strinput=thisMessage.message_id)
                                    thisDeliveryReport.writeReference(strinput=result)
                                    thisDeliveryReport.put()
                                else:
                                    i = i + 1
                                    #thisBudgetPortal.available_credit = thisBudgetPortal.available_credit - 1
                                    thisDeliveryReport = DeliveryReport()
                                    thisDeliveryReport.writeGroupID(thisGroup.group_id)
                                    thisDeliveryReport.writeOrganizationID(strinput=thisSMSAccount.organization_id)
                                    thisDeliveryReport.writeCell(thisContact.cell_number)
                                    thisDeliveryReport.writeDelivered(strinput=False)
                                    thisDate = datetime.datetime.now()
                                    strThisDate = thisDate.date()
                                    strThisTime = thisDate.time()
                                    strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,
                                                                second=strThisTime.second)
                                    thisDeliveryReport.writeDate(strinput=strThisDate)
                                    thisDeliveryReport.writeTime(strinput=strThisTime)
                                    thisDeliveryReport.writeMessageID(strinput=thisMessage.message_id)
                                    thisDeliveryReport.put()
                                thisSMSAccount.total_sms = thisSMSAccount.total_sms - 1
                            except:
                                thisSMSAccount.total_sms = thisSMSAccount.total_sms - 1
                                i = i + 1


                        thisSMSAccount.put()

                        self.response.write("""</tbody><tfoot><tr>
                                <tr>
                                    <td>Names</td>
                                    <td>Surname</td>
                                    <td>Cell</td>
                                    <td>Status</td>
                                </tr>
                                </tfoot>
                                </table>
                        """)

                        i = i + 1
                        thisMessage.writeSubmitted(strinput=True)

                        thisDate = datetime.datetime.now()
                        strThisDate = thisDate.date()
                        strThisTime = thisDate.time()
                        strThisTime = datetime.time(hour=strThisTime.hour,minute=strThisTime.minute,second=strThisTime.second)
                        thisMessage.writeDateSubmitted(strinput=strThisDate)
                        thisMessage.writeTimeSubmitted(strinput=strThisTime)
                        thisMessage.put()

                    elif thisSMSAccount.use_portal == "Twilio":
                        findRequest = MyTwilioPortal.query()
                        thisTwilioPortalList = findRequest.fetch()

                        if len(thisTwilioPortalList) > 0:
                            thisTwilioPortal = thisTwilioPortalList[0]
                        else:
                            thisTwilioPortal = MyTwilioPortal()

                        i = 0
                        self.response.write("""
                        <table id="SentTable" class="table table-bordered table-striped">
                            <thead>
                                <tr>
                                    <td>Names</td>
                                    <td>Surname</td>
                                    <td>Cell</td>
                                    <td>Status</td>
                                </tr>
                            </thead>
                            <tbody>
                        """)
                        while (thisSMSAccount.total_sms > 0) and (i < len(thisSMSContactsList)):
                            try:
                                thisContact = thisSMSContactsList[i]
                                thisDate = datetime.datetime.now()
                                thisDate = thisDate.date()

                                result = thisTwilioPortal.sendSMS(strTo=thisContact.cell_number, strFrom=thisTwilioPortal.strMySMSNumber, strMessage=thisMessage.message)

                                if result == None:
                                    isSent = False
                                    self.response.write(
                                        """<tr> <td> """ + thisContact.names + """</td><td> """ + thisContact.surname + """</td><td>""" + thisContact.cell_number + """</td><td> <span class="label label-danger">Not Sent</span> </td></tr>""")
                                else:
                                    isSent = True
                                    logging.info("THIS IS THE RETURNED RESULT : " + str(result))
                                    self.response.write(
                                        """<tr> <td> """ + thisContact.names + """</td><td> """ + thisContact.surname + """</td><td>""" + thisContact.cell_number + """</td><td> <span class="label label-success">Sent</span> </td></tr>""")

                                if isSent:
                                    i = i + 1

                                    thisDeliveryReport = DeliveryReport()
                                    thisDeliveryReport.writeGroupID(thisGroup.group_id)
                                    thisDeliveryReport.writeOrganizationID(strinput=thisSMSAccount.organization_id)
                                    thisDeliveryReport.writeCell(thisContact.cell_number)
                                    thisDeliveryReport.writeDelivered(strinput=True)
                                    thisDate = datetime.datetime.now()
                                    strThisDate = thisDate.date()
                                    strThisTime = thisDate.time()
                                    strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,
                                                                second=strThisTime.second)
                                    thisDeliveryReport.writeDate(strinput=strThisDate)
                                    thisDeliveryReport.writeTime(strinput=strThisTime)
                                    thisDeliveryReport.writeMessageID(strinput=thisMessage.message_id)
                                    thisDeliveryReport.writeReference(strinput=result)
                                    thisDeliveryReport.put()
                                else:
                                    i = i + 1
                                    # thisBudgetPortal.available_credit = thisBudgetPortal.available_credit - 1
                                    thisDeliveryReport = DeliveryReport()
                                    thisDeliveryReport.writeGroupID(thisGroup.group_id)
                                    thisDeliveryReport.writeOrganizationID(strinput=thisSMSAccount.organization_id)
                                    thisDeliveryReport.writeCell(thisContact.cell_number)
                                    thisDeliveryReport.writeDelivered(strinput=False)
                                    thisDate = datetime.datetime.now()
                                    strThisDate = thisDate.date()
                                    strThisTime = thisDate.time()
                                    strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,
                                                                second=strThisTime.second)
                                    thisDeliveryReport.writeDate(strinput=strThisDate)
                                    thisDeliveryReport.writeTime(strinput=strThisTime)
                                    thisDeliveryReport.writeMessageID(strinput=thisMessage.message_id)
                                    thisDeliveryReport.put()
                                thisSMSAccount.total_sms = thisSMSAccount.total_sms - 1
                            except:
                                thisSMSAccount.total_sms = thisSMSAccount.total_sms - 1
                                i = i + 1

                        thisSMSAccount.put()

                        self.response.write("""</tbody><tfoot><tr>
                                <tr>
                                    <td>Names</td>
                                    <td>Surname</td>
                                    <td>Cell</td>
                                    <td>Status</td>
                                </tr>
                                </tfoot>
                                </table>
                        """)

                        i = i + 1
                        thisMessage.writeSubmitted(strinput=True)

                        thisDate = datetime.datetime.now()
                        strThisDate = thisDate.date()
                        strThisTime = thisDate.time()
                        strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,
                                                    second=strThisTime.second)
                        thisMessage.writeDateSubmitted(strinput=strThisDate)
                        thisMessage.writeTimeSubmitted(strinput=strThisTime)
                        thisMessage.put()

                else:
                    self.response.write("Please verify your organization before sending SMS Messages")

        elif vstrChoice == "6":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrGroupID = self.request.get('vstrGroupID')
                vstrMessageID = self.request.get('vstrMessageID')

                findRequest = DeliveryReport.query(DeliveryReport.group_id == vstrGroupID, DeliveryReport.message_id == vstrMessageID, DeliveryReport.response_received == True)
                thisDeliveryReportList = findRequest.fetch()

                template = template_env.get_template('templates/sms/groups/responses/responseslist.html')
                context = {'thisDeliveryReportList':thisDeliveryReportList}
                self.response.write(template.render(context))




class BuyCreditsHandler(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):


        from dashboard import Employees,AccountDetails
        from accounts import Organization
        from myTwilio import MyTwilioPortal

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            #+ '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')


            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrOrganizationID = self.request.get('vstrOrganizationID')
                vstrSMSPackages = self.request.get('vstrSMSPackages')
                vstrDepositAmount = self.request.get('vstrDepositAmount')
                vstrDepositMethod = self.request.get('vstrDepositMethod')

                findRequest = SMSAccount.query(SMSAccount.organization_id == thisMainAccount.organization_id)
                thisSMSAccountList = findRequest.fetch()

                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]
                    thisSMSAccount.writeDepositReference(strinput=thisSMSAccount.CreateDepositReference())
                    thisSMSAccount.put()

                    thisDepositAccount = AccountDetails()
                    if vstrDepositMethod == "Direct Deposit":
                        templates = template_env.get_template('templates/sms/groups/deposits/direct.html')
                        context = {'thisSMSAccount':thisSMSAccount,'thisAccount':thisMainAccount,'vstrSMSPackages':vstrSMSPackages,'vstrDepositAmount':vstrDepositAmount,'thisDepositAccount':thisDepositAccount}
                        self.response.write(templates.render(context))
                    elif vstrDepositMethod == "PAYPAL":
                        templates = template_env.get_template('templates/sms/groups/deposits/paypal.html')
                        context = {'thisSMSAccount':thisSMSAccount,'thisAccount':thisMainAccount,'vstrSMSPackages':vstrSMSPackages,'vstrDepositAmount':vstrDepositAmount}
                        self.response.write(templates.render(context))

                    elif vstrDepositMethod == "EFT":
                        templates = template_env.get_template('templates/sms/groups/deposits/eft.html')
                        context = {'thisSMSAccount':thisSMSAccount,'thisAccount':thisMainAccount,'vstrSMSPackages':vstrSMSPackages,'vstrDepositAmount':vstrDepositAmount}
                        self.response.write(templates.render(context))

        elif vstrChoice == "1":
            #+ '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrOrganizationID = self.request.get('vstrOrganizationID')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = SMSAccount.query(SMSAccount.organization_id == vstrOrganizationID)
                thisSMSAccountList = findRequest.fetch()

                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]

                    findRequest = Employees.query()
                    thisBankAccountList = findRequest.fetch()

                    if len(thisBankAccountList) > 0:
                        thisBankAccount = thisBankAccountList[0]
                    else:
                        thisBankAccount = Employees()

                    strMessage = ""
                    strAccountNumber = "Account Holder : " + thisBankAccount.strAccountHolder + "%0A"
                    strBankName = "Bank Name : " + thisBankAccount.strBankName + "%0A"
                    strBranchName = "Branch Name : " + thisBankAccount.strBranchName + "%0A"
                    strBranchCode = "Branch Code : " + thisBankAccount.strBranchCode  + "%0A"
                    strDepositReference = "Reference : " + thisSMSAccount.deposit_reference + "%0A"

                    strMessage = strAccountNumber + strBankName + strBranchName + strBranchCode  + strDepositReference

                    findRequest = Organization.query(Organization.strOrganizationID == vstrOrganizationID)
                    thisOrganizationList = findRequest.fetch()

                    if len(thisOrganizationList) > 0:
                        thisOrganization = thisOrganizationList[0]


                        if thisOrganization.verified:

                            if thisSMSAccount.use_portal == "Vodacom":
                                findRequest = SMSPortalVodacom.query()
                                thisVodaPortalList = findRequest.fetch()
                                if len(thisVodaPortalList) > 0:
                                    thisVodaPortal = thisVodaPortalList[0]
                                else:
                                    thisVodaPortal = SMSPortalVodacom()
                                RecipientList = []
                                RecipientList.append(thisOrganization.cell)
                                if thisVodaPortal.CronSendMessages(strCellNumberList=RecipientList, strMessage=strMessage, strAccountID=thisBankAccount.staff_id):
                                    self.response.write("Successfully sent banking details to your mobile phone")
                                else:
                                    self.response.write("Error sending banking details to mobile please try again later")

                            elif thisSMSAccount.use_portal == "Budget":
                                findRequest = SMSPortalBudget.query()
                                thisBudgetPortalList = findRequest.fetch()
                                if len(thisBudgetPortalList) > 0:
                                    thisBudgetPortal = thisBudgetPortalList[0]
                                else:
                                    thisBudgetPortal = SMSPortalBudget()

                                if not(thisBudgetPortal.SendCronMessage(strMessage=strMessage, strCell=thisOrganization.cell) == None):
                                    self.response.write("Successfully sent banking details to your mobile phone")
                                else:
                                    self.response.write("Error sending banking details to mobile please try again later")

                            elif thisSMSAccount.use_portal == "ClickSend":
                                findRequest = ClickSendSMSPortal.query()
                                thisClickSendList = findRequest.fetch()

                                if len(thisClickSendList) > 0:
                                    thisClickSend = thisClickSendList[0]
                                else:
                                    thisClickSend = ClickSendSMSPortal()

                                    strResult = thisClickSend.SendSMS(strCell=thisOrganization.cell, strMessage=strMessage)

                                    if strResult != None:
                                        self.response.write("Successfully sent Banking Details to your mobile phone")
                                    else:
                                        self.response.write("Error sending Banking Details to mobile please try again later")


                            elif thisSMSAccount.use_portal == "Twilio":
                                findRequest = MyTwilioPortal.query()
                                thisTwilioList = findRequest.fetch()

                                if len(thisTwilioList) > 0:
                                    thisTwilio = thisTwilioList[0]
                                else:
                                    thisTwilio = MyTwilioPortal()

                                strResult = thisTwilio.sendSMS(strTo=thisOrganization.cell, strFrom=thisTwilio.strMySMSNumber, strMessage=strMessage)

                                if strResult != None:
                                    self.response.write("Successfully sent Banking Details to your mobile phone")
                                else:
                                    self.response.write("Error sending Banking Details to mobile please try again later")

                        else:
                            self.response.write("Please verify your organization before you can purchase any SMS Credit")
                    else:
                        self.response.write("Please create you organization account before purchasing any credit")


def HandleSMSPushReply(strFromCell,strReply,strOriginalMessage,strOriginalMessageID,strOriginalSenderID):
    """
    Handle this Reply here
    :param strFromCell:
    :param strReply:
    :param strOriginalMessage:
    :param strOriginalMessageID:
    :param strOriginalSenderID:
    :return:
    """
    logging.info("SMS PUSH REPLIES WORKS here is the reply message : " + strReply)

def HandleDeliveryReports(strMessageID,strStatus,strStatusCode,strCustomString):
    """

    :param strMessageID: the id of the original message sent
    :param strStatus:  the status of the message either DELIVERED UNDELIVERED
    :param strStatusCode: i dont know what this is
    :param strCustomString:  still dont know what this is
    :return:
    """
    pass


class ClickSendRoutersHandler(webapp2.RequestHandler):
    def post(self):
        """
            4. Push - POST the reply to your website or application.

                If you prefer, we can push message replies to your server as they arrive with us.

                1. Log into your account.
                2. Click on 'SMS' then 'Settings' tab.
                3. Click on the 'Reply/Incoming SMS Settings' menu.
                4. Select 'Forward to URL'.
                5. Enter the URL and click 'Save'.

                The following parameters will be POSTED to the URL specified.

                | Parameter | Type | Description |
            |---|---|---|
            | `from` |string| Recipient Mobile Number that sent the reply message. |
            | `message` |string| Reply SMS message body. |
            | `originalmessage` |string| Original SMS message body. |
            | `originalmessageid` |string| Original SMS message ID. Returned when originally sending the message. |
            | `originalsenderid` |string| Original mobile number (sender ID) that the SMS was sent from. |
            | `customstring` |string| A custom string used when sending the original message. |
            | `username` |string| The API username used to send the original message. |



            # Delivery Reports
            **PUSH**

            If you prefer, we can push message replies to your server as they arrive with us.

            1. Log into your account.
            2. Click on 'SMS' then 'Settings' tab.
            3. Click on the 'SMS Delivery Report Settings' menu.
            4. Select 'Forward to URL'.
            5. Enter the URL and click 'Save'.

            The following parameters will be POSTED to the URL specified.

            | Parameter | Type | Description |
            |---|---|---|
            |`messageid`|string|SMS message ID. Returned when originally sending the message.|
            |`status`|string|Delivery status. Either 'Delivered' or 'Undelivered'.|
            |`status_code`|integer|Delivery status code. The temporary status codes can update at any time.|
            |`customstring`|string|A custom string used when sending the original message.|
            |`username`|string|The API username used to send the original message.|



            **Push Inbound SMS**

            If you prefer, we can push message replies to your server as they arrive with us.

            1. Log into your account.
            2. Click on 'SMS' then 'Settings' tab.
            3. Click on the 'Reply/Incoming SMS Settings' menu.
            4. Select 'Forward to URL'.
            5. Enter the URL and click 'Save'.

            + Parameters

                + username: myusername(required,string) - Your api username.
                + key: 094F2_FA56B10A_0F8F6B_A35FD650D829(required,string) - You can find this in your account area under 'API Credentials' at the top of the screen.
                + messageid: DAA581CB_D739_4675_A506_993679713FF8 (optional, string) - The message ID of the sms. If not provided, all unread results will be returned.

            + Request (application/x-www-form-urlencoded)

                    username=myusername&key=094F2_FA56B10A_0F8F6B_A35FD650D829&messageid=DAA581CB_D739_4675_A506_993679713FF8

            + Response 200 (application/json)

                    <?xml version='1.0' encoding='UTF-8' ?>
                    <xml>
                        <replies replycount='2'>
                            <reply>
                                <from>+61411111111</from>
                                <message>This is a reply</message>
                                <originalmessage>Hello. Please reply</originalmessage>
                                <originalmessageid>D9F15F83-34EC-6A31-A57E-7E8FB0966D78</originalmessageid>
                                <originalsenderid>+61400000000</originalsenderid>
                                <customstring></customstring>
                                <username>testuser101</username>
                            </reply>
                            <reply>
                                <from>+61422222222</from>
                                <message>This is another reply</message>
                                <originalmessage>Hello. Please reply</originalmessage>
                                <originalmessageid>F15F83H8-15AC-3R31-777E-7E8FB09SSDP2</originalmessageid>
                                <originalsenderid>+61400000000</originalsenderid>
                                <customstring></customstring>
                                <username>testuser101</username>
                            </reply>
                        </replies>
                        <result>0000</result>
                        <errortext>Success</errortext>
                    </xml>

        :return:
        """

        #TODO- simply take this url append a specific endpoint to execute different push urls for clicksend the handle all
        #TODO- of them here on this router, the else part of the router must redirest to the home page

        URL = self.request.url
        strURLlist = URL.split("/")
        strFunction = strURLlist[6]

        if strFunction == "push-sms-reply":
            #TODO- create this push url on click send https://sa-sms.appspot.com/sms/clicksend/push-sms-reply
            strFromCell = self.request.get('from')
            strReply = self.request.get('message')
            strOriginalMessage = self.request.get('originalmessage')
            strOriginalMessageID = self.request.get('originalmessageid')
            strOriginalSenderID = self.request.get('originalsenderid')
            strUserName = self.request.get('username')
            HandleSMSPushReply(strFromCell=strFromCell,strReply=strReply,strOriginalMessage=strOriginalMessage,strOriginalMessageID=strOriginalMessageID,strOriginalSenderID=strOriginalSenderID)

        elif strFunction == "push-sms-delivery":
            #TODO- SMS Delivery report https://sa-sms.appspot.com/sms/clicksend/push-sms-delivery
            vstrMessageID = self.request.get("messageid")
            strStatus = self.request.get("status")
            strStatusCode = self.request.get("status_code")
            strCustomString = self.request.get("customstring")

            HandleDeliveryReports(strMessageID=vstrMessageID,strStatus=strStatus,strStatusCode=strStatusCode,strCustomString=strCustomString)


class TwilioCallbacksRoutersHandler(webapp2.RequestHandler):

    def ProcessCallBack(self):
            pass

    def get(self):
        """
        both the get and the post must do the exact same thing

        :return:
        """
        from advertise import SentReport
        message_sid = self.request.get("MessageSid")
        message_status = self.request.get("MessageStatus")
        import logging

        findRequest = DeliveryReport.query(DeliveryReport.message_id == message_sid)
        thisDeliveryList = findRequest.fetch()

        if len(thisDeliveryList) > 0:
            thisDelivery = thisDeliveryList[0]
            thisDelivery.writeSendingStatus(strinput=message_status)
            thisDelivery.put()
        else:
            pass

        findRequest = SentReport.query(SentReport.ref == message_sid)
        thisSentReportList = findRequest.fetch()

        if len(thisSentReportList) > 0:
            thisSentReport = thisSentReportList[0]
            if message_status in ["sent","Sent","Delivered","Sending"]:
                thisSentReport.writeReportDone(strinput=True)
            thisSentReport.writeMessageStatus(strinput=message_status)
            thisSentReport.put()
            logging.info(message_sid + " " + message_status)


    def post(self):
        """
        both the get and the post must do the exact same thing

        :return:
        """
        from advertise import SentReport
        message_sid = self.request.get("MessageSid")
        message_status = self.request.get("MessageStatus")
        import logging

        findRequest = DeliveryReport.query(DeliveryReport.message_id == message_sid)
        thisDeliveryList = findRequest.fetch()

        if len(thisDeliveryList) > 0:
            thisDelivery = thisDeliveryList[0]
            thisDelivery.writeSendingStatus(strinput=message_status)
            thisDelivery.put()
        else:
            pass

        findRequest = SentReport.query(SentReport.ref == message_sid)
        thisSentReportList = findRequest.fetch()

        if len(thisSentReportList) > 0:
            thisSentReport = thisSentReportList[0]
            if message_status in ["sent","Sent","Delivered","Sending"]:
                thisSentReport.writeReportDone(strinput=True)
            thisSentReport.writeMessageStatus(strinput=message_status)
            thisSentReport.put()
            logging.info(message_sid + " " + message_status)


class TwilioResponsesHandler(webapp2.RequestHandler):
    def get(self):
        """
            used to obtain responses from twilio
        :return:
        """
        pass
    def post(self):
        """
            used to obtain responses from messages sent from twilio
            this work as a call back url and will be called by twilio when a response is available
            see status
        :return:
        """

app = webapp2.WSGIApplication([
    ('/admin/mysms', mySMSHandler),
    ('/admin/sms/groups', SMSGroupHandler),
    ('/sms/groupman/.*', GroupManagerHandler),
    ('/sms/manage/.*', thisSMSManagerHandler),
    ('/sms/credits', BuyCreditsHandler),
    ('/sms/clicksend/.*',ClickSendRoutersHandler),
    ('/twilio/callback/status', TwilioCallbacksRoutersHandler),
    ('/twilio/responses', TwilioResponsesHandler)


], debug=True)



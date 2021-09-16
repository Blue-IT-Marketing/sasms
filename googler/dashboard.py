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
import os

import jinja2
from google.cloud import ndb
import google.cloud.datastore as gcs

my_default_retry_params = gcs.RetryParams(initial_delay=0.2,
                                          max_delay=5.0,
                                          backoff_factor=2,
                                          max_retry_period=50)

gcs.set_default_retry_params(my_default_retry_params)
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

from userRights import UserRights
from contact import ContactMessages
from accounts import Accounts
import datetime

class TopUpVerifications(ndb.Expando):
    organization_id = ndb.StringProperty()
    top_up_reference = ndb.StringProperty()
    deposit_slip_filename = ndb.StringProperty()
    public_sub_link = ndb.StringProperty(default="https://storage.googleapis.com/sa-sms.appspot.com/")
    account_name = ndb.StringProperty(default="Adverts") # Surveys, Bulk SMS,FAX
    sms_credits = ndb.IntegerProperty(default=0)
    credit_amount = ndb.IntegerProperty(default=0)
    verified = ndb.BooleanProperty(default=False)
    date_verified = ndb.DateProperty()
    time_verified = ndb.TimeProperty()
    verified_by_uid = ndb.StringProperty()

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
    def writeTopUpReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.top_up_reference = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDepositSlipFileName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.deposit_slip_filename = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAccountName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.account_name = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSMSCredits(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.sms_credits = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeCreditAmount(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.credit_amount = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeVerified(self,strinput):
        try:
            if strinput in [True,False]:
                self.verified = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateVerified(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.date_verified = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeVerified(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.time_verified = strinput
                return True
            else:
                return False
        except:
            return False
    def writeVerifiedByUserID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.verified_by_uid = strinput
                return True
            else:
                return False
        except:
            return False

class Employees(ndb.Expando):
    staff_id = ndb.StringProperty()
    reference = ndb.StringProperty()
    names = ndb.StringProperty()
    surname = ndb.StringProperty()
    cell = ndb.StringProperty()
    tel = ndb.StringProperty()
    email = ndb.StringProperty()
    position = ndb.StringProperty(default="Admin") # Technical, Marketing, Consultant
    send_notices = ndb.BooleanProperty(default=True)

    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.tel = strinput
                return True
            else:
                return False
        except:
            return False

    def writeStaffID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.staff_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strReference = strinput
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
    def writeEmail(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEmail = strinput
                return True
            else:
                return False
        except:
            return False
    def writePosition(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.position = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNotices(self,strinput):
        try:

            if strinput in [True,False]:
                self.send_notices = strinput
                return True
            else:
                return False
        except:
            return False

class Consultants(ndb.Expando):
    staff_id = ndb.StringProperty()
    reference = ndb.StringProperty()
    names = ndb.StringProperty()
    surname = ndb.StringProperty()
    cell = ndb.StringProperty()
    tel = ndb.StringProperty()
    email = ndb.StringProperty()
    position = ndb.StringProperty(default="Admin") # Technical, Marketing, Consultant
    send_notices = ndb.BooleanProperty(default=True)

    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.tel = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStaffID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.staff_id = strinput
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
    def writePosition(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.position = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNotices(self,strinput):
        try:

            if strinput in [True,False]:
                self.send_notices = strinput
                return True
            else:
                return False
        except:
            return False

class AccountDetails(ndb.Expando):
    staff_id = ndb.StringProperty()
    account_holder = ndb.StringProperty(default="Cellbright Trading")
    account_holder = ndb.StringProperty(default="1134 612 265")
    bank_name = ndb.StringProperty(default="Nedbank")
    branch_name = ndb.StringProperty(default="Universal")
    branch_code = ndb.StringProperty(default="198765")

    def writeStaffID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.staff_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAccountHolder(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.account_holder = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAccountNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.account_holder = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBankName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.bank_name = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBranchName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.branch_name = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBranchCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.branch_code = strinput
                return True
            else:
                return False
        except:
            return False


#TODO- Intergrate clicksend to my solutions https://dashboard.clicksend.com
#TODO- Also Intergrate Faxto https://api.fax.to/numbers

class BlueITMarketing(ndb.Expando):

    staff_id = ndb.StringProperty()
    company_name = ndb.StringProperty(default="Blue IT Marketing Pty LTD")
    reg = ndb.StringProperty(default="2013/078651/07")
    cell = ndb.StringProperty(default="0790471559")
    tel = ndb.StringProperty(default="0159620369")
    email = ndb.StringProperty(default="info@blueitmarketing.co.za")
    website = ndb.StringProperty(default="http://www.blueitmarketing.co.za")
    address = ndb.StringProperty(default="Office G05 Sabina Plaza, Thohoyandou, Limpopo, South Africa 0950")

    def writeStaffID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strStaffID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCompanyName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.company_name = strinput
                return True
            else:
                return False

        except:
            return False
    def writeCompanyReg(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.reg = strinput
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
    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.tel = strinput
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
    def writeWebsite(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.website = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAddress(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.address = strinput
                return True
            else:
                return False
        except:
            return False


class Dashboardhandler():
    def get(self):

        Guser = users.get_current_user()

        if Guser:
            if users.is_current_user_admin():

                findRequest = ContactMessages.query(ContactMessages.response_sent == False)
                thisContactMessagesList = findRequest.fetch()

                template = template_env.get_template('templates/dashboard/dashboard.html')
                context = {'thisContactMessagesList':thisContactMessagesList}
                self.response.write(template.render(context))

class ContactsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = ContactMessages.query(ContactMessages.response_sent == False)
            thisContactMessageList = findRequest.fetch()

            template = template_env.get_template('templates/dashboard/dashfiles/contact.html')
            context = {'thisContactMessageList':thisContactMessageList}
            self.response.write(template.render(context))


class BulkSMSHandler(webapp2.RequestHandler):

    def get(self):
        from mysms import SMSPortalVodacom, SMSPortalBudget,SMSAccount
        Guser = users.get_current_user
        if users.is_current_user_admin:

            findRequests = SMSPortalVodacom.query()
            thisSMSPortalVodacomList = findRequests.fetch()

            if len(thisSMSPortalVodacomList) > 0:
                thisVodacomPortal = thisSMSPortalVodacomList[0]
            else:
                thisVodacomPortal = SMSPortalVodacom()

            findRequests = SMSPortalBudget.query()
            thisBudgetPortalList = findRequests.fetch()

            if len(thisBudgetPortalList) > 0:
                thisBudgetPortal = thisBudgetPortalList[0]

            else:
                thisBudgetPortal = SMSPortalBudget()

            thisBudgetPortal.writeAvailableCredit(strinput=thisBudgetPortal.CheckCredits())
            thisBudgetPortal.put()

            findRequests = SMSAccount.query()
            thisSMSAccountList = findRequests.fetch()

            template = template_env.get_template('templates/dashboard/dashfiles/BulkSMS.html')
            context = {'thisBudgetPortal':thisBudgetPortal,'thisVodacomPortal':thisVodacomPortal,'thisSMSAccountList':thisSMSAccountList}
            self.response.write(template.render(context))


    def post(self):
        from mysms import SMSPortalVodacom, SMSPortalBudget,SMSAccount,Groups
        from accounts import Organization,Accounts
        Guser = users.get_current_user
        if users.is_current_user_admin:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                vstrSenderAddress = self.request.get('vstrSenderAddress')
                vstrEmailAddress = self.request.get('vstrEmailAddress')
                vstrCSVEmail = self.request.get('vstrCSVEmail')
                vstrSMSSizeLimit = self.request.get('vstrSMSSizeLimit')
                vstrBuyRate = self.request.get('vstrBuyRate')
                vstrSellRate = self.request.get('vstrSellRate')
                vstrAvailableCredit = self.request.get('vstrAvailableCredit')
                vstrPortalLogin = self.request.get('vstrPortalLogin')
                vstrPortalPassword = self.request.get('vstrPortalPassword')
                vstrPortalAddress = self.request.get('vstrPortalAddress')
                vstrSystemCredit = self.request.get('vstrSystemCredit')

                findRequest = SMSPortalVodacom.query()
                thisVodacomPortalList = findRequest.fetch()
                if len(thisVodacomPortalList) > 0:
                    thisVodacomPortal = thisVodacomPortalList[0]
                else:
                    thisVodacomPortal = SMSPortalVodacom()

                thisVodacomPortal.writeSystemCredit(strinput=vstrSystemCredit)
                thisVodacomPortal.writeCSVEmail(strinput=vstrCSVEmail)
                thisVodacomPortal.writeEmailAddress(strinput=vstrEmailAddress)
                thisVodacomPortal.writeSMSSixeLimit(strinput=vstrSMSSizeLimit)
                thisVodacomPortal.writeAvailableCredit(strinput=vstrAvailableCredit)
                thisVodacomPortal.writeSellRate(strinput=vstrSellRate)
                thisVodacomPortal.writePortalAddress(strinput=vstrPortalAddress)
                thisVodacomPortal.writeSenderAddress(strinput=vstrSenderAddress)
                thisVodacomPortal.writeBuyRate(strinput=vstrBuyRate)
                thisVodacomPortal.writePortaLogin(strinput=vstrPortalLogin)
                thisVodacomPortal.writePassword(strinput=vstrPortalPassword)

                thisVodacomPortal.put()

                self.response.write("Successfully updated vodacom SMS portal settings")

            elif vstrChoice == "1":
                vstrOrganizationID = self.request.get('vstrOrganizationID')
                vstrAdditionalCredit = self.request.get('vstrAdditionalCredit')

                findRequest = SMSAccount.query(SMSAccount.strOrganizationID == vstrOrganizationID)
                thisSMSAccountList = findRequest.fetch()

                if len(thisSMSAccountList) > 0 and (int(vstrAdditionalCredit) > 0):
                    thisSMSAccount = thisSMSAccountList[0]

                    thisSMSAccount.writeOrganizationID(strinput=vstrOrganizationID)
                    thisSMSAccount.AddTotalSMS(strinput=vstrAdditionalCredit)
                    thisSMSAccount.put()
                    self.response.write("Successfully added new credit amount please refresh your browser to see new values")
                else:
                    self.response.write("Error Crediting Account")

            elif vstrChoice == "2":
                thisBlueITMarketing = BlueITMarketing()

                findRequest = SMSAccount.query(SMSAccount.strOrganizationID == thisBlueITMarketing.strStaffID)
                thisSMSAccountList = findRequest.fetch()

                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]
                else:
                    thisSMSAccount = SMSAccount()

                findRequest = Groups.query(Groups.strOrganizationID == thisSMSAccount.strOrganizationID)
                thisGroupsList = findRequest.fetch()

                template = template_env.get_template('templates/sms/creategroups.html')
                context = {'thisGroupsList':thisGroupsList}
                self.response.write(template.render(context))

            elif vstrChoice == "3":
                findRequest = Organization.query()
                Orglist = findRequest.fetch()

                for org in Orglist:
                    org.put()

                findRequest = Organization.query(Organization.strVerified == True,Organization.strSuspended == False)
                thisActiveList = findRequest.fetch()
                findRequest = Organization.query(Organization.strVerified == False,Organization.strSuspended == False)
                thisNotActiveList = findRequest.fetch()
                findRequest = Organization.query(Organization.strSuspended == True)
                thisSuspendedList = findRequest.fetch()


                templates = template_env.get_template('templates/dashboard/dashfiles/accountlist.html')
                context = {'thisActiveList':thisActiveList,'thisNewAccountsList':thisNotActiveList,'thisSuspendedList':thisSuspendedList}
                self.response.write(templates.render(context))

class BlueITMarketingHandler(webapp2.RequestHandler):
    def get(self):
        from mysms import SMSAccount
        if users.is_current_user_admin():

            findRequest = Employees.query()
            thisAdminStaffList = findRequest.fetch()

            findRequest = Consultants.query()
            thisConsultantList = findRequest.fetch()

            findRequest = AccountDetails.query()
            thisBankDetailsList = findRequest.fetch()

            findRequest = BlueITMarketing.query()
            thisBlueITMarketingList = findRequest.fetch()

            if len(thisBlueITMarketingList) > 0:
                thisBlueITMarketing = thisBlueITMarketingList[0]
            else:
                thisBlueITMarketing = BlueITMarketing()

            thisAdmin = Employees()

            findRequest = SMSAccount.query(SMSAccount.strOrganizationID == thisAdmin.staff_id)
            thisSMSAccountList = findRequest.fetch()

            if len(thisSMSAccountList) > 0:
                thisSMSAccount = thisSMSAccountList[0]

            else:
                thisSMSAccount = SMSAccount()
                thisSMSAccount.writeOrganizationID(strinput=thisAdmin.staff_id)
                thisSMSAccount.writeUsePortal(strinput="Budget")
                thisSMSAccount.put()
                findRequest = SMSAccount.query(SMSAccount.strOrganizationID == thisAdmin.staff_id)
                thisSMSAccountList = findRequest.fetch()
                thisSMSAccount = thisSMSAccountList[0]


            templates = template_env.get_template('templates/dashboard/dashfiles/blueitmarketing.html')
            context = {'thisAdminStaffList':thisAdminStaffList,'thisBankDetailsList':thisBankDetailsList,'thisSMSAccount':thisSMSAccount,
                       'thisBlueITMarketing':thisBlueITMarketing,'thisConsultantList':thisConsultantList}
            self.response.write(templates.render(context))



    def post(self):
        from mysms import SMSAccount
        if users.is_current_user_admin():
            vstrChoice  = self.request.get('vstrChoice')

            if vstrChoice == "0":

                vstrNames = self.request.get('vstrNames')
                vstrSurname = self.request.get('vstrSurname')
                vstrCell = self.request.get('vstrCell')
                vstrTel = self.request.get('vstrTel')
                vstrEmail = self.request.get('vstrEmail')
                vstrPosition = self.request.get('vstrPosition')
                vstrSendNotices = self.request.get('vstrSendNotices')

                findRequest = Employees.query(Employees.cell == vstrCell)
                thisEmployeesList = findRequest.fetch()

                if len(thisEmployeesList) > 0:
                    thisEmployee = thisEmployeesList[0]

                else:
                    thisEmployee = Employees()

                thisEmployee.writeNames(strinput=vstrNames)
                thisEmployee.writeSurname(strinput=vstrSurname)
                thisEmployee.writeCell(strinput=vstrCell)
                thisEmployee.writeTel(strinput=vstrTel)
                thisEmployee.writeEmail(strinput=vstrEmail)
                thisEmployee.writePosition(strinput=vstrPosition)
                if vstrSendNotices == "YES":
                    thisEmployee.writeNotices(strinput=True)
                else:
                    thisEmployee.writeNotices(strinput=False)

                thisEmployee.put()
                self.response.write("Employee Successfully updated")

            elif vstrChoice == "1":

                vstrConsNames = self.request.get('vstrConsNames')
                vstrConsSurname = self.request.get('vstrConsSurname')
                vstrConsCell = self.request.get('vstrConsCell')
                vstrConsTel =self.request.get('vstrConsTel')
                vstrConsEmail = self.request.get('vstrConsEmail')
                vstrConsPosition = self.request.get('vstrConsPosition')
                vstrConsSendNotices = self.request.get('vstrConsSendNotices')


                findRequest = Consultants.query(Consultants.cell == vstrConsCell)
                thisConsultantsList = findRequest.fetch()

                if len(thisConsultantsList) > 0:
                    thisConsultant = thisConsultantsList[0]
                else:
                    thisConsultant = Consultants()

                thisConsultant.writeNames(strinput=vstrConsNames)
                thisConsultant.writeSurname(strinput=vstrConsSurname)
                thisConsultant.writeCell(strinput=vstrConsCell)
                thisConsultant.writeTel(strinput=vstrConsTel)
                thisConsultant.writeEmail(strinput=vstrConsEmail)
                thisConsultant.writePosition(strinput=vstrConsPosition)
                if  vstrConsSendNotices == "YES":
                    thisConsultant.writeNotices(strinput=True)
                else:
                    thisConsultant.writeNotices(strinput=False)

                thisConsultant.put()
                self.response.write("Successfully updated Consultant Details")

            elif vstrChoice == "2":
                vstrAccountHolder = self.request.get('vstrAccountHolder')
                vstrAccountNumber = self.request.get('vstrAccountNumber')
                vstrBankName = self.request.get('vstrBankName')
                vstrBranchName = self.request.get('vstrBranchName')
                vstrBranchCode = self.request.get('vstrBranchCode')

                findRequest = AccountDetails.query(AccountDetails.account_holder == vstrAccountNumber)
                thisAccountDetailsList = findRequest.fetch()

                if len(thisAccountDetailsList) > 0:
                    thisAccount = thisAccountDetailsList[0]
                else:
                    thisAccount = AccountDetails()

                thisAccount.writeAccountHolder(strinput=vstrAccountHolder)
                thisAccount.writeAccountNumber(strinput=vstrAccountNumber)
                thisAccount.writeBankName(strinput=vstrBankName)
                thisAccount.writeBranchName(strinput=vstrBranchName)
                thisAccount.writeBranchCode(strinput=vstrBranchCode)

                thisAccount.put()

                self.response.write("Account Details Successfully Updated")

            elif vstrChoice == "3":
                vstrTotalSMS = self.request.get('vstrTotalSMS')
                vstrPortal = self.request.get('vstrPortal')

                thisBlueITMarketing = BlueITMarketing()
                findRequest = SMSAccount.query(SMSAccount.strOrganizationID == thisBlueITMarketing.strStaffID)
                thisSMSAccountList = findRequest.fetch()

                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]
                else:
                    thisSMSAccount = SMSAccount()
                    thisSMSAccount.writeOrganizationID(strinput=thisBlueITMarketing.strStaffID)

                thisSMSAccount.writeTotalSMS(strinput=vstrTotalSMS)
                thisSMSAccount.writeUsePortal(strinput=vstrPortal)
                thisSMSAccount.put()

                self.response.write("Successfully updated SMS Account")



class AdvertiseHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from advertise import OurContacts
        from myapi import PartnerSites,EndPoints
        if Guser:
            findRequest = OurContacts.query()
            thisContactList = findRequest.fetch(limit=10000)

            findRequest = PartnerSites.query()
            thisPartnerSitesList = findRequest.fetch()

            findRequest = EndPoints.query()
            thisEndPointsList = findRequest.fetch()

            template = template_env.get_template('templates/dashboard/dashfiles/leadslist.html')
            context = {'thisContactList':thisContactList,'thisPartnerSitesList':thisPartnerSitesList,'thisEndPointsList':thisEndPointsList}
            self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        from advertise import OurContacts
        from myapi import PartnerSites,EndPoints
        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                vstrNames = self.request.get('vstrNames')
                vstrSurname = self.request.get('vstrSurname')
                vstrCellNumber = self.request.get('vstrCellNumber')
                vstrEmail = self.request.get('vstrEmail')

                vstrCellNumber = vstrCellNumber.strip()
                if vstrCellNumber.startswith("27"):
                    vstrCellNumber = vstrCellNumber.replace('27','0',1)

                if vstrCellNumber.startswith("0"):
                    pass
                else:
                    vstrCellNumber = "0" + vstrCellNumber

                vstrNames = vstrNames.strip()
                vstrSurname = vstrSurname.strip()
                vstrEmail = vstrEmail.strip()

                findRequest = OurContacts.query(OurContacts.cell == vstrCellNumber)
                thisContactList = findRequest.fetch()

                if len(thisContactList) > 0:
                    thisContact = thisContactList[0]

                else:
                    thisContact = OurContacts()
                    thisContact.writeOurContactID(strinput=thisContact.CreateContactID())


                thisContact.writeNames(strinput=vstrNames)
                thisContact.writeSurname(strinput=vstrSurname)
                thisContact.writeEmail(strinput=vstrEmail)
                thisContact.writeCell(strinput=vstrCellNumber)
                thisContact.put()

                self.response.write("Successfully Saved Contact")

            elif vstrChoice == "1":
                vstrContacts = self.request.get('vstrContacts')


                vstrContactList = vstrContacts.split("|")
                i = 0

                for thisContact in vstrContactList:
                    try:
                        thisContactList = thisContact.split(',')
                        if len(thisContactList) > 0:
                            strCell = thisContactList[0]
                            strEmail = thisContactList[1]
                            strNames = thisContactList[2]
                            strSurname = thisContactList[3]

                            strCell = strCell.strip()
                            if strCell.startswith("27"):
                                strCell = strCell.replace('27','0',count=1)

                            if strCell.startswith("0"):
                                pass
                            else:
                                strCell = "0" + strCell

                            strEmail = strEmail.strip()
                            strNames = strNames.strip()
                            strSurname = strSurname.strip()

                            findRequest = OurContacts.query(OurContacts.cell == strCell)
                            thisContactList = findRequest.fetch()

                            if len(thisContactList) > 0:
                                thisContact = thisContactList[0]
                            else:
                                thisContact = OurContacts()
                                thisContact.writeOurContactID(strinput=thisContact.CreateContactID())

                            thisContact.writeNames(strinput=strNames)
                            thisContact.writeSurname(strinput=strSurname)
                            thisContact.writeCell(strinput=strCell)
                            thisContact.writeEmail(strinput=strEmail)
                            thisContact.put()
                            i += 1
                    except:
                        pass

                self.response.write("Successfully Loaded :  " + str(i) + " Contacts")

            elif vstrChoice == "2":
                vstrRemoveCell = self.request.get('vstrRemoveCell')
                vstrRemoveCell = vstrRemoveCell.strip()

                findRequest = OurContacts.query(OurContacts.cell == vstrRemoveCell)
                thisContactList = findRequest.fetch()

                for thisContact in thisContactList:
                    thisContact.key.delete()

                self.response.write("Successfull removed contact")

            elif vstrChoice == "3":
                vstrPartnerURL = self.request.get('vstrPartnerURL')
                vstrPartnerURL = vstrPartnerURL.strip()

                findRequest = PartnerSites.query(PartnerSites.strURL == vstrPartnerURL)
                thisPartnerSiteList = findRequest.fetch()

                if len(thisPartnerSiteList) > 0:
                    thisPartnerSite = thisPartnerSiteList[0]
                else:
                    thisPartnerSite = PartnerSites()
                    thisPartnerSite.writeAPIKey(strinput=thisPartnerSite.CreateAPIKey())
                    thisPartnerSite.writeAPISecret(strinput=thisPartnerSite.CreateAPISecret())
                    thisPartnerSite.writeSiteID(strinput=thisPartnerSite.CreateSiteID())

                thisPartnerSite.writeURL(strinput=vstrPartnerURL)
                thisPartnerSite.put()
                self.response.write("Successfully update partner site")

            elif vstrChoice == "4":
                #TODO-Revise end points definitions to include extra variables to detect the service
                vstrEndpoint = self.request.get('vstrEndpoint')
                vstrEndpoint = vstrEndpoint.strip()

                findRequest = EndPoints.query(EndPoints.strPointURL == vstrEndpoint)
                thisEndpointList = findRequest.fetch()

                if len(thisEndpointList) > 0:
                    thisEndpoint = thisEndpointList[0]
                else:
                    thisEndpoint = EndPoints()
                    thisEndpoint.writePointID(strinput=thisEndpoint.CreatePointID())
                    thisEndpoint.writeAPiKey(strinput=thisEndpoint.CreateAPIKey())
                    thisEndpoint.writeAPISecret(strinput=thisEndpoint.CreateAPiSecret())

                thisEndpoint.writePointURL(strinput=vstrEndpoint)
                thisEndpoint.put()

                self.response.write("Successfully updated end point")


class TicketsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from contact import TicketUsers,StaffMembers,Tickets
        if Guser:
            vstrChoice  = self.request.get('vstrChoice')

            if vstrChoice == "0":

                findRequest = Tickets.query(Tickets.ticket_open == True)
                thisTicketList = findRequest.fetch()
                thisUsersList = []
                for thisTicket in thisTicketList:

                    findRequest = TicketUsers.query(TicketUsers.uid == thisTicket.uid)
                    thisTicketUsersList = findRequest.fetch()
                    if len(thisTicketUsersList) > 0:
                        thisTicketUser = thisTicketUsersList[0]
                        if thisTicketUser in thisUsersList:
                            pass
                        else:
                            thisUsersList.append(thisTicketUser)

                template = template_env.get_template('templates/dashboard/dashfiles/SupportTickets.html')
                context = {'thisUsersList':thisUsersList}
                self.response.write(template.render(context))

    def post(self):
        from contact import TicketUsers, StaffMembers, Tickets,CommentThread,Comments
        Guser = users.get_current_user()
        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                vstrUserID = self.request.get('vstrUserID')

                findRequest = Tickets.query(Tickets.strUserID == vstrUserID, Tickets.ticket_open == True)
                thisTicketsList = findRequest.fetch()
                if len(thisTicketsList) > 0:
                    thisTicket = thisTicketsList[0]

                    findRequest = CommentThread.query(CommentThread.ticket_id == thisTicket.ticket_id)
                    thisCommentThreadList = findRequest.fetch()

                    if len(thisCommentThreadList) > 0:
                        thisThread = thisCommentThreadList[0]

                        findRequest = Comments.query(Comments.thread_id == thisThread.thread_id)
                        thisCommentList = findRequest.fetch()
                        thisCommentList.reverse()

                        template = template_env.get_template('templates/dashboard/dashfiles/subTicketChat.html')
                        context = {'thisCommentList':thisCommentList,'thisTicket':thisTicket,'thisThread':thisThread}
                        self.response.write(template.render(context))

                elif vstrChoice == "1":
                    vstrComment = self.request.get('vstrComment')
                    vstrTicketID = self.request.get('vstrTicketID')
                    vstrThreadID = self.request.get('vstrThreadID')
                    vstrUserID = self.request.get('vstrUserID')

                    findRequest = Tickets.query(Tickets.ticket_id == vstrTicketID)
                    thisTicketsList = findRequest.fetch()

                    if len(thisTicketsList) > 0:
                        thisTicket = thisTicketsList[0]

                        findRequest = CommentThread.query(CommentThread.thread_id == vstrThreadID)
                        thisCommentThreadList = findRequest.fetch()

                        vstrDateTime = datetime.datetime.now()
                        strThisDate = datetime.date(year=vstrDateTime.year,month=vstrDateTime.month,day=vstrDateTime.day)
                        strThisTime = datetime.time(hour=vstrDateTime.hour,minute=vstrDateTime.minute,second=vstrDateTime.second)


                        if len(thisCommentThreadList) > 0:
                            thisThread = thisCommentThreadList[0]

                            thisComment = Comments()
                            thisComment.writeAuthorID(strinput=Guser.user_id())
                            thisComment.writeCommentID(strinput=thisComment.CreateCommentID())
                            thisComment.writeIsClientComment(strinput=False)
                            thisComment.writeThreadID(strinput=vstrThreadID)
                            thisComment.writeCommentDate(strinput=strThisDate)
                            thisComment.writeCommentTime(strinput=strThisTime)
                            thisComment.writeComment(strinput=vstrComment)
                            thisThread.AddCommentID(strinput=thisComment.comment_id)
                            thisComment.put()
                            thisThread.put()
                            findRequest = Comments.query(Comments.thread_id == thisThread.thread_id)
                            thisCommentList = findRequest.fetch()
                            thisCommentList.reverse()
                            template = template_env.get_template('templates/dashboard/dashfiles/subTicketChat.html')
                            context = {'thisCommentList': thisCommentList,'thisThread':thisThread,'thisTicket':thisTicket}
                            self.response.write(template.render(context))
                        else:
                            self.response.write("Comments not found")
                    else:
                        self.response.write("Ticket not found")


                elif vstrChoice == "2":
                    vstrTicketID = self.request.get('vstrTicketID')
                    vstrThreadID = self.request.get('vstrThreadID')
                    vstrUserID = self.request.get('vstrUserID')

                    findRequest = Tickets.query(Tickets.ticket_id == vstrTicketID)
                    thisTicketsList = findRequest.fetch()

                    if len(thisTicketsList) > 0:
                        thisTicket = thisTicketsList[0]
                    else:
                        thisTicket = Tickets()

                    findRequest = CommentThread.query(CommentThread.ticket_id == vstrTicketID, CommentThread.thread_id == vstrThreadID)
                    thisCommentThreadList = findRequest.fetch()

                    if len(thisCommentThreadList) > 0:
                        thisThread = thisCommentThreadList[0]


                        findRequest = Comments.query(Comments.thread_id == vstrThreadID)
                        thisCommentList = findRequest.fetch()
                        thisCommentList.reverse()
                        template = template_env.get_template('templates/dashboard/dashfiles/AutoUpdate.html')
                        context = {'thisCommentList': thisCommentList,'thisThread':thisThread,'thisTicket':thisTicket}
                        self.response.write(template.render(context))


class GlobalReportsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from mysms import DeliveryReport
        from advertise import SentReport
        from surveys import MultiChoiceSurveys

        if Guser:
            #TODO- Make Queries and obtain all the relevant reports
            #TODO- Consider Limit the results to only the last 30 days in case the report generation takes too long
            findRequest = DeliveryReport.query()
            thisDeliveryList = findRequest.fetch()

            findRequest= SentReport.query()
            thisAdvertReportList = findRequest.fetch()

            findRequest = MultiChoiceSurveys.query()
            thisSurveyReportsList = findRequest.fetch()

            #TODO- PLease structure properly the reporting system for sent surveys, the reports must be beneficial to the end user

            template = template_env.get_template('templates/dashboard/dashfiles/globalSentReports.html')
            context = {'thisDeliveryList':thisDeliveryList,'thisAdvertReportList':thisAdvertReportList,'thisSurveyReportsList':thisSurveyReportsList}
            self.response.write(template.render(context))

class TopUpVerificationHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = TopUpVerifications.query(TopUpVerifications.verified == False)
            thisTopUpVerificationList = findRequest.fetch()
            template = template_env.get_template('templates/dashboard/topup/topup.html')
            context = {'thisTopUpVerificationList':thisTopUpVerificationList}
            self.response.write(template.render(context))



class thisTopUpVerificationHandler(webapp2.RequestHandler):
    def get(self):
        from accounts import Organization

        if users.is_current_user_admin():
            URL = self.request.url
            strURLlist = URL.split("/")
            strTopUpReference = strURLlist[len(strURLlist) - 1]

            findRequest = TopUpVerifications.query(TopUpVerifications.top_up_reference == strTopUpReference)
            thisTopUpAccountList = findRequest.fetch()

            if len(thisTopUpAccountList) > 0:
                thisTopUpAccount = thisTopUpAccountList[0]

                findRequest = Organization.query(Organization.strOrganizationID == thisTopUpAccount.organization_id)
                thisOrgList = findRequest.fetch()

                if len(thisOrgList) > 0:
                    thisOrg = thisOrgList[0]
                else:
                    thisOrg = Organization()

                template = template_env.get_template('templates/dashboard/topup/thisVerification.html')
                context = {'thisOrg':thisOrg,'thisTopUpAccount':thisTopUpAccount}
                self.response.write(template.render(context))

    def post(self):
        from accounts import Organization
        from advertise import AddAccount
        from surveys import SurveyAccount
        from myfax import FaxAccount
        if users.is_current_user_admin():
            vstrChoice = self.request.get('vstrChoice')


            if vstrChoice == "0":
                vstrDepositSlipFilename = self.request.get('vstrDepositSlipFilename')
                vstrTopUpReference = self.request.get('vstrTopUpReference')

                gcs_file = gcs.open("/bucket/"+vstrDepositSlipFilename)
                self.response.write(gcs_file)

            elif vstrChoice == "1":
                vstrTopUpReference = self.request.get('vstrTopUpReference')
                vstrAccountName = self.request.get('vstrAccountName')

                if vstrAccountName == "Adverts":
                    findRequest = AddAccount.query(AddAccount.top_up_reference == vstrTopUpReference)
                    thisAdvertisingAccountList = findRequest.fetch()

                    if len(thisAdvertisingAccountList) > 0:
                        thisAdvertAccount = thisAdvertisingAccountList[0]
                        thisAdvertAccount.total_credits += thisAdvertAccount.top_up_credit
                        thisAdvertAccount.top_up_credit = 0

                        thisAdvertAccount.total_top_up_cost  = 0

                        thisAdvertAccount.put()

                        #TODO-Consider Creating an Invoice for the payment here

                elif vstrAccountName == "Surveys":
                    findRequest = SurveyAccount.query(SurveyAccount.strTopUpReference == vstrTopUpReference)
                    thisSurveyAccountList = findRequest.fetch()

                    if len(thisSurveyAccountList) > 0:
                        thisSurveyAccount = thisSurveyAccountList[0]
                        thisSurveyAccount.total_credits += thisSurveyAccount.top_up_credit
                        thisSurveyAccount.top_up_credit = 0
                        thisSurveyAccount.total_top_up_cost = 0

                        thisSurveyAccount.put()
                        # TODO-Consider Creating an Invoice for the payment here

                elif (vstrAccountName == "Bulk SMS") or (vstrAccountName == "BulkSMS"):
                    pass

                elif vstrAccountName == "FAX":
                    findRequest = FaxAccount.query(FaxAccount.strTopUpReference == vstrTopUpReference)
                    thisFaxAccountList = findRequest.fetch()

                    if len(thisFaxAccountList) > 0:
                        thisFaxAccount = thisFaxAccountList[0]

                        thisFaxAccount.strCreditInPages += thisFaxAccount.top_up_credit
                        thisFaxAccount.top_up_credit = 0
                        thisFaxAccount.total_top_up_cost = 0
                        thisFaxAccount.put()
                        # TODO-Consider Creating an Invoice for the payment here



                findRequest = TopUpVerifications.query(TopUpVerifications.top_up_reference == vstrTopUpReference)
                thisTopUpVerificationList = findRequest.fetch()

                if len(thisTopUpVerificationList) > 0:
                    thisTopUpVerification = thisTopUpVerificationList[0]

                    thisTopUpVerification.writeVerified(strinput=True)
                    Guser = users.get_current_user()
                    vstrThisDate = datetime.datetime.now()
                    strThisDate = datetime.date(year=vstrThisDate.year,month=vstrThisDate.month,day=vstrThisDate.day)
                    strThisTime = datetime.time(hour=vstrThisDate.hour,minute=vstrThisDate.minute,second=vstrThisDate.second)

                    thisTopUpVerification.writeVerifiedByUserID(strinput=Guser.user_id())
                    thisTopUpVerification.writeDateVerified(strinput=strThisDate)
                    thisTopUpVerification.writeTimeVerified(strinput=strThisTime)
                    thisTopUpVerification.put()
                    self.response.write("Account Successfully verified")


                #TODO- Include a means of Viewing sent reports on the dashboard- meaning the dashboard will retrieve all
                #TODO- Messages statuses and also responses and make them viewable per account and also wholistically
                #TODO- Also finish up on Advert Status and Order State dialogs
                #TODO- Create a tab for responses on the advert and also a tab for message delivery statuses on the advert
                #TODO- Note that a whole message status and delivery report will also be found on the client account window
                #TODO- System wide message status and responses tab shall also be found right on the entry to the dashboard


class ThisMarketingHandler(webapp2.RequestHandler):
    def get(self):
        from marketing import FacebookMessages,FacebookGroups,FaceGroupAutoPosterSettings,TwitterMessages,TwitterSettings

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            findRequest = FacebookMessages.query()
            thisMessagesList = findRequest.fetch()
            template = template_env.get_template('templates/dashboard/marketing/internal/facebook.html')
            context = {'thisMessagesList':thisMessagesList}
            self.response.write(template.render(context))

        elif vstrChoice == "1":
            findRequest = TwitterMessages.query()
            thisTwitterMessagesList = findRequest.fetch()
            findRequest = TwitterSettings.query()
            thisTwitterSettingsList = findRequest.fetch()
            template = template_env.get_template('templates/dashboard/marketing/internal/twitter.html')
            context = {'thisTwitterMessagesList':thisTwitterMessagesList,'thisTwitterSettingsList':thisTwitterSettingsList}
            self.response.write(template.render(context))




    def post(self):
        from marketing import FacebookMessages,TwitterMessages,TwitterSettings

        vstrChoice = self.request.get("vstrChoice")

        if vstrChoice == "0":
            vstrMessage = self.request.get('vstrMessage')
            thisMessage = FacebookMessages()

            thisMessage.writeMessage(strinput=vstrMessage)
            thisMessage.writeMessageStatus(strinput="Ready")
            thisMessage.writeMessageID(strinput=thisMessage.CreateMessageID())
            thisMessage.put()
            self.response.write("Message Created Successfully")
        elif vstrChoice == "1":
            strMessageID = self.request.get('vstrMessageID')
            findRequest = FacebookMessages.query(FacebookMessages.message_id == strMessageID)
            thisMessageList = findRequest.fetch()

            if len(thisMessageList) > 0:
                thisMessage = thisMessageList[0]
                template = template_env.get_template('templates/dashboard/marketing/internal/face-message-reader.html')
                context = {'thisMessage':thisMessage}
                self.response.write(template.render(context))
        elif vstrChoice == "2":
            vstrMessage = self.request.get('vstrMessage')
            thisMessage = TwitterMessages()
            thisMessage.writeMessage(strinput=vstrMessage)
            thisMessage.writeMessageID(strinput=thisMessage.CreateMessageID())
            thisMessage.writeMessageStatus(strinput="Ready")
            thisMessage.put()
            self.response.write("Message Created Successfully")
        elif vstrChoice == "3":
            strMessageID = self.request.get('vstrMessageID')
            findRequest = TwitterMessages.query(TwitterMessages.message_id == strMessageID)
            thisMessageList = findRequest.fetch()

            if len(thisMessageList) > 0:
                thisMessage = thisMessageList[0]
                template = template_env.get_template('templates/dashboard/marketing/internal/tweet-reader.html')
                context = {'thisMessage':thisMessage}
                self.response.write(template.render(context))

        elif vstrChoice == "4":
            vstrConsumerAPI = self.request.get('vstrConsumerAPI')
            vstrConsumerSecret = self.request.get('vstrConsumerSecret')
            vstrAccessTokenKey = self.request.get('vstrAccessTokenKey')
            vstrAccessTokenSecret = self.request.get('vstrAccessTokenSecret')

            thisTwitterSettings = TwitterSettings()
            thisTwitterSettings.writeConsumerAPI(strinput=vstrConsumerAPI)
            thisTwitterSettings.writeConsumerSecret(strinput=vstrConsumerSecret)
            thisTwitterSettings.writeAccessTokenKey(strinput=vstrAccessTokenKey)
            thisTwitterSettings.writeAccessTokenSecret(strinput=vstrAccessTokenSecret)
            thisTwitterSettings.writeCredentialsWorks(strinput=True)
            thisTwitterSettings.put()
            self.response.write("Successfully saved Twitter Settings")


app = webapp2.WSGIApplication([
    ('/dashboard', Dashboardhandler),
    ('/dashboard/contacts', ContactsHandler),
    ('/dashboard/bulksms', BulkSMSHandler),
    ('/dashboard/blueitmarketing', BlueITMarketingHandler),
    ('/dashboard/advertise', AdvertiseHandler),
    ('/dashboard/tickets', TicketsHandler),
    ('/dashboard/globalreports', GlobalReportsHandler),
    ('/dashboard/topupverification', TopUpVerificationHandler),
    ('/dashboard/topup/.*', thisTopUpVerificationHandler),
    ('/dashboard/marketing', ThisMarketingHandler)


], debug=True)


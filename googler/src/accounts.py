import logging
import os
import jinja2
from google.cloud import ndb
import datetime

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
from userRights import UserRights
from firebaseadmin import VerifyAndReturnAccount


class OpenInvites(ndb.Model):
    organization_id = ndb.StringProperty()
    cell = ndb.StringProperty()
    email = ndb.StringProperty()
    security_code = ndb.StringProperty()
    date_sent = ndb.DateProperty(auto_now_add=True)
    time_sent = ndb.TimeProperty(auto_now_add=True)
    accepted = ndb.BooleanProperty(default=False)

    def writeOrganizationID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.organization_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCell(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.cell = strinput
                return True
            else:
                return False
        except:
            return False

    def writeEmail(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.email = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSecurityCode(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.security_code = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateSent(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.date_sent = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeSent(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.time_sent = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAccepted(self, strinput):
        try:
            if strinput in [True, False]:
                self.accepted = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateSecurityCode(self):
        import random, string
        try:
            strSecurityCode = ""
            for i in range(6):
                strSecurityCode += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strSecurityCode
        except:
            return None


class Accounts(ndb.Expando):
    uid = ndb.StringProperty()
    organization_id = ndb.StringProperty()
    names = ndb.StringProperty()
    surname = ndb.StringProperty()
    cell = ndb.StringProperty()
    tel = ndb.StringProperty()
    email = ndb.StringProperty()
    website = ndb.StringProperty()
    verified = ndb.BooleanProperty(default=False)
    verification_id = ndb.StringProperty()
    suspended = ndb.BooleanProperty(default=False)

    photo_url = ndb.StringProperty()
    provider_data = ndb.StringProperty()
    access_token = ndb.StringProperty()

    last_sign_in_date = ndb.DateProperty()
    last_sign_in_time = ndb.TimeProperty()

    def writeLastSignInDate(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.last_sign_in_date = strinput
                return True
            else:
                return False
        except:
            return False

    def writeLastSignInTime(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.last_sign_in_time = strinput
                return True
            else:
                return False
        except:
            return False

    def writePhotoURL(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.photo_url = strinput
                return True
            else:
                return False
        except:
            return False

    def writeProviderData(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.provider_data = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAccessToken(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.access_token = strinput
                return True
            else:
                return False
        except:
            return False

    def writeVerified(self, strinput):
        try:
            if strinput in [True, False]:
                self.verified = strinput
                return True
            else:
                return False

        except:
            return False

    def writeVerificationCode(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.verification_id = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateVerificationCode(self):
        import random, string
        try:
            strVerificationCode = ""
            for i in range(6):
                strVerificationCode += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strVerificationCode
        except:
            return None

    def writeUserID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.uid = strinput
                return True
            else:
                return False
        except:
            return False

    def writeOrganizationID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.organization_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeNames(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.names = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSurname(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.surname = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCell(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.cell = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTel(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.tel = strinput
                return True
            else:
                return False
        except:
            return False

    def writeEmail(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.email = strinput
                return True
            else:
                return False
        except:
            return False

    def writeWebsite(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.website = strinput
                return True
            else:
                return False
        except:
            return False


class Organization(ndb.Expando):
    strUserID = ndb.StringProperty()
    strOrganizationID = ndb.StringProperty()
    strOrganizationName = ndb.StringProperty()
    strDescription = ndb.StringProperty()
    strRegistration = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strTel = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strWebsite = ndb.StringProperty()

    strRegisteringLink = ndb.StringProperty()
    strVerificationCode = ndb.StringProperty()
    strVerified = ndb.BooleanProperty(default=False)

    strSuspended = ndb.BooleanProperty(default=False)

    def writeRegisteringLink(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strRegisteringLink = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateRegisteringLink(self):
        import random, string
        try:
            strRegLink = ""
            for i in range(255):
                strRegLink += random.SystemRandom().choice(
                    string.digits + string.ascii_uppercase + string.digits + string.ascii_lowercase)
            return strRegLink
        except:
            return None

    def writeVerificationCode(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strVerificationCode = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateVerificiationCode(self):
        import random, string
        try:
            strVerificationCode = ""
            for i in range(8):
                strVerificationCode += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strVerificationCode
        except:
            return None

    def writeVerified(self, strinput):
        try:
            if strinput in [True, False]:
                self.strVerified = strinput
                return True
            else:
                return False
        except:
            return False

    def writeUserID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeOrganizationID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strOrganizationID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeOrganizationName(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strOrganizationName = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDescription(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strDescription = strinput
                return True
            else:
                return False
        except:
            return False

    def writeRegistration(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strRegistration = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCell(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTel(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTel = strinput
                return True
            else:
                return False
        except:
            return False

    def writeEmail(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEmail = strinput
                return True
            else:
                return False
        except:
            return False

    def writeWebsite(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strWebsite = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateOrgID(self):
        import random, string
        try:
            strOrganizationID = ""
            for i in range(256):
                strOrganizationID += random.SystemRandom().choice(string.digits + string.ascii_lowercase)

            return strOrganizationID
        except:
            return None

    def writeSuspended(self, strinput):
        try:
            if strinput in [True, False]:
                self.strSuspended = strinput
                return True
            else:
                return False
        except:
            return False


class BankAccountDetails(ndb.Expando):
    strUserID = ndb.StringProperty()
    strOrganizationID = ndb.StringProperty()
    strAccountHolder = ndb.StringProperty()
    strAccountNumber = ndb.StringProperty()
    strAccountType = ndb.StringProperty()
    strBankName = ndb.StringProperty()
    strBranchName = ndb.StringProperty()
    strBranchCode = ndb.StringProperty()

    def writeUserID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeOrganizationID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strOrganizationID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAccountHolder(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccountHolder = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAccountNumber(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccountNumber = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAccountType(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccountType = strinput
                return True
            else:
                return False
        except:
            return False

    def writeBankName(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBankName = strinput
                return True
            else:
                return False
        except:
            return False

    def writeBranchName(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBranchName = strinput
                return True
            else:
                return False
        except:
            return False

    def writeBranchCode(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBranchCode = strinput
                return True
            else:
                return False
        except:
            return False


class Payments(ndb.Expando):
    strUserID = ndb.StringProperty()
    strOrganizationID = ndb.StringProperty()
    strReference = ndb.StringProperty()

    def writeUserID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeOrganizationID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strOrganizationID = strinput
                return True
            else:
                return False
        except:
            return False


class OrganizaHandler(webapp2.RequestHandler):
    def get(self):

        vstrUserID = self.request.get('vstrUserID')
        vstrEmail = self.request.get('vstrEmail')
        vstrAccessToken = self.request.get('vstrAccessToken')

        thisAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

        if thisAccount != None:

            findRequest = Organization.query(Organization.strUserID == thisAccount.uid)
            thisOrgList = findRequest.fetch()

            if len(thisOrgList) > 0:
                thisOrg = thisOrgList[0]
            else:
                thisOrg = Organization()

            findRequest = BankAccountDetails.query(
                BankAccountDetails.strOrganizationID == thisAccount.organization_id)
            thisBankAccountList = findRequest.fetch()

            if len(thisBankAccountList) > 0:
                thisBankAccount = thisBankAccountList[0]
            else:
                thisBankAccount = BankAccountDetails()

            findRequest = UserRights.query(UserRights.strUserID == vstrUserID, UserRights.strAdminUser == True)
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser:
                template = template_env.get_template('templates/organization/org.html')
                context = {'thisOrg': thisOrg, 'thisBankAccount': thisBankAccount}
                self.response.write(template.render(context))
            else:
                template = template_env.get_template('templates/organization/orgread.html')
                context = {'thisOrg': thisOrg}
                self.response.write(template.render(context))
        else:
            # Account not found new user
            thisOrg = Organization()
            thisBankAccount = BankAccountDetails()
            template = template_env.get_template('templates/organization/org.html')
            context = {'thisOrg': thisOrg, 'thisBankAccount': thisBankAccount}
            self.response.write(template.render(context))

    def post(self):

        from mysms import SMSAccount
        from myemail import SendEmail

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrOrganization = self.request.get('vstrOrganization')
            vstrDescription = self.request.get('vstrDescription')
            vstrRegistration = self.request.get('vstrRegistration')
            vstrCell = self.request.get('vstrCell')
            vstrTel = self.request.get('vstrTel')
            vstrEmail = self.request.get('vstrEmail')
            vstrWebsite = self.request.get('vstrWebsite')

            findRequest = Organization.query(Organization.strEmail == vstrEmail)
            thisOrgList = findRequest.fetch()

            if len(thisOrgList) > 0:
                thisOrg = thisOrgList[0]

                if thisOrg.verified:

                    self.response.write("You have already created an account and its verified")
                else:
                    self.response.write(
                        "Your Organization details already captured please click on verification status to verify your account")

            else:
                thisOrg = Organization()

                thisOrg.writeOrganizationID(strinput=thisOrg.CreateOrgID())
                thisOrg.writeUserID(strinput=vstrUserID)
                thisOrg.writeOrganizationName(strinput=vstrOrganization)
                thisOrg.writeDescription(strinput=vstrDescription)
                thisOrg.writeRegistration(strinput=vstrRegistration)
                thisOrg.writeCell(strinput=vstrCell)
                thisOrg.writeTel(strinput=vstrTel)
                thisOrg.writeEmail(strinput=vstrEmail)
                thisOrg.writeWebsite(strinput=vstrWebsite)
                thisOrg.writeRegisteringLink(strinput=thisOrg.CreateRegisteringLink())
                thisOrg.writeVerificationCode(strinput=thisOrg.CreateVerificiationCode())
                thisOrg.put()

                findRequest = Accounts.query(Accounts.uid == vstrUserID)
                thisAccountList = findRequest.fetch()

                if len(thisAccountList) > 0:
                    thisAccount = thisAccountList[0]

                else:
                    thisAccount = Accounts()

                thisAccount.writeOrganizationID(strinput=thisOrg.strOrganizationID)
                thisAccount.writeUserID(strinput=vstrUserID)
                thisAccount.writeEmail(strinput=vstrEmail)
                thisAccount.put()

                findRequest = UserRights.query(UserRights.strUserID == vstrUserID)
                thisUserRightList = findRequest.fetch()

                if len(thisUserRightList) > 0:
                    thisUserRight = thisUserRightList[0]
                else:
                    thisUserRight = UserRights()

                thisUserRight.writeUserID(strinput=vstrUserID)
                thisUserRight.writeEmail(strinput=vstrEmail)
                thisUserRight.setAdminUser(strinput=True)
                thisUserRight.setSuperUser(strinput=False)
                thisUserRight.setGeneralUser(strinput=False)
                thisUserRight.put()

                findRequest = SMSAccount.query(SMSAccount.organization_id == thisOrg.strOrganizationID)
                thisSMSAccountList = findRequest.fetch()

                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]
                else:
                    thisSMSAccount = SMSAccount()

                thisSMSAccount.writeOrganizationID(strinput=thisOrg.strOrganizationID)
                thisSMSAccount.put()
                # Consider using SendMail
                strMessage = """
                <h3>Thank you</h3>
                <p>For registering your organization with Blue IT Marketing Contact and Messaging Management
                application please click on the link below to activate your account</p>

                <a href="https://sa-sms.appspot.com/org/reg/""" + thisOrg.strRegisteringLink + """ ">Registration Link</a> <br>

                Thank You
                Blue IT Marketing Pty LTD
                Team
                """
                # def SendEmail(strFrom,strTo,subject,body,strTextType,strAttachFileContent=None,strAttachFileName=None):
                if SendEmail(strFrom="verifications@sa-sms.appspotmail.com", strTo=thisOrg.strEmail,
                             strSubject="Business Messaging and Contact Management Account Activation",
                             strBody=strMessage, strTextType='text/html'):
                    self.response.write(
                        "Successfully created organization Account an Email is sent to your email address for verification")
                else:
                    self.response.write(
                        "Successfully created organization Account please remember to verify your account")

        elif vstrChoice == "1":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrAccountHolder = self.request.get('vstrAccountHolder')
            vstrAccountNumber = self.request.get('vstrAccountNumber')
            vstrAccountType = self.request.get('vstrAccountType')
            vstrBankName = self.request.get('vstrBankName')
            vstrBranchName = self.request.get('vstrBranchName')
            vstrBranchCode = self.request.get('vstrBranchCode')

            findRequest = UserRights.query(UserRights.strUserID == vstrUserID)
            thisUserRightList = findRequest.fetch()

            if len(thisUserRightList) > 0:
                thisUserRight = thisUserRightList[0]

                if thisUserRight.strAdminUser:

                    findRequest = Accounts.query(Accounts.uid == vstrUserID)
                    thisAccountList = findRequest.fetch()

                    if len(thisAccountList) > 0:
                        thisAccount = thisAccountList[0]

                        findRequest = BankAccountDetails.query(
                            BankAccountDetails.strOrganizationID == thisAccount.organization_id)
                        thisBankAccountList = findRequest.fetch()

                        if len(thisBankAccountList) > 0:
                            thisBankAccount = thisBankAccountList[0]
                        else:
                            thisBankAccount = BankAccountDetails()

                        thisBankAccount.writeAccountHolder(strinput=vstrAccountHolder)
                        thisBankAccount.writeAccountNumber(strinput=vstrAccountNumber)
                        thisBankAccount.writeAccountType(strinput=vstrAccountType)
                        thisBankAccount.writeBankName(strinput=vstrBankName)
                        thisBankAccount.writeBranchName(strinput=vstrBranchName)
                        thisBankAccount.writeBranchCode(strinput=vstrBranchCode)
                        thisBankAccount.writeUserID(strinput=vstrUserID)
                        thisBankAccount.writeOrganizationID(strinput=thisAccount.organization_id)
                        thisBankAccount.put()

                        self.response.write("Organization Bank Account successfully updated")
                    else:
                        self.response.write("Error updating Bank Account")
                else:
                    self.response.write("You have insufficient rights to manage Organization Bank Accounts")
            else:
                self.response.write("You have insufficient rights to manage Organization Bank Accounts")


class ManageUsersHandler(webapp2.RequestHandler):
    def get(self):
        # Admin Users
        vstrUserID = self.request.get('vstrUserID')
        vstrEmail = self.request.get('vstrEmail')
        vstrAccessToken = self.request.get('vstrAccessToken')

        findRequest = UserRights.query(UserRights.strUserID == vstrUserID)
        thisUserRightList = findRequest.fetch()

        if len(thisUserRightList) > 0:
            thisAdmin = thisUserRightList[0]

            if thisAdmin.strAdminUser:
                findRequest = Accounts.query(Accounts.uid == vstrUserID)
                thisAccountList = findRequest.fetch()

                if len(thisAccountList) > 0:
                    thisAccount = thisAccountList[0]

                    findRequest = Accounts.query(Accounts.organization_id == thisAccount.organization_id,
                                                 Accounts.verified == True, Accounts.suspended == False)
                    thisActiveAccountList = findRequest.fetch()

                    findRequest = Accounts.query(Accounts.organization_id == thisAccount.organization_id,
                                                 Accounts.verified == True, Accounts.suspended == True)
                    thisSuspendedAccountList = findRequest.fetch()

                    findRequest = OpenInvites.query(OpenInvites.organization_id == thisAccount.organization_id)
                    thisSentInvitesList = findRequest.fetch()

                    templates = template_env.get_template('templates/users/users.html')
                    context = {'thisActiveAccountList': thisActiveAccountList,
                               'thisSuspendedAccountList': thisSuspendedAccountList, 'thisAccount': thisAccount,
                               'thisSentInvitesList': thisSentInvitesList}
                    self.response.write(templates.render(context))
                else:
                    ErrorMessage = "Error accessign users manager please verify your account first"
                    template = template_env.get_template("templates/errors/suberror.html")
                    context = {'ErrorMessage': ErrorMessage}
                    self.response.write(template.render(context))

            else:
                self.response.write("You cant access users list since you dont belong to any admin groups")
        else:
            self.response.write("TODO2- Show an interface allowing the user to create his or her account details")

    def post(self):
        from mysms import SMSAccount, SMSPortalBudget, SMSPortalVodacom, ClickSendSMSPortal
        from myTwilio import MyTwilioPortal

        vstrChoice = self.request.get('vstrChoice')
        if vstrChoice == "0":

            # '&vstrUserID=' + struid + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrNames = self.request.get('vstrNames')
            vstrSurname = self.request.get('vstrSurname')
            vstrCell = self.request.get('vstrCell')
            vstrTel = self.request.get('vstrTel')
            vstrEmail = self.request.get('vstrEmail')
            vstrWebsite = self.request.get('vstrWebsite')

            thisAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if thisAccount != None:
                pass
            else:
                thisAccount = Accounts()
                thisAccount.writeUserID(strinput=vstrUserID)
                findRequest = Organization.query(Organization.strUserID == vstrUserID)
                thisOrgList = findRequest.fetch()

                if len(thisOrgList) > 0:
                    thisOrg = thisOrgList[0]
                    thisAccount.writeOrganizationID(strinput=thisOrg.organization_id)

            thisAccount.writeNames(strinput=vstrNames)
            thisAccount.writeSurname(strinput=vstrSurname)
            thisAccount.writeCell(strinput=vstrCell)
            thisAccount.writeTel(strinput=vstrTel)
            thisAccount.writeEmail(strinput=vstrEmail)
            thisAccount.writeWebsite(strinput=vstrWebsite)
            thisAccount.writeVerificationCode(strinput=thisAccount.CreateVerificationCode())
            thisAccount.writeAccessToken(strinput=vstrAccessToken)
            thisAccount.put()

            self.response.write("Account information saved successfully")


        elif vstrChoice == "1":
            # '&vstrUserID=' + struid + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrCell = self.request.get('vstrCell')
            vstrEmail = self.request.get('vstrEmail')
            logging.info(vstrCell)

            thisAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if thisAccount != None:
                pass
            else:
                thisAccount = Accounts()

            findRequest = UserRights.query(UserRights.strUserID == thisAccount.uid)
            thisUserRightList = findRequest.fetch()

            if len(thisUserRightList) > 0:
                thisUserRight = thisUserRightList[0]

                if thisUserRight.strAdminUser:
                    findRequest = SMSAccount.query(SMSAccount.organization_id == thisAccount.organization_id)
                    thisSMSAccountList = findRequest.fetch()
                    logging.info("User rights ok and inside SMS Account aso the account is ok")

                    if len(thisSMSAccountList) > 0:
                        thisSMSAccount = thisSMSAccountList[0]

                        strMessageHeader = "Blue IT Marketing" + "%0A"
                        strAppName = "Bulk Messaging and Contact Management" + "%0A"
                        strMessage = "This is an invitation sent by : " + thisAccount.names + "  " + thisAccount.surname + "%0A"
                        strMessage2 = " please click the following link to start using our app as part of their team : " + "%0A"
                        strlink = "https://sa-sms.appspot.com/admin/users/invites"

                        strInviteMessage = strMessageHeader + strAppName + strMessage + strMessage2 + strlink

                        logging.info("We will be sending this message to the user : " + strInviteMessage)

                        if thisSMSAccount.total_sms > 0:

                            if thisSMSAccount.use_portal == "Vodacom":
                                findRequest = SMSPortalVodacom.query()
                                thisVodaPortalList = findRequest.fetch()
                                if len(thisVodaPortalList) > 0:
                                    thisVodaPortal = thisVodaPortalList[0]
                                else:
                                    thisVodaPortal = SMSPortalVodacom()

                                strCellList = []
                                strCellList.append(vstrCell)
                                logging.info("Sending Message using Vodacom")

                                if thisVodaPortal.cron_send_messages(cell_number_list=strCellList,
                                                                     message=strInviteMessage,
                                                                     account_id=thisAccount.organization_id):
                                    thisSMSAccount.total_sms = thisSMSAccount.total_sms - 4
                                    self.response.write("Successfully sent an invitation message")
                                else:
                                    self.response.write("Error sending SMS Invitation")

                            elif thisSMSAccount.use_portal == "Budget":
                                findRequest = SMSPortalBudget.query()
                                thisBudgetPortalList = findRequest.fetch()
                                if len(thisBudgetPortalList) > 0:
                                    thisBudgetPortal = thisBudgetPortalList[0]
                                else:
                                    thisBudgetPortal = SMSPortalBudget()

                                logging.info("Sending message using budget")

                                if thisBudgetPortal.SendCronMessage(strCell=vstrCell,
                                                                    strMessage=strInviteMessage) != None:
                                    thisSMSAccount.total_sms = thisSMSAccount.total_sms - 4
                                    self.response.write("Successfully sent an invite message")
                                else:
                                    self.response.write("Error sending SMS Invitation")

                            elif thisSMSAccount.use_portal == "Twilio":
                                findRequest = MyTwilioPortal.query()
                                myTwilioPortalList = findRequest.fetch()

                                if len(myTwilioPortalList) > 0:
                                    thisTwilioPortal = myTwilioPortalList[0]
                                else:
                                    thisTwilioPortal = MyTwilioPortal()

                                logging.info("Sending invitations through Twilio Portal")

                                if thisTwilioPortal.send_sms(to_cell=vstrCell, message=strInviteMessage) != None:
                                    thisSMSAccount.total_sms = thisSMSAccount.total_sms - 4
                                    self.response.write("Successfully sent an invite message")
                                else:
                                    self.response.write("Error sending SMS Invitation")
                            elif thisSMSAccount.use_portal == "ClickSend":
                                findRequest = ClickSendSMSPortal.query()
                                MyClickSendPortalList = findRequest.fetch()

                                if len(MyClickSendPortalList) > 0:
                                    thisClickSendPortal = MyClickSendPortalList[0]
                                else:
                                    thisClickSendPortal = ClickSendSMSPortal()

                                logging.info("Sending Invitations through Click Send Portal")

                                if thisClickSendPortal.send_sms(cell=vstrCell, message=strInviteMessage) != None:
                                    thisSMSAccount.total_sms = thisSMSAccount.total_sms - 4
                                    self.response.write("Successfully sent an invite message")
                                else:
                                    self.response.write("Error sending SMS Invitation")

                            else:
                                self.response.write(
                                    "Cannot find an useful portal to send messages...please contact the system administrator")

                            thisSMSAccount.put()

                            findRequest = OpenInvites.query(OpenInvites.cell == vstrCell)
                            thisOpenInviteList = findRequest.fetch()

                            if len(thisOpenInviteList) > 0:
                                thisOpenInvite = thisOpenInviteList[0]
                            else:
                                thisOpenInvite = OpenInvites()

                            thisDateTime = datetime.datetime.now()
                            strThisDate = thisDateTime.date()
                            strThisTime = thisDateTime.time()

                            thisOpenInvite.writeOrganizationID(strinput=thisSMSAccount.organization_id)
                            thisOpenInvite.writeCell(strinput=vstrCell)
                            thisOpenInvite.writeEmail(strinput=vstrEmail)
                            thisOpenInvite.writeSecurityCode(strinput=thisOpenInvite.CreateSecurityCode())
                            thisOpenInvite.writeDateSent(strinput=strThisDate)
                            thisOpenInvite.writeTimeSent(strinput=strThisTime)
                            thisOpenInvite.put()
                        else:
                            self.response.write("Cannot send SMS Invitation Please contact your system admin")
                    else:
                        self.response.write(
                            "Cannot Access your SMS Account please contact your system administrator or recreate your account")
                else:
                    self.response.write("You have insufficient rights to send user invitations")
            else:
                self.response.write("You have insufficient rights to send user invitations")


class ThisOrgAccountActivationHandler(webapp2.RequestHandler):

    def get(self):
        from dashboard import Employees
        from mysms import SMSAccount, SMSPortalVodacom, SMSPortalBudget, ClickSendSMSPortal
        from myTwilio import MyTwilioPortal
        import logging
        URL = self.request.url
        strURLList = URL.split('/')
        strRegLink = strURLList[len(strURLList) - 1]

        findRequest = Organization.query(Organization.strRegisteringLink == strRegLink)
        thisOrgList = findRequest.fetch()

        if len(thisOrgList) > 0:
            thisOrg = thisOrgList[0]

            thisAdminStaff = Employees()
            findRequests = SMSAccount.query(SMSAccount.organization_id == thisAdminStaff.staff_id)
            thisSMSAccountList = findRequests.fetch()

            if len(thisSMSAccountList) > 0:
                thisSMSAccount = thisSMSAccountList[0]
            else:
                thisSMSAccount = SMSAccount()
                thisSMSAccount.writeOrganizationID(strinput=thisAdminStaff.staff_id)
                thisSMSAccount.writeUsePortal(strinput="Budget")
                thisSMSAccount.put()

            ReceipientList = []
            ReceipientList.append(thisOrg.cell)
            strMessage = thisOrg.verification_id

            if thisSMSAccount.use_portal == "Vodacom":
                findRequests = SMSPortalVodacom.query()
                thisVodaPortalList = findRequests.fetch()

                if len(thisVodaPortalList) > 0:
                    Voda = thisVodaPortalList[0]
                else:
                    Voda = SMSPortalVodacom()
                    Voda.put()

                if Voda.cron_send_messages(cell_number_list=ReceipientList, message=strMessage,
                                           account_id=thisAdminStaff.staff_id):
                    logging.info("Successfully sent activation message")
                else:
                    logging.info("Error sending activation message")

            elif thisSMSAccount.use_portal == "Budget":
                findRequests = SMSPortalBudget.query()
                thisBudgetPortalList = findRequests.fetch()

                if len(thisBudgetPortalList) > 0:
                    thisBudget = thisBudgetPortalList[0]
                else:
                    thisBudget = SMSPortalBudget()
                    thisBudget.put()
                strSent = False
                for thisNumber in ReceipientList:
                    strRef = thisBudget.SendCronMessage(strCell=thisNumber, strMessage=strMessage)

                    if strRef != None:
                        logging.info("Successfully sent Verification Mesage")
                    else:
                        logging.info("Error Sending Verification Message")



            elif thisSMSAccount.use_portal == "ClickSend":
                findRequest = ClickSendSMSPortal.query()
                thisClickSendList = findRequest.fetch()

                if len(thisClickSendList) > 0:
                    thisClickSend = thisClickSendList[0]
                else:
                    thisClickSend = ClickSendSMSPortal()

                for thisNumber in ReceipientList:
                    strRef = thisClickSend.send_sms(cell=thisNumber, message=strMessage)

                    if strRef != None:
                        logging.info("Successfully sent Verification Mesage")
                    else:
                        logging.info("Error Sending Verification Message")

            elif thisSMSAccount.use_portal == "Twilio":
                findRequest = MyTwilioPortal.query()
                thisMyTwilioPortalList = findRequest.fetch()

                if len(thisMyTwilioPortalList) > 0:
                    thisTwilioPortal = thisMyTwilioPortalList[0]
                else:
                    thisTwilioPortal = MyTwilioPortal()

                for thisNumber in ReceipientList:
                    strRef = thisTwilioPortal.send_sms(to=thisNumber, message=strMessage,
                                                       from_cell=thisTwilioPortal.sms_number)
                    if strRef != None:
                        logging.info("Successfully sent Verification Mesage")
                    else:
                        logging.info("Error Sending Verification Message")

            findRequest = SMSAccount.query(SMSAccount.organization_id == thisOrg.organization_id)
            thisSMSAccountList = findRequest.fetch()

            if len(thisSMSAccountList) > 0:
                thisSMSAccount = thisSMSAccountList[0]
            else:
                thisSMSAccount = SMSAccount()

            templates = template_env.get_template('templates/organization/thisVerification.html')
            context = {'thisOrg': thisOrg, 'thisSMSAccount': thisSMSAccount}
            self.response.write(templates.render(context))

    def post(self):

        # + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
        vstrUserID = self.request.get('vstrUserID')
        vstrEmail = self.request.get('vstrEmail')
        vstrAccessToken = self.request.get('vstrAccessToken')

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            vstrRegLink = self.request.get('vstrRegLink')
            vstrVerificationCode = self.request.get('vstrVerificationCode')

            findRequest = Organization.query(Organization.strRegisteringLink == vstrRegLink)
            thisOrgList = findRequest.fetch()

            if len(thisOrgList) > 0:
                thisOrg = thisOrgList[0]

                if thisOrg.verification_id == vstrVerificationCode:
                    thisOrg.writeVerified(strinput=True)
                    thisOrg.put()
                    findRequest = Accounts.query(Accounts.uid == vstrUserID)
                    thisAccountList = findRequest.fetch()
                    if len(thisAccountList) > 0:
                        thisAccount = thisAccountList[0]
                        thisAccount.writeVerified(strinput=True)
                        thisAccount.put()

                    self.response.write(
                        "Your Account is verified please buy SMS Credits to start using our Contact and Messaging Management Application")
                else:
                    self.response.write("Error Verifying your account, please try again")
            else:
                self.response.write("Fatal Error registering your organization please inform our system administrator")


class ThisOrgHandler(webapp2.RequestHandler):
    def get(self):
        from advertise import Orders
        from mysms import SMSAccount
        URL = self.request.url
        strURLlist = URL.split("/")
        strOrganizationID = strURLlist[len(strURLlist) - 1]

        findRequest = Organization.query(Organization.strOrganizationID == strOrganizationID)
        thisOrgList = findRequest.fetch()

        if len(thisOrgList) > 0:
            thisOrg = thisOrgList[0]
        else:
            thisOrg = Organization()

        findRequest = SMSAccount.query(SMSAccount.organization_id == thisOrg.strOrganizationID)
        thisSMSAccountList = findRequest.fetch()

        if len(thisSMSAccountList) > 0:
            thisSMSAccount = thisSMSAccountList[0]
        else:
            thisSMSAccount = SMSAccount()

        findRequest = Accounts.query(Accounts.organization_id == strOrganizationID, Accounts.verified == True,
                                     Accounts.suspended == False)
        thisActiveUserAccountsList = findRequest.fetch()
        findRequest = Accounts.query(Accounts.organization_id == strOrganizationID, Accounts.verified == False,
                                     Accounts.suspended == False)
        thisNewUserAccountsList = findRequest.fetch()
        findRequest = Accounts.query(Accounts.organization_id == strOrganizationID, Accounts.verified == True,
                                     Accounts.suspended == True)
        thisSuspendedUserAccountsList = findRequest.fetch()

        findRequest = Orders.query(Orders.organization_id == strOrganizationID, Orders.fully_paid == True)
        thisActiveAdvertisingOrdersList = findRequest.fetch()

        findRequest = Orders.query(Orders.organization_id == strOrganizationID, Orders.fully_paid == False)
        thisOutStandingAdvertisingOrderList = findRequest.fetch()

        templates = template_env.get_template('templates/dashboard/dashfiles/thisorg.html')
        context = {'thisOrg': thisOrg, 'thisSMSAccount': thisSMSAccount,
                   'thisActiveUserAccountsList': thisActiveUserAccountsList,
                   'thisNewUserAccountsList': thisNewUserAccountsList,
                   'thisSuspendedUserAccountsList': thisSuspendedUserAccountsList,
                   'thisActiveAdvertisingOrdersList': thisActiveAdvertisingOrdersList,
                   'thisOutStandingAdvertisingOrderList': thisOutStandingAdvertisingOrderList}
        self.response.write(templates.render(context))

    def post(self):
        from mysms import SMSAccount
        if users.is_current_user_admin():
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                vstrUserID = self.request.get('vstrUserID')
                vstrEmail = self.request.get('vstrEmail')
                vstrAccessToken = self.request.get('vstrAccessToken')

                vstrOrganizationName = self.request.get('vstrOrganizationName')
                vstrDescription = self.request.get('vstrDescription')
                vstrRegistration = self.request.get('vstrRegistration')
                vstrCell = self.request.get('vstrCell')
                vstrTel = self.request.get('vstrTel')
                vstrEmail = self.request.get('vstrEmail')
                vstrWebsite = self.request.get('vstrWebsite')
                vstrRegisteringLink = self.request.get('vstrRegisteringLink')
                vstrVerificationCode = self.request.get('vstrVerificationCode')
                vstrVerified = self.request.get('vstrVerified')
                vstrSuspended = self.request.get('vstrSuspended')

                findRequest = Organization.query(Organization.strCell == vstrCell, Organization.strEmail == vstrEmail)
                thisOrgList = findRequest.fetch()

                if len(thisOrgList) > 0:
                    thisOrg = thisOrgList[0]
                else:
                    thisOrg = Organization()

                thisOrg.writeOrganizationName(strinput=vstrOrganizationName)
                thisOrg.writeDescription(strinput=vstrDescription)
                thisOrg.writeRegistration(strinput=vstrRegistration)
                thisOrg.writeCell(strinput=vstrCell)
                thisOrg.writeTel(strinput=vstrTel)
                thisOrg.writeEmail(strinput=vstrEmail)
                thisOrg.writeWebsite(strinput=vstrWebsite)
                thisOrg.writeRegisteringLink(strinput=vstrRegisteringLink)
                thisOrg.writeVerificationCode(strinput=vstrVerificationCode)
                if vstrVerified == "YES":
                    thisOrg.writeVerified(strinput=True)
                else:
                    thisOrg.writeVerified(strinput=False)

                if vstrSuspended == "YES":
                    thisOrg.writeSuspended(strinput=True)
                else:
                    thisOrg.writeSuspended(strinput=False)

                thisOrg.put()

                self.response.write("Organization details updated successfully")

            elif vstrChoice == "1":
                # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                vstrUserID = self.request.get('vstrUserID')
                vstrEmail = self.request.get('vstrEmail')
                vstrAccessToken = self.request.get('vstrAccessToken')

                vstrOrganizationID = self.request.get('vstrOrganizationID')
                vstrCreditAmount = self.request.get('vstrCreditAmount')
                vstrCostPerSMS = self.request.get('vstrCostPerSMS')
                vstrTotalSMS = self.request.get('vstrTotalSMS')
                vstrDateCredited = self.request.get('vstrDateCredited')
                vstrTimeCredited = self.request.get('vstrTimeCredited')
                vstrUsePortal = self.request.get('vstrUsePortal')
                vstrDepositReference = self.request.get('vstrDepositReference')

                findRequest = SMSAccount.query(SMSAccount.organization_id == vstrOrganizationID)
                thisSMSAccountList = findRequest.fetch()

                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]
                    logging.info("SMS Account found")
                else:
                    thisSMSAccount = SMSAccount()

                thisSMSAccount.writeOrganizationID(strinput=vstrOrganizationID)
                thisSMSAccount.writeCreditAmount(strinput=vstrCreditAmount)
                thisSMSAccount.writeCostPerSMS(strinput=vstrCostPerSMS)
                thisSMSAccount.writeTotalSMS(strinput=vstrTotalSMS)
                thisSMSAccount.writeUsePortal(strinput=vstrUsePortal)
                thisSMSAccount.writeDepositReference(strinput=vstrDepositReference)
                thisSMSAccount.put()
                self.response.write("SMS Account successfully updated")


class UsersInvitesHandler(webapp2.RequestHandler):
    def get(self):
        # TODO- check to see if we dont need to return database results here
        template = template_env.get_template('templates/users/invites.html')
        context = {}
        self.response.write(template.render(context))

    def post(self):
        from mysms import SMSAccount, SMSPortalBudget, ClickSendSMSPortal
        from myTwilio import MyTwilioPortal
        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAcceptToken = self.request.get('vstrAcceptToken')

            vstrCell = self.request.get('vstrCell')

            findRequest = OpenInvites.query(OpenInvites.cell == vstrCell)
            thisOpenInvitesList = findRequest.fetch()

            if len(thisOpenInvitesList) > 0:
                thisOpenInvite = thisOpenInvitesList[0]

                findRequest = Organization.query(Organization.strCell == vstrCell)
                thisOrganizationList = findRequest.fetch()
                if len(thisOrganizationList) > 0:
                    thisOrg = thisOrganizationList[0]

                    findRequest = SMSAccount.query(SMSAccount.organization_id == thisOrg.organization_id)
                    thisSMSAccountList = findRequest.fetch()

                    if len(thisSMSAccountList) > 0:
                        thisSMSAccount = thisSMSAccountList[0]

                        findRequest = SMSPortalBudget.query()
                        thisBudgetPortaList = findRequest.fetch()

                        if len(thisBudgetPortaList) > 0:
                            thisBudgetPortal = thisBudgetPortaList[0]
                            thisBudgetPortal.SendCronMessage(strCell=vstrCell,
                                                             strMessage=thisOpenInvite.security_code)
                            thisSMSAccount.total_sms -= 1
                            thisSMSAccount.put()

                    template = template_env.get_template('templates/users/sub/accept.html')
                    context = {'thisOpenInvite': thisOpenInvite, 'thisOrg': thisOrg}
                    self.response.write(template.render(context))
                else:
                    self.response.write("Your invitation is not present in the system")

            else:
                self.response.write("Your invitation is not present in the system")

        elif vstrChoice == "1":
            # '&vstrUserID=' + struid + '&vstrAcceptToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrAcceptToken = self.request.get('vstrAcceptToken')

            vstrNames = self.request.get('vstrNames')
            vstrSurname = self.request.get('vstrSurname')
            vstrCell = self.request.get('vstrCell')
            vstrEmail = self.request.get('vstrEmail')
            vstrSecurityCode = self.request.get('vstrSecurityCode')

            findRequest = OpenInvites.query(OpenInvites.cell == vstrCell)
            thisOpenInviteList = findRequest.fetch()

            if len(thisOpenInviteList) > 0:
                thisOpenInvite = thisOpenInviteList[0]

                if vstrSecurityCode == thisOpenInvite.security_code:

                    if thisOpenInvite.cell == vstrCell:

                        findRequest = Accounts.query(Accounts.cell == thisOpenInvite.cell)
                        thisAccountList = findRequest.fetch()

                        if len(thisAccountList) > 0:
                            thisAccount = thisAccountList[0]
                            self.response.write("You already have an account in the system")
                        else:
                            thisAccount = Accounts()
                            thisAccount.writeOrganizationID(strinput=thisAccount.organization_id)
                            thisAccount.writeCell(strinput=vstrCell)
                            thisAccount.writeEmail(strinput=vstrEmail)
                            thisAccount.writeNames(strinput=vstrNames)
                            thisAccount.writeSurname(strinput=vstrSurname)
                            thisAccount.writeUserID(strinput=vstrUserID)
                            thisAccount.writeVerificationCode(strinput=thisAccount.CreateVerificationCode())
                            thisAccount.put()
                            self.response.write("You have successfully signed up and can using your account")
                    else:
                        self.response.write("Invalid cell number")
                else:
                    self.response.write("Invalid Security code")
            else:
                self.response.write("Fatal Error Your cell number is not attached to any invitation")

        elif vstrChoice == "2":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAcceptToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAcceptToken = self.request.get('vstrAcceptToken')

            vstrCell = self.request.get('vstrCell')

            findRequest = OpenInvites.query(OpenInvites.cell == vstrCell)
            thisOpenInviteList = findRequest.fetch()

            if len(thisOpenInviteList) > 0:
                thisOpenInvite = thisOpenInviteList[0]

                findRequest = SMSAccount.query(SMSAccount.organization_id == thisOpenInvite.organization_id)
                thisSMSAccountList = findRequest.fetch()

                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]

                    if thisSMSAccount.use_portal == "Budget":

                        findRequest = SMSPortalBudget.query()
                        thisBudgetPortaList = findRequest.fetch()

                        if len(thisBudgetPortaList) > 0:
                            thisBudgetPortal = thisBudgetPortaList[0]
                            if thisBudgetPortal.SendCronMessage(strCell=vstrCell,
                                                                strMessage=thisOpenInvite.security_code) != None:
                                thisSMSAccount.total_sms = thisSMSAccount.total_sms - 1
                                thisSMSAccount.put()
                                self.response.write("Security Code successfully sent please enter the code")

                    elif thisSMSAccount.use_portal == "Twilio":
                        findRequest = MyTwilioPortal.query()
                        MyTwilioPortalList = findRequest.fetch()

                        if len(MyTwilioPortalList) > 0:
                            thisTwilioPortal = MyTwilioPortalList[0]
                        else:
                            thisTwilioPortal = MyTwilioPortal()

                        if thisTwilioPortal.send_sms(to=vstrCell, message=thisOpenInvite.security_code) != None:
                            thisSMSAccount.total_sms = thisSMSAccount.total_sms - 1
                            thisSMSAccount.put()
                            self.response.write("Security Code successfully sent please enter the code")

                    elif thisSMSAccount.use_portal == "ClickSend":
                        findRequest = ClickSendSMSPortal.query()
                        MyClickSendPortaList = findRequest.fetch()

                        if len(MyClickSendPortaList) > 0:
                            thisClickSendPortal = MyClickSendPortaList[0]
                        else:
                            thisClickSendPortal = ClickSendSMSPortal()

                        if thisClickSendPortal.send_sms(cell=vstrCell, message=thisOpenInvite.security_code) != None:
                            thisSMSAccount.total_sms = thisSMSAccount.total_sms - 1
                            thisSMSAccount.put()
                            self.response.write("Security Code successfully sent please enter the code")


class ThisAdvertAccountHandler(webapp2.RequestHandler):
    def get(self):
        """
            Besides account and or order payment verification we can also use this screen to check on the advert stats of the user

        :return:
        """

        from advertise import Orders, Advert

        URL = self.request.url
        strURLlist = URL.split("/")
        strDepositReference = strURLlist[len(strURLlist) - 1]

        # The Actual Order requested
        findRequest = Orders.query(Orders.deposit_reference == strDepositReference)
        thisOrderList = findRequest.fetch()

        if len(thisOrderList) > 0:
            thisOrder = thisOrderList[0]
        else:
            thisOrder = Orders()

        # Organization details of the owner of the account
        findRequest = Organization.query(Organization.strOrganizationID == thisOrder.organization_id)
        thisOrgList = findRequest.fetch()

        if len(thisOrgList) > 0:
            thisOrg = thisOrgList[0]
        else:
            thisOrg = Organization()

        # Main Account Details of the owner of the account
        findRequest = Accounts.query(Accounts.uid == thisOrder.uid)
        thisAccountList = findRequest.fetch()

        if len(thisAccountList) > 0:
            thisAccount = thisAccountList[0]
        else:
            thisAccount = Accounts()

        # The Advert being paid for
        findRequest = Advert.query(Advert.advert_id == thisOrder.advert_id)
        thisAdvertList = findRequest.fetch()

        if len(thisAdvertList) > 0:
            thisAdvert = thisAdvertList[0]
        else:
            thisAdvert = Advert()

        from advertise import Payments  # This is to force the use of payments class in adverts
        # Payment details Advert
        findRequest = Payments.query(Payments.order_id == thisOrder.order_id)
        thisRelatedPaymentList = findRequest.fetch()

        # User Organization Payment Details
        findRequest = Payments.query(Payments.organization_id == thisOrder.organization_id)
        thisOrganizationPaymentsList = findRequest.fetch()

        template = template_env.get_template('templates/dashboard/payments/AdvertOrders.html')
        context = {'thisOrder': thisOrder, 'thisOrg': thisOrg, 'thisAccount': thisAccount, 'thisAdvert': thisAdvert,
                   'thisRelatedPaymentList': thisRelatedPaymentList,
                   'thisOrganizationPaymentsList': thisOrganizationPaymentsList}
        self.response.write(template.render(context))

    def post(self):
        from advertise import Payments, Orders
        vstrChoice = self.request.get('vstrChoice')
        if vstrChoice == "0":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrDepositReference = self.request.get('vstrDepositReference')
            vstrAmount = self.request.get('vstrAmount')
            vstrPaymentMethod = self.request.get('vstrPaymentMethod')

            findRequest = Orders.query(Orders.deposit_reference == vstrDepositReference)
            thisOrderList = findRequest.fetch()

            if len(thisOrderList) > 0:
                thisOrder = thisOrderList[0]
            else:
                thisOrder = Orders()

            vstrThisDate = datetime.datetime.now()
            strThisDate = vstrThisDate.date()
            strThisTime = datetime.time(hour=vstrThisDate.hour, minute=vstrThisDate.minute, second=vstrThisDate.second)

            thisPayment = Payments()
            thisPayment.writeOrderID(strinput=thisOrder.order_id)
            thisPayment.writeUserID(strinput=thisOrder.uid)
            thisPayment.writeOrganizationID(strinput=thisOrder.organization_id)
            thisPayment.writePaymentID(strinput=thisPayment.CreatePaymentID())
            thisPayment.writeDepositReference(strinput=thisOrder.deposit_reference)

            thisPayment.writeAmountPaid(strinput=vstrAmount)
            thisPayment.writePaymentMethod(strinput=vstrPaymentMethod)

            thisPayment.writeDatePaid(strinput=strThisDate)
            thisPayment.writeTimePaid(strinput=strThisTime)
            thisPayment.writePaymentVerified(strinput=True)
            thisPayment.put()
            strTotalPaid = thisOrder.total_paid + int(vstrAmount)
            thisOrder.writeTotalPaid(strinput=strTotalPaid)
            if thisOrder.total_paid >= thisOrder.quoted_amount:
                thisOrder.writeFullyPaid(strinput=True)
                thisOrder.writeRunOrder(strinput=True)
            thisOrder.put()

            self.response.write("Successfully verified payment")


class AccountsAPIHandler(webapp2.RequestHandler):
    def get(self):
        from myapi import EndPoints
        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            findRequest = Accounts.query(Accounts.uid == vstrUserID)
            thisAccountList = findRequest.fetch()
            if len(thisAccountList) > 0:
                thisAccount = thisAccountList[0]
                if thisAccount.verified:
                    findRequest = EndPoints.query(EndPoints.organization_id == thisAccount.organization_id)
                    thisEndPointList = findRequest.fetch()

                    if len(thisEndPointList) > 0:
                        thisEndPoint = thisEndPointList[0]
                    else:
                        thisEndPoint = EndPoints()
                        thisEndPoint.writeAPiKey(strinput=thisEndPoint.CreateAPIKey())
                        thisEndPoint.writeAPISecret(strinput=thisEndPoint.CreateAPISecret())
                        thisEndPoint.writePointID(strinput=thisEndPoint.CreatePointID())
                        thisEndPoint.writeOrganizationID(strinput=thisAccount.organization_id)
                        thisEndPoint.put()

                    template = template_env.get_template('templates/api/UserEndPoint.html')
                    context = {'thisEndPoint': thisEndPoint}
                    self.response.write(template.render(context))

        else:
            self.response.write("No valid choice")

    def post(self):
        from myapi import EndPoints
        vstrChoice = self.request.get('vstrChoice')
        # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
        vstrUserID = self.request.get('vstrUserID')
        vstrEmail = self.request.get('vstrEmail')
        vstrAccessToken = self.request.get('vstrAccessToken')

        if vstrChoice == "0":
            vstrPointURL = self.request.get('vstrPointURL')

            findRequest = Accounts.query(Accounts.uid == vstrUserID)
            thisAccountList = findRequest.fetch()

            if len(thisAccountList) > 0:
                thisAccount = thisAccountList[0]

                findRequest = EndPoints.query(EndPoints.organization_id == thisAccount.organization_id)
                thisEndPointList = findRequest.fetch()

                if len(thisEndPointList) > 0:
                    thisEndPoint = thisEndPointList[0]
                    thisEndPoint.writePointURL(strinput=vstrPointURL)
                    thisEndPoint.put()
                    self.response.write("Successfully updated API")
                else:
                    self.response.write("Fatal Error updating API")
            else:
                self.response.write("Account not Valid")


class ManageCreditHandler(webapp2.RequestHandler):
    def get(self):
        from mysms import SMSAccount
        from advertise import AddAccount
        from surveys import SurveyAccount
        from affiliates import Affiliate
        vstrUserID = self.request.get('vstrUserID')
        vstrEmail = self.request.get('vstrEmail')
        vstrAccessToken = self.request.get('vstrAccessToken')

        findRequest = Accounts.query(Accounts.uid == vstrUserID)
        thisAccountList = findRequest.fetch()
        if len(thisAccountList) > 0:
            thisAccount = thisAccountList[0]

            findRequest = SMSAccount.query(SMSAccount.organization_id == thisAccount.organization_id)
            thisSMSAccountList = findRequest.fetch()
            if len(thisSMSAccountList) > 0:
                thisSMSAccount = thisSMSAccountList[0]
            else:
                thisSMSAccount = SMSAccount()

            findRequest = AddAccount.query(AddAccount.organization_id == thisAccount.organization_id)
            thisAddAccountList = findRequest.fetch()

            if len(thisAddAccountList) > 0:
                thisAddAccount = thisAddAccountList[0]
            else:
                thisAddAccount = AddAccount()

            findRequest = SurveyAccount.query(SurveyAccount.organization_id == thisAccount.organization_id)
            thisSurveyAccountList = findRequest.fetch()

            if len(thisSurveyAccountList) > 0:
                thisSurveyAccount = thisSurveyAccountList[0]
            else:
                thisSurveyAccount = SurveyAccount()

            findRequest = Affiliate.query(Affiliate.uid == vstrUserID)
            thisAffiliateList = findRequest.fetch()

            if len(thisAffiliateList) > 0:
                thisAffilite = thisAffiliateList[0]
            else:
                thisAffilite = Affiliate()

            template = template_env.get_template('templates/account/managecredits.html')
            context = {'thisSMSAccount': thisSMSAccount, 'thisAddAccount': thisAddAccount,
                       'thisSurveyAccount': thisSurveyAccount, 'thisAffilite': thisAffilite}
            self.response.write(template.render(context))

    def post(self):

        from advertise import AddAccount
        from mysms import SMSAccount
        from surveys import SurveyAccount
        from affiliates import Affiliate

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrBulkCredits = self.request.get('vstrBulkCredits')
            vstrBulkTransferCredits = self.request.get('vstrBulkTransferCredits')

            if vstrBulkTransferCredits == "Adverts":
                findRequest = Accounts.query(Accounts.uid == vstrUserID)
                thisAccountList = findRequest.fetch()

                if len(thisAccountList) > 0:
                    thisAccount = thisAccountList[0]
                    findRequest = AddAccount.query(AddAccount.organization_id == thisAccount.organization_id)
                    thisAdvertAccountList = findRequest.fetch()

                    if len(thisAdvertAccountList) > 0:
                        thisAdvertAccount = thisAdvertAccountList[0]

                        findRequest = SMSAccount.query(SMSAccount.organization_id == thisAccount.organization_id)
                        thisSMSAccountList = findRequest.fetch()

                        if len(thisSMSAccountList) > 0:
                            thisSMSAccount = thisSMSAccountList[0]
                            if (thisSMSAccount.total_sms >= int(vstrBulkCredits)) and (int(vstrBulkCredits) > 10):
                                thisSMSAccount.total_sms = thisSMSAccount.total_sms - int(vstrBulkCredits)
                                thisAdvertAccount.total_credits += int(vstrBulkCredits)
                                thisSMSAccount.put()
                                thisAdvertAccount.put()
                                self.response.write(
                                    "Successfully transferred " + vstrBulkCredits + " SMS Credits to your Advert Account")
                            else:
                                self.response.write(
                                    "Unable to transfer credits insufficient credit in your Bulk SMS Account")
                        else:
                            self.response.write("Fatal Error transferring Bulk SMS Credits")
                    else:
                        self.response.write(
                            "You do not have an Advertising Account please create an advertising account")
                else:
                    self.response.write("Cannot effect credit transfer as you do not have an account yet")

            elif vstrBulkTransferCredits == "Surveys":
                findRequest = Accounts.query(Accounts.uid == vstrUserID)
                thisAccountList = findRequest.fetch()

                if len(thisAccountList) > 0:
                    thisAccount = thisAccountList[0]
                    findRequest = SurveyAccount.query(SurveyAccount.organization_id == thisAccount.organization_id)
                    thisSurveyAccountList = findRequest.fetch()

                    if len(thisSurveyAccountList) > 0:
                        thisSurveyAccount = thisSurveyAccountList[0]
                        findRequest = SMSAccount.query(SMSAccount.organization_id == thisAccount.organization_id)
                        thisSMSAccountList = findRequest.fetch()

                        if len(thisSMSAccountList) > 0:
                            thisSMSAccount = thisSMSAccountList[0]
                            if (thisSMSAccount.total_sms >= int(vstrBulkCredits)) and (int(vstrBulkCredits) > 10):
                                thisSMSAccount.total_sms = thisSMSAccount.total_sms - int(vstrBulkCredits)
                                thisSurveyAccount.total_credits += int(vstrBulkCredits)
                                thisSMSAccount.put()
                                thisSurveyAccount.put()
                                self.response.write(
                                    "Successfully Transferred " + vstrBulkCredits + " Credits into your Survey Account")
                            else:
                                self.response.write(
                                    "Unable to transfer credits insufficient credit in your Bulk SMS Account")
                        else:
                            self.response.write("Fatal Error transferring Bulk SMS Credits")
                    else:
                        self.response.write("You do not have a survey Account please create an survey account")
                else:
                    self.response.write("Cannot effect credit transfer as you do not have an account yet")
        elif vstrChoice == "1":
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrAdvertsCredits = self.request.get("vstrAdvertsCredits")
            vstrAdvertsTransferCredits = self.request.get("vstrAdvertsTransferCredits")

            if vstrAdvertsTransferCredits == "BulkSMS":
                findRequest = Accounts.query(Accounts.uid == vstrUserID)
                thisAccountList = findRequest.fetch()

                if len(thisAccountList) > 0:
                    thisAccount = thisAccountList[0]
                    findRequest = AddAccount.query(AddAccount.organization_id == thisAccount.organization_id)
                    thisAdvertAccountList = findRequest.fetch()

                    if len(thisAdvertAccountList) > 0:
                        thisAdvertAccount = thisAdvertAccountList[0]
                        findRequest = SMSAccount.query(SMSAccount.organization_id == thisAccount.organization_id)
                        thisSMSAccountList = findRequest.fetch()
                        if len(thisSMSAccountList) > 0:
                            thisSMSAccount = thisSMSAccountList[0]

                            if ((thisAdvertAccount.total_credits >= int(vstrAdvertsCredits)) and (
                                    int(vstrAdvertsCredits) > 0)):
                                thisAdvertAccount.total_credits = thisAdvertAccount.total_credits - int(
                                    vstrAdvertsCredits)
                                thisSMSAccount.total_sms += int(vstrAdvertsCredits)
                                thisSMSAccount.put()
                                thisAdvertAccount.put()
                                self.response.write(
                                    "Successfully Transferred " + vstrAdvertsCredits + " Credits into your Bulk SMS Account")
                            else:
                                self.response.write(
                                    "Unable to transfer credits insufficient credit in your Advert Account")
                        else:
                            self.response.write("Fatal Error you do not have an active Bulk SMS Account")
                    else:
                        self.response.write("Fatal Error you do not have an Advert Account")
                else:
                    self.response.write("Cannot Effect credit transfer as you do not have an account yet")

            elif vstrAdvertsTransferCredits == "Surveys":

                findRequest = Accounts.query(Accounts.uid == vstrUserID)
                thisAccountList = findRequest.fetch()

                if len(thisAccountList) > 0:
                    thisAccount = thisAccountList[0]
                    findRequest = AddAccount.query(AddAccount.organization_id == thisAccount.organization_id)
                    thisAdvertAccountList = findRequest.fetch()

                    if len(thisAdvertAccountList) > 0:
                        thisAdvertAccount = thisAdvertAccountList[0]
                        findRequest = SurveyAccount.query(
                            SurveyAccount.organization_id == thisAccount.organization_id)
                        thisSurveyAccountList = findRequest.fetch()
                        if len(thisSurveyAccountList) > 0:
                            thisSurveyAccount = thisSurveyAccountList[0]

                            if ((thisAdvertAccount.total_credits >= int(vstrAdvertsCredits)) and (
                                    int(vstrAdvertsCredits) > 0)):
                                thisAdvertAccount.total_credits = thisAdvertAccount.total_credits - int(
                                    vstrAdvertsCredits)
                                thisSurveyAccount.total_credits += int(vstrAdvertsCredits)
                                thisAdvertAccount.put()
                                thisSurveyAccount.put()
                                self.response.write(
                                    "Successfully Transferred " + vstrAdvertsCredits + " Credits into your Survey Account")
                            else:
                                self.response.write(
                                    "Unable to transfer credits insufficient credit in your Advert Account")
                        else:
                            self.response.write("Fatal Error you do not have an active Survey Account")
                    else:
                        self.response.write("Fatal Error you do not have an Advert Account")
                else:
                    self.response.write("Cannot Effect credit transfer as you do not have an account yet")
        elif vstrChoice == "2":
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrSurveyCredits = self.request.get("vstrSurveyCredits")
            vstrSurveyTransferCredits = self.request.get("vstrSurveyTransferCredits")

            if vstrSurveyTransferCredits == "BulkSMS":
                findRequest = Accounts.query(Accounts.uid == vstrUserID)
                thisAccountList = findRequest.fetch()

                if len(thisAccountList) > 0:
                    thisAccount = thisAccountList[0]

                    findRequest = SurveyAccount.query(SurveyAccount.organization_id == thisAccount.organization_id)
                    thisSurveyAccountList = findRequest.fetch()

                    if len(thisSurveyAccountList) > 0:
                        thisSurveyAccount = thisSurveyAccountList[0]
                        findRequest = SMSAccount.query(SMSAccount.organization_id == thisAccount.organization_id)
                        thisSMSAccountList = findRequest.fetch()
                        if len(thisSMSAccountList) > 0:
                            thisSMSAccount = thisSMSAccountList[0]

                            if (thisSurveyAccount.total_credits >= int(vstrSurveyCredits)):
                                thisSurveyAccount.total_credits = thisSurveyAccount.total_credits - int(
                                    vstrSurveyCredits)
                                thisSMSAccount.total_sms += int(vstrSurveyCredits)
                                thisSMSAccount.put()
                                thisSurveyAccount.put()
                                self.response.write(
                                    "Successfully transferred " + vstrSurveyCredits + " Survey Credits to Bulk SMS Credits")
                            else:
                                self.response.write("Error Insufficient Credits to effect Transfer")
                        else:
                            self.response.write(
                                "Error Unable to effect Transfer you do not have a valid Bulk SMS Account")
                    else:
                        self.response.write("Error unable to effect transfer you do not have a valid Survey Account")
                else:
                    self.response.write("Error unable to effect transfer you do not have a valid System Account")

            elif vstrSurveyTransferCredits == "Adverts":
                findRequest = Accounts.query(Accounts.uid == vstrUserID)
                thisAccountList = findRequest.fetch()

                if len(thisAccountList) > 0:
                    thisAccount = thisAccountList[0]

                    findRequest = SurveyAccount.query(SurveyAccount.organization_id == thisAccount.organization_id)
                    thisSurveyAccountList = findRequest.fetch()

                    if len(thisSurveyAccountList) > 0:
                        thisSurveyAccount = thisSurveyAccountList[0]

                        findRequest = AddAccount.query(AddAccount.organization_id == thisAccount.organization_id)
                        thisAdvertAccountList = findRequest.fetch()

                        if len(thisAdvertAccountList) > 0:
                            thisAdvertAccount = thisAdvertAccountList[0]

                            if (thisSurveyAccount.total_credits >= int(vstrSurveyCredits)):
                                thisSurveyAccount.total_credits = thisSurveyAccount.total_credits - int(
                                    vstrSurveyCredits)
                                thisAdvertAccount.total_credits += int(vstrSurveyCredits)
                                thisSurveyAccount.put()
                                thisAdvertAccount.put()
                                self.response.write(
                                    "Successfully transferred " + vstrSurveyCredits + " Survey Credits into your Advertising Account")
                            else:
                                self.response.write("Error insufficient Credits to effect Transfer")
                        else:
                            self.response.write(
                                "Error unable to effect transfer you do not have a valid Advertising Account")
                    else:
                        self.response.write("Errror unable to effect transfer you do not have a valid Survey Account")
                else:
                    self.response.write("Error unable to effect transfer you do not have a valid System Account")
        elif vstrChoice == "3":
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrAffiliateCredits = self.request.get("vstrAffiliateCredits")
            vstrAffiliateTransferCredits = self.request.get("vstrAffiliateTransferCredits")

            if vstrAffiliateTransferCredits == "BulkSMS":

                findRequest = Accounts.query(Accounts.uid == vstrUserID)
                thisAccountList = findRequest.fetch()

                if len(thisAccountList) > 0:
                    thisAccount = thisAccountList[0]

                    findRequest = SMSAccount.query(SMSAccount.organization_id == thisAccount.organization_id)
                    thisSMSAccountList = findRequest.fetch()

                    if len(thisSMSAccountList) > 0:
                        thisSMSAccount = thisSMSAccountList[0]

                        findRequest = Affiliate.query(Affiliate.uid == vstrUserID)
                        thisAffiliateList = findRequest.fetch()
                        if len(thisAffiliateList) > 0:
                            thisAffiliate = thisAffiliateList[0]

                            if thisAffiliate.available_credit >= int(vstrAffiliateCredits):
                                thisAffiliate.available_credit = thisAffiliate.available_credit - int(
                                    vstrAffiliateCredits)
                                thisSMSAccount.total_sms += int(vstrAffiliateCredits)
                                thisAffiliate.put()
                                thisSMSAccount.put()
                                self.response.write(
                                    "Successfully transferred " + vstrAffiliateCredits + " Affiliate Credits into your Bulk SMS Account")
                            else:
                                self.response.write(
                                    "Error Transferring Credit insufficient Credit on your Affiliate Account")
                        else:
                            self.response.write("Error you do not have an active Affiliate Account")

                    else:
                        self.response.write("Error you do not have a valid Bulk SMS Account")
                else:
                    self.response.write("Error you do not have a valid System Account")

            elif vstrAffiliateTransferCredits == "Adverts":

                findRequest = Accounts.query(Accounts.uid == vstrUserID)
                thisAccountList = findRequest.fetch()

                if len(thisAccountList) > 0:
                    thisAccount = thisAccountList[0]

                    findRequest = AddAccount.query(AddAccount.organization_id == thisAccount.organization_id)
                    thisAdvertList = findRequest.fetch()
                    if len(thisAdvertList) > 0:
                        thisAdvert = thisAdvertList[0]

                        findRequest = Affiliate.query(Affiliate.uid == vstrUserID)
                        thisAffiliateList = findRequest.fetch()
                        if len(thisAffiliateList) > 0:
                            thisAffiliate = thisAffiliateList[0]

                            if thisAffiliate.available_credit >= int(vstrAffiliateCredits):
                                thisAffiliate.available_credit = thisAffiliate.available_credit - int(
                                    vstrAffiliateCredits)
                                thisAdvert.total_credits += int(vstrAffiliateCredits)
                                thisAffiliate.put()
                                thisAdvert.put()
                                self.response.write(
                                    "Successfully transferred " + vstrAffiliateCredits + " Affiliate Credits into your Advertising Account")
                            else:
                                self.response.write(
                                    "Error Transferring Credit insufficient Credit on your Affiliate Account")
                        else:
                            self.response.write("Error you do not have an active Affiliate Account")
                    else:
                        self.response.write("Error you do not have a valid Advertising Account")
                else:
                    self.response.write("Error you do not have a Valid System Account")

            elif vstrAffiliateTransferCredits == "Survey":
                findRequest = Accounts.query(Accounts.uid == vstrUserID)
                thisAccountList = findRequest.fetch()

                if len(thisAccountList) > 0:
                    thisAccount = thisAccountList[0]

                    findRequest = SurveyAccount.query(SurveyAccount.organization_id == thisAccount.organization_id)
                    thisSurveyList = findRequest.fetch()
                    if len(thisSurveyList) > 0:
                        thisSurvey = thisSurveyList[0]

                        findRequest = Affiliate.query(Affiliate.uid == vstrUserID)
                        thisAffiliateList = findRequest.fetch()
                        if len(thisAffiliateList) > 0:
                            thisAffiliate = thisAffiliateList[0]

                            if thisAffiliate.available_credit >= int(vstrAffiliateCredits):
                                thisAffiliate.available_credit = thisAffiliate.available_credit - int(
                                    vstrAffiliateCredits)
                                thisSurvey.total_credits += int(vstrAffiliateCredits)
                                thisAffiliate.put()
                                thisSurvey.put()
                                self.response.write(
                                    "Successfully transferred " + vstrAffiliateCredits + " Affiliate Credits into your survey Account")
                            else:
                                self.response.write(
                                    "Error Transferring Credit insufficient Credit on your Affiliate Account")
                        else:
                            self.response.write("Error you do not have an active Affiliate Account")
                    else:
                        self.response.write("Error you do not have a valid Survey Account")
                else:
                    self.response.write("Error you do not have a Valid System Account")


app = webapp2.WSGIApplication([
    ('/admin/org', OrganizaHandler),
    ('/admin/users', ManageUsersHandler),
    ('/org/reg/.*', ThisOrgAccountActivationHandler),
    ('/thisorg/.*', ThisOrgHandler),
    ('/admin/users/invites', UsersInvitesHandler),
    ('/org/advaccounts/.*', ThisAdvertAccountHandler),
    ('/accounts/api', AccountsAPIHandler),
    ('/accounts/credits', ManageCreditHandler)

], debug=True)

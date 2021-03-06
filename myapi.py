import os
from google.appengine.api import urlfetch
import webapp2
import jinja2
from google.appengine.ext import ndb
import logging
import datetime

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
strDefaultWhiteList = ["https://church-admins.appspot.com",
                       "https://sa-loans.appspot.com",
                       "https://ab-loan.appspot.com",
                       "https://pro-finance.appspot.com",
                       "https://midey-finance.appspot.com",
                       "https://client-trace.appspot.com",
                       "https://choosen-loan.appspot.com",
                       "https://manage-hotels.appspot.com",
                       "https://p2ptraders-app.appspot.com",
                       "https://rinde-cashloan.appspot.com",
                       "https://sa-sms.appspot.com",
                       "https://sa-fax.appspot.com",
                       "https://justice-ndou.appspot.com",
                       "https://freelancing-solutions.appspot.com",
                       "https://easy-hosting.appspot.com",
                       "https://cloud-job.appspot.com",]
class WhiteList(ndb.Expando):
    strURL = ndb.StringProperty()

    def writeURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strURL = strinput
                return True
            else:
                return False
        except:
            return False


class ErrorMessages(ndb.Expando):

    strLangCode = ndb.StringProperty()

    strOrganizationID = ndb.StringProperty() #TODO Allow organization to select Language, then use the translate API to translate all the interfaces and html documents

    strMessReportNotFound = ndb.StringProperty(default="Report not found")
    strMessAccountNotVerified = ndb.StringProperty(default="Account not verified")
    strMessAccountNotValid = ndb.StringProperty(default="Account not valid")
    strMessWebsiteNotAuthorized = ndb.StringProperty(default="Website not authorized for use with API")
    strMessAuthenticationError = ndb.StringProperty(default="Authentication error")
    strMessErrorSendingMessage = ndb.StringProperty(default="Error sending message")
    strMessInsufficientCredit = ndb.StringProperty(default="Insufficient credit")

class Const(ndb.Expando):
    strNoDataCode = ndb.StringProperty(default="X0001")
    strDataSplitter = ndb.StringProperty(default="-")
    strAPIGroupID = ndb.StringProperty(default="APIGROUP")

class PartnerSites(Const):
    """
        Return data format for contacts
        name-surname-cell-email
    """
    strSiteName = ndb.StringProperty(default="Church Admin")
    strServiceName = ndb.StringProperty(default="Contacts")
    strSiteID = ndb.StringProperty()
    strURL = ndb.StringProperty(default="https://church-admins.appspot.com")
    strAPIKey = ndb.StringProperty(default=os.environ.get('BIM_INTERNAL_API'))
    strAPISecret = ndb.StringProperty(default=os.environ.get('BIM_INTERNAL_SECRET'))

    def writeSiteID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSiteID = strinput
                return True
            else:
                return False

        except:
            return False
    def CreateSiteID(self):
        import random,string
        try:
            strSiteID = ""
            for i in range(256):
                strSiteID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strSiteID
        except:
            return None
    def writeURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strURL = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAPIKey(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAPIKey = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateAPIKey(self):
        import random,string
        try:
            strAPIKey = ""
            for i in range(512):
                strAPIKey += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strAPIKey
        except:
            return None
    def CreateAPISecret(self):
        import random,string
        try:
            strSecretCode = ""
            for i in range(512):
                strSecretCode += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strSecretCode
        except:
            return None
    def writeAPISecret(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAPISecret = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSiteName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSiteName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeServiceName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strServiceName = strinput
                return True
            else:
                return False
        except:
            return False

    def FetchMessage(self):
        """
            call the partner site through its API and fetch contact information
            if there comes a need to add more information on the contact another API and API call can be built
        :return:
        """
        pass

    def FetchContact(self,index):
        """
        Please implement a matching protocol on church admin

        :return:
        """
        try:
            form_data = "&api=" + self.strAPIKey + "&secret=" + self.strAPISecret + "&index=" + str(index)
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            url = self.strURL + "/epinternal/contacts-get" # The end point for internal contact get
            result = urlfetch.fetch(url=self.strURL,payload=form_data,method=urlfetch.POST,headers=headers,validate_certificate=True)
            if (result.status_code >= 200) and (result.status_code < 400):
                return result.content
            else:
                return self.strNoDataCode
        except urlfetch.Error:
            return self.strNoDataCode

    def FetchContactsJSONList(self):
        """

        :param index: total contacts to return
        :return:
        """
        try:
            form_data = "&api=" + self.strAPIKey + "&secret=" + self.strAPISecret
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            url = self.strURL + "/epinternal/contacts-get" # The end point for internal contact get
            result = urlfetch.fetch(url=self.strURL,payload=form_data,method=urlfetch.POST,headers=headers,validate_certificate=True)
            if (result.status_code >= 200) and (result.status_code < 400):
                return result.content
            else:
                return self.strNoDataCode
        except urlfetch.Error:
            return self.strNoDataCode


#TODO- Consider implementing PartnerSites on internal consumer services API


class EndPoints(Const):

    strOrganizationID = ndb.StringProperty() #Used only for external API that uses internal resources example message sending API
    strServiceName = ndb.StringProperty(default="Contacts")
    strPointID = ndb.StringProperty()
    strPointURL = ndb.StringProperty()
    #TODO- Organizations must be given their own contacts end point key and secret, and also their websites included
    #TODO- in the white list
    strAPIKey = ndb.StringProperty()
    strAPISecret = ndb.StringProperty()

    def writeOrganizationID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strOrganizationID = strinput
                return True
            else:
                return False
        except:
            return False

    def writePointID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPointID = strinput
                return True
            else:
                return False
        except:
            return False

    def writePointURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPointURL = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAPiKey(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAPIKey = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAPISecret(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAPISecret = strinput
                return True
            else:
                return False
        except:
            return False

    def CreatePointID(self):
        import random,string
        try:
            strPointID = ""
            for i in range(256):
                self.strPointID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strPointID
        except:
            return None

    def CreateAPIKey(self):
        import random,string
        try:
            strAPIKey = ""
            for i in range(256):
                strAPIKey += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strAPIKey
        except:
            return None

    def CreateAPISecret(self):
        import random,string
        try:
            strAPISecret = ""
            for i in range(256):
                strAPISecret += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strAPISecret
        except:
            return None

class RoutesHandler(webapp2.RequestHandler):

    def MyContactsHandler(self,strChoice):
        from advertise import OurContacts
        logging.info("Entering the contact handler")

        if strChoice == "0":
            findRequest = OurContacts.query()
            thisContactList = findRequest.fetch()
            strReturn = len(thisContactList)
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write(str(strReturn))
        elif strChoice == "1":
            logging.info("Path executing ok")
            findRequest = OurContacts.query()
            thisContactList = findRequest.fetch()
            strLimit = len(thisContactList)
            strLimit = strLimit - 1
            self.response.headers['Content-Type'] = 'application/json'
            template = template_env.get_template('templates/api/contactresults.json')
            context = {'thisContactList': thisContactList,'strLimit':strLimit}
            self.response.write(template.render(context))

    def AddContactsHandler(self,strNames,strSurname,strCell,strEmail):
        from advertise import OurContacts
        findRequest = OurContacts.query(OurContacts.strCell == strCell)
        thisContactsList = findRequest.fetch()

        if len(thisContactsList) == 0:
            thisContact = OurContacts()
            thisContact.writeOurContactID(strinput=thisContact.CreateContactID())
            thisContact.writeNames(strinput=strNames)
            thisContact.writeSurname(strinput=strSurname)
            thisContact.writeCell(strinput=strCell)
            thisContact.writeEmail(strinput=strEmail)
            thisContact.put()
            self.response.headers["Content-Type"] = "text/plain"
            self.response.status_code = 200
            self.response.write("Contact Added Successfully")
        else:
            self.response.headers["Content-Type"] = "text/plain"
            self.response.status_code = 409
            self.response.write("Error Contact Already Added")
    def ContactExistHandler(self,strCell):
        from advertise import OurContacts
        findRequest = OurContacts.query(OurContacts.strCell == strCell)
        thisContactList = findRequest.fetch()

        if len(thisContactList) > 0:
            thisContact = thisContactList[0]

            template = template_env.get_template("templates/api/contact.json")
            context = {'thisContact': thisContact}
            self.response.headers["Content-Type"] = "application/json"
            self.response.write(template.render(context))
        else:
            self.response.headers["Content-Type"] = "text/plain"
            self.response.status_code = 404
            self.response.write("Contact Not Found")
    def SendMessageHandler(self,strMessage,strCell,strOrganizationID,thisEndPoint):
        from mysms import SMSAccount,SMSPortalBudget,Messages,DeliveryReport,SMSContacts,Groups

        findRequest = SMSAccount.query(SMSAccount.strOrganizationID == strOrganizationID)
        thisSMSAccountList = findRequest.fetch()
        thisMessage = Messages()

        if len(thisSMSAccountList) > 0:
            thisSMSAccount = thisSMSAccountList[0]

            if thisSMSAccount.strTotalSMS > 0:
                findRequest = SMSPortalBudget.query()
                thisPortalList = findRequest.fetch()
                if len(thisPortalList) > 0:
                    thisPortal = thisPortalList[0]

                    #TODO- Once sending messages using our own reference is perfected replace this with our internal reference

                    ref = thisPortal.SendCronMessage(strMessage=strMessage, strCell=strCell)
                    if not (ref == None):
                        vstrThisDate = datetime.datetime.now()
                        strThisDate = vstrThisDate.date()
                        strThisTime = datetime.time(hour=vstrThisDate.hour, minute=vstrThisDate.minute,
                                                    second=vstrThisDate.second)

                        thisSMSAccount.writeTotalSMS(strinput=(thisSMSAccount.strTotalSMS - 1))
                        thisSMSAccount.put()


                        thisMessage.writeGroupID(strinput=thisEndPoint.strAPIGroupID)
                        thisMessage.writeMessageID(strinput=thisMessage.CreateMessageID())
                        thisMessage.writeMessage(strinput=strMessage)
                        thisMessage.writeDateCreated(strinput=strThisDate)
                        thisMessage.writeTimeCreated(strinput=strThisTime)
                        thisMessage.writeDateSubmitted(strinput=strThisDate)
                        thisMessage.writeTimeSubmitted(strinput=strThisTime)
                        thisMessage.writeSubmitted(strinput=True)
                        thisMessage.put()

                        ThisDeliveryReport = DeliveryReport()
                        ThisDeliveryReport.writeMessageID(strinput=thisMessage.strMessageID)
                        ThisDeliveryReport.writeOrganizationID(strinput=thisEndPoint.strOrganizationID)
                        ThisDeliveryReport.writeDelivered(strinput=True)
                        ThisDeliveryReport.writeCell(strinput=strCell)
                        ThisDeliveryReport.writeGroupID(strinput=thisEndPoint.strAPIGroupID)
                        ThisDeliveryReport.writeDate(strinput=strThisDate)
                        ThisDeliveryReport.writeTime(strinput=strThisTime)
                        ThisDeliveryReport.writeReference(strinput=ref)
                        ThisDeliveryReport.put()

                        findRequest = SMSContacts.query(SMSContacts.strGroupID == thisEndPoint.strAPIGroupID,
                                                        SMSContacts.strCellNumber == strCell)
                        thisSMSContactList = findRequest.fetch()

                        AddContact = False
                        if len(thisSMSContactList) > 0:
                            pass
                        else:
                            thisContact = SMSContacts()
                            thisContact.writeUserID(strinput=thisEndPoint.strAPI)
                            thisContact.writeCellNumber(strinput=strCell)
                            thisContact.writeGroupID(strinput=thisEndPoint.strAPIGroupID)
                            thisContact.writeNames(strinput="API")
                            thisContact.writeSurname(strinput="API")
                            thisContact.put()
                            AddContact = True

                        findRequest = Groups.query(Groups.strOrganizationID == thisEndPoint.strOrganizationID,
                                                   Groups.strGroupID == thisEndPoint.strAPIGroupID)
                        thisGroupList = findRequest.fetch()

                        if len(thisGroupList) > 0:
                            thisGroup = thisGroupList[0]
                        else:
                            thisGroup = Groups()

                            thisGroup.writeGroupID(strinput=EndPoints.strAPIGroupID)
                            thisGroup.writeOrganizationID(strinput=thisEndPoint.strOrganizationID)
                            thisGroup.writeUserID(strinput=thisEndPoint.strAPI)  # THE API Key User means the Group is owned by the API Key
                            thisGroup.writeGroupDescription(strinput="API Group for messages sent through the API")
                            thisGroup.writeGroupName(strinput="API")
                        if AddContact:
                            thisGroup.writeTotalNumbers(strinput=str(thisGroup.strTotalNumbers + 1))
                            thisGroup.put()
                    form_data = "&ref=" + ref
                    self.response.write(form_data)
                else:
                    self.response.headers["Content-Type"] = "text/plain"
                    self.response.status_code = 401
                    self.response.write("Error You do not have a valid account")
            else:
                self.response.headers["Content-Type"] = "text/plain"
                self.response.status_code = 401
                self.response.write("Error insufficient credit")
        else:
            self.response.headers["Content-Type"] = "text/plain"
            self.response.status_code = 401
            self.response.write("Error you do not have a valid account")
    def MessageResponseHandler(self,strRef,strCell):
        from mysms import DeliveryReport

        findRequest = DeliveryReport.query(DeliveryReport.strRef == strRef, DeliveryReport.strCell == strCell)
        thisDeliveryReportList = findRequest.fetch()
        if len(thisDeliveryReportList) > 0:
            thisReport = thisDeliveryReportList[0]

            strResponse = thisReport.strResponse
            strRef = thisReport.strRef
            strCell = thisReport.strCell
            self.response.headers["Content-Type"] = "application/json"
            self.response.status_code = 200
            template = template_env.get_template('templates/api/message-response.json')
            context = {'strResponse':strResponse,'strRef':strRef,'strCell':strCell}
            self.response.write(template.render(context))
        else:
            self.response.headers["Content-Type"] = "text/plain"
            self.response.status_code = 401
            self.response.write("Response not found")
    def MessageStatusHandler(self,strRef,strCell):
        from mysms import DeliveryReport
        findRequest = DeliveryReport.query(DeliveryReport.strRef == strRef, DeliveryReport.strCell == strCell)
        thisDeliveryReportList = findRequest.fetch()
        if len(thisDeliveryReportList) > 0:
            thisReport = thisDeliveryReportList[0]
            strStatus = thisReport.strSendingStatus
            strRef = thisReport.strRef
            strCell = thisReport.strCell

            self.response.headers["Content-Type"] = "application/json"
            self.response.status_code = 200
            template = template_env.get_template('templates/api/message-status.json')
            context = {'strStatus':strStatus,'strRef':strRef,'strCell':strCell}
            self.response.write(template.render(context))

        else:
            self.response.headers["Content-Type"] = "text/plain"
            self.response.status_code = 401
            self.response.write("Error Status not found")
    def CreditsHandler(self,strOrganizationID):
        from mysms import SMSAccount
        from advertise import AddAccount
        from surveys import SurveyAccount
        from affiliates import Affiliate

        findRequest = SMSAccount.query(SMSAccount.strOrganizationID == strOrganizationID)
        thisSMSAccountList = findRequest.fetch()
        if len(thisSMSAccountList) > 0:
            thisSMSAccount = thisSMSAccountList[0]
        else:
            thisSMSAccount = SMSAccount()

        findRequest = AddAccount.query(AddAccount.strOrganizationID == strOrganizationID)
        thisAdvertisingAccountList = findRequest.fetch()
        if len(thisAdvertisingAccountList) > 0:
            thisAdvertisingAccount = thisAdvertisingAccountList[0]
        else:
            thisAdvertisingAccount = AddAccount()

        findRequest = SurveyAccount.query(SurveyAccount.strOrganizationID == strOrganizationID)
        thisSurveyAccountList = findRequest.fetch()
        if len(thisSurveyAccountList) > 0:
            thisSurveyAccount = thisSurveyAccountList[0]
        else:
            thisSurveyAccount = SurveyAccount()

        findRequest = Affiliate.query(Affiliate.strOrganizationID == strOrganizationID)
        thisAffiliateList = findRequest.fetch()
        if len(thisAffiliateList) > 0:
            thisAffiliate = thisAffiliateList[0]
        else:
            thisAffiliate = Affiliate()

        try:
            if thisSMSAccount:
                strBulkSMSCredit = thisSMSAccount.strTotalSMS
            else:
                strBulkSMSCredit = 0
        except:
            strBulkSMSCredit = 0

        try:
            if thisAdvertisingAccount:
                strAdvertisingCredit = thisAdvertisingAccount.strTotalCredits
            else:
                strAdvertisingCredit = 0
        except:
            strAdvertisingCredit = 0

        try:
            if thisSurveyAccount:
                strSurveyCredit = thisSurveyAccount.strTotalCredits
            else:
                strSurveyCredit = 0
        except:
            strSurveyCredit = 0

        try:
            if thisAffiliate:
                strAffiliateCredit = thisAffiliate.strAvailableCredit
            else:
                strAffiliateCredit = 0
        except:
            strAffiliateCredit = 0

        self.response.headers['Content-Type'] = "application/json"
        self.response.status_code = 200
        template = template_env.get_template('templates/api/credits.json')
        context = {'strBulkSMSCredit': strBulkSMSCredit, 'strAdvertisingCredit': strAdvertisingCredit,
                   'strSurveyCredit': strSurveyCredit, 'strAffiliateCredit': strAffiliateCredit}
        self.response.write(template.render(context))
    def SetAdvertHandler(self,strAdvert,strStartDate,strStartTime,strCreditLimit,thisEndPoint):
        """
                            strAdvert = self.request.get('advert')
                            strLimit = self.request.get('limit')
                            strStart = self.request.get('startdate')
                            strTime = self.request.get('starttime')

        :return:
        """
        from advertise import AddAccount,Advert

        findRequest = AddAccount.query(AddAccount.strOrganizationID == thisEndPoint.strOrganizationID)
        thisAdvertAccountList = findRequest.fetch()

        if len(thisAdvertAccountList) > 0:
            thisAdvertAccount = thisAdvertAccountList[0]

            if thisAdvertAccount.strTotalCredits <= int(strCreditLimit):
                thisAdvert = Advert()
                thisAdvert.writeUserID(strinput=thisEndPoint.strAPIKey)
                thisAdvert.writeOrganizationID(strinput=thisEndPoint.strOrganizationID)
                thisAdvert.writeAdvert(strinput=strAdvert)
                thisAdvert.writeAdvertID(strinput=thisAdvert.CreateAdvertID())
                thisAdvert.writeAdvertIsPaid(strinput=True)
                thisAdvert.writeAssignedCredit(strinput=strCreditLimit)
                #strAdvertSize = len(strAdvert)
                #strAdvertSize = strAdvertSize/150 #TODO- find out how to round to the next value
                #thisAdvert.writeAdvertSize(strinput=strAdvertSize)
                thisAdvert.writeRunFromCredit(strinput=True)

                thisAdvert.writeStartTime(strinput=strStartTime)
                thisAdvert.writeStartDate(strinput=strStartDate)

                vstrThisDateTime = datetime.datetime.now()
                strThisDate = datetime.date(year=vstrThisDateTime.year,month=vstrThisDateTime.month,day=vstrThisDateTime.day)
                strThisTime = datetime.time(hour=vstrThisDateTime.hour,minute=vstrThisDateTime.minute,second=vstrThisDateTime.second)
                thisAdvert.writeDateCreated(strinput=strThisDate)
                thisAdvert.writeTimeCreated(strinput=strThisTime)


                self.response.headers['Content-Type'] = "application/json"
                self.response.status_code = 200
                template = template_env.get_template('templates/api/setadvert.json')
                context = {'strRef':thisAdvert.strAdvertID,'strCredit':thisAdvert.strAssignedCredit}
                self.response.write(template.render(context))
            else:
                self.response.headers["Content-Type"] = "text/plain"
                self.response.status_code = 401
                self.response.write("Error Insufficient Credit")
        else:
            self.response.headers["Content-Type"] = "text/plain"
            self.response.status_code = 401
            self.response.write("Error Account not found")
    def AdvertStatsHandler(self,strRef):
        """
            Advert Statistics
        :return:
        """
        from advertise import Stats

        findRequest = Stats.query(Stats.strAdvertID == strRef)
        thisStatsList = findRequest.fetch()

        #TODO- Statistics must be updated every time responses are received

        if len(thisStatsList) > 0:

            strLimit = len(thisStatsList)
            strLimit = strLimit - 1

            template = template_env.get_template('templates/api/advert-stats.json')
            context = {'thisStatsList':thisStatsList,'strLimit':strLimit}
            self.response.write(template.render(context))
        else:
            self.response.headers["Content-Type"] = "text/plain"
            self.response.status_code = 401
            self.response.write("Stats not found")
    def AdvertResponsesHandler(self,strRef):
        """
            Advert Responses
        :param strRef:
        :return:

        """
        from advertise import Responses

        findRequest = Responses.query(Responses.strAdvertID == strRef)
        thisResponsesList = findRequest.fetch()

        if len(thisResponsesList) > 0:

            strLimit = len(thisResponsesList)
            strLimit = strLimit -1

            self.response.headers['Content-Type'] = "application/json"
            self.response.status_code = 200
            template = template_env.get_template('templates/api/advert-responses.json')
            context = {'thisResponsesList':thisResponsesList,'strLimit':strLimit}
            self.response.write(template.render(context))
        else:
            self.response.headers['Content-Type'] = "text/plain"
            self.response.status_code = 401
            self.response.write("Responses not available")
    def AdvertAccountCredit(self,strOrganizationID):

        from advertise import AddAccount
        findRequest = AddAccount.query(AddAccount.strOrganizationID == strOrganizationID)
        thisAdvertiseAccountList = findRequest.fetch()

        if len(thisAdvertiseAccountList) > 0:
            thisAdvertAccount = thisAdvertiseAccountList[0]
        else:
            thisAdvertAccount = AddAccount()

        self.response.headers['Content-Type'] = "application/json"
        template = template_env.get_template('templates/api/credit.json')
        context = {'strTotalCredits': thisAdvertAccount.strTotalCredits}
        self.response.write(template.render(context))
    def BuildSurveyHandler(self,strQuestion,strAnswers,strOrganizationID,strSurveyID=None,strName=None,strDescription=None):
        """
        Call initially to set up a survey
        call consecutively with the survey id to add questions and answers
        :param strQuestion:
        :param strAnswers:
        :return:
        """
        from surveys import Surveys,MultiChoiceSurveys

        if strSurveyID != None:

            thisSurveyQuestions = MultiChoiceSurveys()
            thisSurveyQuestions.writeSurveyID(strinput=strSurveyID)
            thisSurveyQuestions.writeQuestionID(strinput=thisSurveyQuestions.CreateQuestionID())
            thisSurveyQuestions.writeQuestion(strinput=strQuestion)
            strAnswersList = strAnswers.split("|")
            if len(strAnswersList) == 4:
                thisSurveyQuestions.writeChoiceOne(strinput=strAnswersList[0])
                thisSurveyQuestions.writeChoiceTwo(strinput=strAnswersList[1])
                thisSurveyQuestions.writeChoiceThree(strinput=strAnswersList[2])
                thisSurveyQuestions.writeChoiceFour(strinput=strAnswersList[3])
                thisSurveyQuestions.put()
                template = template_env.get_template('templates/api/build-survey-question.json')
                context = {"thisSurveyQuestions": thisSurveyQuestions}
                self.response.headers['Content-Type'] = "application/json"
                self.response.status_code = 200
                self.response.write(template.render(context))
            else:
                self.response.headers['Content-Type'] = "text/html"
                self.response.status_code = 401
                self.response.write("""
                
                Error please provide 4 Answers in this format <br>
                XXXXXX = answer<br>
                
                XXXXX|XXXXX|XXXXX|XXXXX
                
                """)

        else:
            thisSurvey = Surveys()
            thisSurvey.writeOrganizationID(strinput=strOrganizationID)
            thisSurvey.writeSurveyID(strinput=strSurveyID)
            if strName != None:
                thisSurvey.writeSurveyName(strinput=strName)
            if strDescription != None:
                thisSurvey.writeSurveyDescription(strinput=strDescription)
            thisSurvey.writeSurveyType(strinput="multichoice")

            vstrDateTime = datetime.datetime.now()
            strThisDate =datetime.date(year=vstrDateTime.year,month=vstrDateTime.month,day=vstrDateTime.day)
            strThisTime = datetime.time(hour=vstrDateTime.hour,minute=vstrDateTime.minute,second=vstrDateTime.second)


            thisSurvey.writeDateCreated(strinput=strThisDate)
            thisSurvey.writeTimeCreated(strinput=strThisTime)
            thisSurvey.writeSurveyStatus(strinput="Building")
            thisSurvey.writeSurveyID(strinput=thisSurvey.CreateSurveyID())
            thisSurvey.put()
            template = template_env.get_template('templates/api/build-survey-init.json')
            context = {"thisSurvey":thisSurvey}
            self.response.headers['Content-Type'] = "application/json"
            self.response.status_code = 200
            self.response.write(template.render(context))
    def SetSurveyHandler(self,strSurveyID,strStartDate,strStartTime,strCreditLimit,strOrganizationID):
        """
        :param strSurveyID:

        call to setup the time and date that the survey must start executing

        :param strStartDate:
        :param strStartTime:
        :param strCreditLimit:
        :return:
        """
        from surveys import Surveys,SurveyAccount

        try:
            strStartDateList = strStartDate.split("-")
            strStartYear = strStartDateList[0]
            strStartMonth = strStartDateList[1]
            strStartDay = strStartDateList[2]
            strStartDate = datetime.date(year=int(strStartYear),month=int(strStartMonth),day=int(strStartDay))
        except:
            strStartDate = datetime.datetime.now()
            strStartDate = strStartDate.date()

        try:
            strStartTimeList = strStartTime.split(":")
            strStartHour = strStartTimeList[0]
            strStartMinute = strStartTimeList[1]
            strStartTime = datetime.time(hour=int(strStartHour),minute=int(strStartMinute),second=0)
        except:
            strStartTime = datetime.datetime.now()
            strStartTime = strStartTime.time()

        findRequest = Surveys.query(Surveys.strSurveyID == strSurveyID)
        thisSurveyList = findRequest.fetch()



        if len(thisSurveyList) > 0:
            thisSurvey = thisSurveyList[0]

            thisSurvey.writeStartDate(strinput=strStartDate)
            thisSurvey.writeStartTime(strinput=strStartTime)
            if int(strCreditLimit) > 0:
                findRequest = SurveyAccount.query(SurveyAccount.strOrganizationID == strOrganizationID)
                thisSurveyAccountList = findRequest.fetch()

                if len(thisSurveyAccountList) > 0:
                    thisSurveyAccount =  thisSurveyAccountList[0]

                    if thisSurveyAccount.strTotalCredits > int(strCreditLimit):
                        thisSurveyAccount.strTotalCredits = thisSurveyAccount.strTotalCredits - int(strCreditLimit)
                        thisSurveyAccount.put()
                        thisSurvey.writeRunFromCredit(strinput=True)
                        thisSurvey.writeSurveyIsPaid(strinput=True)
                        thisSurvey.strAssignedCredit += int(strCreditLimit)
                        thisSurvey.writeSurveyStatus(strinput="Scheduled")
                        thisSurvey.put()
                        #Build survey init also works for returning survey status
                        template = template_env.get_template('templates/api/build-survey-init.json')
                        context = {"thisSurvey": thisSurvey}
                        self.response.headers['Content-Type'] = "application/json"
                        self.response.status_code = 200
                        self.response.write(template.render(context))

                    else:
                        self.response.headers['Content-Type'] = "text/plain"
                        self.response.status_code = 401
                        self.response.write("Error insufficient credit")
                else:
                    self.response.headers['Content-Type'] = "text/plain"
                    self.response.status_code = 401
                    self.response.write("Error survey not found")
            else:
                self.response.headers['Content-Type'] = "text/plain"
                self.response.status_code = 401
                self.response.write("Error Invalid credit assignment")
        else:
            self.response.headers['Content-Type'] = "text/plain"
            self.response.status_code = 401
            self.response.write("Error Survey does not exist please check your Survey ID")
    def SurveyStatus(self,strSurveyID):
        """
            using survey reference number return status
        :param strRef:
        :return:
        """
        from surveys import Surveys

        findRequest = Surveys.query(Surveys.strSurveyID == strSurveyID)
        thisSurveysList = findRequest.fetch()

        if len(thisSurveysList) > 0:
            thisSurvey = thisSurveysList[0]

            template = template_env.get_template('templates/api/build-survey-init.json')
            context = {"thisSurvey": thisSurvey}
            self.response.headers['Content-Type'] = "application/json"
            self.response.status_code = 200
            self.response.write(template.render(context))
        else:
            self.response.headers['Content-Type'] = "text/plain"
            self.response.status_code = 401
            self.response.write("Error survey not found")
    def SurveyResponses(self,strSurveyID):
        """
            return survey responses
        :param strRef:
        :return:
        """
        from surveys import MultiChoiceSurveyAnswers

        findRequest = MultiChoiceSurveyAnswers.query(MultiChoiceSurveyAnswers.strSurveyID == strSurveyID)
        thisSurveyAnswersList = findRequest.fetch()
        strLimit = len(thisSurveyAnswersList) - 1

        template = template_env.get_template('templates/api/surveys-answers.json')
        context = {'thisSurveyAnswersList':thisSurveyAnswersList,'strLimit':strLimit}
        self.response.headers['Content-Type'] = "application/json"
        self.response.status_code = 200
        self.response.write(template.render(context))
    def SurveyCredit(self,strOrganizationID):
        from surveys import SurveyAccount
        findRequest = SurveyAccount.query(SurveyAccount.strOrganizationID == strOrganizationID)
        thisSurveyAccountList = findRequest.fetch()

        if len(thisSurveyAccountList) > 0:
            thisSurveyAccount = thisSurveyAccountList[0]
        else:
            thisSurveyAccount = SurveyAccount()

        self.response.headers['Content-Type'] = "application/json"
        template = template_env.get_template('templates/api/credit.json')
        context = {'strTotalCredits': thisSurveyAccount.strTotalCredits}
        self.response.write(template.render(context))
    def SendFax(self,strFaxMediaURL,strFaxNumber,thisEndPoint):
        from myfax import FaxAccount,FaxSettings,SentFax
        from mysms import ClickSendSMSPortal
        from myTwilio import MyTwilioPortal

        findRequest = FaxAccount.query(FaxAccount.strOrganizationID == thisEndPoint.strOrganizationID)
        thisFaxAccountList = findRequest.fetch()

        if len(thisFaxAccountList) > 0:
            thisFaxAccount = thisFaxAccountList[0]

            if thisFaxAccount.strCreditInPages > 0:
                #TODO- Check which portal to use if clicksend download the file and send if Twilio send as is

                if thisFaxAccount.strUsePortal == "ClickSend":

                    thisPortal = ClickSendSMSPortal()
                    strFaxFileName = "" #TODO find a way to download the file from the link  provided
                    thisPortal.sendFax(strFaxNumber=strFaxNumber,strFaxFileName=strFaxFileName)
                    #TODO- generate a reference number to go with the fax, this will allow status messages
                    #TODO- Save the fax reference number on the sent faxes class and then a response back to the client app

                elif thisFaxAccount.strUsePortal == "Twilio":
                    thisPortal = MyTwilioPortal()
                    findRequest = FaxSettings.query(FaxSettings.strOrganizationID == thisEndPoint.strOrganizationID)
                    thisFaxSettingsList = findRequest.fetch()

                    if len(thisFaxSettingsList) > 0:
                        thisFaxSettings = thisFaxSettingsList[0]
                        strRef = thisPortal.sendFax(strFrom=thisFaxSettings.strFaxNumber,strTo=strFaxNumber,strFaxURL=strFaxMediaURL)

                        #TODO- Consider also donwloading the fax file here once obtained send as fax, obtain the filename below
                        strFileName = ""
                        vstrThisDateTime = datetime.datetime.now()
                        strThisDate = datetime.date(year=vstrThisDateTime.year,month=vstrThisDateTime.month,day=vstrThisDateTime.day)
                        strThisTime = datetime.time(hour=vstrThisDateTime.hour,minute=vstrThisDateTime.minute,second=vstrThisDateTime.second)

                        thisSentFax = SentFax()
                        thisSentFax.writeOrganizationID(strinput=thisEndPoint.strOrganizationID)
                        thisSentFax.writeUserID(strinput=thisEndPoint.strAPIKey)
                        thisSentFax.writeFaxNumber(strinput=strFaxNumber)
                        thisSentFax.writeDateSent(strinput=strThisDate)
                        thisSentFax.writeTimeSent(strinput=strThisTime)
                        thisSentFax.writeDateCreated(strinput=strThisDate)
                        thisSentFax.writeTimeCreated(strinput=strThisTime)
                        thisSentFax.writeFaxFilename(strinput=strFileName)
                        thisSentFax.writeFaxReference(strinput=strRef)
                        thisSentFax.writeStatus(strinput="Sent")
                        thisSentFax.put()

                        self.response.headers['Content-Type'] = "application/json"
                        template = template_env.get_template('templates/api/sendfax.json')
                        context = {'strRef': strRef}
                        self.response.write(template.render(context))
    def FaxStatus(self,strRef):
        pass

    def ReceiveFax(self,strFaxEmail):
        pass

    def FaxCredit(self,strOrganizationID):
        from myfax import FaxAccount
        findRequest = FaxAccount.query(FaxAccount.strOrganizationID == strOrganizationID)
        thisFaxAccountList = findRequest.fetch()

        if len(thisFaxAccountList) > 0:
            thisFaxAccount = thisFaxAccountList[0]
        else:
            thisFaxAccount = FaxAccount()

        self.response.headers['Content-Type'] = "application/json"
        template = template_env.get_template('templates/api/credit.json')
        context = {'strTotalCredits': thisFaxAccount.strCreditInPages}
        self.response.write(template.render(context))

    def get(self):
        """
            definitions of all my endpoints
        :return:
        """
        self.response.headers['Content-Type'] = "application/json"
        template = template_env.get_template('templates/api/endpoint/endpoints.json')
        context = {}
        self.response.write(template.render(context))

    def post(self):
        """
                '/endpoints/contacts-get'
                '/endpoints/contact-add'
                '/endpoints/contact-exist'
                '/endpoints/message-send'
                '/endpoints/message-response
                '/endpoints/message-status'
                '/endpoints/credits'
                '/endpoints/advert-set'
                '/endpoints/advert-stats'
                '/endpoints/advert-responses'
                '/endpoints/advert-credit'
                '/endpoints/survey-set'
                '/endpoints/survey-status'
                '/endpoints/survey-responses'
                '/endpoints/survey-credit'
                '/endpoints/fax-send'
                '/endpoints/fax-status'
                '/endpoints/fax-receive'
                '/endpoints/fax-credit'

                Make sure that the calling ip address or website address is passed correctly
                second fect the api and secret
                third check the called url and
                last obtain the extra variables
                last call the correct function and execute
                :return:
        """
        from accounts import Organization
        URL = self.request.url
        strURLlist = URL.split("/")
        strFunction = strURLlist[4]
        #TODO-turn all Handlers into local functions
        logging.info("this is the function : " + strFunction)

        strAPI = self.request.get('api')
        strSecret = self.request.get('secret')
        try:
            if os.environ["REMOTE_ADDR"] != None:
                strOriginURL = os.environ["REMOTE_ADDR"]
            else:
                strOriginURL = self.request.remote_addr
        except:
            strOriginURL = self.request.remote_addr

        #TODO- find out how self.request.remote_addr is different from self.request.host_url
        logging.info(strOriginURL)

        findRequest = EndPoints.query(EndPoints.strAPIKey == strAPI, EndPoints.strAPISecret == strSecret)
        thisEndPointList = findRequest.fetch()

        if len(thisEndPointList) > 0:
            thisEndPoint = thisEndPointList[0]
            logging.info("We got my END point ")

            strMyPointURL = str(thisEndPoint.strPointURL)
            strOriginURL = str(strOriginURL)

            if strMyPointURL.startswith(strOriginURL):
                logging.info("We got my point url is equal to endpoint")

                findRequest = Organization.query(Organization.strOrganizationID == thisEndPoint.strOrganizationID)
                thisOrgList = findRequest.fetch()

                if len(thisOrgList) > 0:
                    thisOrg = thisOrgList[0]

                    if thisOrg.strVerified:
                        logging.info("Organization is verified")

                        if strFunction == "contacts-get":
                            strChoice = self.request.get('choice')
                            self.MyContactsHandler(strChoice=strChoice)
                        elif strFunction == "contact-add":
                            strCell = self.request.get('cell')
                            strEmail = self.request.get('email')
                            strNames = self.request.get('names')
                            strSurname = self.request.get('surname')
                            #AddContactsHandler(self, strNames, strSurname, strCell, strEmail):
                            self.AddContactsHandler(strNames=strNames,strSurname=strSurname,strCell=strCell,strEmail=strEmail)

                        elif strFunction == "contact-exist":

                            strCell = self.request.get('cell')
                            self.ContactExistHandler(strCell=strCell)

                        elif strFunction == "message-send":
                            strCell = self.request.get('cell')
                            strMessage = self.request.get('message')
                            # SendMessage(self, strMessage, strCell, strOrganizationID, thisEndPoint):
                            self.SendMessageHandler(strMessage=strMessage,strCell=strCell,strOrganizationID=thisOrg.strOrganizationID,thisEndPoint=thisEndPoint)

                        elif strFunction == "message-response":
                            strCell = self.request.get('cell')
                            strRef = self.request.get('ref')

                            self.MessageResponseHandler(strCell=strCell,strRef=strRef)

                        elif strFunction == "message-status":
                            strCell = self.request.get('cell')
                            strRef = self.request.get('ref')
                            self.MessageStatusHandler(strRef=strRef,strCell=strCell)

                        elif strFunction == "credits":
                            self.CreditsHandler(strOrganizationID=thisEndPoint.strOrganizationID)

                        elif strFunction == "advert-set":
                            strAdvert = self.request.get('advert')
                            strCreditLimit = self.request.get('credit-limit')
                            strStartDate = self.request.get('start-date')
                            vstrStartDateList = strStartDate.split("-")
                            strStartYear = vstrStartDateList[0]
                            strStartMonth = vstrStartDateList[1]
                            strStartDay = vstrStartDateList[2]
                            strStartDate = datetime.date(year=int(strStartYear),month=int(strStartMonth),day=int(strStartDay))


                            strStartTime = self.request.get('start-time')
                            vstrStartTimeList = strStartTime.split(":")
                            strStartHour = vstrStartTimeList[0]
                            strStartMinute = vstrStartTimeList[1]
                            strStartTime = datetime.time(hour=int(strStartHour),minute=int(strStartMinute),second=0)


                            self.SetAdvertHandler(strAdvert=strAdvert,strStartDate=strStartDate,strStartTime=strStartTime,strCreditLimit=strCreditLimit,thisEndPoint=thisEndPoint)


                        elif strFunction == "advert-stats":
                            strRef = self.request.get('ref')
                            self.AdvertStatsHandler(strRef=strRef)

                        elif strFunction == "advert-responses":
                            strRef = self.request.get('ref')
                            self.AdvertResponsesHandler(strRef=strRef)

                        elif strFunction == "advert-credit":
                            self.AdvertAccountCredit(strOrganizationID=thisEndPoint.strOrganizationID)

                        elif strFunction == "survey-build":
                            strQuestion = self.request.get('survey-question')
                            strAnswers = self.request.get('answers-list')
                            strOrganizationID = self.request.get('org-id')
                            strSurveyID = self.request.get('survey-id')
                            strName = self.request.get('survey-name')
                            strDescription = self.request.get('survey-description')
                            self.BuildSurveyHandler(strQuestion=strQuestion,strAnswers=strAnswers,strOrganizationID=strOrganizationID,strSurveyID=strSurveyID,strName=strName,strDescription=strDescription)

                        elif strFunction == "survey-set":
                            #def SetSurveyHandler(self, strSurvey, strStartDate, strStartTime, strCreditLimit):
                            strOrganizationID = self.request.get('org-id')
                            strSurveyID = self.request.get('survey-id')
                            strStartDate = self.request.get('start-date')
                            strStartTime = self.request.get('start-time')
                            strCreditLimit = self.request.get('credit-limit')
                            self.SetSurveyHandler(strSurveyID=strSurveyID,strStartDate=strStartDate,strStartTime=strStartTime,strCreditLimit=strCreditLimit,strOrganizationID=strOrganizationID)

                        elif strFunction == "survey-status":
                            strSurveyID = self.request.get('survey-id')
                            self.SurveyStatus(strSurveyID=strSurveyID)

                        elif strFunction == "survey-responses":
                            strSurveyID = self.request.get('survey-id')
                            self.SurveyResponses(strSurveyID=strSurveyID)

                        elif strFunction == "survey-credit":
                            self.SurveyCredit(strOrganizationID=thisEndPoint.strOrganizationID)

                        elif strFunction == "fax-send":
                            #def SendFax(self,strFaxMediaURL,strFaxNumber):
                            strFaxMediaURL = self.request.get('media-url')
                            strFaxNumber = self.request.get('fax-number')
                            self.SendFax(strFaxMediaURL=strFaxMediaURL,strFaxNumber=strFaxNumber,thisEndPoint=thisEndPoint.strOrganizationID)

                        elif strFunction == "fax-status":
                            strRef = self.request.get('ref')
                            self.FaxStatus(strRef=strRef)
                        elif strFunction == "fax-receive":
                            strFaxToEmailAddress = self.request.get('fax-email')
                            self.ReceiveFax(strFaxEmail=strFaxToEmailAddress)
                        elif strFunction == "fax-credit":
                            self.FaxCredit(strOrganizationID=thisEndPoint.strOrganizationID)
                    else:
                        self.response.headers["Content-Type"] = "text/plain"
                        self.response.status_code = 401
                        self.response.write("Error Your Organization is not verified please verify your organization")
                else:
                    self.response.headers["Content-Type"] = "text/plain"
                    self.response.status_code = 401
                    self.response.write("Error You do not have a valid account")
            else:
                self.response.headers["Content-Type"] = "text/plain"
                self.response.status_code = 401
                self.response.write("Error your Domain is not Authorized to use this endpoint")
        else:
            self.response.headers["Content-Type"] = "text/plain"
            self.response.status_code = 401
            self.response.write("Aunthentication Error")


app = webapp2.WSGIApplication([
    ('/endpoints/.*', RoutesHandler)
    #TODO- Create Advertising Endpoints and also Surveys End Points---Refine this idea its prooving to be difficult
], debug=True)
import os
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
import logging
import datetime

from accounts import Accounts

from dashboard import AccountDetails
from errormessages import MyErrors
from mysms import SMSPortalBudget

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class SurveyAccount(ndb.Expando):
    """
        Advertising Account
    """
    strUserID = ndb.StringProperty()
    strAccountID = ndb.StringProperty()
    strOrganizationID = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strTel = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strWebsite = ndb.StringProperty()

    strDate = ndb.DateProperty(auto_now_add=True)
    strTime = ndb.TimeProperty(auto_now_add=True)

    strTotalCredits = ndb.IntegerProperty(default=0)


    strTotalTopUpCost = ndb.IntegerProperty(default=0)
    strTopUpCredit = ndb.IntegerProperty(default=0)
    strTopUpReference = ndb.StringProperty()
    strTopUpInvoiceLink = ndb.StringProperty()
    strPayByDate = ndb.DateProperty()
    strDateInvoiceCreated = ndb.DateProperty()
    strDepositSlipFileName = ndb.StringProperty()


    def writeDepositSlipFilename(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strDepositSlipFileName = strinput
                return True
            else:
                return False
        except:
            return False


    def writeDateInvoiceCreated(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateInvoiceCreated = strinput
                return True
            else:
                return False
        except:
            return False
    def writePayByDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strPayByDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTotalTopUpCost(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalTopUpCost = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def CreateTopUpInvoiceLink(self,strinput):
        """
            strinput should be TopUpReference
        :param strinput:
        :return:
        """
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTopUpInvoiceLink = "/surveys/topup/invoice/" +  strinput
                return True
            else:
                return False
        except:
            return False
    def writeTopUpReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTopUpReference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTopUpCredit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTopUpCredit = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def CreateTopUpReference(self):
        import random,string
        try:
            strTopUpReference = ""
            for i in range(12):
                strTopUpReference += random.SystemRandom().choice(string.digits + string.ascii_uppercase)

            return strTopUpReference
        except:
            return None



    def writeTotalCredits(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTotalCredits = int(strinput)
                return True
            else:
                return False
        except:
            return False



    def writeUserID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False
        #TODO- Intergrate Organization Account to the Add Account
        #TODO- this will allow all users to access the same organization
        #TODO- Advertising Account
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
    def writeNames(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strNames = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurname(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurname = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTel = strinput
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
    def writeWebsite(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strWebsite = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAccountID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccountID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateAccountID(self):
        import string,random
        try:
            strAccountID = ""
            for i in range(256):
                strAccountID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)

            return strAccountID
        except:
            return None
    def writeDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTime = strinput
                return True
            else:
                return False
        except:
            return False

class SurveyContactLists(ndb.Expando):
    strListID = ndb.StringProperty()
    #TODO- Please make sure that the advert account is used to obtain the user id so that only users who owns
    #TODO- Advertising Accounts can create Survey Lists

    strUserID = ndb.StringProperty()
    strOrganizationID = ndb.StringProperty()
    strName = ndb.StringProperty()

    strDescription = ndb.StringProperty()
    strTotal = ndb.IntegerProperty(default=0)
    strDate = ndb.DateProperty(auto_now_add=True)
    strTime = ndb.TimeProperty(auto_now_add=True)

    def writeListID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strListID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateListID(self):
        import random,string
        try:
            strListID = ""
            for i in range(256):
                strListID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strListID
        except:
            return None
    def writeUserID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False
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
    def writeName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strDescription = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTotalContacts(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotal = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeDate(self,strinput):
        try:

            if isinstance(strinput,datetime.date):
                self.strDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTime = strinput
                return True
            else:
                return False
        except:
            return False

class SurveyContacts(ndb.Expando):
    """
        Survey Contacts Contacts for surveys organised by list ID
    """
    strListID = ndb.StringProperty()
    strContactID = ndb.StringProperty()

    strName = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()

    def writeListID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strListID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strContactID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateContactID(self):
        import string,random
        try:
            strContactID = ""
            for i in range(256):
                strContactID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strContactID
        except:
            return None
    def writeName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurname(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurname = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False

class SurveySchedules(ndb.Expando):
    """
        Schedule ID is used to differentiate one schedule from another
        uid used to identify the user creating the schedule
        Schedule Name and Description for user identification
        ListID is used to recognize the contact list to send the survey to
        SurveyID is used to recognize the actual Survey to send as scheduled


        Survey Status
        Scheduled Survey is one which will run at a later date and time
        Running Schedule is one in which its still running listening to user
        responses and sending more questions
        Completed is one in which all questions and responses are sent

    """
    strScheduleID = ndb.StringProperty()
    strUserID = ndb.StringProperty()
    strListID = ndb.StringProperty()
    strSurveyID = ndb.StringProperty()
    strName = ndb.StringProperty()
    strDescription = ndb.StringProperty()
    strStartDate = ndb.DateProperty()
    strStartTime = ndb.TimeProperty()
    strNotifyOnStart = ndb.BooleanProperty(default=True)
    strNotifyOnEnd = ndb.BooleanProperty(default=True)
    strActivateSchedule = ndb.BooleanProperty(default=False) #TODO- Schedule Active to allow schedule to run

    strSurveyStatus = ndb.StringProperty(default="Scheduled") # Running , Completed, Suspended
    strDateStatusChange = ndb.DateProperty()
    strTimeStatusChange = ndb.TimeProperty()


    def writeScheduleID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strScheduleID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateScheduleID(self):
        import random,string
        try:
            strScheduleID = ""
            for i in range(256):
                strScheduleID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strScheduleID
        except:
            return None
    def writeUserID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strDescription = strinput
                return True
            else:
                return False
        except:
            return False
    def writeListID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strListID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurveyID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurveyID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStartDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strStartDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStartTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strStartTime = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNotifyOnStart(self,strinput):
        try:
            if strinput in [True,False]:
                self.strNotifyOnStart = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNotifyOnEnd(self,strinput):
        try:
            if strinput in [True,False]:
                self.strNotifyOnEnd = strinput
                return True
            else:
                return False
        except:
            return False
    def writeActivateSchedule(self,strinput):
        try:
            if strinput in [True,False]:
                self.strActivateSchedule = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurveyStatus(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ["Scheduled","Running","Completed","Suspended"]:
                self.strSurveyStatus = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateStatusChange(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateStatusChange = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeStatusChange(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeStatusChange = strinput
                return True
            else:
                return False
        except:
            return False

class Surveys(ndb.Expando):
    strUserID = ndb.StringProperty()
    strOrganizationID = ndb.StringProperty()

    strSurveyID = ndb.StringProperty()
    strName = ndb.StringProperty()
    strDescription = ndb.StringProperty()
    strSurveyType = ndb.StringProperty(default="multichoice") # general
    strDateCreated = ndb.DateProperty(auto_now_add=True)
    strTimeCreated = ndb.TimeProperty(auto_now_add=True)

    strStartDate = ndb.DateProperty()
    strStartTime = ndb.TimeProperty()

    strSurveyStatus = ndb.StringProperty(default="Scheduled") # Running, Completed, Scheduled,Building
    strSurveyIsPaid = ndb.BooleanProperty(default=False)

    strAssignedCredit = ndb.IntegerProperty(default=0)

    strRunFromCredit = ndb.BooleanProperty(default=False)


    def writeUserID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False
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
    def CreateSurveyID(self):
        import random,string
        try:
            strSurveyID = ""
            for i in range(256):
                strSurveyID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strSurveyID
        except:
            return None
    def writeSurveyID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurveyID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurveyName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurveyDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strDescription = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateCreated(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateCreated = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeCreated(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeCreated = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurveyType(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurveyType = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStartDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strStartDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStartTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strStartTime = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurveyStatus(self,strinput):
        try:
            if strinput in ["Scheduled","Running","Completed"]:
                self.strSurveyStatus = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurveyIsPaid(self,strinput):
        try:
            if strinput in [True,False]:
                self.strSurveyIsPaid = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAssignedCredit(self,strinput):
        try:
            strinput = str(strinput)
            if (strinput.isdigit()) and (int(strinput) > 0):
                self.strAssignedCredit = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeRunFromCredit(self,strinput):
        try:

            if strinput in [True,False]:
                self.strRunFromCredit = strinput
                return True
            else:
                return False
        except:
            return False

class MultiChoiceSurveys(ndb.Expando):
    strIndex = ndb.IntegerProperty()
    strSurveyID = ndb.StringProperty()
    strQuestionID = ndb.StringProperty()
    strQuestion = ndb.StringProperty()
    strChoiceOne = ndb.StringProperty(default="undefined")
    strChoiceTwo = ndb.StringProperty(default="undefined")
    strChoiceThree = ndb.StringProperty(default="undefined")
    strChoiceFour = ndb.StringProperty(default="undefined")
    strDateCreated = ndb.DateTimeProperty(auto_now_add=True)
    # We will sort the qeustions by making use of the Date Created Field
    # This Means the tracker will keep the current Question ID then the next
    # question will be the question with the later date if not exit



    def writeSurveyID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurveyID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeQuestionID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strQuestionID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateQuestionID(self):
        import random,string
        try:
            strQuestionID = ""
            for i in range(256):
                strQuestionID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strQuestionID
        except:
            return None
    def writeQuestion(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strQuestion = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChoiceOne(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strChoiceOne = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChoiceTwo(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strChoiceTwo = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChoiceThree(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strChoiceThree = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChoiceFour(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strChoiceFour = strinput
                return True
            else:
                return False
        except:
            return False

class MultiChoiceSurveyAnswers(ndb.Expando):
    strCell = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strRef = ndb.StringProperty()
    strSurveyID = ndb.StringProperty()
    strQuestionID = ndb.StringProperty()
    strQuestion = ndb.StringProperty()
    strOptionNumber = ndb.IntegerProperty(default=0) # If Zero it means user did not answer
    strDateTime = ndb.DateTimeProperty(auto_now_add=True)


    def writeRef(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strRef = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurveyID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurveyID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeQuestion(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strQuestion = strinput
                return True
            else:
                return False
        except:
            return False
    def writeQuestionID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strQuestionID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOptionNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strOptionNumber = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeNames(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strNames = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSurname(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurname = strinput
                return True
            else:
                return False
        except:
            return False

class GeneralQuestionsSurvey(ndb.Expando):
    strSurveyID = ndb.StringProperty()
    strQuestionID = ndb.StringProperty()
    strQuestion = ndb.StringProperty()

    def writeSurveyID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurveyID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeQuestionID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strQuestionID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateQuestionID(self):
        import random,string
        try:
            strQuestionID = ""
            for i in range(256):
                strQuestionID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strQuestionID
        except:
            return None
    def writeQuestion(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strQuestion = strinput
                return True
            else:
                return False
        except:
            return False

class SurveyOrders(ndb.Expando):

    strUserID = ndb.StringProperty()
    strOrganizationID = ndb.StringProperty()
    strSurveyID = ndb.StringProperty()
    strItemCount = ndb.IntegerProperty(default=0)
    strOrderID = ndb.StringProperty()
    strScheduleID = ndb.StringProperty()
    strTotalSMS = ndb.IntegerProperty(default=0)
    strQoutedAmount = ndb.FloatProperty(default=0)
    strTotalPaid = ndb.IntegerProperty(default=0)
    strFullyPaid = ndb.BooleanProperty(default=False)
    strOrderCompleted = ndb.BooleanProperty(default=False)
    strOrderStartDate = ndb.DateProperty()
    strOrderStartTime = ndb.TimeProperty()
    strDepositReference = ndb.StringProperty()
    strRunOrder = ndb.BooleanProperty(default=False)

    def writeUserID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False
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
    def writeSurveyID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurveyID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeItemCount(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strItemCount = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeOrderID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strOrderID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateOrderID(self):
        import random,string
        try:
            strOrderID = ""
            for i in range(256):
                strOrderID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strOrderID
        except:
            return None
    def writeQuoteAmount(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strQoutedAmount = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeTotalPaid(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalPaid = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeFullyPaid(self,strinput):
        try:
            if strinput in [True,False]:
                self.strFullyPaid = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOrderCompleted(self,strinput):
        try:
            if strinput in [True,False]:
                self.strOrderCompleted = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOrderStartDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strOrderStartDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOrderStartTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strOrderStartTime = strinput
                return True
            else:
                return False
        except:
            return False
    def writeScheduleID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strScheduleID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTotalSMS(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalSMS = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def CreatedDepositReference(self):
        import random, string
        try:
            strDepReference = ""
            for i in range(6):
                strDepReference += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strDepReference
        except:
            return None
    def writeDepositReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strDepositReference = strinput
                return True
            else:
                return False
        except:
            return False
    def writeRunOrder(self,strinput):
        try:
            if strinput in [True,False]:
                self.strRunOrder = strinput
                return True
            else:
                return False

        except:
            return False

class SurveyPayments(ndb.Expando):

    """
        Try using a method where in the administrator section i can verify all loaded payments through their Deposit Reference
        Generated in the Orders Class , The Reference is only used for the specific order only .

        once a payment verification is received an invoice is generated and the order marked as paid if fully paid and the totla paid amount
        adjusted...on the payment record the same is done for easy creation of invoices...
    """
    strUserID = ndb.StringProperty()
    strOrderID = ndb.StringProperty()
    strOrganizationID = ndb.StringProperty()
    strPaymentID = ndb.StringProperty()
    strDepositReference = ndb.StringProperty() # Intergrate this with payments class
    strAmountPaid = ndb.IntegerProperty(default=0)
    strPaymentMethod = ndb.StringProperty(default="Direct Deposit") # Cash , EFT
    strDatePaid = ndb.DateProperty(auto_now_add=True)
    strTimePaid = ndb.TimeProperty(auto_now_add=True)
    strPaymentVerified = ndb.BooleanProperty(default=False)
    strDateVerified = ndb.BooleanProperty(default=False)
    strTimeVerified = ndb.BooleanProperty(default=False)
    #TODO- When verification is effected remember to set the dates and time

    def writeUserID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False
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
    def writeOrderID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strOrderID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreatePaymentID(self):
        import random,string
        try:
            strPaymentID = ""
            for i in range(256):
                strPaymentID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strPaymentID
        except:
            return None
    def writePaymentID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPaymentID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAmountPaid(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strAmountPaid = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writePaymentMethod(self,strinput):
        try:

            if strinput in ["Direct Deposit","Cash","EFT","PayPal"]:
                self.strPaymentMethod = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDatePaid(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDatePaid = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimePaid(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimePaid = strinput
                return True
            else:
                return False
        except:
            return False
    def writePaymentVerified(self,strinput):
        try:
            if strinput in [True,False]:
                self.strPaymentVerified = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDepositReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strDepositReference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateVerified(self,strinput):
        try:

            if isinstance(strinput,datetime.date):
                self.strDateVerified = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeVerified(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeVerified = strinput
                return True
            else:
                return False
        except:
            return False

class SurveyTracker(ndb.Expando):
    """
        If a response is received then on the next interaction the next question
        must be asked
        If Question Expired then survey must be terminated and cell marked as non responsive

        if Question is not being answered for five consecutive runs then mark user as not participating

        The tracker keeps record of only the present question answer session for each user
        for each survey

        if client participation is False then dont run the Survey Tracker

        create the tracker record for each client when a message is sent


    """

    strSurveyID = ndb.StringProperty()
    strCurrentQuestionID = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strRef = ndb.StringProperty()
    strResponseReceived = ndb.BooleanProperty(default=False)
    strClientParticipation = ndb.BooleanProperty(default=True)
    strDate = ndb.DateProperty()
    strTime = ndb.TimeProperty()
    strIsLastQuestion = ndb.BooleanProperty(default=False)
    strRunTimes = ndb.IntegerProperty(default=0) # Count how many times the Tracker ran looking for answers

    def writeSurveyID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurveyID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCurrentQuestionID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCurrentQuestionID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False
    def writeResponseReceived(self,strinput):
        try:
            if strinput in [True,False]:
                self.strResponseReceived = strinput
                return True
            else:
                return False
        except:
            return False
    def writeClientParticipation(self,strinput):
        try:
            if strinput in [True,False]:
                self.strClientParticipation = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTime = strinput
                return True
            else:
                return False
        except:
            return False
    def writeIsLastQuestion(self,strinput):
        try:
            if strinput in [True,False]:
                self.strIsLastQuestion = strinput
                return True
            else:
                return False
        except:
            return False
    def writeRunTimes(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strRunTimes = int(strinput)
                return True
            else:
                return False
        except:
            return False

class GeneralQuestionsAnswers(ndb.Expando):
    strCell = ndb.StringProperty()
    strSurveyID = ndb.StringProperty()
    strQuestionID = ndb.StringProperty()
    strAnswer = ndb.StringProperty()

    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCell =strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurveyID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurveyID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeQuestionID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strQuestionID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAnswer(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAnswer = strinput
                return True
            else:
                return False
        except:
            return False


from firebaseadmin import VerifyAndReturnAccount

class SurveyHandler(webapp2.RequestHandler):


    #TODO- do this for all utilities

    def get(self):
        template = template_env.get_template('templates/surveys/mainsurvey.html')
        context = {}
        self.response.write(template.render(context))

    def post(self):
        from accounts import Organization
        vstrChoice = self.request.get('vstrChoice')
        # Uploading a Survey

        if vstrChoice == "0":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                if thisMainAccount.verified:
                    findRequest = Surveys.query(Surveys.strOrganizationID == thisMainAccount.organization_id)
                    thisSurveysList = findRequest.fetch()

                    template = template_env.get_template('templates/surveys/surveys.html')
                    context = {'thisSurveysList': thisSurveysList}
                    self.response.write(template.render(context))
                else:
                    thisErrors = MyErrors()

                    ErrorMessage = thisErrors.strAccountNotVerified
                    template = template_env.get_template('templates/errors/suberror.html')
                    context = {'ErrorMessage': ErrorMessage, 'thisErrors': thisErrors}
                    self.response.write(template.render(context))
            else:
                thisErrors = MyErrors()

                ErrorMessage = thisErrors.strAccountError
                template = template_env.get_template('templates/errors/suberror.html')
                context = {'ErrorMessage': ErrorMessage, 'thisErrors': thisErrors}
                self.response.write(template.render(context))

        # Upload Survey
        elif vstrChoice == "1":

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrSurveyName = self.request.get('vstrSurveyName')
            vstrDescription = self.request.get('vstrDescription')
            vstrSurveyType = self.request.get('vstrSurveyType')


            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = Surveys.query(Surveys.strOrganizationID == thisMainAccount.organization_id, Surveys.strName == vstrSurveyName)
                thisSurveysList = findRequest.fetch()

                if len(thisSurveysList) > 0:
                    self.response.write("The survey already exist please edit the existing survey Instead")
                else:
                    thisSurvey = Surveys()

                    vstrThisDate = datetime.datetime.now()
                    strThisDate = vstrThisDate.date()

                    strThisTime = datetime.time(hour=vstrThisDate.hour,minute=vstrThisDate.minute,second=vstrThisDate.second)
                    thisSurvey.writeSurveyName(strinput=vstrSurveyName)
                    thisSurvey.writeSurveyDescription(strinput=vstrDescription)

                    thisSurvey.writeSurveyType(strinput=vstrSurveyType)
                    thisSurvey.writeDateCreated(strinput=strThisDate)
                    thisSurvey.writeTimeCreated(strinput=strThisTime)
                    thisSurvey.writeUserID(strinput=vstrUserID)
                    thisSurvey.writeSurveyID(strinput=thisSurvey.CreateSurveyID())
                    thisSurvey.writeOrganizationID(strinput=thisMainAccount.organization_id)
                    thisSurvey.put()
                    self.response.write("Survey Successfully created please dont forget to create your survey questions")
            else:
                self.response.write("Create your main account")


        # Survey Accounts

        elif vstrChoice == "2":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                if thisMainAccount.verified:
                    findRequest = SurveyAccount.query(SurveyAccount.strOrganizationID == thisMainAccount.organization_id)
                    thisSurveyAccountList = findRequest.fetch()
                    if len(thisSurveyAccountList) > 0:
                        thisSurveyAccount = thisSurveyAccountList[0]
                    else:
                        thisSurveyAccount = SurveyAccount()

                    template = template_env.get_template('templates/surveys/sub/accounts.html')
                    context = {'thisSurveyAccount':thisSurveyAccount,}
                    self.response.write(template.render(context))


        # Main Screen Surveys Orders
        elif vstrChoice == "3":

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                if thisMainAccount.verified:
                    findRequest = SurveyOrders.query(SurveyOrders.strOrganizationID == thisMainAccount.organization_id)
                    thisOrdersList = findRequest.fetch()

                    template = template_env.get_template('templates/surveys/orders/mainorderlist.html')
                    context = {'thisOrdersList':thisOrdersList}
                    self.response.write(template.render(context))

        #Update Survey Account
        elif vstrChoice == "4":

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrNames = self.request.get('vstrNames')
            vstrSurname = self.request.get('vstrSurname')
            vstrCell = self.request.get('vstrCell')
            vstrTel = self.request.get('vstrTel')
            vstrEmail = self.request.get('vstrEmail')
            vstrWebsite = self.request.get('vstrWebsite')


            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                if thisMainAccount.verified:
                    findRequest = SurveyAccount.query(SurveyAccount.strOrganizationID == thisMainAccount.organization_id)
                    thisSurveyAccountList = findRequest.fetch()
                    if len(thisSurveyAccountList) > 0:
                        thisSurveyAccount = thisSurveyAccountList[0]
                    else:
                        thisSurveyAccount = SurveyAccount()
                        thisSurveyAccount.writeOrganizationID(strinput=thisMainAccount.organization_id)
                        thisSurveyAccount.writeUserID(strinput=vstrUserID)
                        thisSurveyAccount.writeAccountID(strinput=thisSurveyAccount.CreateAccountID())
                    thisSurveyAccount.writeNames(strinput=vstrNames)
                    thisSurveyAccount.writeSurname(strinput=vstrSurname)
                    thisSurveyAccount.writeCell(strinput=vstrCell)
                    thisSurveyAccount.writeTel(strinput=vstrTel)
                    thisSurveyAccount.writeEmail(strinput=vstrEmail)
                    thisSurveyAccount.writeWebsite(strinput=vstrWebsite)
                    vstrDateTime = datetime.datetime.now()
                    strThisDate = vstrDateTime.date()
                    strThisTime = datetime.time(hour=vstrDateTime.hour,minute=vstrDateTime.minute,second=vstrDateTime.second)
                    thisSurveyAccount.writeDate(strinput=strThisDate)
                    thisSurveyAccount.writeTime(strinput=strThisTime)
                    thisSurveyAccount.put()
                    self.response.write("Successfully updated Survey Account")
                else:
                    thisErrors = MyErrors()

                    ErrorMessage = thisErrors.strAccountNotVerified
                    template = template_env.get_template('templates/errors/suberror.html')
                    context = {'ErrorMessage': ErrorMessage, 'thisErrors': thisErrors}
                    self.response.write(template.render(context))
            else:
                thisErrors = MyErrors()

                ErrorMessage = thisErrors.strAccountError
                template = template_env.get_template('templates/errors/suberror.html')
                context = {'ErrorMessage': ErrorMessage, 'thisErrors': thisErrors}
                self.response.write(template.render(context))

        elif vstrChoice == "5":
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')



            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                if thisMainAccount.verified:
                    findRequest = SurveyPayments.query(SurveyPayments.strOrganizationID == thisMainAccount.organization_id)
                    thisPaymentList = findRequest.fetch()

                    template = template_env.get_template('templates/surveys/invoices/invoicelist.html')
                    context = {'thisPaymentList':thisPaymentList}
                    self.response.write(template.render(context))


        elif vstrChoice == "6":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')



            vstrAddCredits = self.request.get("vstrAddCredits")
            vstrPaymentMethod = self.request.get("vstrPaymentMethod")

            findRequest = SMSPortalBudget.query()
            thisPortalBudgetList = findRequest.fetch()

            if len(thisPortalBudgetList) > 0:
                thisPortal = thisPortalBudgetList[0]
            else:
                thisPortal = SMSPortalBudget()

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = SurveyAccount.query(SurveyAccount.strOrganizationID == thisMainAccount.organization_id)
                thisSurveyAccountList = findRequest.fetch()

                if len(thisSurveyAccountList) > 0:
                    thisSurveyAccount = thisSurveyAccountList[0]

                    if vstrPaymentMethod == "DirectDeposit":
                        vstrThisDate = datetime.datetime.now()
                        strThisDate = datetime.date(year=vstrThisDate.year,month=vstrThisDate.month,day=vstrThisDate.day)
                        vstrThisDate += datetime.timedelta(days=30)
                        strPayByDate = datetime.date(year=vstrThisDate.year, month=vstrThisDate.month, day=vstrThisDate.day)
                        strTotalCost = (thisPortal.strAdvertSellRate * int(vstrAddCredits))/100

                        thisSurveyAccount.writeTotalTopUpCost(strinput=strTotalCost)

                        thisSurveyAccount.writeTopUpCredit(strinput=vstrAddCredits)
                        thisSurveyAccount.writeTopUpReference(strinput=thisSurveyAccount.CreateTopUpReference())
                        thisSurveyAccount.CreateTopUpInvoiceLink(strinput=thisSurveyAccount.strTopUpReference)
                        thisSurveyAccount.writePayByDate(strinput=strPayByDate)
                        thisSurveyAccount.writeDateInvoiceCreated(strinput=strThisDate)
                        thisSurveyAccount.put()
                        findRequest = SurveyAccount.query(SurveyAccount.strOrganizationID == thisMainAccount.organization_id)
                        thisSurveyAccountList = findRequest.fetch()
                        if len(thisSurveyAccountList) > 0:
                            thisSurveyAccount = thisSurveyAccountList[0]

                            self.response.write("""
                            Top up Credit successfully processed please click on this link to view your <strong><a href=" """ + thisSurveyAccount.strTopUpInvoiceLink + """ ">Proforma Invoice</a></strong>""")


        elif vstrChoice == "7":

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')


            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = Organization.query(Organization.strOrganizationID == thisMainAccount.organization_id)
                thisOrgList = findRequest.fetch()

                if len(thisOrgList) > 0:
                    thisOrg = thisOrgList[0]
                else:
                    thisOrg = Organization()

                if thisMainAccount.verified and thisOrg.strVerified:
                    findRequest = Surveys.query(Surveys.strOrganizationID == thisMainAccount.organization_id)
                    thisSurveysList = findRequest.fetch()

                    strTotalSurveys = len(thisSurveysList)

                    findRequest = SurveyAccount.query(SurveyAccount.strOrganizationID == thisMainAccount.organization_id)
                    thisSurveysAccountList = findRequest.fetch()
                    if len(thisSurveysAccountList) > 0:
                        thisSurveyAccount = thisSurveysAccountList[0]
                    else:
                        thisSurveyAccount = SurveyAccount()

                    template = template_env.get_template('templates/surveys/sub/SurveysSubmenu.html')
                    context = {'thisSurveysList': thisSurveysList, 'thisSurveyAccount': thisSurveyAccount,
                               'strTotalSurveys': strTotalSurveys}
                    self.response.write(template.render(context))


class ThisSurveyHandler(webapp2.RequestHandler):

    


    def get(self):

        URL = self.request.url
        strURLlist = URL.split("/")
        strSurveyID = strURLlist[len(strURLlist) - 1]

        findRequest = Surveys.query(Surveys.strSurveyID == strSurveyID)
        thisSurveyList = findRequest.fetch()

        if len(thisSurveyList) > 0:
            thisSurvey = thisSurveyList[0]

            findRequest = SurveyAccount.query(SurveyAccount.strOrganizationID == thisSurvey.organization_id)
            thisSurveyAccountList = findRequest.fetch()

            if len(thisSurveyAccountList) > 0:
                thisSurveyAccount = thisSurveyAccountList[0]
            else:
                thisSurveyAccount = SurveyAccount()


            if thisSurvey.strSurveyType == "multichoice":
                findRequest = MultiChoiceSurveys.query(MultiChoiceSurveys.strSurveyID == strSurveyID)
                thisMultiChoiceSurveysList = findRequest.fetch()

                template = template_env.get_template('templates/surveys/multi/multichoice.html')
                context = {'thisMultiChoiceSurveysList':thisMultiChoiceSurveysList,'strSurveyID':strSurveyID,'thisSurvey':thisSurvey,'thisSurveyAccount':thisSurveyAccount}
                self.response.write(template.render(context))
            elif thisSurvey.strSurveyType == "general":
                findRequest = GeneralQuestionsSurvey.query(GeneralQuestionsSurvey.strSurveyID == strSurveyID)
                thisGeneralQuestionsSurveyList = findRequest.fetch()
                template = template_env.get_template('templates/survey/general/general.html')
                context = {'thisGeneralQuestionsSurveyList':thisGeneralQuestionsSurveyList}
                self.response.write(template.render(context))
            else:
                self.response.write("Fatal Error unable to determine survey type please contact the system admin")

    def post(self):

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')


            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrSurveyID = self.request.get('vstrSurveyID')

                findRequest = Surveys.query(Surveys.strSurveyID == vstrSurveyID)
                thisSurveysList = findRequest.fetch()
                if len(thisSurveysList) > 0:
                    thisSurvey = thisSurveysList[0]

                    findRequest = SurveyAccount.query(SurveyAccount.strOrganizationID == thisSurvey.organization_id)
                    thisSurveyAccountList = findRequest.fetch()

                    if len(thisSurveyAccountList) > 0:
                        thisSurveyAccount = thisSurveyAccountList[0]
                    else:
                        thisSurveyAccount = SurveyAccount()



                    template = template_env.get_template('templates/surveys/multi/survey.html')
                    context = {'thisSurvey':thisSurvey,'thisSurveyAccount':thisSurveyAccount}
                    self.response.write(template.render(context))


        #Update Multi choice Survey

        elif vstrChoice == "1":

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                vstrSurveyID = self.request.get('vstrSurveyID')
                vstrSurveyName = self.request.get('vstrSurveyName')
                vstrDescription = self.request.get('vstrDescription')
                vstrSurveyType = self.request.get('vstrSurveyType')

                findRequest = Surveys.query(Surveys.strSurveyID == vstrSurveyID)
                thisSurveysList = findRequest.fetch()

                if len(thisSurveysList) > 0:
                    thisSurvey = thisSurveysList[0]
                    thisSurvey.writeSurveyName(strinput=vstrSurveyName)
                    thisSurvey.writeSurveyDescription(strinput=vstrDescription)
                    thisSurvey.writeSurveyType(strinput=vstrSurveyType)
                    thisSurvey.put()
                    self.response.write("Survey Successfully updated")

        #Survey Questions Multi choice

        elif vstrChoice == "2":
            #+ '&vstrSurveyID=' + vstrSurveyID + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrSurveyID = self.request.get('vstrSurveyID')

                findRequest = MultiChoiceSurveys.query(MultiChoiceSurveys.strSurveyID == vstrSurveyID)
                thisMultiChoiceSurveyList = findRequest.fetch()
                findRequest = Surveys.query(Surveys.strSurveyID == vstrSurveyID)
                thisSurveysList = findRequest.fetch()

                if len(thisSurveysList) > 0:
                    thisSurvey = thisSurveysList[0]
                else:
                    thisSurvey = Surveys()

                template = template_env.get_template('templates/surveys/multi/surveyQuestions.html')
                context = {'thisMultiChoiceSurveyList':thisMultiChoiceSurveyList,'vstrSurveyID':vstrSurveyID,'thisSurvey':thisSurvey}
                self.response.write(template.render(context))
            #Survey Questions Multi choice

        elif vstrChoice == "3":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrQuestion = self.request.get('vstrQuestion')
                vstrChoiceOne = self.request.get('vstrChoiceOne')
                vstrChoiceTwo = self.request.get('vstrChoiceTwo')
                vstrChoiceThree = self.request.get('vstrChoiceThree')
                vstrChoiceFour = self.request.get('vstrChoiceFour')
                vstrSurveyID = self.request.get('vstrSurveyID')

                findRequest = MultiChoiceSurveys.query(MultiChoiceSurveys.strSurveyID == vstrSurveyID,MultiChoiceSurveys.strQuestion == vstrQuestion)
                thisMultiChoiceSurveyList = findRequest.fetch()

                if len(thisMultiChoiceSurveyList) > 0:
                    thisMultiChoiceSurvey = thisMultiChoiceSurveyList[0]
                else:
                    thisMultiChoiceSurvey = MultiChoiceSurveys()
                    thisMultiChoiceSurvey.writeQuestionID(strinput=thisMultiChoiceSurvey.CreateQuestionID())

                thisMultiChoiceSurvey.writeSurveyID(strinput=vstrSurveyID)
                thisMultiChoiceSurvey.writeQuestion(strinput=vstrQuestion)
                thisMultiChoiceSurvey.writeChoiceOne(strinput=vstrChoiceOne)
                thisMultiChoiceSurvey.writeChoiceTwo(strinput=vstrChoiceTwo)
                thisMultiChoiceSurvey.writeChoiceThree(strinput=vstrChoiceThree)
                thisMultiChoiceSurvey.writeChoiceFour(strinput=vstrChoiceFour)
                thisMultiChoiceSurvey.put()
                self.response.write("Survey Question successfully uploaded")
            # Survey Response for multi choice
        elif vstrChoice == "4":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                vstrSurveyID = self.request.get('vstrSurveyID')

                findRequest = MultiChoiceSurveyAnswers.query(MultiChoiceSurveyAnswers.strSurveyID == vstrSurveyID)
                thisSurveyAnswersList = findRequest.fetch()

                findRequest = Surveys.query(Surveys.strSurveyID == vstrSurveyID)
                thisSurveysList = findRequest.fetch()
                if len(thisSurveysList) > 0:
                    thisSurvey = thisSurveysList[0]
                else:
                    thisSurvey = Surveys()

                template = template_env.get_template('templates/surveys/multi/responses.html')
                context = {'thisSurveyAnswersList':thisSurveyAnswersList,'thisSurvey':thisSurvey}
                self.response.write(template.render(context))
        elif vstrChoice == "5":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrSurveyID = self.request.get('vstrSurveyID')

                findRequest = SurveyAccount.query(SurveyAccount.strUserID == vstrUserID)
                thisSurveyAccountList = findRequest.fetch()
                if len(thisSurveyAccountList) > 0:
                    thisSurveyAccount = thisSurveyAccountList[0]
                else:
                    thisSurveyAccount = SurveyAccount()



                findRequest = SurveyContactLists.query(SurveyContactLists.strOrganizationID == thisSurveyAccount.strOrganizationID)
                thisSurveyContactLists = findRequest.fetch()

                template = template_env.get_template('templates/surveys/contacts/mycontacts.html')
                context = {'thisSurveyContactLists':thisSurveyContactLists,'vstrSurveyID':vstrSurveyID,'thisSurveyAccount':thisSurveyAccount}
                self.response.write(template.render(context))
        elif vstrChoice == "6":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrSurveyID = self.request.get('vstrSurveyID')
                vstrOrganizationID = self.request.get('vstrOrganizationID')
                vstrListName = self.request.get('vstrListName')
                vstrListDescription = self.request.get('vstrListDescription')

                findRequest = SurveyContactLists.query(SurveyContactLists.strOrganizationID == vstrOrganizationID,SurveyContactLists.strName == vstrListName)
                thisSurveyContactLists = findRequest.fetch()

                if len(thisSurveyContactLists) > 0:

                    self.response.write("Survey Contact List already present please edit list")
                else:
                    thisSurveyCList = SurveyContactLists()
                    thisSurveyCList.writeListID(strinput=thisSurveyCList.CreateListID())
                    thisSurveyCList.writeUserID(strinput=vstrUserID)
                    thisSurveyCList.writeName(strinput=vstrListName)
                    thisSurveyCList.writeDescription(strinput=vstrListDescription)
                    thisSurveyCList.writeOrganizationID(strinput=vstrOrganizationID)
                    vstrThisDate = datetime.datetime.now()
                    strThisDate = vstrThisDate.date()
                    strThisTime = datetime.time(hour=vstrThisDate.hour,minute=vstrThisDate.minute,second=vstrThisDate.second)
                    thisSurveyCList.writeDate(strinput=strThisDate)
                    thisSurveyCList.writeTime(strinput=strThisTime)
                    thisSurveyCList.writeTotalContacts(strinput=0)
                    thisSurveyCList.put()
                    self.response.write("Successfully uploaded Survey Contact Lists")
            #Manage Survey Schedules

        elif vstrChoice == "7":

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):



                vstrSurveyID = self.request.get('vstrSurveyID')

                findRequest = Accounts.query(Accounts.uid == vstrUserID)
                thisMainAccountList = findRequest.fetch()

                if len(thisMainAccountList) > 0:
                    thisMainAccount = thisMainAccountList[0]

                    findRequest = SurveySchedules.query(SurveySchedules.strSurveyID == vstrSurveyID)
                    thisSurveySchedulesList = findRequest.fetch()

                    findRequest = SurveyContactLists.query(SurveyContactLists.strOrganizationID == thisMainAccount.organization_id)
                    thisContactLists = findRequest.fetch()


                    template = template_env.get_template('templates/surveys/schedules/schedules.html')
                    context = {'thisSurveySchedulesList':thisSurveySchedulesList,'thisContactLists':thisContactLists,'vstrSurveyID':vstrSurveyID}
                    self.response.write(template.render(context))
            #Create Multi choice surve order

        elif vstrChoice == "8":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                vstrSurveyID = self.request.get('vstrSurveyID')

                findRequest = SurveySchedules.query(SurveySchedules.strSurveyID == vstrSurveyID)
                thisSurveyScheduleList = findRequest.fetch()

                findRequest = SurveyOrders.query(SurveyOrders.strSurveyID == vstrSurveyID)
                thisOrdersList = findRequest.fetch()

                template = template_env.get_template('templates/surveys/orders/neworder.html')
                context = {'thisSurveyScheduleList':thisSurveyScheduleList,'vstrSurveyID':vstrSurveyID,'thisOrdersList':thisOrdersList}
                self.response.write(template.render(context))

        elif vstrChoice == "9":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                vstrSurveyID = self.request.get('vstrSurveyID')
                vstrSelectSchedule = self.request.get('vstrSelectSchedule')
                vstrDepositMethod = self.request.get('vstrDepositMethod')


                findRequest = SMSPortalBudget.query()
                thisBudgetPortalList = findRequest.fetch()
                if len(thisBudgetPortalList) > 0:
                    thisBudgetPortal = thisBudgetPortalList[0]

                    findRequest = SurveySchedules.query(SurveySchedules.strScheduleID == vstrSelectSchedule)
                    thisSchedulesList = findRequest.fetch()
                    if len(thisSchedulesList) > 0:
                        thisSchedule = thisSchedulesList[0]

                        findRequest = SurveyContactLists.query(SurveyContactLists.strListID == thisSchedule.strListID)
                        thisContactLists = findRequest.fetch()

                        findRequest = Surveys.query(Surveys.strSurveyID == vstrSurveyID)
                        thisSurveyList = findRequest.fetch()

                        if len(thisSurveyList) > 0:
                            thisSurvey = thisSurveyList[0]

                            if thisSurvey.strSurveyType == "multichoice":
                                findRequest = MultiChoiceSurveys.query(MultiChoiceSurveys.strSurveyID == vstrSurveyID)
                                thisMultiChoiceSurveyList = findRequest.fetch()

                                strTotalSurveyQuestions = len(thisMultiChoiceSurveyList)
                            else:
                                strTotalSurveyQuestions = 0
                        else:
                            strTotalSurveyQuestions = 0


                        strTotalContacts = len(thisContactLists)
                        logging.info(thisBudgetPortal.strAdvertSellRate)
                        strSellRate = thisBudgetPortal.strAdvertSellRate / 100
                        logging.info(strSellRate)
                        strQuotedAmount = float(strTotalContacts * strTotalSurveyQuestions * strSellRate)
                        logging.info(strQuotedAmount)




                        thisSurveyOrder = SurveyOrders()
                        thisSurveyOrder.writeUserID(strinput=vstrUserID)
                        thisSurveyOrder.writeOrganizationID(strinput=thisMainAccount.organization_id)
                        thisSurveyOrder.writeOrderStartDate(strinput=thisSchedule.strStartDate)
                        thisSurveyOrder.writeOrderStartTime(strinput=thisSchedule.strStartTime)
                        thisSurveyOrder.writeSurveyID(strinput=thisSchedule.strSurveyID)
                        thisSurveyOrder.writeItemCount(strinput=1)
                        thisSurveyOrder.writeOrderID(strinput=thisSurveyOrder.CreateOrderID())
                        thisSurveyOrder.writeScheduleID(strinput=thisSchedule.strScheduleID)
                        thisSurveyOrder.writeTotalSMS(strinput=strTotalContacts)
                        thisSurveyOrder.writeQuoteAmount(strinput=strQuotedAmount)
                        thisSurveyOrder.writeTotalPaid(strinput=0)
                        thisSurveyOrder.writeFullyPaid(strinput=False)
                        thisSurveyOrder.writeOrderCompleted(strinput=False)
                        thisSurveyOrder.writeDepositReference(strinput=thisSurveyOrder.CreatedDepositReference())
                        thisSurveyOrder.writeRunOrder(strinput=False)
                        thisSurveyOrder.put()

                        self.response.write("Survey order successfully created")
        elif vstrChoice == "10":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrCreditToAssign = self.request.get("vstrCreditToAssign")
                vstrAvailableCredit = self.request.get("vstrAvailableCredit")
                vstrSurveyID = self.request.get("vstrSurveyID")

                findRequest = Surveys.query(Surveys.strSurveyID == vstrSurveyID)
                thisSurveyList = findRequest.fetch()

                if len(thisSurveyList) > 0:
                    thisSurvey = thisSurveyList[0]

                    if int(vstrAvailableCredit) >= int(vstrCreditToAssign):
                        thisSurvey.writeAssignedCredit(strinput=vstrCreditToAssign)

                        thisSurvey.writeRunFromCredit(strinput=True)
                        thisSurvey.writeSurveyIsPaid(strinput=True)
                        thisSurvey.writeSurveyStatus(strinput="Scheduled")

                        thisSurvey.put()

                        findRequest = SurveyAccount.query(SurveyAccount.strOrganizationID == thisSurvey.organization_id)
                        thisSurveyAccountList = findRequest.fetch()

                        vstrAvailableCredit = int(vstrAvailableCredit) - int(vstrCreditToAssign)

                        if len(thisSurveyAccountList) > 0:
                            thisSurveyAccount =  thisSurveyAccountList[0]
                            thisSurveyAccount.writeTotalCredits(strinput=vstrAvailableCredit)
                            thisSurveyAccount.put()

                            #TODO- find a way to check if the scheduled date and time is in the feature if not set it in the feature and inform the user of this on the email
                            #TODO- Send an email informing the user that the survey will start running as scheduled
                            #TODO- send an SMS to the user informing them that their survey will run
                            self.response.write("Successfully assigned available credit to Survey")
                        else:
                            self.response.write("Error assiging available Credit")
                    else:
                        self.response.write("Error Insufficient Credit")
                else:
                    self.response.write("Fatal Error Survey not found")


class ThisSurveyContactsListHandler(webapp2.RequestHandler):

    

    def get(self):
        URL = self.request.url
        strURLlist = URL.split("/")
        strListID = strURLlist[len(strURLlist) - 1]

        findRequest = SurveyContactLists.query(SurveyContactLists.strListID == strListID)
        thisSurveyContactList = findRequest.fetch()

        if len(thisSurveyContactList) > 0:
            thisSurveyConList = thisSurveyContactList[0]
        else:
            thisSurveyConList = SurveyContactLists()

        findRequest = SurveyContacts.query(SurveyContacts.strListID == strListID)
        thisContactList = findRequest.fetch()


        template = template_env.get_template('templates/surveys/contacts/thiscontactlist.html')
        context = {'thisSurveyConList':thisSurveyConList,'thisContactList':thisContactList}
        self.response.write(template.render(context))

    def post(self):

        vstrChoice = self.request.get('vstrChoice')
        if vstrChoice == "0":

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrListID = self.request.get('vstrListID')

                findRequest = SurveyContacts.query(SurveyContacts.strListID == vstrListID)
                thisContactList = findRequest.fetch()

                template = template_env.get_template('templates/surveys/contacts/sublist.html')
                context = {'thisContactList':thisContactList,'vstrListID':vstrListID}
                self.response.write(template.render(context))

        elif vstrChoice == "1":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrListID = self.request.get('vstrListID')
                vstrName = self.request.get('vstrNames')
                vstrName = vstrName.strip()
                vstrSurname = self.request.get('vstrSurname')
                vstrSurname = vstrSurname.strip()
                vstrCell = self.request.get('vstrCellNumber')
                vstrCell = vstrCell.strip()
                if not(vstrCell == None) and ((len(vstrCell) == 10) or (len(vstrCell) == 13)):
                    findRequest = SurveyContacts.query(SurveyContacts.strListID == vstrListID,SurveyContacts.strCell == vstrCell)
                    thisContactList = findRequest.fetch()

                    if len(thisContactList) > 0:
                        ThisContact = thisContactList[0]
                    else:
                        ThisContact = SurveyContacts()
                        ThisContact.writeContactID(strinput=ThisContact.CreateContactID())
                        ThisContact.writeListID(strinput=vstrListID)

                    ThisContact.writeName(strinput=vstrName)
                    ThisContact.writeSurname(strinput=vstrSurname)
                    ThisContact.writeCell(strinput=vstrCell)
                    ThisContact.put()
                    findRequest = SurveyContactLists.query(SurveyContactLists.strListID == vstrListID)
                    thisSurveyConList = findRequest.fetch()
                    if len(thisSurveyConList) > 0:
                        thisSurveyList = thisSurveyConList[0]

                        thisSurveyList.strTotal += 1
                        thisSurveyList.put()

                    self.response.write("Survey Contact Successfully loaded")
                else:
                    self.response.write("Please enter a valid cell phone number")

        #Bulk Upload Contact Lists
        elif vstrChoice == "2":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrContacts = self.request.get('vstrContacts')
                vstrListID = self.request.get('vstrListID')

                strContactList = vstrContacts.split("|")
                strTotalLoaded = 0
                for thisContact in strContactList:
                    try:
                        if len(thisContact) > 0:
                            strSplitContact = thisContact.split(',')
                            if len(strSplitContact) == 3:
                                strCell = strSplitContact[0]
                                strCell = strCell.strip()
                                strNames = strSplitContact[1]
                                strNames = strNames.strip()
                                strSurname = strSplitContact[2]
                                strSurname = strSurname.strip()
                                if not(strCell == None) and ((len(strCell) == 10) or (len(strCell) == 13)):
                                    findRequest = SurveyContacts.query(SurveyContacts.strListID == vstrListID,SurveyContacts.strCell == strCell)
                                    thisSurveyConList = findRequest.fetch()
                                    if len(thisSurveyConList) > 0:
                                        thisSurveyCon = thisSurveyConList[0]
                                    else:
                                        thisSurveyCon = SurveyContacts()
                                        thisSurveyCon.writeListID(strinput=vstrListID)
                                        thisSurveyCon.writeContactID(strinput=thisSurveyCon.CreateContactID())

                                    thisSurveyCon.writeCell(strinput=strCell)
                                    thisSurveyCon.writeName(strinput=strNames)
                                    thisSurveyCon.writeSurname(strinput=strSurname)
                                    thisSurveyCon.put()
                                    strTotalLoaded += 1
                                    self.response.write("""Contact Loaded : <strong>""" + thisContact + """</strong> <br> """)
                    except:
                        pass

                findRequest = SurveyContactLists.query(SurveyContactLists.strListID == vstrListID)
                thisContactLister = findRequest.fetch()

                if len(thisContactLister) > 0:
                    thisConLister = thisContactLister[0]
                    thisConLister.strTotal += strTotalLoaded
                    thisConLister.put()

                if strTotalLoaded == 0:
                    self.response.write("Failure while loading you contacts please check your cell numbers")

        #Bulk Remove Contact List
        elif vstrChoice == "3":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrListID = self.request.get('vstrListID')
                vstrListID = vstrListID.strip()
                vstrRemoveCell =self.request.get('vstrRemoveCell')
                vstrRemoveCell = vstrRemoveCell.strip()

                findRequest = SurveyContacts.query(SurveyContacts.strCell == vstrRemoveCell,SurveyContacts.strListID == vstrListID)
                thisSurveyContactsList = findRequest.fetch()

                isDel = False
                strTotalRemoved = 0
                for thisContact in thisSurveyContactsList:
                    thisContact.key.delete()
                    isDel = True
                    strTotalRemoved += 1

                findRequest = SurveyContactLists.query(SurveyContactLists.strListID == vstrListID)
                thisContactLister = findRequest.fetch()

                if len(thisContactLister) > 0:
                    thisConLister = thisContactLister[0]
                    thisConLister.strTotal = thisConLister.strTotal - strTotalRemoved
                    thisConLister.put()

                if isDel:
                    self.response.write("Survey Contact Deleted Successfully")
                else:
                    self.response.write("Survey Contact not found / Already Deleted")


class ThisSchedulesHandler(webapp2.RequestHandler):

    

    def get(self):

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken

            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrSurveyID = self.request.get('vstrSurveyID')
                vstrListID = self.request.get('vstrContactList')
                vstrName = self.request.get('vstrName')
                vstrName = vstrName.strip()
                vstrDescription = self.request.get('vstrDescription')
                vstrDescription = vstrDescription.strip()
                vstrStartDate = self.request.get('vstrStartDate')
                vstrStartTime = self.request.get('vstrStartTime')
                vstrNotifyOnStart = self.request.get('vstrNotifyOnStart')
                if vstrNotifyOnStart == "YES":
                    vstrNotifyOnStart = True
                else:
                    vstrNotifyOnStart = False
                vstrNotifyOnEnd = self.request.get('vstrNotifyOnEnd')
                if vstrNotifyOnEnd == "YES":
                    vstrNotifyOnEnd = True
                else:
                    vstrNotifyOnEnd = False


                try:
                    strStartDateList = vstrStartDate.split("/")
                    strMonth = strStartDateList[0]
                    strDay = strStartDateList[1]
                    strYear = strStartDateList[2]


                    strThisStartDate = datetime.date(year=int(strYear),month=int(strMonth),day=int(strDay))
                except:
                    strThisStartDate = datetime.datetime.now()
                    strThisStartDate += datetime.timedelta(days=1)
                    strThisStartDate = strThisStartDate.date()


                try:
                    strStartTimeList = vstrStartTime.split(" ")
                    strThisTime = strStartTimeList[0]
                    strThisTimeList = strThisTime.split(":")
                    strHour = strThisTimeList[0]
                    strMinute = strThisTimeList[1]

                    strDayString = strStartTimeList[1]
                    if strDayString == "PM":
                        strHour = 12 + int(strHour)

                    strThisTime = datetime.time(hour=int(strHour),minute=int(strMinute),second=0)
                except:
                    strThisTime = datetime.datetime.now()
                    strThisTime = datetime.time(hour=strThisTime.hour,minute=strThisTime.minute,second=strThisTime.second)

                findRequest = SurveySchedules.query(SurveySchedules.strSurveyID == vstrSurveyID, SurveySchedules.strName == vstrName)
                thisSurveySchedulesList = findRequest.fetch()
                if len(thisSurveySchedulesList) > 0:
                    self.response.write("Survey Schedule Already Created please just edit the schedule")
                else:
                    thisSurveySchedule = SurveySchedules()
                    thisSurveySchedule.writeUserID(strinput=vstrUserID)
                    thisSurveySchedule.writeListID(strinput=vstrListID)
                    thisSurveySchedule.writeSurveyID(strinput=vstrSurveyID)
                    thisSurveySchedule.writeName(strinput=vstrName)
                    thisSurveySchedule.writeDescription(strinput=vstrDescription)
                    thisSurveySchedule.writeNotifyOnStart(vstrNotifyOnStart)
                    thisSurveySchedule.writeNotifyOnEnd(strinput=vstrNotifyOnEnd)
                    thisSurveySchedule.writeStartDate(strinput=strThisStartDate)
                    thisSurveySchedule.writeStartTime(strinput=strThisTime)
                    thisSurveySchedule.writeScheduleID(strinput=thisSurveySchedule.CreateScheduleID())
                    thisSurveySchedule.writeActivateSchedule(strinput=True)
                    thisSurveySchedule.put()
                    self.response.write("Survey Schedule Successfully uploaded and activated")


class ThisPaymentHandler(webapp2.RequestHandler):


    def get(self):
        URL =self.request.url
        strURLlist = URL.split("/")
        strOrderID = strURLlist[len(strURLlist) - 1]

        findRequest = SurveyOrders.query(SurveyOrders.strOrderID == strOrderID)
        thisOrdersList = findRequest.fetch()

        if len(thisOrdersList) > 0:
            thisOrder = thisOrdersList[0]

            template = template_env.get_template('templates/surveys/orders/makepayment.html')
            context = {'thisOrder':thisOrder,'strSurveyID':thisOrder.strSurveyID}
            self.response.write(template.render(context))

    def post(self):
        from accounts import Organization
        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrSurveyID = self.request.get('vstrSurveyID')
                vstrOrderID = self.request.get('vstrOrderID')
                findRequest = SurveyOrders.query(SurveyOrders.strOrderID == vstrOrderID)
                thisOrderList = findRequest.fetch()
                if len(thisOrderList) > 0:
                    thisOrder = thisOrderList[0]
                    template = template_env.get_template('templates/surveys/orders/subPayment.html')
                    context = {'thisOrder':thisOrder}
                    self.response.write(template.render(context))


        elif vstrChoice == "1":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrDepositAmount = self.request.get('vstrDepositAmount')
                vstrDepositMethod = self.request.get('vstrDepositMethod')
                vstrSurveyID = self.request.get('vstrSurveyID')
                vstrOrderID = self.request.get('vstrOrderID')

                findRequest = SurveyOrders.query(SurveyOrders.strOrderID == vstrOrderID)
                thisSurveyOrdersList = findRequest.fetch()

                if len(thisSurveyOrdersList) > 0:
                    thisSurveyOrder = thisSurveyOrdersList[0]


                    if int(vstrDepositAmount) > 0:

                        vstrThisDate = datetime.datetime.now()
                        strThisDate = vstrThisDate.date()
                        strThisTime = datetime.time(hour=vstrThisDate.hour,minute=vstrThisDate.minute,second=vstrThisDate.second)

                        thisPayment = SurveyPayments()

                        thisPayment.writeUserID(strinput=vstrUserID)
                        thisPayment.writeOrderID(strinput=thisSurveyOrder.strOrderID)
                        thisPayment.writeOrganizationID(strinput=thisSurveyOrder.organization_id)
                        thisPayment.writeDepositReference(strinput=thisSurveyOrder.strDepositReference)
                        thisPayment.writePaymentID(strinput=thisPayment.CreatePaymentID())
                        thisPayment.writeAmountPaid(strinput=vstrDepositAmount)
                        thisPayment.writePaymentMethod(strinput=vstrDepositMethod)
                        thisPayment.writeDatePaid(strinput=strThisDate)
                        thisPayment.writeTimePaid(strinput=strThisTime)
                        thisPayment.writePaymentVerified(strinput=False)
                        thisPayment.put()
                        self.response.write("""
                        Payment request Successfully generated please <a href="/surveys/invoices/"""+ thisPayment.strPaymentID + """">click here to print your invoice</a>                        
                        """)

class ThisInvoicesHandler(webapp2.RequestHandler):
    def get(self):

        from accounts import Organization

        URL = self.request.url
        strURLlist = URL.split("/")
        strPaymentID = strURLlist[len(strURLlist) - 1]

        findRequest = SurveyPayments.query(SurveyPayments.strPaymentID == strPaymentID)
        thisSurveyPaymentList = findRequest.fetch()

        if len(thisSurveyPaymentList) > 0:
            thisPayment = thisSurveyPaymentList[0]

            findRequest = Organization.query(Organization.strOrganizationID == thisPayment.organization_id)
            thisOrgList = findRequest.fetch()
            if len(thisOrgList) > 0:
                thisOrg = thisOrgList[0]
            else:
                thisOrg = Organization()

            findRequest = SurveyOrders.query(SurveyOrders.strOrderID == thisPayment.strOrderID)
            thisOrdersList = findRequest.fetch()

            if len(thisOrdersList) > 0:
                thisOrder = thisOrdersList[0]

                findRequest = Surveys.query(Surveys.strSurveyID == thisOrder.strSurveyID)
                thisSurveyList = findRequest.fetch()

                if len(thisSurveyList) > 0:
                    thisSurvey = thisSurveyList[0]
                else:
                    thisSurvey = Surveys()


                template = template_env.get_template('templates/surveys/orders/directdeposit.html')
                context = {'thisOrg':thisOrg,'thisPayment':thisPayment,'thisSurvey':thisSurvey}
                self.response.write(template.render(context))


class ThisSurveyScheduleHandler(webapp2.RequestHandler):
    def get(self):
        URL = self.request.url
        strURLlist = URL.split("/")
        strScheduleID = strURLlist[len(strURLlist) - 1]

        findRequest = SurveySchedules.query(SurveySchedules.strScheduleID == strScheduleID)
        thisSurveyScheduleList = findRequest.fetch()

        if len(thisSurveyScheduleList) > 0:
            thisSchedule = thisSurveyScheduleList[0]
        else:
            thisSchedule = SurveySchedules()

        template = template_env.get_template('templates/surveys/schedules/thisSchedule.html')
        context = {'thisSchedule':thisSchedule}
        self.response.write(template.render(context))

    def post(self):

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                vstrScheduleID = self.request.get('vstrScheduleID')

                findRequest = SurveySchedules.query(SurveySchedules.strScheduleID == vstrScheduleID)
                thisSurveyScheduleList = findRequest.fetch()

                if len(thisSurveyScheduleList) > 0:
                    thisSchedule = thisSurveyScheduleList[0]
                else:
                    thisSchedule = SurveySchedules()

                template = template_env.get_template('templates/surveys/schedules/subSchedule.html')
                context = {'thisSchedule':thisSchedule}
                self.response.write(template.render(context))

        elif vstrChoice == "1":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrScheduleID = self.request.get('vstrScheduleID')
                vstrName = self.request.get('vstrName')
                vstrDescription = self.request.get('vstrDescription')
                vstrStartDate = self.request.get('vstrStartDate')
                vstrStartTime = self.request.get('vstrStartTime')
                vstrNotifyOnStart = self.request.get('vstrNotifyOnStart')
                vstrNotifyOnEnd = self.request.get('vstrNotifyOnEnd')
                vstrActivateSchedule = self.request.get('vstrActivateSchedule')


                try:
                    if vstrNotifyOnStart == "YES":
                        vstrNotifyOnStart = True
                    else:
                        vstrNotifyOnStart = False

                    if vstrNotifyOnEnd == "YES":
                        vstrNotifyOnEnd = True
                    else:
                        vstrNotifyOnEnd = False

                    if vstrActivateSchedule == "YES":
                        vstrActivateSchedule = True
                    else:
                        vstrActivateSchedule = False


                    vstrStartDateList = vstrStartDate.split("-")
                    vstrYear = vstrStartDateList[0]
                    vstrMonth = vstrStartDateList[1]
                    vstrDay = vstrStartDateList[2]

                    vstrTimeList = vstrStartTime.split(":")
                    vstrHour = vstrTimeList[0]
                    vstrMinute = vstrTimeList[1]
                    vstrSecond = vstrTimeList[2]

                    thisDate = datetime.date(year=int(vstrYear),month=int(vstrMonth),day=int(vstrDay))
                    thisTime = datetime.time(hour=int(vstrHour),minute=int(vstrMinute),second=int(vstrSecond))

                    findRequest = SurveySchedules.query(SurveySchedules.strScheduleID == vstrScheduleID)
                    thisSurveyScheduleList = findRequest.fetch()

                    if len(thisSurveyScheduleList) > 0:
                        thisSchedule = thisSurveyScheduleList[0]

                        thisSchedule.writeStartTime(strinput=thisTime)
                        thisSchedule.writeStartDate(strinput=thisDate)
                        thisSchedule.writeNotifyOnStart(strinput=vstrNotifyOnStart)
                        thisSchedule.writeNotifyOnEnd(strinput=vstrNotifyOnEnd)
                        thisSchedule.writeName(strinput=vstrName)
                        thisSchedule.writeDescription(strinput=vstrDescription)
                        thisSchedule.writeActivateSchedule(strinput=vstrActivateSchedule )
                        thisSchedule.put()
                        self.response.write("Successfully update schedule")
                    else:
                        self.response.write("Error Unable to find your schedule")
                except:
                    self.response.write("There was an error with your input please rectify the error and try again")

        elif vstrChoice == "2":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrScheduleID = self.request.get('vstrScheduleID')

                findRequest = SurveySchedules.query(SurveySchedules.strScheduleID == vstrScheduleID)
                thisScheduleList = findRequest.fetch()

                for thisSchedule in thisScheduleList:
                    findRequest = SurveyOrders.query(SurveyOrders.strScheduleID == thisSchedule.strScheduleID)
                    thisOrdersList = findRequest.fetch()
                    if len(thisOrdersList) > 0:
                        self.response.write("Schedule cannot be deleted as there are orders based on the schedule")
                    else:
                        thisSchedule.key.delete()
                        self.response.write("Schedule Deleted successfully")


class ThisTopUpInvoiceHandler(webapp2.RequestHandler):
    def get(self):
        from accounts import Organization

        URL = self.request.url
        strURLlist = URL.split("/")
        strTopUpReference = strURLlist[len(strURLlist) - 1]

        findRequest = SurveyAccount.query(SurveyAccount.strTopUpReference == strTopUpReference)
        thisSurveyAccountList = findRequest.fetch()

        logging.info("INVOICE HANDLER RUNNING ............")

        if len(thisSurveyAccountList) > 0:
            thisSurveyAccount = thisSurveyAccountList[0]

            findRequest = Organization.query(Organization.strOrganizationID == thisSurveyAccount.organization_id)
            thisOrgList = findRequest.fetch()
            if len(thisOrgList) > 0:
                thisOrg = thisOrgList[0]
            else:
                thisOrg =Organization()

            findRequest = AccountDetails.query()
            thisBluetITAccountList = findRequest.fetch()

            if len(thisBluetITAccountList) > 0:
                thisBlueITAccount = thisBluetITAccountList[0]
            else:
                thisBlueITAccount = AccountDetails()

            template = template_env.get_template("templates/surveys/sub/topupproforma.html")
            context = {'thisOrg':thisOrg,'thisSurveyAccount':thisSurveyAccount,'thisBlueITAccount':thisBlueITAccount}
            self.response.write(template.render(context))

    def post(self):
        from dashboard import TopUpVerifications

        vstrChoice = self.request.get('vstrChoice')


        if vstrChoice == "0":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrTopUpReference = self.request.get("vstrTopUpReference")
                vstrYourReferenceNumber = self.request.get("vstrYourReferenceNumber")
                vstrDepositSlipFile = self.request.get("vstrDepositSlipFile")

                findRequest = SurveyAccount.query(SurveyAccount.strOrganizationID == thisMainAccount.organization_id)
                thisSurveyAccountList = findRequest.fetch()

                if len(thisSurveyAccountList) > 0:
                    thisSurveyAccount = thisSurveyAccountList[0]
                    if vstrYourReferenceNumber == vstrTopUpReference:
                        thisSurveyAccount.writeDepositSlipFilename(strinput=vstrDepositSlipFile)
                        thisSurveyAccount.put()
                        thisVerifications = TopUpVerifications()
                        thisVerifications.writeOrganizationID(strinput=thisSurveyAccount.organization_id)
                        thisVerifications.writeAccountName(strinput="Surveys")
                        thisVerifications.writeCreditAmount(strinput=thisSurveyAccount.strTotalTopUpCost)
                        thisVerifications.writeDepositSlipFileName(strinput=vstrDepositSlipFile)
                        thisVerifications.writeSMSCredits(strinput=thisSurveyAccount.strTopUpCredit)
                        thisVerifications.writeTopUpReference(strinput=vstrYourReferenceNumber)
                        thisVerifications.put()

                        self.response.write("Successfully Uploaded Deposit slip file : " + vstrDepositSlipFile)
                    else:
                        thisSurveyAccount.writeDepositSlipFilename(strinput=vstrDepositSlipFile)
                        thisSurveyAccount.put()
                        thisVerifications = TopUpVerifications()
                        thisVerifications.writeOrganizationID(strinput=thisSurveyAccount.organization_id)
                        thisVerifications.writeAccountName(strinput="Surveys")
                        thisVerifications.writeCreditAmount(strinput=thisSurveyAccount.strTotalTopUpCost)
                        thisVerifications.writeDepositSlipFileName(strinput=vstrDepositSlipFile)
                        thisVerifications.writeSMSCredits(strinput=thisSurveyAccount.strTopUpCredit)
                        thisVerifications.writeTopUpReference(strinput=vstrTopUpReference)
                        thisVerifications.put()

                        self.response.write("Reference Verification Error, deposit will take longer to verify please use our support tickets to enquire if it takes more than three days")

app = webapp2.WSGIApplication([
    ('/surveys', SurveyHandler),
    ('/surveys/manage/.*', ThisSurveyHandler),
    ('/surveys/contacts/.*', ThisSurveyContactsListHandler),
    ('/surveys/schedules', ThisSchedulesHandler),
    ('/surveys/schedules/.*', ThisSurveyScheduleHandler),
    ('/surveys/payments/.*', ThisPaymentHandler),
    ('/surveys/invoices/.*', ThisInvoicesHandler),
    ('/surveys/topup/invoice/.*', ThisTopUpInvoiceHandler)

], debug=True)

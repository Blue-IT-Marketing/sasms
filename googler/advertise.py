import os
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users


import logging
import datetime
from google.appengine.api import app_identity

from accounts import Accounts
from dashboard import AccountDetails
from errormessages import MyErrors
from mysms import SMSPortalBudget

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


class OurContacts(ndb.Expando):
    """
        This are system contacts uploaded by Blue IT Marketing from the dashboard
        ref is the message reference
    """
    strContactID = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()

    strEmail = ndb.StringProperty()

    def CreateContactID(self):
        import random,string
        try:
            strContactID = ""
            for i in range(256):
                strContactID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strContactID
        except:
            return None
    def writeOurContactID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strContactID = strinput
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
######################################################################
######################################################################
################Surveys and Adverts ##################################
######################################################################
######################################################################

class AddAccount(ndb.Expando):
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
    strTopUpInvoiceLink = ndb.StringProperty(default="/adverts/topup/invoice/")
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
                self.strTopUpInvoiceLink = "/adverts/topup/invoice/" +  strinput
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
            if strinput.isdigit():
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
            if strinput.isdigit():
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

class Advert(ndb.Expando):
    strUserID = ndb.StringProperty()
    strOrganizationID = ndb.StringProperty()

    strAccountID = ndb.StringProperty()
    strAdvertID = ndb.StringProperty()

    strAdvert = ndb.StringProperty()
    strAdvertSize = ndb.IntegerProperty(default=1)

    strDateCreated = ndb.DateProperty(auto_now_add=True)
    strTimeCreated = ndb.TimeProperty(auto_now_add=True)

    strStartDate = ndb.DateProperty()
    strStartTime = ndb.TimeProperty()

    strAdvertStatus = ndb.StringProperty(default="Scheduled") # Running, Completed, Scheduled
    strAdvertIsPaid = ndb.BooleanProperty(default=False)

    strAssignedCredit = ndb.IntegerProperty(default=0)
    strRunFromCredit = ndb.BooleanProperty(default=False)

    strUsePortal = ndb.StringProperty(default="Budget") # ClickSend Twilio Vodacom


    def writeUsePortal(self,strinput):
        try:
            strinput = str(strinput)

            if strinput != None:
                self.strUsePortal = strinput
                return True
            else:
                return False
        except:
            return False


    def writeAssignedCredit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strAssignedCredit += int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeAdvertSize(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAdvertSize = int(strinput)
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
    def writeAdvertID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAdvertID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateAdvertID(self):
        import random,string
        try:
            strAdvertID = ""
            for i in range(256):
                strAdvertID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strAdvertID
        except:
            return None
    def writeAdvert(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAdvert = strinput
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
    def writeAdvertStatus(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ["Scheduled","Running","Completed"]:
                self.strAdvertStatus = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAdvertIsPaid(self,strinput):
        try:
            if strinput in [True,False]:
                self.strAdvertIsPaid = strinput
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

class Stats(ndb.Expando):
    """
        TODO- Order ID was not originally included make sure it is included in all places
    """
    strAdvertID = ndb.StringProperty()
    strOrderID = ndb.StringProperty()
    strTotalSent = ndb.IntegerProperty(default=0)
    strTotalRemaining = ndb.IntegerProperty(default=0)
    strTotalResponses = ndb.IntegerProperty(default=0)
    strNoResponse = ndb.IntegerProperty(default=0)


    def writeAdvertID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAdvertID = strinput
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

    def writeTotalSent(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalSent = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeTotalRemaining(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalRemaining = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeNoResponses(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strNoResponse = int(strinput)
                return True
            else:
                return False
        except:
            return False

class Responses(ndb.Expando):
    """
        Use the Sent Report Class to obtain references for sent messages
        and then populate this class with all messages that were actually sent
    """
    strAdvertID = ndb.StringProperty()
    strRef = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strResponse = ndb.StringProperty()
    strDateReceived = ndb.DateProperty(auto_now_add=True)
    strTimeReceived = ndb.TimeProperty(auto_now_add=True)

    def writeAdvertID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAdvertID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strRef = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateReference(self):
        import random,string
        try:
            strReference = ""
            for i in range(255):
                strReference += random.SystemRandom().choice(string.digits + string.ascii_lowercase)
            return strReference
        except:
            return None
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

    def writeResponse(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strResponse = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateReceived(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateReceived = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeReceived(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeReceived = strinput
                return True
            else:
                return False
        except:
            return False

class SentReport(ndb.Expando):
    strReportID = ndb.StringProperty()
    strAdvertID = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strRef = ndb.StringProperty() # Message Reference for getting back a response
    strOrderID = ndb.StringProperty()
    strDateSent = ndb.DateProperty(auto_now_add=True)
    strTimeSent = ndb.TimeProperty(auto_now_add=True)
    strAdvertSent = ndb.BooleanProperty(default=True)
    strMessageStatus = ndb.StringProperty(default="Sent") # Delivered, Undelivered
    strReportDone = ndb.BooleanProperty(default=False)
    strResponseChecked = ndb.BooleanProperty(default=False)

    strPortalUsed = ndb.StringProperty(default="Budget") # Twilio ClickSend Vodacom

    def writePortalUsed(self,strinput):
        try:
            strinput = str(strinput)
            strinput = strinput.strip()
            strinput = strinput.capitalize()
            if strinput in ["Budget","Twilio","ClickSend","Vodacom"]:
                self.strPortalUsed = strinput
                return True
            else:
                return False
        except:
            return False


    def writeAdvertID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAdvertID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeReportID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strReportID = strinput
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
    def writeDateSent(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateSent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeSent(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeSent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAdvertSent(self,strinput):
        try:
            if strinput in [True,False]:
                self.strAdvertSent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMessageStatus(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMessageStatus = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMessageReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strRef = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateReportID(self):
        import random,string
        try:
            strReportID = ""
            for i in range(256):
                strReportID += random.SystemRandom().choice(string.digits + string.ascii_lowercase)
            return strReportID
        except:
            return None

    def writeReportDone(self,strinput):
        try:
            if strinput in [True,False]:
                self.strReportDone = strinput
                return True
            else:
                return False
        except:
            return False

    def writeResponseChecked(self,strinput):
        try:
            if strinput in [True,False]:
                self.strResponseChecked = strinput
                return True
            else:
                return False
        except:
            return False

class AdvertPackages(ndb.Expando):
    strPackageID = ndb.StringProperty()
    strName = ndb.StringProperty()
    strDescription = ndb.StringProperty()
    strTotalCredits = ndb.IntegerProperty(default=1000)
    strPrice = ndb.IntegerProperty(default=350)


    def writePackageID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPackageID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreatePackageID(self):
        import string,random
        try:
            strPackageID = ""
            for i in range(256):
                strPackageID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)

            return strPackageID
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
    def writeTotalCredits(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTotalCredits = strinput
                return True
            else:
                return False

        except:
            return False
    def writePrice(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strPrice = int(strinput)
                return True
            else:
                return False
        except:
            return False

class Orders(ndb.Expando):
    """
        #RunOrder Activated by an auto payment system or by admin on manual deposit reference verification, once activated the order will start running
    """
    strUserID = ndb.StringProperty()
    strOrganizationID = ndb.StringProperty()
    strAdvertID = ndb.StringProperty()
    strItemCount = ndb.IntegerProperty(default=0)
    strOrderID = ndb.StringProperty()
    strTotalSMS = ndb.IntegerProperty(default=0)
    strQoutedAmount = ndb.IntegerProperty(default=0)
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
    def writeAdvertID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAdvertID = strinput
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

class Payments(ndb.Expando):
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


from firebaseadmin import VerifyAndReturnAccount


class AdvertiseHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/advertise/advertise.html')
        context = {}
        self.response.write(template.render(context))

    def post(self):

        from mysms import SMSPortalBudget
        from accounts import Organization

        vstrChoice  = self.request.get('vstrChoice')

        if vstrChoice == "0":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                if thisMainAccount.verified:
                    findRequest = AddAccount.query(AddAccount.strOrganizationID == thisMainAccount.organization_id)
                    thisAddAccountList = findRequest.fetch()

                    if len(thisAddAccountList) > 0:
                        thisAddAccount = thisAddAccountList[0]
                    else:
                        thisAddAccount = AddAccount()

                    template = template_env.get_template('templates/advertise/sub/account.html')
                    context = {'thisAddAccount':thisAddAccount}
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

        elif vstrChoice == "1":

            vstrNames = self.request.get('vstrNames')
            vstrSurname = self.request.get('vstrSurname')
            vstrCell = self.request.get('vstrCell')
            vstrTel = self.request.get('vstrTel')

            vstrWebsite = self.request.get('vstrWebsite')

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = AddAccount.query(AddAccount.strOrganizationID == thisMainAccount.organization_id)
                thisAddAccountList = findRequest.fetch()

                if len(thisAddAccountList) > 0:
                    thisAddAccount = thisAddAccountList[0]
                else:
                    thisAddAccount = AddAccount()
                thisAddAccount.writeUserID(strinput=vstrUserID)
                thisAddAccount.writeAccountID(strinput=thisAddAccount.CreateAccountID())
                thisAddAccount.writeOrganizationID(strinput=thisMainAccount.organization_id)
                thisAddAccount.writeNames(strinput=vstrNames)
                thisAddAccount.writeCell(strinput=vstrCell)
                thisAddAccount.writeEmail(strinput=vstrEmail)
                thisAddAccount.writeSurname(strinput=vstrSurname)
                thisAddAccount.writeWebsite(strinput=vstrWebsite)
                thisAddAccount.put()

                self.response.write("Account details saved successfully")

        elif vstrChoice == "2":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                if thisMainAccount.verified:

                    findRequest = Advert.query(Advert.strOrganizationID == thisMainAccount.organization_id)
                    thisAdvertList = findRequest.fetch()

                    template = template_env.get_template('templates/advertise/sub/adverts.html')
                    context = {'thisAdvertList':thisAdvertList}
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
        elif vstrChoice == "3":
            vstrAdvert = self.request.get('vstrAdvert')
            vstrPackage = self.request.get('vstrPackage')
            vstrStartDate = self.request.get('vstrStartDate')
            vstrStartTime = self.request.get('vstrStartTime')
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

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

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = AddAccount.query(AddAccount.strOrganizationID == thisMainAccount.organization_id)
                thisAddAccountList = findRequest.fetch()

                if len(thisAddAccountList) > 0:
                    thisAddAccount = thisAddAccountList[0]

                    thisAdvert = Advert()
                    thisAdvert.writeUserID(strinput=vstrUserID)
                    thisAdvert.writeAccountID(strinput=thisAddAccount.strAccountID)
                    thisAdvert.writeOrganizationID(strinput=thisAddAccount.organization_id)
                    thisAdvert.writeAdvertID(strinput=thisAdvert.CreateAdvertID())
                    thisAdvert.writeAdvert(strinput=vstrAdvert)
                    thisAdvert.writeStartDate(strinput=strThisStartDate)
                    thisAdvert.writeStartTime(strinput=strThisTime)
                    thisAdvert.writeAdvertStatus(strinput="Scheduled")

                    thisAdvert.put()

                    thisStats = Stats()
                    thisStats.writeAdvertID(strinput=thisAdvert.strAdvertID)
                    thisStats.writeTotalRemaining(strinput=str(vstrPackage))
                    thisStats.put()

                    findRequest = SMSPortalBudget.query()
                    thisBudgetPortalList = findRequest.fetch()

                    if len(thisBudgetPortalList) > 0:
                        thisBudget = thisBudgetPortalList[0]
                    else:
                        thisBudget = SMSPortalBudget()

                    thisOrder = Orders()
                    thisOrder.writeUserID(strinput=vstrUserID)
                    thisOrder.writeOrganizationID(strinput=thisAddAccount.organization_id)
                    thisOrder.writeItemCount(strinput=str(1))
                    thisOrder.writeFullyPaid(strinput=False)
                    thisOrder.writeTotalSMS(strinput=vstrPackage)
                    strQuoteAmount = ((thisBudget.strAdvertSellRate * thisOrder.strTotalSMS)/100)

                    thisOrder.writeQuoteAmount(strinput=strQuoteAmount)
                    thisOrder.writeOrderID(strinput=thisOrder.CreateOrderID())
                    thisOrder.writeAdvertID(strinput=thisAdvert.strAdvertID)
                    thisOrder.writeOrderStartDate(strinput=strThisStartDate)
                    thisOrder.writeOrderStartTime(strinput=strThisTime)
                    thisOrder.writeOrderCompleted(strinput=False)
                    thisOrder.put()

                    self.response.write("Successfully created advert please open Orders to pay for your advert in order to enable it to go live")
                else:
                    self.response.write("Unable to create an advert as you do not have an active advertising account")

        elif vstrChoice == "4":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                if thisMainAccount.verified:

                    #TODO- Note that intergrating an advert account allows for granular or more relevant user rights to be created inside the advert account

                    findRequest = Orders.query(Orders.strOrganizationID == thisMainAccount.organization_id, Orders.strFullyPaid == True)
                    thisPaidList = findRequest.fetch()

                    findRequest = Orders.query(Orders.strOrganizationID == thisMainAccount.organization_id, Orders.strFullyPaid == False)
                    thisNewOrdersList = findRequest.fetch()

                    template = template_env.get_template('templates/advertise/sub/orders.html')
                    context = {'thisPaidList':thisPaidList,'thisNewOrdersList':thisNewOrdersList}
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


        elif vstrChoice == "5":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                if thisMainAccount.verified:

                    findRequest = Payments.query(Payments.strOrganizationID == thisMainAccount.organization_id)
                    thisPaymentsList = findRequest.fetch()

                    template = template_env.get_template('templates/advertise/paymethods/invoices.html')
                    context = {'thisPaymentsList':thisPaymentsList}
                    self.response.write(template.render(context))

        elif vstrChoice == "6":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

            vstrAddCredits = self.request.get("vstrAddCredits")
            vstrPaymentMethod = self.request.get("vstrPaymentMethod")
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = AddAccount.query(AddAccount.strOrganizationID == thisMainAccount.organization_id)
                thisAdvertAccountList = findRequest.fetch()

                findRequest = SMSPortalBudget.query()
                thisPortalBudgetList = findRequest.fetch()

                if len(thisPortalBudgetList) > 0:
                    thisPortal = thisPortalBudgetList[0]
                else:
                    thisPortal = SMSPortalBudget()


                if len(thisAdvertAccountList) > 0:
                    thisAdvertAccount = thisAdvertAccountList[0]

                    if vstrPaymentMethod == "DirectDeposit":
                        vstrThisDate = datetime.datetime.now()
                        strThisDate = datetime.date(year=vstrThisDate.year,month=vstrThisDate.month,day=vstrThisDate.day)
                        vstrThisDate += datetime.timedelta(days=30)
                        strPayByDate = datetime.date(year=vstrThisDate.year,month=vstrThisDate.month,day=vstrThisDate.day)
                        strTotalCost = (thisPortal.strAdvertSellRate * int(vstrAddCredits))/100
                        thisAdvertAccount.writeTotalTopUpCost(strinput=strTotalCost)
                        #thisAdvertAccount.writeTotalCredits(strinput=vstrAddCredits)
                        thisAdvertAccount.writeTopUpCredit(strinput=vstrAddCredits) #Will be added to Total Credits on verification of payment
                        logging.info(thisAdvertAccount.strTotalTopUpCost)
                        thisAdvertAccount.writeTopUpReference(strinput=thisAdvertAccount.CreateTopUpReference())
                        thisAdvertAccount.CreateTopUpInvoiceLink(strinput=thisAdvertAccount.strTopUpReference)
                        thisAdvertAccount.writePayByDate(strinput=strPayByDate)
                        thisAdvertAccount.writeDateInvoiceCreated(strinput=strThisDate)
                        thisAdvertAccount.put()
                        findRequest = AddAccount.query(AddAccount.strOrganizationID == thisMainAccount.organization_id)
                        thisAdvertAccountList = findRequest.fetch()
                        if len(thisAdvertAccountList) > 0:
                            thisAdvertAccount = thisAdvertAccountList[0]
                            self.response.write("""
                            Top Up Credit successfully processed please click on this link to view your <strong><a href=" """ + thisAdvertAccount.strTopUpInvoiceLink + """ ">Proforma Invoice</a></strong>
                            """)

        elif vstrChoice == "7":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = Advert.query(Advert.strOrganizationID == thisMainAccount.organization_id)
                thisAdvertsList = findRequest.fetch()
                strTotalAdverts = len(thisAdvertsList)

                findRequest = AddAccount.query(AddAccount.strOrganizationID == thisMainAccount.organization_id)
                thisAdvertiseAccountList = findRequest.fetch()
                if len(thisAdvertiseAccountList) > 0:
                    thisAdvertAccount = thisAdvertiseAccountList[0]
                else:
                    thisAdvertAccount = AddAccount()

                template = template_env.get_template('templates/advertise/sub/advertisesubmenu.html')
                context = {'strTotalAdverts': strTotalAdverts, 'thisAdvertAccount': thisAdvertAccount}
                self.response.write(template.render(context))


class ThisAdvertHandler(webapp2.RequestHandler):
    def get(self):
        URL = self.request.url
        strURLlist = URL.split('/')
        strAdvertID = strURLlist[len(strURLlist) - 1]

        findRequest = Advert.query(Advert.strAdvertID == strAdvertID)
        thisAdvertList = findRequest.fetch()

        if len(thisAdvertList) > 0:
            thisAdvert = thisAdvertList[0]

            findRequest = AddAccount.query(AddAccount.strOrganizationID == thisAdvert.organization_id)
            thisAdvertisingAccountList = findRequest.fetch()

            if len(thisAdvertisingAccountList) > 0:
                thisAdvertAccount = thisAdvertisingAccountList[0]
            else:
                thisAdvertAccount = AddAccount()

            template = template_env.get_template('templates/advertise/sub/AdManager.html')
            context = {'thisAdvert':thisAdvert,'thisAdvertAccount':thisAdvertAccount}
            self.response.write(template.render(context))

    def post(self):
        from accounts import Organization
        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            strAdvertID = self.request.get('vstrAdvertID')

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')


            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = Advert.query(Advert.strAdvertID == strAdvertID)
                thisAdvertList = findRequest.fetch()

                if len(thisAdvertList) > 0:
                    thisAdvert = thisAdvertList[0]
                    findRequest = AddAccount.query(AddAccount.strOrganizationID == thisAdvert.organization_id)
                    thisAdvertAccountList = findRequest.fetch()
                    if len(thisAdvertAccountList) > 0:
                        thisAdvertAccount = thisAdvertAccountList[0]
                    else:
                        thisAdvertAccount = AddAccount()

                    template = template_env.get_template('templates/advertise/manager/advert.html')
                    context = {'thisAdvert':thisAdvert,'thisAdvertAccount':thisAdvertAccount}
                    self.response.write(template.render(context))

        elif vstrChoice == "1":
            vstrAdvertID = self.request.get('vstrAdvertID')
            vstrAdvert = self.request.get('vstrAdvert')
            vstrTotalSMS = self.request.get('vstrTotalSMS')
            vstrStartDate = self.request.get('vstrStartDate')
            vstrStartTime = self.request.get('vstrStartTime')

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                try:
                    if "-" in vstrStartDate:
                        strStartDateList = vstrStartDate.split("-")
                        strMonth = strStartDateList[1]
                        strDay = strStartDateList[2]
                        strYear = strStartDateList[0]

                    else:
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
                    if " " in vstrStartTime:
                        strStartTimeList = vstrStartTime.split(" ")
                        strThisTime = strStartTimeList[0]
                        strThisTimeList = strThisTime.split(":")
                        strHour = strThisTimeList[0]
                        strMinute = strThisTimeList[1]
                    else:
                        strStartTimeList = vstrStartTime.split(":")
                        strHour = strStartTimeList[0]
                        strMinute = strStartTimeList[1]



                    strDayString = strStartTimeList[1]
                    if strDayString == "PM":
                        strHour = 12 + int(strHour)

                    strThisTime = datetime.time(hour=int(strHour),minute=int(strMinute),second=0)
                except:
                    strThisTime = datetime.datetime.now()
                    strThisTime = datetime.time(hour=strThisTime.hour,minute=strThisTime.minute,second=strThisTime.second)

                findRequest = Advert.query(Advert.strAdvertID == vstrAdvertID)
                thisAdvertList = findRequest.fetch()

                if len(thisAdvertList) > 0:
                    thisAdvert = thisAdvertList[0]

                    thisAdvert.writeAdvert(strinput=vstrAdvert)
                    thisAdvert.writeStartDate(strinput=strThisStartDate)
                    thisAdvert.writeStartTime(strinput=strThisTime)
                    thisAdvert.put()
                    self.response.write("Successfully updated Advert")
                else:
                    self.response.write("Fatal Error updating Advert")

        elif vstrChoice == "2":
            vstrAdvertID = self.request.get('vstrAdvertID')

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                findRequest = Stats.query(Stats.strAdvertID == vstrAdvertID)
                thisStatsList = findRequest.fetch()

                if len(thisStatsList) > 0:
                    thisStats = thisStatsList[0]

                else:
                    thisStats = Stats()

                template = template_env.get_template('templates/advertise/manager/MyStatistics.html')
                context = {'thisStats':thisStats}
                self.response.write(template.render(context))

        elif vstrChoice == "3":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')


            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrAdvertID = self.request.get('vstrAdvertID')

                findRequest = Advert.query(Advert.strAdvertID == vstrAdvertID)
                thisAdvertList = findRequest.fetch()

                if len(thisAdvertList) > 0:
                    thisAdvert = thisAdvertList[0]
                else:
                    thisAdvert = Advert()


                if thisAdvert.strAdvertStatus in ["Running","Completed"]:
                    findRequest = Orders.query(Orders.strAdvertID == thisAdvert.strAdvertID)
                    thisOrderList = findRequest.fetch()
                    #TODO-Please finish up the contacts functions allow it to load as many contacts as
                    #TODO-Possible and then start running adverts, also consider adding the contacts list
                    #TODO-on adverts, to make it easier for users to load their own contacts


                findRequest = Responses.query(Responses.strAdvertID == vstrAdvertID)
                thisResponsesList = findRequest.fetch()

                template = template_env.get_template('templates/advertise/responses/advert.html')
                context = {'thisResponsesList':thisResponsesList}
                self.response.write(template.render(context))

        elif vstrChoice == "4":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrAdvertID = self.request.get('vstrAdvertID')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = Orders.query(Orders.strAdvertID == vstrAdvertID)
                thisOrdersList = findRequest.fetch()


                ThisPaymentsList = []
                for thisOrder in thisOrdersList:
                    findRequest = Payments.query(Payments.strOrderID == thisOrder.strOrderID)
                    thisPaymentList = findRequest.fetch()

                    for thisPayment in thisPaymentList:
                        ThisPaymentsList.append(thisPayment)


                findRequest = Orders.query(Orders.strAdvertID == vstrAdvertID,Orders.strFullyPaid == False)
                thisUpaidOrderList = findRequest.fetch()


                findRequest = Advert.query(Advert.strAdvertID == vstrAdvertID)
                thisAdvertList = findRequest.fetch()

                if len(thisAdvertList) > 0:
                    thisAdvert = thisAdvertList[0]


                    findRequest = AddAccount.query(AddAccount.strOrganizationID == thisAdvert.organization_id)
                    thisAdvertAccountList = findRequest.fetch()

                    if len(thisAdvertAccountList) > 0:
                        thisAdvertAccount = thisAdvertAccountList[0]


                    template = template_env.get_template('templates/advertise/manager/payments.html')
                    context = {'ThisPaymentsList':ThisPaymentsList,'thisOrdersList':thisOrdersList,'thisAdvert':thisAdvert,'thisUpaidOrderList':thisUpaidOrderList,'thisAdvertAccount':thisAdvertAccount}
                    self.response.write(template.render(context))

        elif vstrChoice == "5":
            vstrAdvertID = self.request.get('vstrAdvertID')
            vstrPackage = self.request.get('vstrPackage')
            vstrStartDate = self.request.get('vstrStartDate')
            vstrStartTime = self.request.get('vstrStartTime')

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                try:
                    strStartDateList = vstrStartDate.split("/")
                    strMonth = strStartDateList[0]
                    strDay = strStartDateList[1]
                    strYear = strStartDateList[2]

                    strThisStartDate = datetime.date(year=int(strYear), month=int(strMonth), day=int(strDay))
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

                    strThisTime = datetime.time(hour=int(strHour), minute=int(strMinute), second=0)
                except:
                    strThisTime = datetime.datetime.now()
                    strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute, second=strThisTime.second)


                thisOrder = Orders()
                thisOrder.writeUserID(strinput=vstrUserID)
                thisOrder.writeOrganizationID(strinput=thisMainAccount.organization_id)
                thisOrder.writeAdvertID(strinput=vstrAdvertID)
                thisOrder.writeOrderStartDate(strinput=strThisStartDate)
                thisOrder.writeOrderStartTime(strinput=strThisTime)
                thisOrder.writeTotalSMS(strinput=vstrPackage)


                findRequest = SMSPortalBudget.query()
                thisBudgetPortalList = findRequest.fetch()

                if len(thisBudgetPortalList) > 0:
                    thisBudget = thisBudgetPortalList[0]
                else:
                    thisBudget = SMSPortalBudget()

                findRequest = Stats.query(Stats.strAdvertID == vstrAdvertID)
                thisStatList = findRequest.fetch()

                if len(thisStatList) > 0:
                    thisStats = thisStatList[0]
                else:
                    thisStats = Stats()

                #TODO- Investigate the Quotation System the way it is , is not satisfactory there might be bugs here
                strQuoteAmount = ((thisBudget.strAdvertSellRate * thisOrder.strTotalSMS) / 100)
                thisOrder.writeQuoteAmount(strinput=strQuoteAmount)
                thisOrder.writeOrderID(strinput=thisOrder.CreateOrderID())

                thisOrder.writeOrderStartDate(strinput=strThisStartDate)
                thisOrder.writeOrderStartTime(strinput=strThisTime)
                thisOrder.writeOrderCompleted(strinput=False)
                thisOrder.writeItemCount(strinput=str(1))
                thisOrder.put()
                thisStats.writeTotalRemaining(strinput=str(thisStats.strTotalRemaining + int(vstrPackage)))
                thisStats.put()
                self.response.write("Successfully created new order for advert")

        elif vstrChoice == "6":
            vstrAdvertID = self.request.get('vstrAdvertID')
            vstrSelectOrder = self.request.get('vstrSelectOrder')
            vstrPaymentMethod = self.request.get('vstrPaymentMethod')
            vstrTotalCredits = self.request.get('vstrTotalCredits')

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                if vstrPaymentMethod == "Direct Deposit":
                    findRequest = Orders.query(Orders.strOrderID == vstrSelectOrder)
                    thisOrderList = findRequest.fetch()

                    if len(thisOrderList) > 0:
                        thisOrder = thisOrderList[0]
                    else:
                        thisOrder = Orders()

                    thisOrder.writeDepositReference(strinput=thisOrder.CreatedDepositReference())
                    thisOrder.put()

                    findRequest = Advert.query(Advert.strAdvertID == vstrAdvertID)
                    thisAdvertList = findRequest.fetch()

                    if len(thisAdvertList) > 0:
                        thisAdvert = thisAdvertList[0]
                    else:
                        thisAdvert = Advert()

                    findRequest = AccountDetails.query()
                    thisBlueITAccountList = findRequest.fetch()

                    if len(thisBlueITAccountList) > 0:
                        thisBlueITAccount = thisBlueITAccountList[0]
                    else:
                        thisBlueITAccount = AccountDetails()

                    findRequest = Organization.query(Organization.strOrganizationID == thisAdvert.strOrganizationID)
                    thisOrgList = findRequest.fetch()

                    if len(thisOrgList) > 0:
                        thisOrg = thisOrgList[0]
                    else:
                        thisOrg = Organization()

                    findRequest = AddAccount.query(AddAccount.strOrganizationID == thisAdvert.strOrganizationID)
                    thisAdvertAccountList = findRequest.fetch()

                    if len(thisAdvertAccountList) > 0:
                        thisAdvertAccount = thisAdvertAccountList[0]
                    else:
                        thisAdvertAccount = AddAccount()


                    template = template_env.get_template('templates/advertise/sub/OrdersProformaInvoice.html')
                    context = {'thisOrg':thisOrg,'thisOrder':thisOrder,'thisAdvert':thisAdvert,'thisBlueITAccount':thisBlueITAccount,'thisAdvertAccount':thisAdvertAccount}
                    self.response.write(template.render(context))

                elif vstrPaymentMethod == "Available Credit":
                    pass
                #TODO- Please finish up this payment method, please make sure this method of payment works with others

        elif vstrChoice == "7":

            vstrAdvertID = self.request.get('vstrAdvertID')
            vstrOrderID = self.request.get('vstrOrderID')

            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = Orders.query(Orders.strOrderID == vstrOrderID)
                thisOrderList = findRequest.fetch()

                if len(thisOrderList) > 0:
                    thisOrder = thisOrderList[0]
                else:
                    thisOrder = Orders()

                findRequest = Advert.query(Advert.strAdvertID == vstrAdvertID)
                thisAdvertList = findRequest.fetch()

                if len(thisAdvertList) > 0:
                    thisAdvert = thisAdvertList[0]
                else:
                    thisAdvert = Advert()


                findRequest = AccountDetails.query()
                thisDepositAccountList = findRequest.fetch()

                if len(thisDepositAccountList) > 0:
                    thisDepositAccount = thisDepositAccountList[0]
                else:
                    thisDepositAccount = AccountDetails()


                findRequest = SMSPortalBudget.query()
                thisBudgetPortalList = findRequest.fetch()

                if len(thisBudgetPortalList) > 0:
                    thisBudgetPortal = thisBudgetPortalList[0]
                else:
                    thisBudgetPortal = SMSPortalBudget()

                #TODO- Finish up sending message
                vstrMessage = "Business Messaging and Contact Management : " + "%0A"
                vstrDepositAmount = "Deposit Amount : " + "%0A"
                vstrSMSPackage = "SMS Package : " +  "%0A"
                vstrAccountHolder = "Account Holder : " + thisDepositAccount.strAccountHolder + "%0A"
                vstrAccountNumber = "Account Number : " + thisDepositAccount.strAccountNumber + "%0A"
                vstrBankName = "Bank Name : " + thisDepositAccount.strBankName + "%0A"
                vstrBranchName = "Branch Name : " + thisDepositAccount.strBranchName + "%0A"
                vstrBranchCode = "Branch Code : " + thisDepositAccount.strBranchCode + "%0A"
                vstrBanking = vstrAccountHolder + vstrAccountNumber + vstrBankName + vstrBranchName + vstrBranchCode
                vstrReference = "Deposit Reference : " + thisOrder.strDepositReference

                vstrMessage = vstrMessage + vstrDepositAmount + vstrSMSPackage + vstrBanking + vstrReference

                thisBudgetPortal.SendCronMessage(strMessage=vstrMessage, strCell=thisMainAccount.cell)

        elif vstrChoice == "8":
            vstrAdvertID = self.request.get("vstrAdvertID")
            vstrAvailableCredit = self.request.get("vstrAvailableCredit")
            vstrCreditToAssign = self.request.get("vstrCreditToAssign")
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = Advert.query(Advert.strAdvertID == vstrAdvertID)
                thisAdvertList = findRequest.fetch()


                if len(thisAdvertList) > 0:
                    thisAdvert = thisAdvertList[0]
                    if int(vstrAvailableCredit) >= int(vstrCreditToAssign):
                        thisAdvert.writeAssignedCredit(strinput=vstrCreditToAssign)

                        thisAdvert.writeRunFromCredit(strinput=True)
                        thisAdvert.writeAdvertIsPaid(strinput=True)
                        thisAdvert.writeAdvertStatus(strinput="Scheduled")

                        thisAdvert.put()

                        vstrAvailableCredit = int(vstrAvailableCredit) - int(vstrCreditToAssign)
                        findRequest = AddAccount.query(AddAccount.strOrganizationID == thisAdvert.organization_id)
                        thisAdvertAccountList = findRequest.fetch()

                        if len(thisAdvertAccountList) > 0:

                            thisAdvertAccount = thisAdvertAccountList[0]
                            thisAdvertAccount.writeTotalCredits(strinput=vstrAvailableCredit)
                            thisAdvertAccount.put()

                            self.response.write("Successfully assigned available credit to advert")

                        else:
                            self.response.write("Error Assigning Available Credit")
                    else:
                        self.response.write("Error Insufficient available credit")
                else:
                    self.response.write("Fatal Error Advert not found")


class ThisPaymentAdvertHandler(webapp2.RequestHandler):
    def get(self):
        URL = self.request.url
        strURLlist = URL.split("/")
        strOrderID = strURLlist[len(strURLlist) - 1]

        findRequest = Orders.query(Orders.strOrderID == strOrderID)
        thisOrderList = findRequest.fetch()

        if len(thisOrderList) > 0:
            thisOrder = thisOrderList[0]

            findRequest = Advert.query(Advert.strAdvertID == thisOrder.strAdvertID)
            thisAdvertList = findRequest.fetch()

            if len(thisAdvertList) > 0:
                thisAdvert = thisAdvertList[0]

                template = template_env.get_template('templates/advertise/sub/payments.html')
                context = {'thisOrder':thisOrder,'thisAdvert':thisAdvert}
                self.response.write(template.render(context))

class ThisInvoiceHandler(webapp2.RequestHandler):
    def get(self):
        from accounts import Accounts,Organization

        URL = self.request.url
        strURLlist = URL.split("/")
        strPaymentID = strURLlist[len(strURLlist) - 1]

        findRequest = Payments.query(Payments.strPaymentID == strPaymentID)
        thisPaymentList = findRequest.fetch()

        if len(thisPaymentList) > 0:
            thisPayment = thisPaymentList[0]
        else:
            thisPayment = Payments()

        findRequest = Organization.query(Organization.strOrganizationID == thisPayment.strOrganizationID)
        thisOrgList = findRequest.fetch()

        if len(thisOrgList) > 0:
            thisOrg = thisOrgList[0]


            findRequest = Orders.query(Orders.strOrderID == thisPayment.strOrderID)
            thisOrderList = findRequest.fetch()

            if len(thisOrderList) > 0:
                thisOrder = thisOrderList[0]
            else:
                thisOrder = Orders()

            findRequest = Advert.query(Advert.strAdvertID == thisOrder.strAdvertID)
            thisAdvertList = findRequest.fetch()

            if len(thisAdvertList) > 0:
                thisAdvert = thisAdvertList[0]
            else:
                thisAdvert = Advert()

            template = template_env.get_template('templates/advertise/paymethods/invoice.html')
            context = {'thisPayment':thisPayment,'thisOrg':thisOrg,'thisAdvert':thisAdvert}
            self.response.write(template.render(context))

class TopUpInvoiceHandler(webapp2.RequestHandler):

    def get(self):
        from accounts import Organization
        URL = self.request.url
        strURLlist = URL.split("/")
        strTopUpReference = strURLlist[len(strURLlist) - 1]

        findRequest = AddAccount.query(AddAccount.strTopUpReference == strTopUpReference)
        thisAdvertAccountList = findRequest.fetch()

        if len(thisAdvertAccountList) > 0:
            thisAdvertAccount = thisAdvertAccountList[0]
        else:
            thisAdvertAccount = AddAccount()

        findRequest = Organization.query(Organization.strOrganizationID == thisAdvertAccount.strOrganizationID)
        thisOrganizationList = findRequest.fetch()

        if len(thisOrganizationList) > 0:
            thisOrg = thisOrganizationList[0]

            findRequest = AccountDetails.query()
            thisBlueITMarketingAccountList = findRequest.fetch()

            if len(thisBlueITMarketingAccountList) > 0:
                thisBlueITAccount = thisBlueITMarketingAccountList[0]
            else:
                thisBlueITAccount = AccountDetails()

            template = template_env.get_template("templates/advertise/sub/topupproforma.html")
            context = {"thisAdvertAccount":thisAdvertAccount,"thisOrg":thisOrg,"thisBlueITAccount":thisBlueITAccount}
            self.response.write(template.render(context))
        else:
            self.response.write("UEs we are seeing things")


    def post(self):

        from dashboard import TopUpVerifications
        #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
        vstrUserID = self.request.get("vstrUserID")
        vstrEmail = self.request.get("vstrEmail")
        vstrAccessToken = self.request.get("vstrAccessToken")

        vstrChoice = self.request.get('vstrChoice')
        thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
        if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

            if vstrChoice == "0":
                vstrTopUpReference = self.request.get("vstrTopUpReference")
                vstrYourReferenceNumber = self.request.get("vstrYourReferenceNumber")
                vstrDepositSlipFile = self.request.get("vstrDepositSlipFile")

                findRequest = AddAccount.query(AddAccount.strOrganizationID == thisMainAccount.organization_id)
                thisAdvertAccountList = findRequest.fetch()

                if len(thisAdvertAccountList) > 0:
                    thisAdvertAccount = thisAdvertAccountList[0]
                    if vstrYourReferenceNumber == vstrTopUpReference:
                        thisAdvertAccount.writeDepositSlipFilename(strinput=vstrDepositSlipFile)
                        thisAdvertAccount.put()
                        thisVerifications = TopUpVerifications()
                        thisVerifications.writeOrganizationID(strinput=thisAdvertAccount.organization_id)
                        thisVerifications.writeAccountName(strinput="Adverts")
                        thisVerifications.writeCreditAmount(strinput=thisAdvertAccount.strTotalTopUpCost)
                        thisVerifications.writeDepositSlipFileName(strinput=vstrDepositSlipFile)
                        thisVerifications.writeSMSCredits(strinput=thisAdvertAccount.strTopUpCredit)
                        thisVerifications.writeTopUpReference(strinput=vstrYourReferenceNumber)
                        thisVerifications.put()
                        self.response.write("Successfully Uploaded Deposit slip file : " + vstrDepositSlipFile)

                    else:
                        thisAdvertAccount.writeDepositSlipFilename(strinput=vstrDepositSlipFile)
                        thisAdvertAccount.put()
                        thisVerifications = TopUpVerifications()
                        thisVerifications.writeOrganizationID(strinput=thisAdvertAccount.organization_id)
                        thisVerifications.writeAccountName(strinput="Adverts")
                        thisVerifications.writeCreditAmount(strinput=thisAdvertAccount.strTotalTopUpCost)
                        thisVerifications.writeDepositSlipFileName(strinput=vstrDepositSlipFile)
                        thisVerifications.writeSMSCredits(strinput=thisAdvertAccount.strTopUpCredit)
                        thisVerifications.writeTopUpReference(strinput=vstrTopUpReference)
                        thisVerifications.put()
                        self.response.write("Reference Verification Error, deposit will take longer to verify please use our support tickets to enquire if it takes more than three days")


app = webapp2.WSGIApplication([
    ('/advertise', AdvertiseHandler),
    ('/adverts/manage/.*', ThisAdvertHandler),
    ('/adverts/payments/.*', ThisPaymentAdvertHandler),
    ('/adverts/invoice/.*', ThisInvoiceHandler),
    ('/adverts/topup/invoice/.*', TopUpInvoiceHandler)

], debug=True)

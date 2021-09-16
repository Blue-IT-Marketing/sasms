import os
import jinja2
from google.cloud import ndb


import logging
import datetime

from accounts import Accounts
from dashboard import AccountDetails
from errormessages import MyErrors
from mysms import SMSPortalBudget

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


class OurContacts(ndb.Model):
    """
        This are system contacts uploaded by Blue IT Marketing from the dashboard
        ref is the message reference
    """
    contact_id = ndb.StringProperty()
    names = ndb.StringProperty()
    surname = ndb.StringProperty()
    cell = ndb.StringProperty()

    email = ndb.StringProperty()

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
                self.contact_id = strinput
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
######################################################################
######################################################################
################Surveys and Adverts ##################################
######################################################################
######################################################################

class AddAccount(ndb.Model):
    """
        Advertising Account
    """
    uid = ndb.StringProperty()
    account_id = ndb.StringProperty()
    organization_id = ndb.StringProperty()
    names = ndb.StringProperty()
    surname = ndb.StringProperty()
    cell = ndb.StringProperty()
    tel = ndb.StringProperty()
    email = ndb.StringProperty()
    website = ndb.StringProperty()

    date = ndb.DateProperty(auto_now_add=True)
    time = ndb.TimeProperty(auto_now_add=True)
    total_credits = ndb.IntegerProperty(default=0)

    total_top_up_cost = ndb.IntegerProperty(default=0)
    top_up_credit = ndb.IntegerProperty(default=0)
    top_up_reference = ndb.StringProperty()
    top_up_invoice_link = ndb.StringProperty(default="/adverts/topup/invoice/")
    pay_by_date = ndb.DateProperty()
    date_invoice_created = ndb.DateProperty()
    deposit_slip_filename = ndb.StringProperty()


    def writeDepositSlipFilename(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.deposit_slip_filename = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateInvoiceCreated(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.date_invoice_created = strinput
                return True
            else:
                return False
        except:
            return False
    def writePayByDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.pay_by_date = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTotalTopUpCost(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.total_top_up_cost = int(strinput)
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
                self.top_up_invoice_link = "/adverts/topup/invoice/" + strinput
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
    def writeTopUpCredit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.top_up_credit = int(strinput)
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
                self.total_credits = int(strinput)
                return True
            else:
                return False
        except:
            return False
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
        #TODO- Intergrate Organization Account to the Add Account
        #TODO- this will allow all users to access the same organization
        #TODO- Advertising Account
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
    def writeAccountID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.account_id = strinput
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
                self.date = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.time = strinput
                return True
            else:
                return False
        except:
            return False

class Advert(ndb.Model):
    uid = ndb.StringProperty()
    organization_id = ndb.StringProperty()

    account_id = ndb.StringProperty()
    advert_id = ndb.StringProperty()

    advert = ndb.StringProperty()
    advert_size = ndb.IntegerProperty(default=1)

    date_created = ndb.DateProperty(auto_now_add=True)
    time_created = ndb.TimeProperty(auto_now_add=True)

    start_date = ndb.DateProperty()
    start_time = ndb.TimeProperty()

    advert_status = ndb.StringProperty(default="Scheduled") # Running, Completed, Scheduled
    advert_is_paid = ndb.BooleanProperty(default=False)

    assigned_credit = ndb.IntegerProperty(default=0)
    run_from_credit = ndb.BooleanProperty(default=False)

    use_portal = ndb.StringProperty(default="Budget") # ClickSend Twilio Vodacom


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


    def writeAssignedCredit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.assigned_credit += int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeAdvertSize(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.advert_size = int(strinput)
                return True
            else:
                return False
        except:
            return False
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
    def writeAccountID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.account_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAdvertID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.advert_id = strinput
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
                self.advert = strinput
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
    def writeTimeCreated(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.time_created = strinput
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
    def writeAdvertStatus(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ["Scheduled","Running","Completed"]:
                self.advert_status = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAdvertIsPaid(self,strinput):
        try:
            if strinput in [True,False]:
                self.advert_is_paid = strinput
                return True
            else:
                return False
        except:
            return False

    def writeRunFromCredit(self,strinput):
        try:
            if strinput in [True,False]:
                self.run_from_credit = strinput
                return True
            else:
                return False
        except:
            return False

class Stats(ndb.Model):
    """
        TODO- Order ID was not originally included make sure it is included in all places
    """
    advert_id = ndb.StringProperty()
    order_id = ndb.StringProperty()
    total_sent = ndb.IntegerProperty(default=0)
    total_remaining = ndb.IntegerProperty(default=0)
    total_responses = ndb.IntegerProperty(default=0)
    no_response = ndb.IntegerProperty(default=0)


    def writeAdvertID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.advert_id = strinput
                return True
            else:
                return False

        except:
            return False

    def writeOrderID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.order_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTotalSent(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.total_sent = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeTotalRemaining(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.total_remaining = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeNoResponses(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.no_response = int(strinput)
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
    advert_id = ndb.StringProperty()
    reference = ndb.StringProperty()
    cell = ndb.StringProperty()
    response = ndb.StringProperty()
    date_received = ndb.DateProperty(auto_now_add=True)
    time_received = ndb.TimeProperty(auto_now_add=True)

    def writeAdvertID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.advert_id = strinput
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
                self.cell = strinput
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

    def writeDateReceived(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.date_received = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeReceived(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.time_received = strinput
                return True
            else:
                return False
        except:
            return False

class SentReport(ndb.Expando):
    report_id = ndb.StringProperty()
    advert_id = ndb.StringProperty()
    cell = ndb.StringProperty()
    ref = ndb.StringProperty() # Message Reference for getting back a response
    order_id = ndb.StringProperty()
    date_sent = ndb.DateProperty(auto_now_add=True)
    time_sent = ndb.TimeProperty(auto_now_add=True)
    advert_sent = ndb.BooleanProperty(default=True)
    message_status = ndb.StringProperty(default="Sent") # Delivered, Undelivered
    report_done = ndb.BooleanProperty(default=False)
    response_checked = ndb.BooleanProperty(default=False)

    portal_used = ndb.StringProperty(default="Budget") # Twilio ClickSend Vodacom

    def writePortalUsed(self,strinput):
        try:
            strinput = str(strinput)
            strinput = strinput.strip()
            strinput = strinput.capitalize()
            if strinput in ["Budget","Twilio","ClickSend","Vodacom"]:
                self.portal_used = strinput
                return True
            else:
                return False
        except:
            return False


    def writeAdvertID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.advert_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeReportID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.report_id = strinput
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
    def writeOrderID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.order_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateSent(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.date_sent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeSent(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.time_sent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAdvertSent(self,strinput):
        try:
            if strinput in [True,False]:
                self.advert_sent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMessageStatus(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.message_status = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMessageReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.ref = strinput
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
                self.report_done = strinput
                return True
            else:
                return False
        except:
            return False

    def writeResponseChecked(self,strinput):
        try:
            if strinput in [True,False]:
                self.response_checked = strinput
                return True
            else:
                return False
        except:
            return False

class AdvertPackages(ndb.Expando):
    package_id = ndb.StringProperty()
    name = ndb.StringProperty()
    description = ndb.StringProperty()
    total_credits = ndb.IntegerProperty(default=1000)
    price = ndb.IntegerProperty(default=350)


    def writePackageID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.package_id = strinput
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
                self.name = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.description = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTotalCredits(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.total_credits = strinput
                return True
            else:
                return False

        except:
            return False
    def writePrice(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.price = int(strinput)
                return True
            else:
                return False
        except:
            return False

class Orders(ndb.Expando):
    """
        #RunOrder Activated by an auto payment system or by admin on manual deposit reference verification, once activated the order will start running
    """
    uid = ndb.StringProperty()
    organization_id = ndb.StringProperty()
    advert_id = ndb.StringProperty()
    item_count = ndb.IntegerProperty(default=0)
    order_id = ndb.StringProperty()
    total_sms = ndb.IntegerProperty(default=0)
    quoted_amount = ndb.IntegerProperty(default=0)
    total_paid = ndb.IntegerProperty(default=0)
    fully_paid = ndb.BooleanProperty(default=False)
    order_completed = ndb.BooleanProperty(default=False)
    order_start_date = ndb.DateProperty()
    order_start_time = ndb.TimeProperty()
    deposit_reference = ndb.StringProperty()
    run_order = ndb.BooleanProperty(default=False)

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
    def writeAdvertID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.advert_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeItemCount(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.item_count = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeOrderID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.order_id = strinput
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
                self.quoted_amount = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeTotalPaid(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.total_paid = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeFullyPaid(self,strinput):
        try:
            if strinput in [True,False]:
                self.fully_paid = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOrderCompleted(self,strinput):
        try:
            if strinput in [True,False]:
                self.order_completed = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOrderStartDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.order_start_date = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOrderStartTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.order_start_time = strinput
                return True
            else:
                return False
        except:
            return False
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
                self.deposit_reference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeRunOrder(self,strinput):
        try:
            if strinput in [True,False]:
                self.run_order = strinput
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
    uid = ndb.StringProperty()
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
                    findRequest = AddAccount.query(AddAccount.organization_id == thisMainAccount.organization_id)
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

                findRequest = AddAccount.query(AddAccount.organization_id == thisMainAccount.organization_id)
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

                    findRequest = Advert.query(Advert.organization_id == thisMainAccount.organization_id)
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

                findRequest = AddAccount.query(AddAccount.organization_id == thisMainAccount.organization_id)
                thisAddAccountList = findRequest.fetch()

                if len(thisAddAccountList) > 0:
                    thisAddAccount = thisAddAccountList[0]

                    thisAdvert = Advert()
                    thisAdvert.writeUserID(strinput=vstrUserID)
                    thisAdvert.writeAccountID(strinput=thisAddAccount.account_id)
                    thisAdvert.writeOrganizationID(strinput=thisAddAccount.organization_id)
                    thisAdvert.writeAdvertID(strinput=thisAdvert.CreateAdvertID())
                    thisAdvert.writeAdvert(strinput=vstrAdvert)
                    thisAdvert.writeStartDate(strinput=strThisStartDate)
                    thisAdvert.writeStartTime(strinput=strThisTime)
                    thisAdvert.writeAdvertStatus(strinput="Scheduled")

                    thisAdvert.put()

                    thisStats = Stats()
                    thisStats.writeAdvertID(strinput=thisAdvert.advert_id)
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
                    strQuoteAmount = ((thisBudget.strAdvertSellRate * thisOrder.total_sms) / 100)

                    thisOrder.writeQuoteAmount(strinput=strQuoteAmount)
                    thisOrder.writeOrderID(strinput=thisOrder.CreateOrderID())
                    thisOrder.writeAdvertID(strinput=thisAdvert.advert_id)
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

                    findRequest = Orders.query(Orders.organization_id == thisMainAccount.organization_id, Orders.fully_paid == True)
                    thisPaidList = findRequest.fetch()

                    findRequest = Orders.query(Orders.organization_id == thisMainAccount.organization_id, Orders.fully_paid == False)
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

                findRequest = AddAccount.query(AddAccount.organization_id == thisMainAccount.organization_id)
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
                        logging.info(thisAdvertAccount.total_top_up_cost)
                        thisAdvertAccount.writeTopUpReference(strinput=thisAdvertAccount.CreateTopUpReference())
                        thisAdvertAccount.CreateTopUpInvoiceLink(strinput=thisAdvertAccount.top_up_reference)
                        thisAdvertAccount.writePayByDate(strinput=strPayByDate)
                        thisAdvertAccount.writeDateInvoiceCreated(strinput=strThisDate)
                        thisAdvertAccount.put()
                        findRequest = AddAccount.query(AddAccount.organization_id == thisMainAccount.organization_id)
                        thisAdvertAccountList = findRequest.fetch()
                        if len(thisAdvertAccountList) > 0:
                            thisAdvertAccount = thisAdvertAccountList[0]
                            self.response.write("""
                            Top Up Credit successfully processed please click on this link to view your <strong><a href=" """ + thisAdvertAccount.top_up_invoice_link + """ ">Proforma Invoice</a></strong>
                            """)

        elif vstrChoice == "7":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = Advert.query(Advert.organization_id == thisMainAccount.organization_id)
                thisAdvertsList = findRequest.fetch()
                strTotalAdverts = len(thisAdvertsList)

                findRequest = AddAccount.query(AddAccount.organization_id == thisMainAccount.organization_id)
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

        findRequest = Advert.query(Advert.advert_id == strAdvertID)
        thisAdvertList = findRequest.fetch()

        if len(thisAdvertList) > 0:
            thisAdvert = thisAdvertList[0]

            findRequest = AddAccount.query(AddAccount.organization_id == thisAdvert.organization_id)
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

                findRequest = Advert.query(Advert.advert_id == strAdvertID)
                thisAdvertList = findRequest.fetch()

                if len(thisAdvertList) > 0:
                    thisAdvert = thisAdvertList[0]
                    findRequest = AddAccount.query(AddAccount.organization_id == thisAdvert.organization_id)
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

                findRequest = Advert.query(Advert.advert_id == vstrAdvertID)
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


                findRequest = Stats.query(Stats.advert_id == vstrAdvertID)
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

                findRequest = Advert.query(Advert.advert_id == vstrAdvertID)
                thisAdvertList = findRequest.fetch()

                if len(thisAdvertList) > 0:
                    thisAdvert = thisAdvertList[0]
                else:
                    thisAdvert = Advert()


                if thisAdvert.advert_status in ["Running", "Completed"]:
                    findRequest = Orders.query(Orders.advert_id == thisAdvert.advert_id)
                    thisOrderList = findRequest.fetch()
                    #TODO-Please finish up the contacts functions allow it to load as many contacts as
                    #TODO-Possible and then start running adverts, also consider adding the contacts list
                    #TODO-on adverts, to make it easier for users to load their own contacts


                findRequest = Responses.query(Responses.advert_id == vstrAdvertID)
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

                findRequest = Orders.query(Orders.advert_id == vstrAdvertID)
                thisOrdersList = findRequest.fetch()


                ThisPaymentsList = []
                for thisOrder in thisOrdersList:
                    findRequest = Payments.query(Payments.strOrderID == thisOrder.order_id)
                    thisPaymentList = findRequest.fetch()

                    for thisPayment in thisPaymentList:
                        ThisPaymentsList.append(thisPayment)


                findRequest = Orders.query(Orders.advert_id == vstrAdvertID, Orders.fully_paid == False)
                thisUpaidOrderList = findRequest.fetch()


                findRequest = Advert.query(Advert.advert_id == vstrAdvertID)
                thisAdvertList = findRequest.fetch()

                if len(thisAdvertList) > 0:
                    thisAdvert = thisAdvertList[0]


                    findRequest = AddAccount.query(AddAccount.organization_id == thisAdvert.organization_id)
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

                findRequest = Stats.query(Stats.advert_id == vstrAdvertID)
                thisStatList = findRequest.fetch()

                if len(thisStatList) > 0:
                    thisStats = thisStatList[0]
                else:
                    thisStats = Stats()

                #TODO- Investigate the Quotation System the way it is , is not satisfactory there might be bugs here
                strQuoteAmount = ((thisBudget.strAdvertSellRate * thisOrder.total_sms) / 100)
                thisOrder.writeQuoteAmount(strinput=strQuoteAmount)
                thisOrder.writeOrderID(strinput=thisOrder.CreateOrderID())

                thisOrder.writeOrderStartDate(strinput=strThisStartDate)
                thisOrder.writeOrderStartTime(strinput=strThisTime)
                thisOrder.writeOrderCompleted(strinput=False)
                thisOrder.writeItemCount(strinput=str(1))
                thisOrder.put()
                thisStats.writeTotalRemaining(strinput=str(thisStats.total_remaining + int(vstrPackage)))
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
                    findRequest = Orders.query(Orders.order_id == vstrSelectOrder)
                    thisOrderList = findRequest.fetch()

                    if len(thisOrderList) > 0:
                        thisOrder = thisOrderList[0]
                    else:
                        thisOrder = Orders()

                    thisOrder.writeDepositReference(strinput=thisOrder.CreatedDepositReference())
                    thisOrder.put()

                    findRequest = Advert.query(Advert.advert_id == vstrAdvertID)
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

                    findRequest = Organization.query(Organization.strOrganizationID == thisAdvert.organization_id)
                    thisOrgList = findRequest.fetch()

                    if len(thisOrgList) > 0:
                        thisOrg = thisOrgList[0]
                    else:
                        thisOrg = Organization()

                    findRequest = AddAccount.query(AddAccount.organization_id == thisAdvert.organization_id)
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

                findRequest = Orders.query(Orders.order_id == vstrOrderID)
                thisOrderList = findRequest.fetch()

                if len(thisOrderList) > 0:
                    thisOrder = thisOrderList[0]
                else:
                    thisOrder = Orders()

                findRequest = Advert.query(Advert.advert_id == vstrAdvertID)
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
                vstrReference = "Deposit Reference : " + thisOrder.deposit_reference

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

                findRequest = Advert.query(Advert.advert_id == vstrAdvertID)
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
                        findRequest = AddAccount.query(AddAccount.organization_id == thisAdvert.organization_id)
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

        findRequest = Orders.query(Orders.order_id == strOrderID)
        thisOrderList = findRequest.fetch()

        if len(thisOrderList) > 0:
            thisOrder = thisOrderList[0]

            findRequest = Advert.query(Advert.advert_id == thisOrder.advert_id)
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


            findRequest = Orders.query(Orders.order_id == thisPayment.strOrderID)
            thisOrderList = findRequest.fetch()

            if len(thisOrderList) > 0:
                thisOrder = thisOrderList[0]
            else:
                thisOrder = Orders()

            findRequest = Advert.query(Advert.advert_id == thisOrder.advert_id)
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

        findRequest = AddAccount.query(AddAccount.top_up_reference == strTopUpReference)
        thisAdvertAccountList = findRequest.fetch()

        if len(thisAdvertAccountList) > 0:
            thisAdvertAccount = thisAdvertAccountList[0]
        else:
            thisAdvertAccount = AddAccount()

        findRequest = Organization.query(Organization.strOrganizationID == thisAdvertAccount.organization_id)
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

                findRequest = AddAccount.query(AddAccount.organization_id == thisMainAccount.organization_id)
                thisAdvertAccountList = findRequest.fetch()

                if len(thisAdvertAccountList) > 0:
                    thisAdvertAccount = thisAdvertAccountList[0]
                    if vstrYourReferenceNumber == vstrTopUpReference:
                        thisAdvertAccount.writeDepositSlipFilename(strinput=vstrDepositSlipFile)
                        thisAdvertAccount.put()
                        thisVerifications = TopUpVerifications()
                        thisVerifications.writeOrganizationID(strinput=thisAdvertAccount.organization_id)
                        thisVerifications.writeAccountName(strinput="Adverts")
                        thisVerifications.writeCreditAmount(strinput=thisAdvertAccount.total_top_up_cost)
                        thisVerifications.writeDepositSlipFileName(strinput=vstrDepositSlipFile)
                        thisVerifications.writeSMSCredits(strinput=thisAdvertAccount.top_up_credit)
                        thisVerifications.writeTopUpReference(strinput=vstrYourReferenceNumber)
                        thisVerifications.put()
                        self.response.write("Successfully Uploaded Deposit slip file : " + vstrDepositSlipFile)

                    else:
                        thisAdvertAccount.writeDepositSlipFilename(strinput=vstrDepositSlipFile)
                        thisAdvertAccount.put()
                        thisVerifications = TopUpVerifications()
                        thisVerifications.writeOrganizationID(strinput=thisAdvertAccount.organization_id)
                        thisVerifications.writeAccountName(strinput="Adverts")
                        thisVerifications.writeCreditAmount(strinput=thisAdvertAccount.total_top_up_cost)
                        thisVerifications.writeDepositSlipFileName(strinput=vstrDepositSlipFile)
                        thisVerifications.writeSMSCredits(strinput=thisAdvertAccount.top_up_credit)
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

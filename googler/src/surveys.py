import os
import jinja2
import logging
import datetime
from google.cloud import ndb
from accounts import Accounts

from dashboard import AccountDetails
from errormessages import MyErrors
from mysms import SMSPortalBudget

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


class SurveyAccount(ndb.Model):
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

    date_created = ndb.DateProperty(auto_now_add=True)
    time_created = ndb.TimeProperty(auto_now_add=True)

    total_credits = ndb.IntegerProperty(default=0)

    total_top_up_cost = ndb.IntegerProperty(default=0)
    top_up_credit = ndb.IntegerProperty(default=0)
    top_up_reference = ndb.StringProperty()
    top_up_invoice_link = ndb.StringProperty()
    pay_by_date = ndb.DateProperty()
    date_invoice_created = ndb.DateProperty()
    deposit_slip_filename = ndb.StringProperty()

    def writeDepositSlipFilename(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.deposit_slip_filename = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateInvoiceCreated(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.date_invoice_created = strinput
                return True
            else:
                return False
        except:
            return False

    def writePayByDate(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.pay_by_date = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTotalTopUpCost(self, strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.total_top_up_cost = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def CreateTopUpInvoiceLink(self, strinput):
        """
            strinput should be TopUpReference
        :param strinput:
        :return:
        """
        try:
            strinput = str(strinput)
            if strinput != None:
                self.top_up_invoice_link = "/surveys/topup/invoice/" + strinput
                return True
            else:
                return False
        except:
            return False

    def writeTopUpReference(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.top_up_reference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTopUpCredit(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.top_up_credit = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def CreateTopUpReference(self):
        import random, string
        try:
            strTopUpReference = ""
            for i in range(12):
                strTopUpReference += random.SystemRandom().choice(string.digits + string.ascii_uppercase)

            return strTopUpReference
        except:
            return None

    def writeTotalCredits(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.total_credits = int(strinput)
                return True
            else:
                return False
        except:
            return False

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
        # TODO- Intergrate Organization Account to the Add Account
        # TODO- this will allow all users to access the same organization
        # TODO- Advertising Account

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

    def writeAccountID(self, strinput):
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
        import string, random
        try:
            strAccountID = ""
            for i in range(256):
                strAccountID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)

            return strAccountID
        except:
            return None

    def writeDate(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.date_created = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTime(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.time_created = strinput
                return True
            else:
                return False
        except:
            return False


class SurveyContactLists(ndb.Model):
    list_id = ndb.StringProperty()
    # TODO- Please make sure that the advert account is used to obtain the user id so that only users who owns
    # TODO- Advertising Accounts can create Survey Lists

    uid = ndb.StringProperty()
    organization_id = ndb.StringProperty()
    name = ndb.StringProperty()

    description = ndb.StringProperty()
    total = ndb.IntegerProperty(default=0)
    date_created = ndb.DateProperty(auto_now_add=True)
    time_created = ndb.TimeProperty(auto_now_add=True)

    def writeListID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.list_id = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateListID(self):
        import random, string
        try:
            strListID = ""
            for i in range(256):
                strListID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strListID
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

    def writeName(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.name = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDescription(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.description = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTotalContacts(self, strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.total = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeDate(self, strinput):
        try:

            if isinstance(strinput, datetime.date):
                self.date_created = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTime(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.time_created = strinput
                return True
            else:
                return False
        except:
            return False


class SurveyContacts(ndb.Model):
    """
        Survey Contacts Contacts for surveys organised by list ID
    """
    list_id = ndb.StringProperty()
    contact_id = ndb.StringProperty()

    name = ndb.StringProperty()
    surname = ndb.StringProperty()
    cell = ndb.StringProperty()

    def writeListID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.list_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeContactID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.contact_id = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateContactID(self):
        import string, random
        try:
            strContactID = ""
            for i in range(256):
                strContactID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strContactID
        except:
            return None

    def writeName(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.name = strinput
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


class SurveySchedules(ndb.Model):
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
    schedule_id = ndb.StringProperty()
    uid = ndb.StringProperty()
    list_id = ndb.StringProperty()
    survey_id = ndb.StringProperty()
    name = ndb.StringProperty()
    description = ndb.StringProperty()
    start_date = ndb.DateProperty()
    start_time = ndb.TimeProperty()
    notify_on_start = ndb.BooleanProperty(default=True)
    notify_on_end = ndb.BooleanProperty(default=True)
    activate_schedule = ndb.BooleanProperty(default=False)  # TODO- Schedule Active to allow schedule to run

    survey_status = ndb.StringProperty(default="Scheduled")  # Running , Completed, Suspended
    date_status_changed = ndb.DateProperty()
    time_status_changed = ndb.TimeProperty()

    def writeScheduleID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.schedule_id = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateScheduleID(self):
        import random, string
        try:
            strScheduleID = ""
            for i in range(256):
                strScheduleID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strScheduleID
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

    def writeName(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.name = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDescription(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.description = strinput
                return True
            else:
                return False
        except:
            return False

    def writeListID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.list_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSurveyID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.survey_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeStartDate(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.start_date = strinput
                return True
            else:
                return False
        except:
            return False

    def writeStartTime(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.start_time = strinput
                return True
            else:
                return False
        except:
            return False

    def writeNotifyOnStart(self, strinput):
        try:
            if strinput in [True, False]:
                self.notify_on_start = strinput
                return True
            else:
                return False
        except:
            return False

    def writeNotifyOnEnd(self, strinput):
        try:
            if strinput in [True, False]:
                self.notify_on_end = strinput
                return True
            else:
                return False
        except:
            return False

    def writeActivateSchedule(self, strinput):
        try:
            if strinput in [True, False]:
                self.activate_schedule = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSurveyStatus(self, strinput):
        try:
            strinput = str(strinput)
            if strinput in ["Scheduled", "Running", "Completed", "Suspended"]:
                self.survey_status = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateStatusChange(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.date_status_changed = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeStatusChange(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.time_status_changed = strinput
                return True
            else:
                return False
        except:
            return False


class Surveys(ndb.Model):
    uid = ndb.StringProperty()
    organization_id = ndb.StringProperty()

    survey_id = ndb.StringProperty()
    name = ndb.StringProperty()
    description = ndb.StringProperty()
    survey_type = ndb.StringProperty(default="multichoice")  # general
    date_created = ndb.DateProperty(auto_now_add=True)
    time_created = ndb.TimeProperty(auto_now_add=True)

    start_date = ndb.DateProperty()
    start_time = ndb.TimeProperty()

    survey_status = ndb.StringProperty(default="Scheduled")  # Running, Completed, Scheduled,Building
    survey_is_paid = ndb.BooleanProperty(default=False)

    assigned_credit = ndb.IntegerProperty(default=0)

    run_from_credit = ndb.BooleanProperty(default=False)

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

    def CreateSurveyID(self):
        import random, string
        try:
            strSurveyID = ""
            for i in range(256):
                strSurveyID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strSurveyID
        except:
            return None

    def writeSurveyID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.survey_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSurveyName(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.name = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSurveyDescription(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.description = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateCreated(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.date_created = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeCreated(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.time_created = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSurveyType(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.survey_type = strinput
                return True
            else:
                return False
        except:
            return False

    def writeStartDate(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.start_date = strinput
                return True
            else:
                return False
        except:
            return False

    def writeStartTime(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.start_time = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSurveyStatus(self, strinput):
        try:
            if strinput in ["Scheduled", "Running", "Completed"]:
                self.survey_status = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSurveyIsPaid(self, strinput):
        try:
            if strinput in [True, False]:
                self.survey_is_paid = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAssignedCredit(self, strinput):
        try:
            strinput = str(strinput)
            if (strinput.isdigit()) and (int(strinput) > 0):
                self.assigned_credit = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeRunFromCredit(self, strinput):
        try:

            if strinput in [True, False]:
                self.run_from_credit = strinput
                return True
            else:
                return False
        except:
            return False


class MultiChoiceSurveys(ndb.Model):
    index = ndb.IntegerProperty()
    survey_id = ndb.StringProperty()
    question_id = ndb.StringProperty()
    question = ndb.StringProperty()
    choice_one = ndb.StringProperty(default="undefined")
    choice_two = ndb.StringProperty(default="undefined")
    choice_three = ndb.StringProperty(default="undefined")
    choice_four = ndb.StringProperty(default="undefined")
    date_created = ndb.DateTimeProperty(auto_now_add=True)

    # We will sort the qeustions by making use of the Date Created Field
    # This Means the tracker will keep the current Question ID then the next
    # question will be the question with the later date if not exit

    def writeSurveyID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.survey_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeQuestionID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.question_id = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateQuestionID(self):
        import random, string
        try:
            strQuestionID = ""
            for i in range(256):
                strQuestionID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strQuestionID
        except:
            return None

    def writeQuestion(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.question = strinput
                return True
            else:
                return False
        except:
            return False

    def writeChoiceOne(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strChoiceOne = strinput
                return True
            else:
                return False
        except:
            return False

    def writeChoiceTwo(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.choice_two = strinput
                return True
            else:
                return False
        except:
            return False

    def writeChoiceThree(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.choice_three = strinput
                return True
            else:
                return False
        except:
            return False

    def writeChoiceFour(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.choice_four = strinput
                return True
            else:
                return False
        except:
            return False


class MultiChoiceSurveyAnswers(ndb.Model):
    cell = ndb.StringProperty()
    names = ndb.StringProperty()
    surname = ndb.StringProperty()
    reference = ndb.StringProperty()
    survey_id = ndb.StringProperty()
    question_id = ndb.StringProperty()
    question = ndb.StringProperty()
    option_number = ndb.IntegerProperty(default=0)  # If Zero it means user did not answer
    date_time = ndb.DateTimeProperty(auto_now_add=True)

    def writeRef(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.reference = strinput
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

    def writeSurveyID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.survey_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeQuestion(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.question = strinput
                return True
            else:
                return False
        except:
            return False

    def writeQuestionID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.question_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeOptionNumber(self, strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.option_number = int(strinput)
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


class GeneralQuestionsSurvey(ndb.Model):
    survey_id = ndb.StringProperty()
    question_id = ndb.StringProperty()
    question = ndb.StringProperty()

    def writeSurveyID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.survey_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeQuestionID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.question_id = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateQuestionID(self):
        import random, string
        try:
            strQuestionID = ""
            for i in range(256):
                strQuestionID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strQuestionID
        except:
            return None

    def writeQuestion(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.question = strinput
                return True
            else:
                return False
        except:
            return False


class SurveyOrders(ndb.Model):
    uid = ndb.StringProperty()
    organization_id = ndb.StringProperty()
    survey_id = ndb.StringProperty()
    item_count = ndb.IntegerProperty(default=0)
    order_id = ndb.StringProperty()
    schedule_id = ndb.StringProperty()
    total_sms = ndb.IntegerProperty(default=0)
    quoted_amount = ndb.FloatProperty(default=0)
    total_paid = ndb.IntegerProperty(default=0)
    is_fully_paid = ndb.BooleanProperty(default=False)
    order_completed = ndb.BooleanProperty(default=False)
    order_start_date = ndb.DateProperty()
    order_start_time = ndb.TimeProperty()
    deposit_reference = ndb.StringProperty()
    run_order = ndb.BooleanProperty(default=False)

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

    def writeSurveyID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.survey_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeItemCount(self, strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.item_count = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeOrderID(self, strinput):
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
        import random, string
        try:
            strOrderID = ""
            for i in range(256):
                strOrderID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strOrderID
        except:
            return None

    def writeQuoteAmount(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.quoted_amount = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeTotalPaid(self, strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.total_paid = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeFullyPaid(self, strinput):
        try:
            if strinput in [True, False]:
                self.is_fully_paid = strinput
                return True
            else:
                return False
        except:
            return False

    def writeOrderCompleted(self, strinput):
        try:
            if strinput in [True, False]:
                self.order_completed = strinput
                return True
            else:
                return False
        except:
            return False

    def writeOrderStartDate(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.order_start_date = strinput
                return True
            else:
                return False
        except:
            return False

    def writeOrderStartTime(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.order_start_time = strinput
                return True
            else:
                return False
        except:
            return False

    def writeScheduleID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.schedule_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTotalSMS(self, strinput):
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

    def writeDepositReference(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.deposit_reference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeRunOrder(self, strinput):
        try:
            if strinput in [True, False]:
                self.run_order = strinput
                return True
            else:
                return False

        except:
            return False


class SurveyPayments(ndb.Model):
    """
        Try using a method where in the administrator section i can verify all loaded payments through their Deposit Reference
        Generated in the Orders Class , The Reference is only used for the specific order only .

        once a payment verification is received an invoice is generated and the order marked as paid if fully paid and the totla paid amount
        adjusted...on the payment record the same is done for easy creation of invoices...
    """
    uid = ndb.StringProperty()
    order_id = ndb.StringProperty()
    organization_id = ndb.StringProperty()
    payment_id = ndb.StringProperty()
    deposit_reference = ndb.StringProperty()  # Intergrate this with payments class
    amount_paid = ndb.IntegerProperty(default=0)
    payment_method = ndb.StringProperty(default="Direct Deposit")  # Cash , EFT
    date_paid = ndb.DateProperty(auto_now_add=True)
    time_paid = ndb.TimeProperty(auto_now_add=True)
    payment_verified = ndb.BooleanProperty(default=False)
    date_verified = ndb.BooleanProperty(default=False)
    time_verified = ndb.BooleanProperty(default=False)

    # TODO- When verification is effected remember to set the dates and time

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

    def writeOrderID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.order_id = strinput
                return True
            else:
                return False
        except:
            return False

    def CreatePaymentID(self):
        import random, string
        try:
            strPaymentID = ""
            for i in range(256):
                strPaymentID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strPaymentID
        except:
            return None

    def writePaymentID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.payment_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAmountPaid(self, strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.amount_paid = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writePaymentMethod(self, strinput):
        try:

            if strinput in ["Direct Deposit", "Cash", "EFT", "PayPal"]:
                self.payment_method = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDatePaid(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.date_paid = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimePaid(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.time_paid = strinput
                return True
            else:
                return False
        except:
            return False

    def writePaymentVerified(self, strinput):
        try:
            if strinput in [True, False]:
                self.payment_verified = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDepositReference(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.deposit_reference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateVerified(self, strinput):
        try:

            if isinstance(strinput, datetime.date):
                self.date_verified = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeVerified(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.time_verified = strinput
                return True
            else:
                return False
        except:
            return False


class SurveyTracker(ndb.Model):
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

    survey_id = ndb.StringProperty()
    current_question_id = ndb.StringProperty()
    cell = ndb.StringProperty()
    reference = ndb.StringProperty()
    response_received = ndb.BooleanProperty(default=False)
    client_participation = ndb.BooleanProperty(default=True)
    date_created = ndb.DateProperty(auto_now_add=True)
    time_created = ndb.TimeProperty(auto_now_add=True)
    is_last_question = ndb.BooleanProperty(default=False)
    run_times = ndb.IntegerProperty(default=0)  # Count how many times the Tracker ran looking for answers

    def writeSurveyID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.survey_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCurrentQuestionID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.current_question_id = strinput
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

    def writeResponseReceived(self, strinput):
        try:
            if strinput in [True, False]:
                self.response_received = strinput
                return True
            else:
                return False
        except:
            return False

    def writeClientParticipation(self, strinput):
        try:
            if strinput in [True, False]:
                self.client_participation = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDate(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.date_created = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTime(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.time_created = strinput
                return True
            else:
                return False
        except:
            return False

    def writeIsLastQuestion(self, strinput):
        try:
            if strinput in [True, False]:
                self.is_last_question = strinput
                return True
            else:
                return False
        except:
            return False

    def writeRunTimes(self, strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.run_times = int(strinput)
                return True
            else:
                return False
        except:
            return False


class GeneralQuestionsAnswers(ndb.Model):
    cell = ndb.StringProperty()
    survey_id = ndb.StringProperty()
    question_id = ndb.StringProperty()
    answer = ndb.StringProperty()

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

    def writeSurveyID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.survey_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeQuestionID(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.question_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAnswer(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.answer = strinput
                return True
            else:
                return False
        except:
            return False


from firebaseadmin import VerifyAndReturnAccount


class SurveyHandler:

    # TODO- do this for all utilities

    def get(self):
        template = template_env.get_template('templates/surveys/mainsurvey.html')
        context = {}
        self.response.write(template.render(context))

    def post(self):
        from accounts import Organization
        vstrChoice = self.request.get('vstrChoice')
        # Uploading a Survey

        if vstrChoice == "0":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                if thisMainAccount.verified:
                    findRequest = Surveys.query(Surveys.organization_id == thisMainAccount.organization_id)
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

            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrSurveyName = self.request.get('vstrSurveyName')
            vstrDescription = self.request.get('vstrDescription')
            vstrSurveyType = self.request.get('vstrSurveyType')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = Surveys.query(Surveys.organization_id == thisMainAccount.organization_id,
                                            Surveys.name == vstrSurveyName)
                thisSurveysList = findRequest.fetch()

                if len(thisSurveysList) > 0:
                    self.response.write("The survey already exist please edit the existing survey Instead")
                else:
                    thisSurvey = Surveys()

                    vstrThisDate = datetime.datetime.now()
                    strThisDate = vstrThisDate.date()

                    strThisTime = datetime.time(hour=vstrThisDate.hour, minute=vstrThisDate.minute,
                                                second=vstrThisDate.second)
                    thisSurvey.writeSurveyName(strinput=vstrSurveyName)
                    thisSurvey.writeSurveyDescription(strinput=vstrDescription)

                    thisSurvey.writeSurveyType(strinput=vstrSurveyType)
                    thisSurvey.writeDateCreated(strinput=strThisDate)
                    thisSurvey.writeTimeCreated(strinput=strThisTime)
                    thisSurvey.writeUserID(strinput=vstrUserID)
                    thisSurvey.writeSurveyID(strinput=thisSurvey.CreateSurveyID())
                    thisSurvey.writeOrganizationID(strinput=thisMainAccount.organization_id)
                    thisSurvey.put()
                    self.response.write(
                        "Survey Successfully created please dont forget to create your survey questions")
            else:
                self.response.write("Create your main account")


        # Survey Accounts

        elif vstrChoice == "2":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                if thisMainAccount.verified:
                    findRequest = SurveyAccount.query(SurveyAccount.organization_id == thisMainAccount.organization_id)
                    thisSurveyAccountList = findRequest.fetch()
                    if len(thisSurveyAccountList) > 0:
                        thisSurveyAccount = thisSurveyAccountList[0]
                    else:
                        thisSurveyAccount = SurveyAccount()

                    template = template_env.get_template('templates/surveys/sub/accounts.html')
                    context = {'thisSurveyAccount': thisSurveyAccount, }
                    self.response.write(template.render(context))


        # Main Screen Surveys Orders
        elif vstrChoice == "3":

            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                if thisMainAccount.verified:
                    findRequest = SurveyOrders.query(SurveyOrders.organization_id == thisMainAccount.organization_id)
                    thisOrdersList = findRequest.fetch()

                    template = template_env.get_template('templates/surveys/orders/mainorderlist.html')
                    context = {'thisOrdersList': thisOrdersList}
                    self.response.write(template.render(context))

        # Update Survey Account
        elif vstrChoice == "4":

            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrNames = self.request.get('vstrNames')
            vstrSurname = self.request.get('vstrSurname')
            vstrCell = self.request.get('vstrCell')
            vstrTel = self.request.get('vstrTel')
            vstrEmail = self.request.get('vstrEmail')
            vstrWebsite = self.request.get('vstrWebsite')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                if thisMainAccount.verified:
                    findRequest = SurveyAccount.query(SurveyAccount.organization_id == thisMainAccount.organization_id)
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
                    strThisTime = datetime.time(hour=vstrDateTime.hour, minute=vstrDateTime.minute,
                                                second=vstrDateTime.second)
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

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                if thisMainAccount.verified:
                    findRequest = SurveyPayments.query(
                        SurveyPayments.organization_id == thisMainAccount.organization_id)
                    thisPaymentList = findRequest.fetch()

                    template = template_env.get_template('templates/surveys/invoices/invoicelist.html')
                    context = {'thisPaymentList': thisPaymentList}
                    self.response.write(template.render(context))


        elif vstrChoice == "6":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
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

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = SurveyAccount.query(SurveyAccount.organization_id == thisMainAccount.organization_id)
                thisSurveyAccountList = findRequest.fetch()

                if len(thisSurveyAccountList) > 0:
                    thisSurveyAccount = thisSurveyAccountList[0]

                    if vstrPaymentMethod == "DirectDeposit":
                        vstrThisDate = datetime.datetime.now()
                        strThisDate = datetime.date(year=vstrThisDate.year, month=vstrThisDate.month,
                                                    day=vstrThisDate.day)
                        vstrThisDate += datetime.timedelta(days=30)
                        strPayByDate = datetime.date(year=vstrThisDate.year, month=vstrThisDate.month,
                                                     day=vstrThisDate.day)
                        strTotalCost = (thisPortal.advert_sell_rate * int(vstrAddCredits)) / 100

                        thisSurveyAccount.writeTotalTopUpCost(strinput=strTotalCost)

                        thisSurveyAccount.writeTopUpCredit(strinput=vstrAddCredits)
                        thisSurveyAccount.writeTopUpReference(strinput=thisSurveyAccount.CreateTopUpReference())
                        thisSurveyAccount.CreateTopUpInvoiceLink(strinput=thisSurveyAccount.top_up_reference)
                        thisSurveyAccount.writePayByDate(strinput=strPayByDate)
                        thisSurveyAccount.writeDateInvoiceCreated(strinput=strThisDate)
                        thisSurveyAccount.put()
                        findRequest = SurveyAccount.query(
                            SurveyAccount.organization_id == thisMainAccount.organization_id)
                        thisSurveyAccountList = findRequest.fetch()
                        if len(thisSurveyAccountList) > 0:
                            thisSurveyAccount = thisSurveyAccountList[0]

                            self.response.write("""
                            Top up Credit successfully processed please click on this link to view your <strong><a href=" """ + thisSurveyAccount.top_up_invoice_link + """ ">Proforma Invoice</a></strong>""")


        elif vstrChoice == "7":

            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = Organization.query(Organization.strOrganizationID == thisMainAccount.organization_id)
                thisOrgList = findRequest.fetch()

                if len(thisOrgList) > 0:
                    thisOrg = thisOrgList[0]
                else:
                    thisOrg = Organization()

                if thisMainAccount.verified and thisOrg.strVerified:
                    findRequest = Surveys.query(Surveys.organization_id == thisMainAccount.organization_id)
                    thisSurveysList = findRequest.fetch()

                    strTotalSurveys = len(thisSurveysList)

                    findRequest = SurveyAccount.query(SurveyAccount.organization_id == thisMainAccount.organization_id)
                    thisSurveysAccountList = findRequest.fetch()
                    if len(thisSurveysAccountList) > 0:
                        thisSurveyAccount = thisSurveysAccountList[0]
                    else:
                        thisSurveyAccount = SurveyAccount()

                    template = template_env.get_template('templates/surveys/sub/SurveysSubmenu.html')
                    context = {'thisSurveysList': thisSurveysList, 'thisSurveyAccount': thisSurveyAccount,
                               'strTotalSurveys': strTotalSurveys}
                    self.response.write(template.render(context))


class ThisSurveyHandler:

    def get(self):

        URL = self.request.url
        strURLlist = URL.split("/")
        strSurveyID = strURLlist[len(strURLlist) - 1]

        findRequest = Surveys.query(Surveys.survey_id == strSurveyID)
        thisSurveyList = findRequest.fetch()

        if len(thisSurveyList) > 0:
            thisSurvey = thisSurveyList[0]

            findRequest = SurveyAccount.query(SurveyAccount.organization_id == thisSurvey.organization_id)
            thisSurveyAccountList = findRequest.fetch()

            if len(thisSurveyAccountList) > 0:
                thisSurveyAccount = thisSurveyAccountList[0]
            else:
                thisSurveyAccount = SurveyAccount()

            if thisSurvey.survey_type == "multichoice":
                findRequest = MultiChoiceSurveys.query(MultiChoiceSurveys.survey_id == strSurveyID)
                thisMultiChoiceSurveysList = findRequest.fetch()

                template = template_env.get_template('templates/surveys/multi/multichoice.html')
                context = {'thisMultiChoiceSurveysList': thisMultiChoiceSurveysList, 'survey_id': strSurveyID,
                           'thisSurvey': thisSurvey, 'thisSurveyAccount': thisSurveyAccount}
                self.response.write(template.render(context))
            elif thisSurvey.survey_type == "general":
                findRequest = GeneralQuestionsSurvey.query(GeneralQuestionsSurvey.survey_id == strSurveyID)
                thisGeneralQuestionsSurveyList = findRequest.fetch()
                template = template_env.get_template('templates/survey/general/general.html')
                context = {'thisGeneralQuestionsSurveyList': thisGeneralQuestionsSurveyList}
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

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrSurveyID = self.request.get('vstrSurveyID')

                findRequest = Surveys.query(Surveys.survey_id == vstrSurveyID)
                thisSurveysList = findRequest.fetch()
                if len(thisSurveysList) > 0:
                    thisSurvey = thisSurveysList[0]

                    findRequest = SurveyAccount.query(SurveyAccount.organization_id == thisSurvey.organization_id)
                    thisSurveyAccountList = findRequest.fetch()

                    if len(thisSurveyAccountList) > 0:
                        thisSurveyAccount = thisSurveyAccountList[0]
                    else:
                        thisSurveyAccount = SurveyAccount()

                    template = template_env.get_template('templates/surveys/multi/survey.html')
                    context = {'thisSurvey': thisSurvey, 'thisSurveyAccount': thisSurveyAccount}
                    self.response.write(template.render(context))


        # Update Multi choice Survey

        elif vstrChoice == "1":

            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrSurveyID = self.request.get('vstrSurveyID')
                vstrSurveyName = self.request.get('vstrSurveyName')
                vstrDescription = self.request.get('vstrDescription')
                vstrSurveyType = self.request.get('vstrSurveyType')

                findRequest = Surveys.query(Surveys.survey_id == vstrSurveyID)
                thisSurveysList = findRequest.fetch()

                if len(thisSurveysList) > 0:
                    thisSurvey = thisSurveysList[0]
                    thisSurvey.writeSurveyName(strinput=vstrSurveyName)
                    thisSurvey.writeSurveyDescription(strinput=vstrDescription)
                    thisSurvey.writeSurveyType(strinput=vstrSurveyType)
                    thisSurvey.put()
                    self.response.write("Survey Successfully updated")

        # Survey Questions Multi choice

        elif vstrChoice == "2":
            # + '&vstrSurveyID=' + vstrSurveyID + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrSurveyID = self.request.get('vstrSurveyID')

                findRequest = MultiChoiceSurveys.query(MultiChoiceSurveys.survey_id == vstrSurveyID)
                thisMultiChoiceSurveyList = findRequest.fetch()
                findRequest = Surveys.query(Surveys.survey_id == vstrSurveyID)
                thisSurveysList = findRequest.fetch()

                if len(thisSurveysList) > 0:
                    thisSurvey = thisSurveysList[0]
                else:
                    thisSurvey = Surveys()

                template = template_env.get_template('templates/surveys/multi/surveyQuestions.html')
                context = {'thisMultiChoiceSurveyList': thisMultiChoiceSurveyList, 'vstrSurveyID': vstrSurveyID,
                           'thisSurvey': thisSurvey}
                self.response.write(template.render(context))
            # Survey Questions Multi choice

        elif vstrChoice == "3":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
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

                findRequest = MultiChoiceSurveys.query(MultiChoiceSurveys.survey_id == vstrSurveyID,
                                                       MultiChoiceSurveys.question == vstrQuestion)
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

                findRequest = MultiChoiceSurveyAnswers.query(MultiChoiceSurveyAnswers.survey_id == vstrSurveyID)
                thisSurveyAnswersList = findRequest.fetch()

                findRequest = Surveys.query(Surveys.survey_id == vstrSurveyID)
                thisSurveysList = findRequest.fetch()
                if len(thisSurveysList) > 0:
                    thisSurvey = thisSurveysList[0]
                else:
                    thisSurvey = Surveys()

                template = template_env.get_template('templates/surveys/multi/responses.html')
                context = {'thisSurveyAnswersList': thisSurveyAnswersList, 'thisSurvey': thisSurvey}
                self.response.write(template.render(context))
        elif vstrChoice == "5":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrSurveyID = self.request.get('vstrSurveyID')

                findRequest = SurveyAccount.query(SurveyAccount.uid == vstrUserID)
                thisSurveyAccountList = findRequest.fetch()
                if len(thisSurveyAccountList) > 0:
                    thisSurveyAccount = thisSurveyAccountList[0]
                else:
                    thisSurveyAccount = SurveyAccount()

                findRequest = SurveyContactLists.query(
                    SurveyContactLists.organization_id == thisSurveyAccount.organization_id)
                thisSurveyContactLists = findRequest.fetch()

                template = template_env.get_template('templates/surveys/contacts/mycontacts.html')
                context = {'thisSurveyContactLists': thisSurveyContactLists, 'vstrSurveyID': vstrSurveyID,
                           'thisSurveyAccount': thisSurveyAccount}
                self.response.write(template.render(context))
        elif vstrChoice == "6":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrSurveyID = self.request.get('vstrSurveyID')
                vstrOrganizationID = self.request.get('vstrOrganizationID')
                vstrListName = self.request.get('vstrListName')
                vstrListDescription = self.request.get('vstrListDescription')

                findRequest = SurveyContactLists.query(SurveyContactLists.organization_id == vstrOrganizationID,
                                                       SurveyContactLists.name == vstrListName)
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
                    strThisTime = datetime.time(hour=vstrThisDate.hour, minute=vstrThisDate.minute,
                                                second=vstrThisDate.second)
                    thisSurveyCList.writeDate(strinput=strThisDate)
                    thisSurveyCList.writeTime(strinput=strThisTime)
                    thisSurveyCList.writeTotalContacts(strinput=0)
                    thisSurveyCList.put()
                    self.response.write("Successfully uploaded Survey Contact Lists")
            # Manage Survey Schedules

        elif vstrChoice == "7":

            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
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

                    findRequest = SurveySchedules.query(SurveySchedules.survey_id == vstrSurveyID)
                    thisSurveySchedulesList = findRequest.fetch()

                    findRequest = SurveyContactLists.query(
                        SurveyContactLists.organization_id == thisMainAccount.organization_id)
                    thisContactLists = findRequest.fetch()

                    template = template_env.get_template('templates/surveys/schedules/schedules.html')
                    context = {'thisSurveySchedulesList': thisSurveySchedulesList, 'thisContactLists': thisContactLists,
                               'vstrSurveyID': vstrSurveyID}
                    self.response.write(template.render(context))
            # Create Multi choice surve order

        elif vstrChoice == "8":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):
                vstrSurveyID = self.request.get('vstrSurveyID')

                findRequest = SurveySchedules.query(SurveySchedules.survey_id == vstrSurveyID)
                thisSurveyScheduleList = findRequest.fetch()

                findRequest = SurveyOrders.query(SurveyOrders.survey_id == vstrSurveyID)
                thisOrdersList = findRequest.fetch()

                template = template_env.get_template('templates/surveys/orders/neworder.html')
                context = {'thisSurveyScheduleList': thisSurveyScheduleList, 'vstrSurveyID': vstrSurveyID,
                           'thisOrdersList': thisOrdersList}
                self.response.write(template.render(context))

        elif vstrChoice == "9":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
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

                    findRequest = SurveySchedules.query(SurveySchedules.schedule_id == vstrSelectSchedule)
                    thisSchedulesList = findRequest.fetch()
                    if len(thisSchedulesList) > 0:
                        thisSchedule = thisSchedulesList[0]

                        findRequest = SurveyContactLists.query(SurveyContactLists.list_id == thisSchedule.list_id)
                        thisContactLists = findRequest.fetch()

                        findRequest = Surveys.query(Surveys.survey_id == vstrSurveyID)
                        thisSurveyList = findRequest.fetch()

                        if len(thisSurveyList) > 0:
                            thisSurvey = thisSurveyList[0]

                            if thisSurvey.survey_type == "multichoice":
                                findRequest = MultiChoiceSurveys.query(MultiChoiceSurveys.survey_id == vstrSurveyID)
                                thisMultiChoiceSurveyList = findRequest.fetch()

                                strTotalSurveyQuestions = len(thisMultiChoiceSurveyList)
                            else:
                                strTotalSurveyQuestions = 0
                        else:
                            strTotalSurveyQuestions = 0

                        strTotalContacts = len(thisContactLists)
                        logging.info(thisBudgetPortal.advert_sell_rate)
                        strSellRate = thisBudgetPortal.advert_sell_rate / 100
                        logging.info(strSellRate)
                        strQuotedAmount = float(strTotalContacts * strTotalSurveyQuestions * strSellRate)
                        logging.info(strQuotedAmount)

                        thisSurveyOrder = SurveyOrders()
                        thisSurveyOrder.writeUserID(strinput=vstrUserID)
                        thisSurveyOrder.writeOrganizationID(strinput=thisMainAccount.organization_id)
                        thisSurveyOrder.writeOrderStartDate(strinput=thisSchedule.start_date)
                        thisSurveyOrder.writeOrderStartTime(strinput=thisSchedule.start_time)
                        thisSurveyOrder.writeSurveyID(strinput=thisSchedule.survey_id)
                        thisSurveyOrder.writeItemCount(strinput=1)
                        thisSurveyOrder.writeOrderID(strinput=thisSurveyOrder.CreateOrderID())
                        thisSurveyOrder.writeScheduleID(strinput=thisSchedule.schedule_id)
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
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrCreditToAssign = self.request.get("vstrCreditToAssign")
                vstrAvailableCredit = self.request.get("vstrAvailableCredit")
                vstrSurveyID = self.request.get("vstrSurveyID")

                findRequest = Surveys.query(Surveys.survey_id == vstrSurveyID)
                thisSurveyList = findRequest.fetch()

                if len(thisSurveyList) > 0:
                    thisSurvey = thisSurveyList[0]

                    if int(vstrAvailableCredit) >= int(vstrCreditToAssign):
                        thisSurvey.writeAssignedCredit(strinput=vstrCreditToAssign)

                        thisSurvey.writeRunFromCredit(strinput=True)
                        thisSurvey.writeSurveyIsPaid(strinput=True)
                        thisSurvey.writeSurveyStatus(strinput="Scheduled")

                        thisSurvey.put()

                        findRequest = SurveyAccount.query(SurveyAccount.organization_id == thisSurvey.organization_id)
                        thisSurveyAccountList = findRequest.fetch()

                        vstrAvailableCredit = int(vstrAvailableCredit) - int(vstrCreditToAssign)

                        if len(thisSurveyAccountList) > 0:
                            thisSurveyAccount = thisSurveyAccountList[0]
                            thisSurveyAccount.writeTotalCredits(strinput=vstrAvailableCredit)
                            thisSurveyAccount.put()

                            # TODO- find a way to check if the scheduled date and time is in the feature if not set it in the feature and inform the user of this on the email
                            # TODO- Send an email informing the user that the survey will start running as scheduled
                            # TODO- send an SMS to the user informing them that their survey will run
                            self.response.write("Successfully assigned available credit to Survey")
                        else:
                            self.response.write("Error assiging available Credit")
                    else:
                        self.response.write("Error Insufficient Credit")
                else:
                    self.response.write("Fatal Error Survey not found")


class ThisSurveyContactsListHandler:

    def get(self):
        URL = self.request.url
        strURLlist = URL.split("/")
        strListID = strURLlist[len(strURLlist) - 1]

        findRequest = SurveyContactLists.query(SurveyContactLists.list_id == strListID)
        thisSurveyContactList = findRequest.fetch()

        if len(thisSurveyContactList) > 0:
            thisSurveyConList = thisSurveyContactList[0]
        else:
            thisSurveyConList = SurveyContactLists()

        findRequest = SurveyContacts.query(SurveyContacts.list_id == strListID)
        thisContactList = findRequest.fetch()

        template = template_env.get_template('templates/surveys/contacts/thiscontactlist.html')
        context = {'thisSurveyConList': thisSurveyConList, 'thisContactList': thisContactList}
        self.response.write(template.render(context))

    def post(self):

        vstrChoice = self.request.get('vstrChoice')
        if vstrChoice == "0":

            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):
                vstrListID = self.request.get('vstrListID')

                findRequest = SurveyContacts.query(SurveyContacts.list_id == vstrListID)
                thisContactList = findRequest.fetch()

                template = template_env.get_template('templates/surveys/contacts/sublist.html')
                context = {'thisContactList': thisContactList, 'vstrListID': vstrListID}
                self.response.write(template.render(context))

        elif vstrChoice == "1":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrListID = self.request.get('vstrListID')
                vstrName = self.request.get('vstrNames')
                vstrName = vstrName.strip()
                vstrSurname = self.request.get('vstrSurname')
                vstrSurname = vstrSurname.strip()
                vstrCell = self.request.get('vstrCellNumber')
                vstrCell = vstrCell.strip()
                if not (vstrCell == None) and ((len(vstrCell) == 10) or (len(vstrCell) == 13)):
                    findRequest = SurveyContacts.query(SurveyContacts.list_id == vstrListID,
                                                       SurveyContacts.cell == vstrCell)
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
                    findRequest = SurveyContactLists.query(SurveyContactLists.list_id == vstrListID)
                    thisSurveyConList = findRequest.fetch()
                    if len(thisSurveyConList) > 0:
                        thisSurveyList = thisSurveyConList[0]

                        thisSurveyList.total += 1
                        thisSurveyList.put()

                    self.response.write("Survey Contact Successfully loaded")
                else:
                    self.response.write("Please enter a valid cell phone number")

        # Bulk Upload Contact Lists
        elif vstrChoice == "2":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

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
                                if not (strCell == None) and ((len(strCell) == 10) or (len(strCell) == 13)):
                                    findRequest = SurveyContacts.query(SurveyContacts.list_id == vstrListID,
                                                                       SurveyContacts.cell == strCell)
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
                                    self.response.write(
                                        """Contact Loaded : <strong>""" + thisContact + """</strong> <br> """)
                    except:
                        pass

                findRequest = SurveyContactLists.query(SurveyContactLists.list_id == vstrListID)
                thisContactLister = findRequest.fetch()

                if len(thisContactLister) > 0:
                    thisConLister = thisContactLister[0]
                    thisConLister.total += strTotalLoaded
                    thisConLister.put()

                if strTotalLoaded == 0:
                    self.response.write("Failure while loading you contacts please check your cell numbers")

        # Bulk Remove Contact List
        elif vstrChoice == "3":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrListID = self.request.get('vstrListID')
                vstrListID = vstrListID.strip()
                vstrRemoveCell = self.request.get('vstrRemoveCell')
                vstrRemoveCell = vstrRemoveCell.strip()

                findRequest = SurveyContacts.query(SurveyContacts.cell == vstrRemoveCell,
                                                   SurveyContacts.list_id == vstrListID)
                thisSurveyContactsList = findRequest.fetch()

                isDel = False
                strTotalRemoved = 0
                for thisContact in thisSurveyContactsList:
                    thisContact.key.delete()
                    isDel = True
                    strTotalRemoved += 1

                findRequest = SurveyContactLists.query(SurveyContactLists.list_id == vstrListID)
                thisContactLister = findRequest.fetch()

                if len(thisContactLister) > 0:
                    thisConLister = thisContactLister[0]
                    thisConLister.total = thisConLister.total - strTotalRemoved
                    thisConLister.put()

                if isDel:
                    self.response.write("Survey Contact Deleted Successfully")
                else:
                    self.response.write("Survey Contact not found / Already Deleted")


class ThisSchedulesHandler:

    def get(self):

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken

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
                    strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,
                                                second=strThisTime.second)

                findRequest = SurveySchedules.query(SurveySchedules.survey_id == vstrSurveyID,
                                                    SurveySchedules.name == vstrName)
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


class ThisPaymentHandler:

    def get(self):
        URL = self.request.url
        strURLlist = URL.split("/")
        strOrderID = strURLlist[len(strURLlist) - 1]

        findRequest = SurveyOrders.query(SurveyOrders.order_id == strOrderID)
        thisOrdersList = findRequest.fetch()

        if len(thisOrdersList) > 0:
            thisOrder = thisOrdersList[0]

            template = template_env.get_template('templates/surveys/orders/makepayment.html')
            context = {'thisOrder': thisOrder, 'survey_id': thisOrder.survey_id}
            self.response.write(template.render(context))

    def post(self):
        from accounts import Organization
        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrSurveyID = self.request.get('vstrSurveyID')
                vstrOrderID = self.request.get('vstrOrderID')
                findRequest = SurveyOrders.query(SurveyOrders.order_id == vstrOrderID)
                thisOrderList = findRequest.fetch()
                if len(thisOrderList) > 0:
                    thisOrder = thisOrderList[0]
                    template = template_env.get_template('templates/surveys/orders/subPayment.html')
                    context = {'thisOrder': thisOrder}
                    self.response.write(template.render(context))


        elif vstrChoice == "1":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrDepositAmount = self.request.get('vstrDepositAmount')
                vstrDepositMethod = self.request.get('vstrDepositMethod')
                vstrSurveyID = self.request.get('vstrSurveyID')
                vstrOrderID = self.request.get('vstrOrderID')

                findRequest = SurveyOrders.query(SurveyOrders.order_id == vstrOrderID)
                thisSurveyOrdersList = findRequest.fetch()

                if len(thisSurveyOrdersList) > 0:
                    thisSurveyOrder = thisSurveyOrdersList[0]

                    if int(vstrDepositAmount) > 0:
                        vstrThisDate = datetime.datetime.now()
                        strThisDate = vstrThisDate.date()
                        strThisTime = datetime.time(hour=vstrThisDate.hour, minute=vstrThisDate.minute,
                                                    second=vstrThisDate.second)

                        thisPayment = SurveyPayments()

                        thisPayment.writeUserID(strinput=vstrUserID)
                        thisPayment.writeOrderID(strinput=thisSurveyOrder.order_id)
                        thisPayment.writeOrganizationID(strinput=thisSurveyOrder.organization_id)
                        thisPayment.writeDepositReference(strinput=thisSurveyOrder.deposit_reference)
                        thisPayment.writePaymentID(strinput=thisPayment.CreatePaymentID())
                        thisPayment.writeAmountPaid(strinput=vstrDepositAmount)
                        thisPayment.writePaymentMethod(strinput=vstrDepositMethod)
                        thisPayment.writeDatePaid(strinput=strThisDate)
                        thisPayment.writeTimePaid(strinput=strThisTime)
                        thisPayment.writePaymentVerified(strinput=False)
                        thisPayment.put()
                        self.response.write("""
                        Payment request Successfully generated please <a href="/surveys/invoices/""" + thisPayment.payment_id + """">click here to print your invoice</a>                        
                        """)


class ThisInvoicesHandler:
    def get(self):

        from accounts import Organization

        URL = self.request.url
        strURLlist = URL.split("/")
        strPaymentID = strURLlist[len(strURLlist) - 1]

        findRequest = SurveyPayments.query(SurveyPayments.payment_id == strPaymentID)
        thisSurveyPaymentList = findRequest.fetch()

        if len(thisSurveyPaymentList) > 0:
            thisPayment = thisSurveyPaymentList[0]

            findRequest = Organization.query(Organization.strOrganizationID == thisPayment.organization_id)
            thisOrgList = findRequest.fetch()
            if len(thisOrgList) > 0:
                thisOrg = thisOrgList[0]
            else:
                thisOrg = Organization()

            findRequest = SurveyOrders.query(SurveyOrders.order_id == thisPayment.order_id)
            thisOrdersList = findRequest.fetch()

            if len(thisOrdersList) > 0:
                thisOrder = thisOrdersList[0]

                findRequest = Surveys.query(Surveys.survey_id == thisOrder.survey_id)
                thisSurveyList = findRequest.fetch()

                if len(thisSurveyList) > 0:
                    thisSurvey = thisSurveyList[0]
                else:
                    thisSurvey = Surveys()

                template = template_env.get_template('templates/surveys/orders/directdeposit.html')
                context = {'thisOrg': thisOrg, 'thisPayment': thisPayment, 'thisSurvey': thisSurvey}
                self.response.write(template.render(context))


class ThisSurveyScheduleHandler:
    def get(self):
        URL = self.request.url
        strURLlist = URL.split("/")
        strScheduleID = strURLlist[len(strURLlist) - 1]

        findRequest = SurveySchedules.query(SurveySchedules.schedule_id == strScheduleID)
        thisSurveyScheduleList = findRequest.fetch()

        if len(thisSurveyScheduleList) > 0:
            thisSchedule = thisSurveyScheduleList[0]
        else:
            thisSchedule = SurveySchedules()

        template = template_env.get_template('templates/surveys/schedules/thisSchedule.html')
        context = {'thisSchedule': thisSchedule}
        self.response.write(template.render(context))

    def post(self):

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrScheduleID = self.request.get('vstrScheduleID')

                findRequest = SurveySchedules.query(SurveySchedules.schedule_id == vstrScheduleID)
                thisSurveyScheduleList = findRequest.fetch()

                if len(thisSurveyScheduleList) > 0:
                    thisSchedule = thisSurveyScheduleList[0]
                else:
                    thisSchedule = SurveySchedules()

                template = template_env.get_template('templates/surveys/schedules/subSchedule.html')
                context = {'thisSchedule': thisSchedule}
                self.response.write(template.render(context))

        elif vstrChoice == "1":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
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

                    thisDate = datetime.date(year=int(vstrYear), month=int(vstrMonth), day=int(vstrDay))
                    thisTime = datetime.time(hour=int(vstrHour), minute=int(vstrMinute), second=int(vstrSecond))

                    findRequest = SurveySchedules.query(SurveySchedules.schedule_id == vstrScheduleID)
                    thisSurveyScheduleList = findRequest.fetch()

                    if len(thisSurveyScheduleList) > 0:
                        thisSchedule = thisSurveyScheduleList[0]

                        thisSchedule.writeStartTime(strinput=thisTime)
                        thisSchedule.writeStartDate(strinput=thisDate)
                        thisSchedule.writeNotifyOnStart(strinput=vstrNotifyOnStart)
                        thisSchedule.writeNotifyOnEnd(strinput=vstrNotifyOnEnd)
                        thisSchedule.writeName(strinput=vstrName)
                        thisSchedule.writeDescription(strinput=vstrDescription)
                        thisSchedule.writeActivateSchedule(strinput=vstrActivateSchedule)
                        thisSchedule.put()
                        self.response.write("Successfully update schedule")
                    else:
                        self.response.write("Error Unable to find your schedule")
                except:
                    self.response.write("There was an error with your input please rectify the error and try again")

        elif vstrChoice == "2":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrScheduleID = self.request.get('vstrScheduleID')

                findRequest = SurveySchedules.query(SurveySchedules.schedule_id == vstrScheduleID)
                thisScheduleList = findRequest.fetch()

                for thisSchedule in thisScheduleList:
                    findRequest = SurveyOrders.query(SurveyOrders.schedule_id == thisSchedule.schedule_id)
                    thisOrdersList = findRequest.fetch()
                    if len(thisOrdersList) > 0:
                        self.response.write("Schedule cannot be deleted as there are orders based on the schedule")
                    else:
                        thisSchedule.key.delete()
                        self.response.write("Schedule Deleted successfully")


class ThisTopUpInvoiceHandler:
    def get(self):
        from accounts import Organization

        URL = self.request.url
        strURLlist = URL.split("/")
        strTopUpReference = strURLlist[len(strURLlist) - 1]

        findRequest = SurveyAccount.query(SurveyAccount.top_up_reference == strTopUpReference)
        thisSurveyAccountList = findRequest.fetch()

        logging.info("INVOICE HANDLER RUNNING ............")

        if len(thisSurveyAccountList) > 0:
            thisSurveyAccount = thisSurveyAccountList[0]

            findRequest = Organization.query(Organization.strOrganizationID == thisSurveyAccount.organization_id)
            thisOrgList = findRequest.fetch()
            if len(thisOrgList) > 0:
                thisOrg = thisOrgList[0]
            else:
                thisOrg = Organization()

            findRequest = AccountDetails.query()
            thisBluetITAccountList = findRequest.fetch()

            if len(thisBluetITAccountList) > 0:
                thisBlueITAccount = thisBluetITAccountList[0]
            else:
                thisBlueITAccount = AccountDetails()

            template = template_env.get_template("templates/surveys/sub/topupproforma.html")
            context = {'thisOrg': thisOrg, 'thisSurveyAccount': thisSurveyAccount,
                       'thisBlueITAccount': thisBlueITAccount}
            self.response.write(template.render(context))

    def post(self):
        from dashboard import TopUpVerifications

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrTopUpReference = self.request.get("vstrTopUpReference")
                vstrYourReferenceNumber = self.request.get("vstrYourReferenceNumber")
                vstrDepositSlipFile = self.request.get("vstrDepositSlipFile")

                findRequest = SurveyAccount.query(SurveyAccount.organization_id == thisMainAccount.organization_id)
                thisSurveyAccountList = findRequest.fetch()

                if len(thisSurveyAccountList) > 0:
                    thisSurveyAccount = thisSurveyAccountList[0]
                    if vstrYourReferenceNumber == vstrTopUpReference:
                        thisSurveyAccount.writeDepositSlipFilename(strinput=vstrDepositSlipFile)
                        thisSurveyAccount.put()
                        thisVerifications = TopUpVerifications()
                        thisVerifications.writeOrganizationID(strinput=thisSurveyAccount.organization_id)
                        thisVerifications.writeAccountName(strinput="Surveys")
                        thisVerifications.writeCreditAmount(strinput=thisSurveyAccount.total_top_up_cost)
                        thisVerifications.writeDepositSlipFileName(strinput=vstrDepositSlipFile)
                        thisVerifications.writeSMSCredits(strinput=thisSurveyAccount.top_up_credit)
                        thisVerifications.writeTopUpReference(strinput=vstrYourReferenceNumber)
                        thisVerifications.put()

                        self.response.write("Successfully Uploaded Deposit slip file : " + vstrDepositSlipFile)
                    else:
                        thisSurveyAccount.writeDepositSlipFilename(strinput=vstrDepositSlipFile)
                        thisSurveyAccount.put()
                        thisVerifications = TopUpVerifications()
                        thisVerifications.writeOrganizationID(strinput=thisSurveyAccount.organization_id)
                        thisVerifications.writeAccountName(strinput="Surveys")
                        thisVerifications.writeCreditAmount(strinput=thisSurveyAccount.total_top_up_cost)
                        thisVerifications.writeDepositSlipFileName(strinput=vstrDepositSlipFile)
                        thisVerifications.writeSMSCredits(strinput=thisSurveyAccount.top_up_credit)
                        thisVerifications.writeTopUpReference(strinput=vstrTopUpReference)
                        thisVerifications.put()

                        self.response.write(
                            "Reference Verification Error, deposit will take longer to verify please use our support tickets to enquire if it takes more than three days")


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

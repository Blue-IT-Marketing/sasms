import os
import jinja2
from google.cloud import ndb
import logging
import datetime

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class SecurityLog(ndb.Model):

    client_ip = ndb.StringProperty()
    recent_counter = ndb.IntegerProperty(default=0)

    username = ndb.StringProperty()
    date_accessed = ndb.DateProperty()
    time_accessed = ndb.TimeProperty()
    affiliate_link = ndb.StringProperty()
    lock_account = ndb.BooleanProperty(default=False)


    def writeClientIP(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.client_ip = strinput
                return True
            else:
                return False
        except:
            return False

    def writeUserName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.username = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAffiliateLink(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.affiliate_link = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateAccessed(self,strinput):
        try:

            if isinstance(strinput,datetime.date):
                self.date_accessed = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeAccessed(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.time_accessed = strinput
                return True
            else:
                return False
        except:
            return False

class SMSMarket(ndb.Model):
    offer_price = ndb.IntegerProperty(default=25)

    def writeOfferPrice(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.offer_price = int(strinput)
                return True
            else:
                return False
        except:
            return False

class MyAffiliates(ndb.Expando):
    uid = ndb.StringProperty()
    affiliate_id = ndb.StringProperty() # User ID for the Account which is affiliated by this user
    date_created = ndb.DateProperty(auto_now_add=True)
    time_created = ndb.TimeProperty(auto_now_add=True)
    credits = ndb.IntegerProperty(default=0)

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
    def writeAffiliateID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.affiliate_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCredits(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.credits += int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.date_created = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.time_created = strinput
                return True
            else:
                return False
        except:
            return False

class Affiliate(ndb.Expando):
    uid = ndb.StringProperty()
    organization_id = ndb.StringProperty() #TODO- Intergrate organization ID with the affiliate account
    strAffiliateLink = ndb.StringProperty()
    strHitCounter = ndb.IntegerProperty(default=0)
    strTotalSubscriptions = ndb.IntegerProperty(default=0)
    strDiscount = ndb.IntegerProperty(default=0)
    strDate = ndb.DateProperty(auto_now_add=True)
    strTime = ndb.TimeProperty(auto_now_add=True)
    strPaymentMethod = ndb.StringProperty(default="Bank Deposit") # E-Wallet, Buy SMS
    strAvailableCredit = ndb.IntegerProperty(default=0)

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
    def writeAffiliateLink(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAffiliateLink = strinput
                return True
            else:
                return False
        except:
            return False
    def addHitCounter(self):
        try:
            self.strHitCounter += 1
            return True
        except:
            return False
    def addSubscriber(self):
        try:
            self.strTotalSubscriptions += 1
            return True
        except:
            return False
    def RemoveSubscriber(self):
        try:
            self.strTotalSubscriptions -= 1
            return True
        except:
            return False
    def writeDiscount(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strDiscount = int(strinput)
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
    def CreateAffiliateLink(self):
        import random,string
        try:
            strAffiliateLink = ""
            for i in range(128):
                strAffiliateLink += random.SystemRandom().choice(string.digits + string.ascii_lowercase)

            return strAffiliateLink
        except:
            return None
    def writePaymentMethod(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ["Bank Deposit","E-Wallet","Buy SMS"]:
                self.strPaymentMethod = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAvailableCredit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strAvailableCredit += int(strinput)
                return True
            else:
                return False
        except:
            return False

class PresentCredits(ndb.Expando):
    strUserID = ndb.StringProperty()
    strThisDate = ndb.DateProperty() # This Calculation to be performed after end of every month for each user
    strEarnedCredit = ndb.IntegerProperty(default=0) # Total Earned Credit
    strCreditPaid = ndb.BooleanProperty(default=False) # Total Paid Credit
    strPaidAmount = ndb.IntegerProperty(default=0)


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
    def writeThisDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strThisDate = strinput
                return True
            else:
                return False
        except:
            return False
    def AddCredit(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strEarnedCredit += int(strinput)
                return True
            else:
                return False
        except:
            return False
    def SubTractCredit(self, strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strEarnedCredit = self.strEarnedCredit - int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeCreditPaid(self,strinput):
        try:
            if strinput in [True,False]:
                self.strCreditPaid = strinput
                return True
            else:
                return False
        except:
            return False

class PaymentBankAccount(ndb.Expando):
    strUserID = ndb.StringProperty()

    strAccountHolder = ndb.StringProperty()
    strAccountNumber = ndb.StringProperty()

    strBankName = ndb.StringProperty()
    strBranchName = ndb.StringProperty()
    strBranchCode = ndb.StringProperty()

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

    def writeAccountHolder(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccountHolder = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAccountNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccountNumber = strinput
                return True
            else:
                return False
        except:
            return False

    def writeBankName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBankName = strinput
                return True
            else:
                return False
        except:
            return False

    def writeBranchName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBranchName = strinput
                return True
            else:
                return False
        except:
            return False

    def writeBranchCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBranchCode = strinput
                return True
            else:
                return False
        except:
            return False

class WithdrawalRequests(ndb.Expando):

    strUserID = ndb.StringProperty()
    strWithdrawalID = ndb.StringProperty()
    strAmount = ndb.FloatProperty()
    strMethod = ndb.StringProperty(default="Bank Deposit") # E-Wallet
    strDateCreated = ndb.DateProperty(auto_now_add=True)
    strTimeCreated = ndb.TimeProperty(auto_now_add=True)
    strDateToProcess = ndb.DateProperty()
    strWithDrawalStatus = ndb.StringProperty(default="Pending") # Complete

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
    def writeAmount(self,strinput):
        try:
            if isinstance(strinput,float):
                self.strAmount = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMethod(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMethod = strinput
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
    def writeDateToProcess(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateToProcess = strinput
                return True
            else:
                return False

        except:
            return False
    def writeWithdrawalID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strWithdrawalID = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateWithDrawalID(self):
        import string,random
        try:
            strWithdrawalID = ""
            for i in range(255):
                strWithdrawalID += random.SystemRandom().choice(string.digits + string.ascii_lowercase)
            return strWithdrawalID
        except:
            return None

    def writeWithDrawalStatus(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strWithDrawalStatus = strinput
                return True
            else:
                return False
        except:
            return False

class HitCounter(ndb.Expando):

    strAffiliateLink = ndb.StringProperty()

    strHitCounter = ndb.IntegerProperty(default=0)
    strVisitorsCount = ndb.IntegerProperty(default=0)
    strRegCounter = ndb.IntegerProperty(default=0)
    strTimeSpentOnPage = ndb.IntegerProperty(default=0) # Time in Seconds
    strDate = ndb.DateProperty(auto_now_add=True)
    strTime = ndb.TimeProperty(auto_now_add=True)

    def writeAffiliateLink(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAffiliateLink = strinput
                return True
            else:
                return False
        except:
            return False
    def AddHitCounter(self):
        try:
            self.strHitCounter += 1
            return True
        except:
            return False
    def AddVisitorCount(self):
        try:
            self.strVisitorsCount += 1
            return True
        except:
            return False
    def AddRegCounter(self):
        try:
            self.strRegCounter += 1
            return True
        except:
            return False
    def writeTimeSpentOnPage(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTimeSpentOnPage = int(strinput)
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

class Twitter(ndb.Expando):
    strUserID = ndb.StringProperty()
    strAffiliateLink = ndb.StringProperty()

    strConsumerAPI = ndb.StringProperty(default=os.environ.get('TWITTER_CONSUMER_API'))
    strConsumerSecret = ndb.StringProperty(default=os.environ.get('TWITTER_CONSUMER_SECRET'))
    strAccessTokenKey = ndb.StringProperty(default=os.environ.get('TWITTER_ACCESS_TOKEN_KEY'))
    strAccessTokenSecret = ndb.StringProperty(default=os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'))

    strCallBackURL = ndb.StringProperty(default="https://sa-sms.appspot.com")
    strAPPOnlyAuthentication = ndb.StringProperty(default="https://api.twitter.com/oauth2/token")
    strRequestTokenURL = ndb.StringProperty(default="https://api.twitter.com/oauth/request_token")
    strAuthorizeURL = ndb.StringProperty(default="https://api.twitter.com/oauth/authorize")
    strAccessTokenURL = ndb.StringProperty(default="https://api.twitter.com/oauth/access_token")


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
    def writeAffiliateLink(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAffiliateLink = strinput
                return True
            else:
                return False
        except:
            return False
    def writeConsumerAPI(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strConsumerAPI = strinput
                return True
            else:
                return False
        except:
            return False
    def writeConsumerSecret(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strConsumerSecret = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCallBackURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCallBackURL = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAPPOnlyAuthenticationURL(self,strinput):
        try:
            strinput = str(strinput)

            if strinput != None:
                self.strAPPOnlyAuthentication = strinput
                return True
            else:
                return False
        except:
            return False
    def writeRequestTokenURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strRequestTokenURL = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAuthorizeURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAuthorizeURL = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAccessTokenURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccessTokenURL = strinput
                return True
            else:
                return False
        except:
            return False

class MyFacebook(ndb.Expando):
    strUserID = ndb.StringProperty()
    strAffiliateLink = ndb.StringProperty()
    strFacebookAPI = ndb.StringProperty()
    strFacebookSecretCode = ndb.StringProperty()
    strFacebookGroupIDList = ndb.TextProperty()

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
    def writeAffiliateLink(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput  == None):
                self.strAffiliateLink = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFacebookAPI(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFacebookAPI = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFacebookSecretCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFacebookSecretCode = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFacebookGroupIDList(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFacebookGroupIDList = strinput
                return True
            else:
                return False
        except:
            return False

class TransactionHistory(ndb.Expando):
    strUserID = ndb.StringProperty()
    strTransactionID = ndb.StringProperty()
    strDate = ndb.DateProperty()
    strTime = ndb.TimeProperty()
    strTransactionType = ndb.StringProperty(default="Withdrawal") # Buy SMS
    strWithDrawalID = ndb.StringProperty()
    strStatus = ndb.StringProperty(default="Pending") # Complete

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
    def writeTransactionID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTransactionID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDate(self,strinput):
        try:
            if not(strinput,datetime.date):
                self.strDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTime(self,strinput):
        try:
            if not(strinput,datetime.time):
                self.strTime = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTransactionType(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTransactionType = strinput
                return True
            else:
                return False
        except:
            return False
    def writeWithDrawalID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strWithDrawalID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeWithDrawalStatus(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strStatus = strinput
                return True
            else:
                return False
        except:
            return False

from firebaseadmin import VerifyAndReturnAccount

class AffiliateHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/affiliate/affiliate.html')
        context = {}
        self.response.write(template.render(context))

    def post(self):
        from mysms import SMSAccount
        from accounts import Accounts, UserRights,Organization

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = PresentCredits.query(PresentCredits.strUserID == vstrUserID)
                CreditList = findRequest.fetch()

                findRequest = Affiliate.query(Affiliate.uid == vstrUserID)
                thisAffiliateList = findRequest.fetch()

                if len(thisAffiliateList) > 0:
                    thisAffiliate = thisAffiliateList[0]

                    findRequest = SMSMarket.query()
                    SMSMarketList = findRequest.fetch()

                    if len(SMSMarketList) > 0:
                        thisSMSMarket = SMSMarketList[0]
                    else:
                        thisSMSMarket = SMSMarket()

                    findRequest = TransactionHistory.query(TransactionHistory.strUserID == vstrUserID)
                    thisTransactionList = findRequest.fetch()
                else:
                    thisAffiliate = Affiliate()
                    thisSMSMarket = SMSMarket()
                    thisTransactionList = []



                template = template_env.get_template('templates/affiliate/sub/credits.html')
                context = {'CreditList':CreditList,'thisAffiliate':thisAffiliate,'thisSMSMarket':thisSMSMarket,'thisTransactionList':thisTransactionList}
                self.response.write(template.render(context))

        elif vstrChoice == "1":

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = Affiliate.query(Affiliate.uid == vstrUserID)
                thisAffiliateList = findRequest.fetch()

                if len(thisAffiliateList) > 0:
                    thisAffiliate = thisAffiliateList[0]
                else:
                    thisAffiliate = Affiliate()

                findRequest = MyAffiliates.query(MyAffiliates.uid == vstrUserID)
                thisMyAffiliatesList = findRequest.fetch()

                template = template_env.get_template('templates/affiliate/sub/Accountdetails.html')
                context = {'thisAffiliate':thisAffiliate,'thisMyAffiliatesList':thisMyAffiliatesList}
                self.response.write(template.render(context))

        elif vstrChoice == "2":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')


            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrAffiliateLink = self.request.get('vstrAffiliateLink')

                findRequest = Affiliate.query(Affiliate.strAffiliateLink == vstrAffiliateLink)
                thisAffiliateList = findRequest.fetch()

                if len(thisAffiliateList) > 0:
                    self.response.write("NO")
                else:
                    self.response.write("YES")

        elif vstrChoice == "3":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrAffiliateLink = self.request.get('vstrAffiliateLink')
            vstrPaymentMethod = self.request.get('vstrPaymentMethod')
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                findRequest = Affiliate.query(Affiliate.strAffiliateLink == vstrAffiliateLink)
                thisAffiliateLinkList = findRequest.fetch()

                if len(thisAffiliateLinkList) > 0:
                    thisLinkAffiliate = thisAffiliateLinkList[0]

                    findRequest = Affiliate.query(Affiliate.uid == vstrUserID)
                    thisAffiliateList = findRequest.fetch()

                    if len(thisAffiliateList) > 0:
                        thisAffiliate = thisAffiliateList[0]

                        if thisLinkAffiliate.uid == thisAffiliate.uid:
                            thisAffiliate.writeAffiliateLink(strinput=vstrAffiliateLink)
                            thisAffiliate.writePaymentMethod(strinput=vstrPaymentMethod)
                            thisAffiliate.put()
                            self.response.write("Successfully updated Affiliate Account")
                        else:
                            self.response.write("you cannot change your Affiliate Link as the one you are choosing has already been used or you have already changed your affiliate link")
                    else:
                        self.response.write("Fatal Error your affiliate account isnt configured")
                else:
                    findRequest = Affiliate.query(Affiliate.uid == vstrUserID)
                    thisAffiliateList = findRequest.fetch()

                    if len(thisAffiliateList) > 0:
                        thisAffiliate = thisAffiliateList[0]
                        thisAffiliate.writeAffiliateLink(strinput=vstrAffiliateLink)
                        thisAffiliate.writePaymentMethod(strinput=vstrPaymentMethod)
                        thisAffiliate.put()
                        self.response.write("Successfully updated Affiliate Account")
                    else:
                        self.response.write("Fatal Error Affiliate account not found")


        elif vstrChoice == "4":
            vstrSpendCredit = self.request.get('vstrSpendCredit')

            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')


            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = SMSAccount.query(SMSAccount.strOrganizationID == thisMainAccount.organization_id)
                thisSMSAccountList = findRequest.fetch()

                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]

                    findRequest = Affiliate.query(Affiliate.uid == vstrUserID)
                    thisAffiliateList = findRequest.fetch()

                    if len(thisAffiliateList) > 0:
                        thisAffiliate = thisAffiliateList[0]

                        if (not(vstrSpendCredit == None) ) and (thisAffiliate.strAvailableCredit >= int(vstrSpendCredit)):

                            if thisSMSAccount.AddTotalSMS(strinput=vstrSpendCredit):
                                thisAffiliate.strAvailableCredit -= int(vstrSpendCredit)
                                thisSMSAccount.put()
                                thisAffiliate.put()
                                self.response.write("Successfully bought SMS Credits for your organization main SMS Account")
                        else:
                            self.response.write("Spend Credit Error or not enough Available Credits")
                else:
                    self.response.write("SMS Account not found error Buying Credits")

        elif vstrChoice == "5":
            vstrWithdrawalAmount = self.request.get('vstrWithdrawalAmount')
            vstrSelectMethod = self.request.get('vstrSelectMethod')
            vstrWithDrawCredit  = self.request.get('vstrWithDrawCredit')
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')


            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = Affiliate.query(Affiliate.uid == thisMainAccount.uid)
                thisAffiliateList = findRequest.fetch()

                if len(thisAffiliateList) > 0:
                    thisAffiliate = thisAffiliateList[0]

                    if thisAffiliate.strAvailableCredit <= int(vstrWithDrawCredit):
                        thisAffiliate.strAvailableCredit -= int(vstrWithDrawCredit)
                        thisWithDrawalRequest = WithdrawalRequests()
                        thisWithDrawalRequest.writeUserID(strinput=thisMainAccount.uid)
                        vstrWithdrawalAmount = str(vstrWithdrawalAmount)
                        if not (vstrWithdrawalAmount == "0"):
                            vstrWithdrawalAmount = float(vstrWithdrawalAmount)
                            thisWithDrawalRequest.writeAmount(strinput=vstrWithdrawalAmount)
                            strThisDateTime = datetime.datetime.now()
                            strThisDate = strThisDateTime.date()
                            strThisTime = strThisDateTime.time()
                            strThisProcessDate = strThisDateTime
                            strThisProcessDate += datetime.timedelta(days=3)
                            strThisProcessDate = strThisProcessDate.date()

                            thisWithDrawalRequest.writeDateCreated(strinput=strThisDate)
                            thisWithDrawalRequest.writeTimeCreated(strinput=strThisTime)
                            thisWithDrawalRequest.writeDateToProcess(strinput=strThisProcessDate)
                            thisWithDrawalRequest.writeMethod(strinput=vstrSelectMethod)
                            thisWithDrawalRequest.writeWithdrawalID(strinput=thisWithDrawalRequest.CreateWithDrawalID())
                            thisWithDrawalRequest.put()
                            thisAffiliate.put()
                            self.response.write(
                                "Successffully processed your withdrawal Requests your withdrawal can take up to three business days to be finalized")
                        else:
                            self.response.write("Cannot process withdrawal please check your withdrawal amount")
                    else:
                        self.response.write("You do not have enough credit to process this withdrawal request")
                else:
                    self.response.write("Error with your affiliate account")


        elif vstrChoice == "6":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = Affiliate.query(Affiliate.uid == thisMainAccount.uid)
                thisAffiliateList = findRequest.fetch()

                if len(thisAffiliateList) > 0:
                    thisAffiliate = thisAffiliateList[0]

                    findRequest = HitCounter.query(HitCounter.strAffiliateLink == thisAffiliate.affiliate_link)
                    thisHitCountersList = findRequest.fetch()

                    if len(thisHitCountersList) > 0:
                        thisHitCounter = thisHitCountersList[0]
                    else:
                        thisHitCounter = HitCounter()

                    template = template_env.get_template('templates/affiliate/sub/statistics.html')
                    context = {'thisHitCounter':thisHitCounter}
                    self.response.write(template.render(context))

        elif vstrChoice == "7":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):
                findRequest = Affiliate.query(Affiliate.uid == vstrUserID)
                thisAffiliateList = findRequest.fetch()

                if len(thisAffiliateList) > 0:
                    thisAffiliate = thisAffiliateList[0]
                    findRequest = MyFacebook.query(MyFacebook.strUserID == vstrUserID)
                    thisFacebookList = findRequest.fetch()


                    if len(thisFacebookList) > 0:
                        thisFacebook = thisFacebookList[0]
                    else:
                        thisFacebook = MyFacebook()
                        thisFacebook.writeAffiliateLink(strinput=thisAffiliate.affiliate_link)
                        thisFacebook.writeUserID(strinput=vstrUserID)
                        thisFacebook.put()


                    template = template_env.get_template('templates/affiliate/sub/social.html')
                    context = {'thisSocial':thisFacebook}
                    self.response.write(template.render(context))

        elif vstrChoice == "8":
            vstrFacebook = self.request.get('vstrFacebook')
            vstrFacebookCodeSecret = self.request.get('vstrFacebookCodeSecret')
            vstrGroupIDs = self.request.get('vstrGroupIDs')
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID,strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrGroupList = vstrGroupIDs.split(",")

                vstrGroupStr = ""

                for GroupID in vstrGroupList:
                    vstrGroupStr = vstrGroupStr + "," + GroupID

                findRequest = MyFacebook.query(MyFacebook.strUserID == vstrUserID)
                thisFacebookList = findRequest.fetch()

                if len(thisFacebookList) > 0:
                    thisFacebook = thisFacebookList[0]
                else:
                    thisFacebook = MyFacebook()

                thisFacebook.writeUserID(strinput=vstrUserID)
                thisFacebook.writeFacebookAPI(strinput=vstrFacebook)
                thisFacebook.writeFacebookSecretCode(strinput=vstrFacebookCodeSecret)
                thisFacebook.writeFacebookGroupIDList(strinput=vstrGroupStr)
                thisFacebook.put()
                self.response.write("Facebook Settings successfully saved")

        elif vstrChoice == "9":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
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


                findRequest = Affiliate.query(Affiliate.organization_id == thisMainAccount.organization_id)
                thisAffiliateList = findRequest.fetch()

                if len(thisAffiliateList) > 0:
                    thisAffiliate = thisAffiliateList[0]
                else:
                    thisAffiliate = Affiliate()
                    thisAffiliate.writeUserID(strinput=vstrUserID)
                    thisAffiliate.writeOrganizationID(strinput=thisMainAccount.organization_id)
                    thisAffiliate.writeAffiliateLink(thisAffiliate.CreateAffiliateLink())
                    thisAffiliate.put()


                template = template_env.get_template('templates/affiliate/sub/submenu.html')
                context = {'thisAffiliate': thisAffiliate, 'thisOrg': thisOrg}
                self.response.write(template.render(context))

        #Ipdate Twitter
        elif vstrChoice == "10":
            pass



class AffiliatePublicHandler(webapp2.RequestHandler):
    def get(self):
        import time
        from datetime import timedelta

        URL = self.request.url

        strRemoteUser = self.request.remote_user
        try:
            if os.environ["REMOTE_ADDR"] != None:
                strIPAddress = os.environ["REMOTE_ADDR"]
            else:
                strIPAddress = self.request.remote_addr
        except:
            strIPAddress = self.request.remote_addr


        strURLlist = URL.split("/")

        strAffiliateLink = strURLlist[len(strURLlist) - 1]
        findRequest = SecurityLog.query(SecurityLog.client_ip == strIPAddress)
        thisSecurityLogList = findRequest.fetch()

        thisDateTime = datetime.datetime.now()
        strThisDay = thisDateTime.date()
        strThisTime = thisDateTime.time()
        strThisTime = datetime.time(hour=strThisTime.hour,minute=strThisTime.minute,second=strThisTime.second)

        findRequest = HitCounter.query(HitCounter.strAffiliateLink == strAffiliateLink,HitCounter.strDate == strThisDay,HitCounter.strTime == strThisTime)
        thisHitCounterList = findRequest.fetch()

        if len(thisHitCounterList) > 0:
            thisHitCounter = thisHitCounterList[0]
        else:
            thisHitCounter = HitCounter()
            thisHitCounter.writeAffiliateLink(strinput=strAffiliateLink)
            thisHitCounter.writeDate(strinput=strThisDay)
            thisHitCounter.writeTime(strinput=strThisTime)


        thisHitCounter.AddHitCounter()

        if len(thisSecurityLogList) > 0:
            thisSecurityLog = thisSecurityLogList[0]

        else:
            thisSecurityLog = SecurityLog()
            thisSecurityLog.writeClientIP(strinput=strIPAddress)
            thisSecurityLog.writeUserName(strinput=strRemoteUser)
            thisHitCounter.AddVisitorCount()


        strThisDateTime = datetime.datetime.now()
        strThisDate = strThisDateTime.date()
        strThisTime = strThisDateTime.time()
        strSecureThisTime = strThisDateTime
        strSecureThisTime = strSecureThisTime + timedelta(minutes=1)
        strSecureThisTime = strSecureThisTime.time()


        thisHitCounter.put()


        if thisSecurityLog.lock_account:
            time.sleep(30)
            thisSecurityLog.recent_counter = 0
            thisSecurityLog.lock_account = False


        findRequest = Affiliate.query(Affiliate.strAffiliateLink == strAffiliateLink)
        thisAffiliateList = findRequest.fetch()

        if len(thisAffiliateList) > 0:
            thisAffiliate = thisAffiliateList[0]
            if (not(thisSecurityLog.time_accessed == None)) and (thisSecurityLog.time_accessed < strSecureThisTime):
                thisSecurityLog.recent_counter += 1
            else:
                thisSecurityLog.recent_counter = 0

            if thisSecurityLog.recent_counter > 35:
                thisSecurityLog.lock_account = True
            else:
                thisSecurityLog.lock_account = False

            thisSecurityLog.writeDateAccessed(strinput=strThisDate)
            thisSecurityLog.writeTimeAccessed(strinput=strThisTime)

            thisSecurityLog.put()

            findRequest = MyFacebook.query(MyFacebook.strUserID == thisAffiliate.uid)
            thisFacebookList = findRequest.fetch()

            if len(thisFacebookList) > 0:
                thisFacebook = thisFacebookList[0]
            else:
                thisFacebook = MyFacebook()


            template = template_env.get_template('templates/affiliate/sub/public.html')
            context = {'thisAffiliate':thisAffiliate,'thisHitCounter':thisHitCounter,'thisSocial':thisFacebook}
            self.response.write(template.render(context))
        else:
            time.sleep(30)

app = webapp2.WSGIApplication([
    ('/affiliates', AffiliateHandler),
    ('/affiliates/public/.*', AffiliatePublicHandler)
], debug=True)
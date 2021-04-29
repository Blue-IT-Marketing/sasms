
import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import mail
import datetime
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


class ContactMessages(ndb.Expando):
    strMessageReference = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strSubject = ndb.StringProperty()
    strMessage = ndb.StringProperty()
    strMessageExcerpt = ndb.StringProperty()

    strDateSubmitted = ndb.DateProperty(auto_now_add=True)
    strTimeSubmitted = ndb.TimeProperty(auto_now_add=True)

    strResponseSent = ndb.BooleanProperty(default=False)

    def readDateSubmitted(self):
        try:
            strTemp = str(self.strDateSubmitted)
            strTemp = strTemp.strip()

            return strTemp
        except:
            return None
    def readTimeSubmitted(self):
        try:
            strTemp = str(self.strTimeSubmitted)
            strTemp = strTemp.strip()

            return strTemp
        except:
            return None
    def readResposeSent(self):
        try:
            return self.strResponseSent
        except:
            return False
    def writeResponseSent(self,strinput):
        try:

            if strinput in [True,False]:
                self.strResponseSent = strinput
                return True
            else:
                return False
        except:
            return False

    def readNames(self):
        try:
            strTemp = str(self.strNames)
            strTemp = strTemp.strip()

            if strTemp != None:
                return strTemp
            else:
                return None
        except:
            return None
    def writeNames(self,strinput):
        try:
            strinput = str(strinput)
            strinput = strinput.strip()

            if strinput != None:
                self.strNames = strinput
                return True
            else:
                return False
        except:
            return False
    def readEmail(self):
        try:
            strTemp = str(self.strEmail)
            strTemp = strTemp.strip()

            if strTemp != None:
                return strTemp
            else:
                return None
        except:
            return None
    def writeEmail(self,strinput):
        try:
            strinput = str(strinput)
            strinput = strinput.strip()

            if strinput != None:
                self.strEmail = strinput
                return True
            else:
                return False
        except:
            return False
    def readCell(self):
        try:
            strTemp = str(self.strCell)
            strTemp = strTemp.strip()

            if strTemp != None:
                return strTemp
            else:
                return None
        except:
            return None
    def writeCell(self,strinput):
        try:

            strinput = str(strinput)
            strinput = strinput.strip()

            if strinput != None:
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False
    def readSubject(self):
        try:
            strTemp = str(self.strSubject)
            strTemp = strTemp.strip()

            if strTemp != None:
                return strTemp
            else:
                return None

        except:
            return None
    def writeSubject(self,strinput):
        try:
            strinput = str(strinput)
            strinput = strinput.strip()

            if strinput != None:
                self.strSubject = strinput
                return True
            else:
                return False
        except:
            return False

    def readMessage(self):

        try:
            strTemp = str(self.strMessage)
            strTemp = strTemp.strip()

            if strTemp != None:
                return strTemp
            else:
                return None

        except:
            return None

    def writeMessage(self,strinput):
        try:
            strinput = str(strinput)
            strinput = strinput.strip()

            if strinput != None:
                self.strMessage = strinput
                MessageLen = len(self.strMessage)

                if MessageLen > 16:
                    self.strMessageExcerpt = self.strMessage[0:16]
                else:
                    self.strMessageExcerpt = self.strMessage

                return True
            else:
                return False
        except:
            return False

    def sendResponse(self):
        try:
            sender_address = ('support@sa-sms.appspot.com')
            mail.send_mail(sender_address, self.strEmail, self.strSubject, self.strMessage)
            return True
        except:
            return False

class TicketUsers(ndb.Expando):

    strUserID = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strWebsite = ndb.StringProperty()


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

class StaffMembers(ndb.Expando):
    strUserID = ndb.StringProperty()
    strPresentTicketID = ndb.StringProperty()
    strName = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strDepartment = ndb.StringProperty()
    strSkillLevel = ndb.StringProperty(default="Beginner") #Intermediate, Expert
    strUserAssigned = ndb.BooleanProperty(default=False)
    strUserOnline = ndb.BooleanProperty(default=False)
    strNotAvailable = ndb.BooleanProperty(default=False)


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
    def writePresentTicketID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPresentTicketID = strinput
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
    def writeDepartment(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strDepartment = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSkillLevel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ["Beginner","Intermediate","Expert"]:
                self.strSkillLevel = strinput
                return True
            else:
                return False
        except:
            return False
    def writeUserAssigned(self,strinput):
        try:
            if strinput in [True,False]:
                self.strUserAssigned = strinput
                return True
            else:
                return False
        except:
            return False
    def writeUserOnline(self,strinput):
        try:
            if strinput in [True,False]:
                self.strUserOnline = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNotAvailable(self,strinput):
        try:
            if strinput in [True,False]:
                self.strNotAvailable = strinput
                return True
            else:
                return False
        except:
            return False

class Tickets(ndb.Expando):
    strTicketID = ndb.StringProperty()
    strUserID = ndb.StringProperty()
    strSubject = ndb.StringProperty()
    strBody = ndb.StringProperty()
    strDateCreated = ndb.DateProperty()
    strTimeCreated = ndb.TimeProperty()
    strTicketOpen = ndb.BooleanProperty(default=True) # Ticket Open or Close
    strTicketPreference = ndb.StringProperty(default="Normal") # Normal / Urgent
    strDepartment = ndb.StringProperty(default="Sales") # Programming, Hosting

    strTicketEscalated = ndb.BooleanProperty(default=False)
    strAssignedTo = ndb.StringProperty() # Assigned to Carries the ID of the Staff Member assigned the ticket
    strEscalatedToID = ndb.StringProperty() # Staff Member the Ticket is Escalated To

    def writeEscalate(self,strinput):
        try:
            if strinput in [True,False]:
                self.strEscalate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAssignedTo(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAssignedTo = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEscalatedTo(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEscalatedToID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTicketID (self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTicketID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateTicketID(self):
        import random,string
        try:
            strTicketID = ""
            for i in range(256):
                strTicketID += random.SystemRandom().choice(string.digits + string.ascii_lowercase)
            return strTicketID
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
    def writeSubject(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSubject = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBody(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBody = strinput
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
    def writeTicketOpen(self,strinput):
        try:
            if strinput in [True,False]:
                self.strTicketOpen = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTicketPreferences(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ["Normal","Urgent"]:
                self.strTicketPreference = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDepartment(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ["Sales","Programming","Bulk SMS","Advertising","Surveys","Affiliate","Hosting"]:
                self.strDepartment = strinput
                return True
            else:
                return False
        except:
            return False

class CommentThread(ndb.Expando):
    strTicketID = ndb.StringProperty()
    strThreadID = ndb.StringProperty()
    strCommentsList = ndb.StringProperty() # a Comma Separated String with IDS of the comments in order
    strDateTimeCreated = ndb.DateTimeProperty(auto_now_add=True)

    def AddCommentID(self,strinput):
        try:
            strinput = str(strinput)
            if len(strinput) == 16:
                if self.strCommentsList == None:
                    self.strCommentsList = strinput
                    return True
                else:
                    self.strCommentsList = self.strCommentsList + "," + strinput
                    return True
            else:
                return False
        except:
            return False
    def retrieveCommentsList(self):
        try:
            if not(self.strCommentsList == None):
                strTemplList = self.strCommentsList.split(",")
                return strTemplList
            else:
                return []
        except:
            return []
    def RemoveCommentID(self,strinput):
        try:
            strinput = str(strinput)
            if not(self.strCommentsList == None):
                strTempList = self.strCommentsList.split(",")
                if strinput in strTempList:
                    strTempList.remove(strinput)
                    if len(strTempList) > 0:
                        self.strCommentsList = strTempList[0]
                        strTempList = strTempList.remove(strTempList[0])
                        for strinput in strTempList:
                            self.strCommentsList = self.strCommentsList + "," + strinput
                    else:
                        self.strCommentsList = None

                    return True
                else:
                    return False
            else:
                return False
        except:
            return False
    def writeTicketID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTicketID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeThreadID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strThreadID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateThreadID(self):
        import random,string
        try:
            strThreadID = ""
            for i in range(32):
                strThreadID += random.SystemRandom().choice(string.digits + string.ascii_lowercase)
            return strThreadID
        except:
            return None

class Comments(ndb.Expando):
    strAuthorID = ndb.StringProperty()
    strThreadID = ndb.StringProperty()
    strCommentID = ndb.StringProperty() # a Sixteen Character Long ID Identifying this comment
    strComment = ndb.StringProperty()
    strCommentDate = ndb.DateProperty()
    strCommentTime = ndb.TimeProperty()
    isClientComment = ndb.BooleanProperty(default=True)

    def writeAuthorID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAuthorID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeThreadID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strThreadID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCommentID(self,strinput):
        try:
            strinput = str(strinput)
            if len(strinput) == 16:
                self.strCommentID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateCommentID(self):
        import random,string
        try:
            strCommentID = ""
            for i in range(16):
                strCommentID += random.SystemRandom().choice(string.digits + string.ascii_lowercase)
            return strCommentID
        except:
            return None
    def writeComment(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strComment = strinput
                return True
            else:
                return False
        except:
            return False
    def writeIsClientComment(self,strinput):
        try:
            if strinput in [True,False]:
                self.isClientComment = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCommentDate(self,strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.strCommentDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCommentTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strCommentTime = strinput
                return True
            else:
                return False
        except:
            return False

class ThisContactHandler(webapp2.RequestHandler):
    def get(self):
        #TODO - its easier to get session id if it exists
        #TODO- with the session then obtain userid
        #TODO- with the user id retrive the user account from the datastore and use that to retrieve user records

        template = template_env.get_template('templates/contact/contact.html')
        context = {}
        self.response.write(template.render(context))

    def post(self):

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            #'&vstrUserID=' + struid + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrAccessToken = self.request.get('vstrAccessToken')


            strnames = self.request.get('vstrNames')
            strEmail = self.request.get('vstrEmail')
            strcell = self.request.get('vstrCell')
            strsubject = self.request.get('vstrSubject')
            strmessage = self.request.get('vstrMessage')

            ContactMessage = ContactMessages()
            ContactMessage.strMessageReference = vstrUserID
            ContactMessage.writeNames(strinput=strnames)
            ContactMessage.writeEmail(strinput=strEmail)
            ContactMessage.writeCell(strinput=strcell)
            ContactMessage.writeSubject(strinput=strsubject)
            ContactMessage.writeMessage(strinput=strmessage)

            ContactMessage.put()
            self.response.write("""
            Contact Message Submitted Successfully One of our Representatives will get back to you as soon as possible
            """)
        elif vstrChoice == "1":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            findRequest = TicketUsers.query(TicketUsers.strUserID == vstrUserID)
            thisTicketUserList = findRequest.fetch()
            if len(thisTicketUserList) > 0:
                thisTicketUser = thisTicketUserList[0]
            else:
                thisTicketUser = TicketUsers()

            template  = template_env.get_template('templates/contact/sub/subcontact.html')
            context = {'thisTicketUser':thisTicketUser}
            self.response.write(template.render(context))

        elif vstrChoice == "2":
            #TODO- need to pre load tickets for the current user
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            findRequest = TicketUsers.query(TicketUsers.strUserID == vstrUserID)
            thisTicketUserList = findRequest.fetch()
            if len(thisTicketUserList) > 0:
                thisTicketUser = thisTicketUserList[0]
            else:
                thisTicketUser = TicketUsers()

            findRequest = Tickets.query(Tickets.strUserID == vstrUserID)
            thisTicketsList = findRequest.fetch()


            template = template_env.get_template('templates/contact/sub/tickets.html')
            context = {'thisTicketUser':thisTicketUser,'thisTicketsList':thisTicketsList}
            self.response.write(template.render(context))

        elif vstrChoice == "3":
            #'&vstrEmail=' + email + '&vstrUserID=' + struid + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrSubject = self.request.get("vstrSubject")
            vstrBody = self.request.get("vstrBody")
            vstrTicketPreference = self.request.get("vstrTicketPreference")
            vstrDepartment = self.request.get("vstrDepartment")
            vstrNames = self.request.get("vstrNames")
            vstrSurname = self.request.get("vstrSurname")
            vstrCell = self.request.get("vstrCell")
            vstrEmail = self.request.get("vstrEmail")

            findRequest = TicketUsers.query(TicketUsers.strUserID == vstrUserID)
            thisTicketUserList = findRequest.fetch()

            if len(thisTicketUserList) > 0:
                thisTicketUser =  thisTicketUserList[0]
            else:
                thisTicketUser = TicketUsers()
                thisTicketUser.writeUserID(strinput=vstrUserID)
                thisTicketUser.writeNames(strinput=vstrNames)
                thisTicketUser.writeSurname(strinput=vstrSurname)
                thisTicketUser.writeCell(strinput=vstrCell)
                thisTicketUser.writeEmail(strinput=vstrEmail)
                thisTicketUser.put()

            vstrThisDateTime = datetime.datetime.now()
            strThisDate = datetime.date(year=vstrThisDateTime.year,month=vstrThisDateTime.month,day=vstrThisDateTime.day)
            strThisTime = datetime.time(hour=vstrThisDateTime.hour,minute=vstrThisDateTime.minute,second=vstrThisDateTime.second)

            thisTicket = Tickets()
            thisTicket.writeUserID(strinput=vstrUserID)
            thisTicket.writeTicketID(strinput=thisTicket.CreateTicketID())
            thisTicket.writeSubject(strinput=vstrSubject)
            thisTicket.writeBody(strinput=vstrBody)
            thisTicket.writeTicketPreferences(strinput=vstrTicketPreference)
            thisTicket.writeDepartment(strinput=vstrDepartment)
            thisTicket.writeDateCreated(strinput=strThisDate)
            thisTicket.writeTimeCreated(strinput=strThisTime)
            thisTicket.put()
            self.response.write("Ticket Successfully created")

                #TODO- finish this up once done resolving the account issues

        elif vstrChoice == "4":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            template = template_env.get_template('templates/contact/sub/address.html')
            context = {}
            self.response.write(template.render(context))


class ThisTicketHandler(webapp2.RequestHandler):
    def get(self):

        vstrUserID = self.request.get('vstrUserID')
        vstrAccessToken = self.request.get('vstrAccessToken')
        vstrEmail = self.request.get('vstrEmail')

        URL = self.request.url
        strURLlist = URL.split("/")
        strTicketID = strURLlist[len(strURLlist) - 1]

        findRequest = TicketUsers.query(TicketUsers.strUserID == vstrUserID)
        thisTicketUserList = findRequest.fetch()

        if len(thisTicketUserList) > 0:
            thisTicketUser = thisTicketUserList[0]
        else:
            thisTicketUser = TicketUsers()


        findRequest = Tickets.query(Tickets.strUserID == vstrUserID,Tickets.strTicketID == strTicketID)
        thisTicketList = findRequest.fetch()

        if len(thisTicketList) > 0:
            thisTicket = thisTicketList[0]

            findRequest = CommentThread.query(CommentThread.strTicketID == thisTicket.strTicketID).order(+CommentThread.strDateTimeCreated)
            thisCommentThreadsList = findRequest.fetch()
            if len(thisCommentThreadsList) > 0:
                thisThread = thisCommentThreadsList[0]

                strComIDList = thisThread.retrieveCommentsList()
                thisCommentList = []
                for thisComID in strComIDList:
                    findRequest = Comments.query(Comments.strCommentID == thisComID,Comments.strThreadID == thisThread.strThreadID)
                    commList = findRequest.fetch()
                    if len(commList) > 0:
                        thisCommentList.append(commList[0])
                thisCommentList.reverse()

            else:
                thisThread = CommentThread()
                thisThread.writeThreadID(strinput=thisThread.CreateThreadID())
                thisThread.writeTicketID(strinput=thisTicket.strTicketID)
                vstrThisDateTime = datetime.datetime.now()
                strThisDate = datetime.date(year=vstrThisDateTime.year,month=vstrThisDateTime.month,day=vstrThisDateTime.day)
                strThisTime = datetime.time(hour=vstrThisDateTime.hour,minute=vstrThisDateTime.minute,second=vstrThisDateTime.second)
                thisComment = Comments()
                thisComment.writeThreadID(strinput=thisThread.strThreadID)
                thisComment.writeCommentID(strinput=thisComment.CreateCommentID())
                thisComment.writeAuthorID(strinput="000000")
                thisComment.writeIsClientComment(strinput=False)
                thisComment.writeCommentDate(strinput=strThisDate)
                thisComment.writeCommentTime(strinput=strThisTime)
                thisComment.writeComment(strinput="Welcome to our ticketing system a help desk staff member will attend to you soon")
                thisComment.put()
                thisCommentList = []
                thisCommentList.append(thisComment)
                thisThread.AddCommentID(strinput=thisComment.strCommentID)
                thisThread.put()

            template = template_env.get_template('templates/contact/sub/thisTicket.html')
            context = {'thisTicketUser':thisTicketUser,'thisTicket':thisTicket,'thisCommentList':thisCommentList,'thisThread':thisThread}
            self.response.write(template.render(context))

    def post(self):

        vstrChoice = self.request.get("vstrChoice")
        if vstrChoice == "0":
            #'&vstrUserID=' + vstrUserID + '$vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            vstrComment = self.request.get("vstrComment")
            vstrTicketID = self.request.get("vstrTicketID")
            vstrThreadID = self.request.get("vstrThreadID")
            vstrUserID = self.request.get("vstrUserID")

            findRequest = CommentThread.query(CommentThread.strThreadID == vstrThreadID,CommentThread.strTicketID == vstrTicketID)
            thisCommentThreadList = findRequest.fetch()

            vstrThisDateTime = datetime.datetime.now()
            strThisDate = datetime.date(year=vstrThisDateTime.year,month=vstrThisDateTime.month,day=vstrThisDateTime.day)
            strThisTime = datetime.time(hour=vstrThisDateTime.hour,minute=vstrThisDateTime.minute,second=vstrThisDateTime.second)

            if len(thisCommentThreadList) > 0:
                thisCommentThread = thisCommentThreadList[0]
                thisComment = Comments()
                thisComment.writeThreadID(strinput=thisCommentThread.strThreadID)
                thisComment.writeAuthorID(strinput=vstrUserID)
                thisComment.writeIsClientComment(strinput=True)
                thisComment.writeComment(strinput=vstrComment)
                thisComment.writeCommentID(strinput=thisComment.CreateCommentID())
                thisComment.writeCommentDate(strinput=strThisDate)
                thisComment.writeCommentTime(strinput=strThisTime)
                thisCommentThread.AddCommentID(strinput=thisComment.strCommentID)
                thisCommentThread.put()
                thisComment.put()

                findRequest = Comments.query(Comments.strThreadID == thisCommentThread.strThreadID)
                thisCommentList = findRequest.fetch()
                thisCommentList.reverse()
                template = template_env.get_template('templates/contact/sub/AutoUpdate.html')
                context = {'thisCommentList': thisCommentList}
                self.response.write(template.render(context))

        elif vstrChoice == "1":
            #'&vstrUserID=' + vstrUserID + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            vstrUserID = self.request.get("vstrUserID")

            vstrTicketID = self.request.get("vstrTicketID")
            findRequest = TicketUsers.query(TicketUsers.strUserID == vstrUserID)
            thisTicketUserList = findRequest.fetch()

            if len(thisTicketUserList) > 0:
                thisTicketUser = thisTicketUserList[0]
            else:
                thisTicketUser = TicketUsers()

            findRequest = Tickets.query(Tickets.strUserID == vstrUserID, Tickets.strTicketID == vstrTicketID)
            thisTicketList = findRequest.fetch()

            if len(thisTicketList) > 0:
                thisTicket = thisTicketList[0]

                findRequest = CommentThread.query(CommentThread.strTicketID == thisTicket.strTicketID).order(+CommentThread.strDateTimeCreated)
                thisCommentThreadsList = findRequest.fetch()
                if len(thisCommentThreadsList) > 0:
                    thisThread = thisCommentThreadsList[0]

                    strComIDList = thisThread.retrieveCommentsList()
                    thisCommentList = []
                    for thisComID in strComIDList:
                        findRequest = Comments.query(Comments.strCommentID == thisComID,Comments.strThreadID == thisThread.strThreadID)
                        commList = findRequest.fetch()
                        if len(commList) > 0:
                            thisCommentList.append(commList[0])
                    thisCommentList.reverse()

                    template = template_env.get_template('templates/contact/sub/AutoUpdate.html')
                    context = {'thisTicketUser':thisTicketUser,'thisTicket':thisTicket,'thisCommentList':thisCommentList,'thisThread':thisThread}
                    self.response.write(template.render(context))


class readContactHandler(webapp2.RequestHandler):
    def get(self):

        URL = self.request.url
        URLlist = URL.split("/")
        strReference = URLlist[len(URLlist) - 1]

        findRequest = ContactMessages.query(ContactMessages.strMessageReference == strReference)
        thisContactMessagesList = findRequest.fetch()

        if len(thisContactMessagesList) > 0:
            thisContactMessage = thisContactMessagesList[0]
        else:
            thisContactMessage = ContactMessages()

        template = template_env.get_template('templates/contact/readContact.html')
        context = {'thisContactMessage':thisContactMessage}
        self.response.write(template.render(context))


app = webapp2.WSGIApplication([

    ('/contact/tickets/.*', ThisTicketHandler),
    ('/contact/read/.*', readContactHandler),
    ('/contact', ThisContactHandler)

], debug=True)


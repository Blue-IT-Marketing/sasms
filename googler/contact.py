
import os
import jinja2
from google.cloud import ndb
import datetime
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


class ContactMessages(ndb.Model):
    message_reference = ndb.StringProperty()
    names = ndb.StringProperty()
    email = ndb.StringProperty()
    cell = ndb.StringProperty()
    subject = ndb.StringProperty()
    message = ndb.StringProperty()
    message_excerpt = ndb.StringProperty()

    date_submitted = ndb.DateProperty(auto_now_add=True)
    time_submitted = ndb.TimeProperty(auto_now_add=True)

    response_sent = ndb.BooleanProperty(default=False)

    def readDateSubmitted(self):
        try:
            strTemp = str(self.date_submitted)
            strTemp = strTemp.strip()

            return strTemp
        except:
            return None
    def readTimeSubmitted(self):
        try:
            strTemp = str(self.time_submitted)
            strTemp = strTemp.strip()

            return strTemp
        except:
            return None
    def readResposeSent(self):
        try:
            return self.response_sent
        except:
            return False
    def writeResponseSent(self,strinput):
        try:

            if strinput in [True,False]:
                self.response_sent = strinput
                return True
            else:
                return False
        except:
            return False

    def readNames(self):
        try:
            strTemp = str(self.names)
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
                self.names = strinput
                return True
            else:
                return False
        except:
            return False
    def readEmail(self):
        try:
            strTemp = str(self.email)
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
                self.email = strinput
                return True
            else:
                return False
        except:
            return False
    def readCell(self):
        try:
            strTemp = str(self.cell)
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
                self.cell = strinput
                return True
            else:
                return False
        except:
            return False
    def readSubject(self):
        try:
            strTemp = str(self.subject)
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
                self.subject = strinput
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
                    self.message_excerpt = self.strMessage[0:16]
                else:
                    self.message_excerpt = self.strMessage

                return True
            else:
                return False
        except:
            return False

    def sendResponse(self):
        try:
            sender_address = ('support@sa-sms.appspot.com')
            mail.send_mail(sender_address, self.email, self.subject, self.strMessage)
            return True
        except:
            return False

class TicketUsers(ndb.Expando):

    uid = ndb.StringProperty()
    names = ndb.StringProperty()
    surname = ndb.StringProperty()
    cell = ndb.StringProperty()
    email = ndb.StringProperty()
    website = ndb.StringProperty()


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

class StaffMembers(ndb.Expando):
    uid = ndb.StringProperty()
    ticket_id = ndb.StringProperty()
    name = ndb.StringProperty()
    surname = ndb.StringProperty()
    department = ndb.StringProperty()
    skill_level = ndb.StringProperty(default="Beginner") #Intermediate, Expert
    user_assigned = ndb.BooleanProperty(default=False)
    user_online = ndb.BooleanProperty(default=False)
    not_available = ndb.BooleanProperty(default=False)


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
    def writePresentTicketID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.ticket_id = strinput
                return True
            else:
                return False
        except:
            return False
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
    def writeDepartment(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.department = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSkillLevel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ["Beginner","Intermediate","Expert"]:
                self.skill_level = strinput
                return True
            else:
                return False
        except:
            return False
    def writeUserAssigned(self,strinput):
        try:
            if strinput in [True,False]:
                self.user_assigned = strinput
                return True
            else:
                return False
        except:
            return False
    def writeUserOnline(self,strinput):
        try:
            if strinput in [True,False]:
                self.user_online = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNotAvailable(self,strinput):
        try:
            if strinput in [True,False]:
                self.not_available = strinput
                return True
            else:
                return False
        except:
            return False

class Tickets(ndb.Expando):
    ticket_id = ndb.StringProperty()
    uid = ndb.StringProperty()
    subject = ndb.StringProperty()
    body = ndb.StringProperty()
    date_created = ndb.DateProperty()
    time_created = ndb.TimeProperty()
    ticket_open = ndb.BooleanProperty(default=True) # Ticket Open or Close
    ticket_preference = ndb.StringProperty(default="Normal") # Normal / Urgent
    department = ndb.StringProperty(default="Sales") # Programming, Hosting

    ticket_escalated = ndb.BooleanProperty(default=False)
    assigned_to = ndb.StringProperty() # Assigned to Carries the ID of the Staff Member assigned the ticket
    escalated_to_uid = ndb.StringProperty() # Staff Member the Ticket is Escalated To

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
                self.assigned_to = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEscalatedTo(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.escalated_to_uid = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTicketID (self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.ticket_id = strinput
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
                self.subject = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBody(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.body = strinput
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
    def writeTicketOpen(self,strinput):
        try:
            if strinput in [True,False]:
                self.ticket_open = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTicketPreferences(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ["Normal","Urgent"]:
                self.ticket_preference = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDepartment(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ["Sales","Programming","Bulk SMS","Advertising","Surveys","Affiliate","Hosting"]:
                self.department = strinput
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
            ContactMessage.message_reference = vstrUserID
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

            findRequest = TicketUsers.query(TicketUsers.uid == vstrUserID)
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

            findRequest = TicketUsers.query(TicketUsers.uid == vstrUserID)
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

            findRequest = TicketUsers.query(TicketUsers.uid == vstrUserID)
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

        findRequest = TicketUsers.query(TicketUsers.uid == vstrUserID)
        thisTicketUserList = findRequest.fetch()

        if len(thisTicketUserList) > 0:
            thisTicketUser = thisTicketUserList[0]
        else:
            thisTicketUser = TicketUsers()


        findRequest = Tickets.query(Tickets.strUserID == vstrUserID, Tickets.ticket_id == strTicketID)
        thisTicketList = findRequest.fetch()

        if len(thisTicketList) > 0:
            thisTicket = thisTicketList[0]

            findRequest = CommentThread.query(CommentThread.strTicketID == thisTicket.ticket_id).order(+CommentThread.strDateTimeCreated)
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
                thisThread.writeTicketID(strinput=thisTicket.ticket_id)
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
            findRequest = TicketUsers.query(TicketUsers.uid == vstrUserID)
            thisTicketUserList = findRequest.fetch()

            if len(thisTicketUserList) > 0:
                thisTicketUser = thisTicketUserList[0]
            else:
                thisTicketUser = TicketUsers()

            findRequest = Tickets.query(Tickets.strUserID == vstrUserID, Tickets.ticket_id == vstrTicketID)
            thisTicketList = findRequest.fetch()

            if len(thisTicketList) > 0:
                thisTicket = thisTicketList[0]

                findRequest = CommentThread.query(CommentThread.strTicketID == thisTicket.ticket_id).order(+CommentThread.strDateTimeCreated)
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

        findRequest = ContactMessages.query(ContactMessages.message_reference == strReference)
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


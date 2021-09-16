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
import logging
import os
import jinja2
import datetime
from google.cloud import ndb

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

def send_email(strFrom,strTo,strSubject,strBody,strTextType,strAttachFileContent=None,strAttachFileName=None):
    import sendgrid
    from sendgrid.helpers.mail import *
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    try:
        if not(strAttachFileName == None) and (strAttachFileContent == None):
            data = {
                "personalizations": [
                    {
                        "to": [
                            {
                                "email": strTo
                            }
                        ],
                        "subject": strSubject
                    }
                ],
                "from": {
                    "email": strFrom
                },
                "content": [
                    {
                        "type": strTextType,
                        "value": strBody
                    }
                ],
                "attachments": [
                    {
                        "content": strAttachFileContent,
                        "filename": strAttachFileName,
                    }
                ]
            }
        else:
            data = {
                "personalizations": [
                    {
                        "to": [
                            {
                                "email": strTo
                            }
                        ],
                        "subject": strSubject
                    }
                ],
                "from": {
                    "email": strFrom
                },
                "content": [
                    {
                        "type": strTextType,
                        "value": strBody
                    }
                ]
            }

        thisresponse = sg.client.mail.send.post(request_body=data)
        if (thisresponse.status_code >= 200) and (thisresponse.status_code <= 400):
            return True
        else:
            logging.info("Failure sending email")
            return False
    except:
        return False

class MyEmailSettings(ndb.Expando):
    uid = ndb.StringProperty()
    email = ndb.StringProperty()
    name = ndb.StringProperty()
    signature = ndb.StringProperty()
    date_created = ndb.DateProperty(auto_now_add=True)
    time_created = ndb.TimeProperty(auto_now_add=True)

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

    def writeEmailAddress(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.email = strinput
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

    def writeSignature(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.signature = strinput
                return True
            else:
                return False
        except:
            return False

class MyEmail(ndb.Expando):
    """
        Thread ID allows send response emails to be saved in a single thread
    """
    uid = ndb.StringProperty()
    thread_id = ndb.StringProperty()
    email_id = ndb.StringProperty() # Unique ID for every email
    to_address = ndb.StringProperty()
    to_name = ndb.StringProperty()
    subject = ndb.StringProperty()
    body_text = ndb.StringProperty()
    body_html = ndb.StringProperty()

    date_sent = ndb.DateProperty()
    time_sent = ndb.TimeProperty()
    date_created = ndb.DateProperty()
    time_created = ndb.TimeProperty()
    status = ndb.StringProperty(default="Draft") # Sent,  Trash

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
    def writeThreadID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.thread_id = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateEmailID(self):
        import random,string
        try:
            strEmailID = ""
            for i in range(36):
                strEmailID +=  random.SystemRandom().choice(string.ascii_lowercase + string.digits)
            return strEmailID
        except:
            return None

    def writeEmailID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.email_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeToAddress(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.to_address = strinput
                return True
            else:
                return False
        except:
            return False
    def writeToName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.to_name = strinput
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
    def writeBodyText(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.body_text = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBodyHTML(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.body_html = strinput
                return True
            else:
                return False
        except:
            return False
    def writeYearSent(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 2100) and (int(strinput) >= 2016):
                self.year_sent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMonthSent(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 12) and (int(strinput) >= 1):
                self.month_sent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDaySent(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 31) and (int(strinput) >= 1):
                self.date_sent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeCreated(self,strinput):
        try:
            if strinput is not None:
                self.time_created = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeSent(self,strinput):
        try:

            if strinput is not None:
                self.strTimeSent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMonthCreated(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 12) and (int(strinput) >= 1):
                self.strMonthCreated = strinput
                return True
            else:
                return False
        except:
            return False
    def writeYearCreated(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 2100) and (int(strinput) >= 2016):
                self.strYearCreated = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDayCreated(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1) and (int(strinput) <= 31):
                self.date_created = strinput
                return True
            else:
                return False
        except:
            return False
    def changeState(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ['Draft','Sent','Trash']:
                self.status = strinput
                return True
            else:
                return False
        except:
            return False

class MyInbox(ndb.Expando):
    strUserID = ndb.StringProperty()
    strThreadID = ndb.StringProperty()
    strFromAddress = ndb.StringProperty()
    strFromName = ndb.StringProperty()
    strSubject = ndb.StringProperty()
    strBodyText = ndb.StringProperty()
    strBodyHTML = ndb.StringProperty()
    strIsText = ndb.StringProperty(default="No") # YES

    strYearReceived = ndb.StringProperty()
    strMonthReceived = ndb.StringProperty()
    strDayReceived = ndb.StringProperty()

    strTimeReceived = ndb.TimeProperty()

    strStatus = ndb.StringProperty(default="Inbox") # Trash, Junk

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
    def writeFromAddress(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFromAddress = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFromName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFromName = strinput
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
    def writeBodyText(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBodyText = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBodyHTML(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBodyHTML = strinput
                return True
            else:
                return False
        except:
            return False
    def writeYearReceived(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 2100) and (int(strinput) >= 2016):
                self.strYearReceived = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMonthReceived(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 12) and  (int(strinput) >= 1):
                self.strMonthReceived = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDayReceived(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1) and (int(strinput) <= 31):
                self.strDayReceived = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeReceived(self,strinput):
        try:
            if strinput is not None:
                self.strTimeReceived = strinput
                return True
            else:
                return False
        except:
            return False


    def changeState(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ['Inbox','Trash']:
                self.strStatus = strinput
                return True
            else:
                return False
        except:
            return False

class myEmailHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = MyEmailSettings.query(MyEmailSettings.uid == Guser.user_id())
            thisEmailSettingsList = findRequest.fetch()
            if len(thisEmailSettingsList) > 0:
                thisEmailSettings = thisEmailSettingsList[0]
            else:
                thisEmailSettings = MyEmailSettings()


            templates = template_env.get_template("templates/myemail/myemail.html")
            context = {'thisEmailSettings':thisEmailSettings}
            self.response.write(templates.render(context))

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                vstrEmailAddress = self.request.get('vstrEmailAddress')
                vstrName = self.request.get('vstrName')
                vstrSignature = self.request.get('vstrSignature')

                findRequest = MyEmailSettings.query(MyEmailSettings.uid == Guser.user_id())
                thisEmailSettingsList = findRequest.fetch()
                if len(thisEmailSettingsList) > 0:
                    thisEmailSetting = thisEmailSettingsList[0]
                else:
                    thisEmailSetting = MyEmailSettings()

                thisEmailSetting.writeUserID(strinput=Guser.user_id())
                thisEmailSetting.writeEmailAddress(strinput=vstrEmailAddress)
                thisEmailSetting.writeName(strinput=vstrName)
                thisEmailSetting.writeSignature(strinput=vstrSignature)
                thisEmailSetting.put()
                self.response.write("Email Settings Successfully Saved")

            elif vstrChoice == "1":
                findRequest = MyInbox.query(MyInbox.strUserID == Guser.user_id(),MyInbox.strStatus == "Inbox")
                thisInboxList = findRequest.fetch()

                template = template_env.get_template('templates/myemail/email/inbox.html')
                context = {'thisInboxList':thisInboxList}
                self.response.write(template.render(context))

            elif vstrChoice == "2":
                findRequest = MyEmail.query(MyEmail.uid == Guser.user_id(), MyEmail.status == "Sent")
                thisSentEmailsList = findRequest.fetch()

                template = template_env.get_template('templates/myemail/email/sent.html')
                context = {'thisSentEmailsList':thisSentEmailsList}
                self.response.write(template.render(context))

            elif vstrChoice == "3":
                findRequest = MyEmail.query(MyEmail.uid == Guser.user_id(), MyEmail.status == "Draft")
                thisEmailDraftsList = findRequest.fetch()

                template = template_env.get_template('templates/myemail/email/drafts.html')
                context = {'thisEmailDraftsList':thisEmailDraftsList}
                self.response.write(template.render(context))

            elif vstrChoice == "4":
                findRequest = MyEmailSettings.query(MyEmailSettings.uid == Guser.user_id())
                thisEmailSettingsList = findRequest.fetch()

                if len(thisEmailSettingsList) > 0:
                    thisEmailSetting = thisEmailSettingsList[0]

                    template = template_env.get_template('templates/myemail/email/compose.html')
                    context = {'thisEmailSetting':thisEmailSetting}
                    self.response.write(template.render(context))
                else:
                    self.response.write("Please setup your email first")
            elif vstrChoice == "5":
                vstrToEmail = self.request.get('vstrToEmail')
                vstrSubject = self.request.get('vstrSubject')
                vstrEmailText = self.request.get('vstrEmailText')

                thisDraft = MyEmail()
                thisDraft.writeUserID(strinput=Guser.user_id())
                thisDraft.writeSubject(strinput=vstrSubject)
                thisDraft.writeBodyHTML(strinput=vstrEmailText)
                thisDraft.writeToAddress(strinput=vstrToEmail)
                thisDate = datetime.datetime.now()
                thisDate = thisDate.date()
                thisYear = thisDate.year
                thisMonth = thisDate.month
                thisDay = thisDate.day
                thisDraft.writeYearCreated(strinput=str(thisYear))
                thisDraft.writeMonthCreated(strinput=str(thisMonth))
                thisDraft.writeDayCreated(strinput=str(thisDay))
                thisDraft.changeState(strinput="Draft")
                thisTime = datetime.datetime.now()
                thisTime = thisTime.time()

                thisTime = datetime.time(hour=thisTime.hour,minute=thisTime.minute,second=thisTime.second)
                thisDraft.writeTimeCreated(strinput=thisTime)
                thisDraft.put()

                self.response.write("Email Successfully saved as draft")
            elif vstrChoice == "6":
                vstrToEmail = self.request.get('vstrToEmail')
                vstrSubject = self.request.get('vstrSubject')
                vstrEmailText = self.request.get('vstrEmailText')

                thisSent = MyEmail()
                thisSent.writeUserID(strinput=Guser.user_id())
                thisSent.writeSubject(strinput=vstrSubject)
                thisSent.writeBodyHTML(strinput=vstrEmailText)
                thisSent.writeToAddress(strinput=vstrToEmail)
                thisDate = datetime.datetime.now()
                thisDate = thisDate.date()
                thisYear = thisDate.year
                thisMonth = thisDate.month
                thisDay = thisDate.day
                thisSent.writeYearCreated(strinput=str(thisYear))
                thisSent.writeMonthCreated(strinput=str(thisMonth))
                thisSent.writeDayCreated(strinput=str(thisDay))
                thisSent.changeState(strinput="Sent")
                thisTime = datetime.datetime.now()
                thisTime = thisTime.time()

                thisTime = datetime.time(hour=thisTime.hour,minute=thisTime.minute,second=thisTime.second)
                thisSent.writeTimeCreated(strinput=thisTime)

                findRequest = MyEmailSettings.query(MyEmailSettings.uid == Guser.user_id())
                thisEmailSettingsList = findRequest.fetch()

                if len(thisEmailSettingsList) > 0:
                    thisEmailSetting = thisEmailSettingsList[0]

                    thisEmailSetting.email = thisEmailSetting.email + "@sa-sms.appspotmail.com"
                    try:
                        #message = mail.EmailMessage()
                        #message.sender = thisEmailSetting.email
                        #message.to = thisSent.to_address
                        #message.subject = thisSent.subject
                        #message.body = thisSent.body_html
                        #message.send()
                        #def SendEmail(strFrom,strTo,subject,body,strTextType):
                        if SendEmail(strFrom=thisEmailSetting.email, strTo=thisSent.to_address, strSubject=thisSent.subject, strBody=thisSent.body_html, strTextType="text/html"):

                            Now = datetime.datetime.now()
                            thisYear  = Now.year
                            thisMonth = Now.month
                            thisDay = Now.day
                            thisTime = datetime.time(hour=Now.hour,minute=Now.minute,second=Now.second)

                            thisSent.writeYearSent(strinput=str(thisYear))
                            thisSent.writeMonthSent(strinput=str(thisMonth))
                            thisSent.writeDaySent(strinput=str(thisDay))
                            thisSent.writeTimeSent(strinput=thisTime)
                            thisSent.put()
                            self.response.write("Message Successfully sent")
                        else:
                            self.response.write("Error sending messages")
                    except:
                        self.response.write("Error Sending Message")
                else:
                    self.response.write("Please setup your email address before sending email")


class  IncomingMailhandler(InboundMailHandler):
    def receive(self, mail_message):
        """
            find out how to detect the sending email address
        :param mail_message:
        :return:7
        """
        try:
            thisIncoming = MyInbox()

            bodies_list = mail_message.bodies('text/plain')

            if len(bodies_list) > 0:
                pass
            else:
                bodies_list = mail_message.bodies('text/html')

            for content_type, body in bodies_list:
                decode_text = body.decode()


            thisIncoming.writeBodyHTML(strinput=decode_text)
            thisIncoming.writeSubject(strinput=mail_message.subject)
            thisIncoming.writeFromAddress(strinput=mail_message.sender)
            Now = datetime.datetime.now()
            thisYear = Now.year
            thisMonth = Now.month
            thisDay = Now.day

            thisTime = datetime.time(hour=Now.hour,minute=Now.minute,second=Now.second)

            thisIncoming.writeYearReceived(strinput=str(thisYear))
            thisIncoming.writeMonthReceived(strinput=str(thisMonth))
            thisIncoming.writeDayReceived(strinput=str(thisDay))
            thisIncoming.writeTimeReceived(strinput=thisTime)
            thisIncoming.changeState(strinput="Inbox")
            thisIncoming.put()


        except:
            pass


class MyEmailDashboardHandler(webapp2.RequestHandler):
    def get(self):

        findRequest = MyInbox.query()
        thisInboxList = findRequest.fetch()

        template = template_env.get_template('templates/dashboard/emails/emails.html')
        context = {'thisInboxList':thisInboxList}
        self.response.write(template.render(context))

class ThisDashboardEmailHandler(webapp2.RequestHandler):
    def get(self):
        URL = self.request.url
        strURLlist = URL.split("/")
        strThreadID = strURLlist[len(strURLlist) - 1]

        findRequest = MyInbox.query(MyInbox.strThreadID == strThreadID)
        thisInboxList = findRequest.fetch()
        if len(thisInboxList) > 0:
            thisInbox = thisInboxList[0]
        else:
            thisInbox = MyInbox()

        template = template_env.get_template('templates/dashboard/emails/read.html')
        context = {'thisInbox':thisInbox}
        self.response.write(template.render(context))






app = webapp2.WSGIApplication([
    ('/admin/myemail', myEmailHandler),
    ('/dashboard/emails', MyEmailDashboardHandler),
    ('/dashboard/emails/.*', ThisDashboardEmailHandler),
    ('/_ah/mail/.+', IncomingMailhandler)

], debug=True)

#Create an email API and features bulk email features
#If seriouse about building bulk email features consider creating your own SMTP Server
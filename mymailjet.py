"""
This call sends an email to one recipient, using a validated sender address
Do not forget to update the sender address used in the sample
"""


import os
from mailjet_rest import Client
import webapp2
import jinja2
import datetime
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

#TODO- finish this up before use

class MailJet(ndb.Expando):
    strUserID = ndb.StringProperty()
    strAPIKey = ndb.StringProperty(default=os.environ['MJ_APIKEY_PUBLIC'])
    strAPISecret = ndb.StringProperty(default=os.environ['MJ_APIKEY_PRIVATE'])


    def GetMailJet(self):
        try:
            return Client(auth=(self.strAPIKey, self.strAPISecret))
        except:
            return None


    def SendMail(self,FromEmail,FromName,Subject,Text_part,Html_part,ToEmail):
        try:
            data = {
                'FromEmail': FromEmail,
                'FromName': FromName,
                'Subject': Subject,
                'Text-part': Text_part,
                'Html-part': Html_part,
                'Recipients': [
                    {
                        "Email": ToEmail
                    }
                ]
            }
            mailjet = self.GetMailJet()
            if not(mailjet == None):
                return mailjet.send.create(data=data)
            else:
                return None
        except:
            return None


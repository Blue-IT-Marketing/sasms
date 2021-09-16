"""
This call sends an email to one recipient, using a validated sender address
Do not forget to update the sender address used in the sample
"""


import os
import jinja2
import datetime
from google.cloud import ndb
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

#TODO- finish this up before use

class MailJet(ndb.Model):
    uid = ndb.StringProperty()
    api_key = ndb.StringProperty(default=os.environ['MJ_APIKEY_PUBLIC'])
    api_secret = ndb.StringProperty(default=os.environ['MJ_APIKEY_PRIVATE'])


    def GetMailJet(self):
        try:
            return Client(auth=(self.api_key, self.api_secret))
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


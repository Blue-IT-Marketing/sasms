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
import os
import webapp2
import jinja2
import datetime
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import urlfetch
from google.appengine.api import app_identity
import cloudstorage
import urllib, urllib2

from userRights import UserRights
from accounts import Accounts

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
import logging

from twilio.rest import Client

import json
class MyTwilioPortal(ndb.Expando):
    strTwilio_SID = ndb.StringProperty(default=os.environ.get('TWILIO_ACCOUNT_SID'))
    strTwilio_token = ndb.StringProperty(default=os.environ.get('TWILIO_AUTH_TOKEN'))
    strCostPerPage = ndb.IntegerProperty(default=60)
    strMySMSNumber = ndb.StringProperty()
    strMyFaxNumber = ndb.StringProperty()
    strAvailableCredit = ndb.IntegerProperty(default=0)
    strStatusCallBack = ndb.StringProperty(default="https://sa-sms.appspot.com/twilio/callback/status")

    #TODO-Add Modules for Voice, SMS, Receive, Video Conferencing with Video Intellegence API from Google
    #TODO- and Add Translation API for two communications on the contact management module

    def sendSMS(self, strTo, strMessage, strFrom=None, strMediaURL=None):
        """
        :param strTo:
        :param strFrom:
        :param strMessage:
        :param strMediaURL:
        :return:
        {
           "account_sid": "ACb10f84fd6a3b46afb0123544dd927fa1",
           "api_version": "2010-04-01",
           "body": "Jenny please?! I love you <3",
           "num_segments": "1",
           "num_media": "1",
           "date_created": "Wed, 18 Aug 2010 20:01:40 +0000",
           "date_sent": null,
           "date_updated": "Wed, 18 Aug 2010 20:01:40 +0000",
           "direction": "outbound-api",
           "error_code": null,
           "error_message": null,
           "from": "+14158141829",
           "price": null,
           "sid": "MM90c6fc909d8504d45ecdb3a3d5b3556e",
           "status": "queued",
           "to": "+15558675309",
           "uri": "/2010-04-01/Accounts/ACb10f84fd6a3b46afb0123544dd927fa1/Messages/MM90c6fc909d8504d45ecdb3a3d5b3556e.json"
        }
        """
        try:
            client = Client(self.strTwilio_SID, self.strTwilio_token)

            if strFrom == None:
                strFrom = self.strMySMSNumber

            message = client.messages.create(
                to=strTo,
                from_=strFrom,
                body=strMessage,
                status_callback=self.strStatusCallBack,
                media_url=strMediaURL)
            return message.sid
        except:
            return None

    def sendFax(self, strTo, strFaxURL, strFrom=None):
        try:
            client = Client(self.strTwilio_SID, self.strTwilio_token)
            if strFrom == None:
                strFrom = self.strMyFaxNumber

            fax = client.fax.v1.faxes.create(
                from_=strFrom,
                to=strTo,
                media_url=strFaxURL)

            return fax.sid
        except:
            return None

    def retrieveFax(self, strFaxSID):
        try:
            client = Client(self.strTwilio_SID, self.strTwilio_token)
            fax = client.fax.v1.faxes(sid=strFaxSID).fetch()
            return fax
        except:
            return None

    def writeMySMSNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMySMSNumber = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMyFaxNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMyFaxNumber = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAvailableCredit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAvailableCredit = int(strinput)
                return True
            else:
                return False
        except:
            return False



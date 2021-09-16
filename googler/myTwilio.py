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
import jinja2
import datetime
from google.cloud import ndb
from userRights import UserRights
from accounts import Accounts

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
import logging

from twilio.rest import Client

import json
class MyTwilioPortal(ndb.Model):
    twilio_sid = ndb.StringProperty(default=os.environ.get('TWILIO_ACCOUNT_SID'))
    twilio_token = ndb.StringProperty(default=os.environ.get('TWILIO_AUTH_TOKEN'))
    cost_per_page = ndb.IntegerProperty(default=60)
    sms_number = ndb.StringProperty()
    fax_number = ndb.StringProperty()
    available_credit = ndb.IntegerProperty(default=0)
    status_callback = ndb.StringProperty(default="https://sa-sms.appspot.com/twilio/callback/status")

    #TODO-Add Modules for Voice, SMS, Receive, Video Conferencing with Video Intellegence API from Google
    #TODO- and Add Translation API for two communications on the contact management module

    def send_sms(self, to, message, from_cell=None, media_url=None):
        """
        :param to:
        :param from_cell:
        :param message:
        :param media_url:
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
            client = Client(self.twilio_sid, self.twilio_token)

            if from_cell == None:
                from_cell = self.sms_number

            message = client.messages.create(
                to=to,
                from_=from_cell,
                body=message,
                status_callback=self.status_callback,
                media_url=media_url)
            return message.sid
        except:
            return None

    def send_fax(self, to_tel, fax_url, from_=None):
        try:
            client = Client(self.twilio_sid, self.twilio_token)
            if from_ == None:
                from_ = self.fax_number

            fax = client.fax.v1.faxes.create(
                from_=from_,
                to=to_tel,
                media_url=fax_url)

            return fax.sid
        except:
            return None

    def retrieve_fax(self, fax_sid):
        try:
            client = Client(self.twilio_sid, self.twilio_token)
            fax = client.fax.v1.faxes(sid=fax_sid).fetch()
            return fax
        except:
            return None

    def writeMySMSNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.sms_number = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMyFaxNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.fax_number = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAvailableCredit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.available_credit = int(strinput)
                return True
            else:
                return False
        except:
            return False



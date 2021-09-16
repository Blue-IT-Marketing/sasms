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
#
import os
import jinja2
from google.cloud import ndb
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class AdminHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/admin.html')
        context = {}
        self.response.write(template.render(context))


    def post(self):

        from mysms import SMSAccount
        from accounts import Accounts,Organization
        vstrUserID = self.request.get("vstrUserID")
        vstrUserEmail = self.request.get('vstrUserEmail')
        vstraccessToken = self.request.get('vstraccessToken')

        findRequest = Accounts.query(Accounts.uid == vstrUserID)
        thisAccountList = findRequest.fetch()

        if len(thisAccountList) > 0:
            thisAccount = thisAccountList[0]
        else:
            findRequest = Accounts.query(Accounts.email == vstrUserEmail, Accounts.verified == True)
            thisAccountList = findRequest.fetch()

            if len(thisAccountList) > 0:
                thisAccount = thisAccountList[0]
            else:
                thisAccount = Accounts()


        findRequest = SMSAccount.query(SMSAccount.organization_id == thisAccount.organization_id)
        thisSMSAccountList = findRequest.fetch()

        if len(thisSMSAccountList) > 0:
            thisSMSAccount = thisSMSAccountList[0]
        else:
            thisSMSAccount = SMSAccount()


        findRequest = Organization.query(Organization.strOrganizationID == thisAccount.organization_id)
        thisOrgList = findRequest.fetch()

        if len(thisOrgList) > 0:
            thisOrg = thisOrgList[0]
        else:
            thisOrg = Organization()

        template = template_env.get_template('templates/sms/sub/admin.html')
        context = {'thisSMSAccount':thisSMSAccount,'thisAccount':thisAccount,'thisOrg':thisOrg,'vstrUserID':vstrUserID}
        self.response.write(template.render(context))


class ThisAccountHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/account/accounts.html')
        context = {}
        self.response.write(template.render(context))

    def post(self):

        from mysms import SMSAccount
        from accounts import Accounts,Organization

        #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
        vstrUserID = self.request.get('vstrUserID')
        vstrEmail = self.request.get('vstrEmail')
        vstrAccessToken = self.request.get('vstrAccessToken')



        findRequest = Accounts.query(Accounts.uid == vstrUserID)
        thisAccountList = findRequest.fetch()

        if len(thisAccountList) > 0:
            thisAccount = thisAccountList[0]
        else:
            findRequest = Accounts.query(Accounts.email == vstrEmail)
            thisAccountList = findRequest.fetch()

            if len(thisAccountList) > 0:
                thisAccount = thisAccountList[0]
            else:
                thisAccount = Accounts()


        findRequest = SMSAccount.query(SMSAccount.organization_id == thisAccount.organization_id)
        thisSMSAccountList = findRequest.fetch()

        if len(thisSMSAccountList) > 0:
            thisSMSAccount = thisSMSAccountList[0]
        else:
            thisSMSAccount = SMSAccount()

        findRequest = Organization.query(Organization.strOrganizationID == thisAccount.organization_id)
        thisOrgList = findRequest.fetch()

        if len(thisOrgList) > 0:
            thisOrg = thisOrgList[0]
        else:
            thisOrg = Organization()

        template = template_env.get_template('templates/account/accountinfo.html')
        context = {'thisSMSAccount':thisSMSAccount,'thisAccount':thisAccount,'thisOrg':thisOrg}
        self.response.write(template.render(context))

app = webapp2.WSGIApplication([
    ('/admin', AdminHandler),
    ('/account', ThisAccountHandler)

], debug=True)
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
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
import logging
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class UserRights(ndb.Expando):

    strUserID = ndb.StringProperty()
    strUserEmail = ndb.StringProperty()
    strAdminUser = ndb.BooleanProperty(default=True)
    strSuperUser = ndb.BooleanProperty(default=False)
    strGeneralUser = ndb.BooleanProperty(default=False)

    def setAdminUser(self,strinput):
        try:
            if strinput == True:
                self.strAdminUser = strinput
                return True
            elif strinput == False:
                self.strAdminUser = strinput
                return True
            else:
                return False
        except:
            return False

    def setSuperUser(self,strinput):
        try:
            if strinput == True:
                self.strSuperUser = strinput
                return True
            elif strinput == False:
                self.strSuperUser = strinput
                return True
            else:
                return False
        except:
            return False

    def setGeneralUser(self,strinput):
        try:
            if strinput == True:
                self.strGeneralUser = strinput
                return True
            elif strinput == False:
                self.strGeneralUser = strinput
                return True
            else:
                return False
        except:
            return False

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

    def writeEmail(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strUserEmail = strinput
                return True
            else:
                return False
        except:
            return False





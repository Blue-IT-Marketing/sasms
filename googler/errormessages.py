import os
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
import logging
import datetime


template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))



class MyErrors(ndb.Expando):
    strUserRestricted = ndb.StringProperty(default="User Restricted contact your administrator")
    strAccountError = ndb.StringProperty(default="You do not have an active account yet please create your main account to start using the system")
    strAccountNotVerified = ndb.StringProperty(default="Account not verified")
    strUserSuspended = ndb.StringProperty(default="You are currently suspended from your organization account")
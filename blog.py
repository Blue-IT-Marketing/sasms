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
import datetime
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


from firebaseadmin import VerifyAndReturnAccount

class Post(ndb.Expando):
    strPostReference = ndb.StringProperty()
    strPostHeading = ndb.StringProperty()
    strPostBody = ndb.TextProperty()
    strAuthor = ndb.StringProperty()

    strSnippet = ndb.StringProperty()

    strDate = ndb.DateProperty()
    strTime = ndb.TimeProperty()

    strPublished = ndb.BooleanProperty(default=False)

    def writePublished(self,strinput):
        try:
            if strinput in [True,False]:
                self.strPublished = strinput
                return True
            else:
                return False
        except:
            return False

    def writePostReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPostReference = strinput
                return True
            else:
                return False
        except:
            return False

    def writePostHeading(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPostHeading = strinput
                return True
            else:
                return False
        except:
            return False

    def writePostBody(self,strinput):
        try:

            if strinput != None:
                self.strPostBody = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAuthor(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAuthor = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDate = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTime = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSnippet(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSnippet = strinput
                return True
            else:
                return False
        except:
            return False

    def CreatePostReference(self):
        import random,string
        try:
            strPostReference = ""
            for i in range(12):
                strPostReference += random.SystemRandom().choice(string.digits + string.ascii_lowercase)

            return strPostReference
        except:
            return None



class BlogHandler(webapp2.RequestHandler):
    def get(self):

        findRequest = Post.query(Post.strPublished == True).order(Post.strDate)
        thisPostsList = findRequest.fetch()

        if len(thisPostsList) > 0:
            thisPost = thisPostsList[0]
        else:
            thisPost = Post()


        template = template_env.get_template('templates/blog/blog.html')
        context = {'thisPostsList':thisPostsList,'thisPost':thisPost}
        self.response.write(template.render(context))

    def post(self):

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            template = template_env.get_template('templates/dashboard/blog/blog.html')
            context = {}
            self.response.write(template.render(context))

        elif vstrChoice == "1":
            vstrHeading = self.request.get('vstrHeading')
            vstrIntroduction = self.request.get('vstrIntroduction')
            vstrBody = self.request.get('vstrBody')

            vstrThisDateTime = datetime.datetime.now()
            strThisDate = datetime.date(year=vstrThisDateTime.year,month=vstrThisDateTime.month,day=vstrThisDateTime.day)
            strThisTime = datetime.time(hour=vstrThisDateTime.hour,minute=vstrThisDateTime.minute,second=vstrThisDateTime.second)

            thisPost = Post()
            thisPost.writePostHeading(strinput=vstrHeading)
            thisPost.writePostBody(strinput=vstrBody)
            thisPost.writeSnippet(strinput=vstrIntroduction)
            thisPost.writeAuthor(strinput="Justice Ndou")
            thisPost.writeDate(strinput=strThisDate)
            thisPost.writeTime(strinput=strThisTime)
            thisPost.writePublished(strinput=True)
            thisPost.writePostReference(strinput=thisPost.CreatePostReference())
            thisPost.put()
            self.response.write("Blog Post Successfully updated")



class ThisBlogHandler(webapp2.RequestHandler):
    def get(self):
        URL = self.request.url
        strURLList = URL.split("/")
        strPostReference = strURLList[len(strURLList) - 1]

        findRequest = Post.query(Post.strPostReference == strPostReference)
        thisPostList = findRequest.fetch()

        if len(thisPostList) > 0:
            thisPost = thisPostList[0]
        else:
            thisPost = Post()

        template = template_env.get_template('templates/blog/posts/post.html')
        context = {'thisPost':thisPost}
        self.response.write(template.render(context))

    def post(self):
        vstrChoice = self.request.get("vstrChoice")

        if vstrChoice == "0":
            vstrArticleID = self.request.get('vstrarticleID')

            findRequest = Post.query(Post.strPostReference == vstrArticleID)
            thisPostList = findRequest.fetch()

            if len(thisPostList) > 0:
                thisPost = thisPostList[0]
            else:
                thisPost = Post()

            template = template_env.get_template('templates/blog/posts/post-snippet.html')
            context = {'thisPost':thisPost}
            self.response.write(template.render(context))






app = webapp2.WSGIApplication([
    ('/blog', BlogHandler),
    ('/blog/.*', ThisBlogHandler)

], debug=True)
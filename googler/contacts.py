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
import logging
import math
import datetime
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
from myemail import SendEmail


class Notes(ndb.Model):
    
    contact_id = ndb.StringProperty()
    organization_id = ndb.StringProperty()

    subject = ndb.StringProperty()
    notes = ndb.StringProperty()
    date_taken = ndb.DateProperty()
    time_taken = ndb.TimeProperty()

    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.contact_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOrganizationID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.organization_id = strinput
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
    def writeNotes(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.notes = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateTaken(self,strinput):
        try:

            if isinstance(strinput,datetime.date):
                self.date_taken = strinput
                return True
            else:
                return False

        except:
            return False
    def writeTimeTaken(self,strinput):
        try:

            if isinstance(strinput,datetime.time):
                self.time_taken = strinput
                return True
            else:
                return False
        except:
            return False

class Contacts(ndb.Model):
    uid = ndb.StringProperty()
    organization_id = ndb.StringProperty()


    contact_id = ndb.StringProperty()

    id_number = ndb.StringProperty()

    title = ndb.StringProperty()
    names = ndb.StringProperty()
    surname = ndb.StringProperty()
    cell = ndb.StringProperty()
    tel = ndb.StringProperty()
    fax = ndb.StringProperty()
    email = ndb.StringProperty()
    website = ndb.StringProperty()

    date_created = ndb.DateProperty()


    def CreateContactID(self):
        import string,random
        try:
            strContactID = ""
            for i in range(13):
                strContactID +=  random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            return strContactID
        except:
            return None

    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.contact_id = strinput
                return True
            else:
                return False
        except:
            return False


    def writeTitle(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.title = strinput
                return True
            else:
                return False
        except:
            return False

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
    def writeOrganizationID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.organization_id = strinput
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
    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.tel = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFax(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.fax = strinput
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
    def writeDateCreated(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.date_created = strinput
                return True
            else:
                return False
        except:
            return False


    def sendEmailToContact(self,strMessage,strSubject):
        pass

    def sendSMSToContact(self,strMessage):
        pass

    def sendFax(self):
        pass

class PostalAddress(ndb.Model):
    contact_id = ndb.StringProperty()
    organization_id = ndb.StringProperty()
    box = ndb.StringProperty()
    city_town = ndb.StringProperty()
    province = ndb.StringProperty()
    country = ndb.StringProperty()
    postal_code = ndb.StringProperty()


    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)

            if strinput != None:
                self.contact_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOrganizationID(self,strinput):
        try:

            strinput = str(strinput)
            if strinput != None:
                self.organization_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBox(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.box = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCityTown(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.city_town = strinput
                return True
            else:
                return False
        except:
            return False
    def writeProvince(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.province = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCountry(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.country = strinput
                return True
            else:
                return False
        except:
            return False
    def writePostalCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.postal_code = strinput
                return True
            else:
                return False
        except:
            return False

class PhysicalAddress(ndb.Model):
    contact_id = ndb.StringProperty()
    organization_id = ndb.StringProperty()

    stand_number = ndb.StringProperty()
    street_name = ndb.StringProperty()
    city_town = ndb.StringProperty()
    province = ndb.StringProperty()
    country = ndb.StringProperty()
    postal_code = ndb.StringProperty()


    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.contact_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOrganizationID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.organization_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStandNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.stand_number = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStreetName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.street_name = strinput
                return True
            else:
                return False

        except:
            return False
    def writeCityTown(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.city_town = strinput
                return True
            else:
                return False
        except:
            return False
    def writeProvince(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.province =  strinput
                return True
            else:
                return False
        except:
            return False
    def writeCountry(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.country = strinput
                return True
            else:
                return False
        except:
            return False
    def writePostalCode(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.postal_code = strinput
                return True
            else:
                return False
        except:
            return False

class SMSOutBox(ndb.Model):
    contact_id = ndb.StringProperty()
    message_id = ndb.StringProperty()
    message = ndb.StringProperty()
    is_sent = ndb.BooleanProperty(default=False)
    date_sent = ndb.DateProperty()
    time_sent = ndb.TimeProperty()

    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.contact_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeMessageID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.message_id = strinput
                return True
            else:
                return False

        except:
            return False

    def writeMessage(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.message = strinput
                return True
            else:
                return False
        except:
            return False

    def writeIsSent(self,strinput):
        try:
            if strinput in [True,False]:
                self.is_sent = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateSent(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.date_sent = strinput
                return True
            else:
                return False

        except:
            return False

    def writeTimeSent(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.time_sent = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateMessageID(self):
        import random,string
        try:
            strMessageID = ""
            for i in range(13):
                strMessageID += random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            return strMessageID
        except:
            return None

class SMSInBox(ndb.Model):
    contact_id = ndb.StringProperty()
    message_id = ndb.StringProperty()
    response = ndb.StringProperty()
    date_received = ndb.DateProperty()
    time_received = ndb.TimeProperty()


    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.contact_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeMessageID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.message_id = strinput
                return True
            else:
                return False
        except:
            return False

    def writeResponse(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.response = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateReceived(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.date_received = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeReceived(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.time_received = strinput
                return True
            else:
                return False

        except:
            return False

class EmailOutBox(ndb.Model):
    contact_id = ndb.StringProperty()
    subject = ndb.StringProperty()
    message = ndb.StringProperty()
    is_sent = ndb.BooleanProperty(default=False)
    date_sent = ndb.DateProperty()
    time_sent = ndb.TimeProperty()
    message_id = ndb.StringProperty()
    from_email = ndb.StringProperty()

    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)

            if strinput != None:
                self.contact_id = strinput
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

    def writeMessage(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.message = strinput
                return True
            else:
                return False
        except:
            return False

    def writeIsSent(self,strinput):
        try:
            if isinstance(strinput,bool):
                self.is_sent = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateSent(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.date_sent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeSent(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.time_sent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMessageID(self,strinput):
        try:
            if isinstance(strinput,str):
                self.message_id = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateMessageID(self):
        import random,string
        try:
            strMessageID = ""
            for i in range(13):
                strMessageID += random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            return strMessageID
        except:
            return None

    def sendEmail(self):
        """
            sending an email on behalf of the contact
        :return:
        """
        try:
            findRequest = Contacts.query(Contacts.contact_id == self.contact_id)
            thisContactList = findRequest.fetch()

            if len(thisContactList) > 0:
                thisContact = thisContactList[0]

                self.from_email = str(self.contact_id) + "@sa-sms.appspotmail.com"

                if SendEmail(strFrom=self.from_email, strTo=thisContact.email, strSubject=self.subject, strBody=self.message, strTextType='text/plain'):
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False

class EmailInBox(ndb.Model):
    contact_id = ndb.StringProperty()
    subject = ndb.StringProperty()
    response = ndb.StringProperty()
    date_received = ndb.DateProperty()
    time_received = ndb.TimeProperty()
    message_id = ndb.StringProperty()


    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.contact_id = strinput
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


    def writeResponse(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.response = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateReceived(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.date_received = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeReceived(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.time_received = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMessageID(self,strinput):
        try:
            if strinput != None:
                self.message_id = strinput
                return True
            else:
                return False
        except:
            return False


from firebaseadmin import VerifyAndReturnAccount

class ContactsHandler():


    def get(self):

        from accounts import Accounts,UserRights

        vstrUserID = self.request.get('vstrUserID')
        vstrEmail = self.request.get('vstrEmail')
        vstrAccessToken = self.request.get('vstrAccessToken')

        thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
        if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

            findRequests = Contacts.query(Contacts.organization_id == thisMainAccount.organization_id)
            thisContactsList = findRequests.fetch()



            template = template_env.get_template("templates/contacts/contacts.html")
            context = {'thisContactsList':thisContactsList}
            self.response.write(template.render(context))



    def post(self):

        from accounts import Accounts,UserRights

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            vstrNames = self.request.get('vstrNames')
            vstrSurname = self.request.get('vstrSurname')
            vstrCell = self.request.get('vstrCell')
            vstrTel = self.request.get('vstrTel')
            vstrFax = self.request.get('vstrFax')
            vstrEmail = self.request.get('vstrEmail')
            vstrWebsite = self.request.get('vstrWebsite')
            vstrDateCreated = self.request.get('vstrDateCreated')
            vstrTitle= self.request.get('vstrTitle')

            #'&vstrUserID=' + struid + '&vstrAccessToken=' + accessToken

            vstrUserID = self.request.get('vstrUserID')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequests = Contacts.query(Contacts.cell == vstrCell, Contacts.organization_id == thisMainAccount.organization_id)
                thisContactList = findRequests.fetch()

                if len(thisContactList) > 0:
                    thisContact = thisContactList[0]
                else:
                    thisContact = Contacts()
                    thisContact.writeContactID(strinput=thisContact.CreateContactID())

                thisContact.writeOrganizationID(strinput=thisMainAccount.organization_id)
                thisContact.writeNames(strinput=vstrNames)
                thisContact.writeSurname(strinput=vstrSurname)
                thisContact.writeCell(strinput=vstrCell)
                thisContact.writeTel(strinput=vstrTel)
                thisContact.writeFax(strinput=vstrFax)
                thisContact.writeEmail(strinput=vstrEmail)
                thisContact.writeWebsite(strinput=vstrWebsite)
                thisContact.writeDateCreated(strinput=vstrDateCreated)
                thisContact.writeTitle(strinput=vstrTitle)
                thisContact.put()
                self.response.write("Contact successfully uploaded")


class ThisContactHandler():
    def get(self):
        URL = self.request.url
        URLlist = URL.split("/")
        vstrCell = URLlist[len(URLlist) - 1]

        findRequest = Contacts.query(Contacts.cell == vstrCell)
        thisContactList = findRequest.fetch()

        if len(thisContactList) > 0:
            thisContact = thisContactList[0]
        else:
            thisContact = Contacts()

        template   = template_env.get_template('templates/contacts/thisContact.html')
        context = {'thisContact':thisContact}
        self.response.write(template.render(context))

    def post(self):


        from accounts import Accounts,Organization
        from userRights import UserRights
        from mysms import DeliveryReport

        vstrChoice  = self.request.get('vstrChoice')
        if vstrChoice == "0":
            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

            vstrCell = self.request.get('vstrCell')
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequests = Contacts.query(Contacts.cell == vstrCell, Contacts.organization_id == thisMainAccount.organization_id)
                thisContactList = findRequests.fetch()

                if len(thisContactList) > 0:
                    thisContact = thisContactList[0]
                else:
                    thisContact = Contacts()


                findRequests = Notes.query(Notes.contact_id == thisContact.contact_id)
                thisNotesList = findRequests.fetch()

                findRequests = PostalAddress.query(PostalAddress.contact_id == thisContact.contact_id)
                thisPostalAddressList = findRequests.fetch()

                if len(thisPostalAddressList) > 0:
                    thisPostalAddress = thisPostalAddressList[0]
                else:
                    thisPostalAddress = PostalAddress()
                    thisPostalAddress.writeContactID(strinput=thisContact.contact_id)
                    thisPostalAddress.writeOrganizationID(strinput=thisContact.organization_id)
                    thisPostalAddress.put()


                findRequests = PhysicalAddress.query(PhysicalAddress.contact_id == thisContact.contact_id)
                thisPhysicalAddressList = findRequests.fetch()

                if len(thisPhysicalAddressList) > 0:
                    thisPhysicalAddress = thisPhysicalAddressList[0]
                else:
                    thisPhysicalAddress = PhysicalAddress()
                    thisPhysicalAddress.writeContactID(strinput=thisContact.contact_id)
                    thisPhysicalAddress.writeOrganizationID(strinput=thisContact.organization_id)
                    thisPhysicalAddress.put()

                template = template_env.get_template('templates/contacts/sub/manage.html')
                context = {'thisContact':thisContact,'thisNotesList':thisNotesList,'thisPostalAddress':thisPostalAddress,'thisPhysicalAddress':thisPhysicalAddress}
                self.response.write(template.render(context))

        elif vstrChoice == "1":

            vstrContactID = self.request.get('vstrContactID')
            vstrPostalCode = self.request.get('vstrPostalCode')
            vstrCountry = self.request.get('vstrCountry')
            vstrProvince = self.request.get('vstrProvince')
            vstrCityTown = self.request.get('vstrCityTown')
            vstrBox = self.request.get('vstrBox')

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequests = PostalAddress.query(PostalAddress.contact_id == vstrContactID)
                thisPostalAddressList = findRequests.fetch()


                if len(thisPostalAddressList) > 0:
                    thisPostalAddress = thisPostalAddressList[0]
                else:
                    thisPostalAddress = PostalAddress()

                thisPostalAddress.writeOrganizationID(strinput=thisMainAccount.organization_id)
                thisPostalAddress.writeContactID(strinput=vstrContactID)
                thisPostalAddress.writeBox(strinput=vstrBox)
                thisPostalAddress.writeCityTown(strinput=vstrCityTown)
                thisPostalAddress.writeProvince(strinput=vstrProvince)
                thisPostalAddress.writeCountry(strinput=vstrCountry)
                thisPostalAddress.writePostalCode(strinput=vstrPostalCode)
                thisPostalAddress.put()

                self.response.write("Postal Address updated successfully")

        elif vstrChoice == "2":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')


            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):
                vstrSubject = self.request.get('vstrSubject')
                vstrNotes = self.request.get('vstrNotes')
                vstrContactID = self.request.get('vstrContactID')

                findRequests = Notes.query(Notes.contact_id == vstrContactID, Notes.subject == vstrSubject, Notes.notes == vstrNotes)
                thisNotesList = findRequests.fetch()

                if len(thisNotesList) > 0:
                    thisNote = thisNotesList[0]
                else:
                    thisNote = Notes()

                thisNote.writeContactID(strinput=vstrContactID)
                thisNote.writeOrganizationID(strinput=thisMainAccount.organization_id)
                thisDate = datetime.datetime.now()
                thisDate  = thisDate.date()
                thisNote.writeDateTaken(strinput=thisDate)
                thisTime = datetime.datetime.now()
                thisTime  = thisTime.time()
                thisTime = datetime.time(hour=thisTime.hour,minute=thisTime.minute,second=thisTime.second)
                thisNote.writeTimeTaken(strinput=thisTime)
                thisNote.writeSubject(strinput=vstrSubject)
                thisNote.writeNotes(strinput=vstrNotes)
                thisNote.put()

                self.response.write("Note successfully uploaded")

        elif vstrChoice == "3":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrContactID = self.request.get('vstrContactID')
                vstrStandNumber = self.request.get('vstrStandNumber')
                vstrStreetName = self.request.get('vstrStreetName')
                vstrPhyCityTown = self.request.get('vstrPhyCityTown')
                vstrPhyProvince = self.request.get('vstrPhyProvince')
                vstrPhyCountry = self.request.get('vstrPhyCountry')
                vstrPhyPostalCode = self.request.get('vstrPhyPostalCode')

                findRequests = PhysicalAddress.query(PhysicalAddress.contact_id == vstrContactID)
                thisPhysicalAddressList = findRequests.fetch()

                if len(thisPhysicalAddressList) > 0:
                    thisPhysicalAddress = thisPhysicalAddressList[0]
                else:
                    thisPhysicalAddress = PhysicalAddress()

                thisPhysicalAddress.writeContactID(strinput=vstrContactID)
                thisPhysicalAddress.writeOrganizationID(strinput=thisMainAccount.organization_id)
                thisPhysicalAddress.writeStandNumber(strinput=vstrStandNumber)
                thisPhysicalAddress.writeStreetName(strinput=vstrStreetName)
                thisPhysicalAddress.writeCityTown(strinput=vstrPhyCityTown)
                thisPhysicalAddress.writeProvince(strinput=vstrPhyProvince)
                thisPhysicalAddress.writeCountry(strinput=vstrPhyCountry)
                thisPhysicalAddress.writePostalCode(strinput=vstrPhyPostalCode)

                thisPhysicalAddress.put()

                self.response.write("Physical Address successfully updated")

        elif vstrChoice == "4":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrCell = self.request.get('vstrCell')
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                findRequests = Contacts.query(Contacts.organization_id == thisMainAccount.organization_id, Contacts.cell == vstrCell)
                thisContactList = findRequests.fetch()

                if len(thisContactList) > 0:
                    thisContact = thisContactList[0]
                else:
                    thisContact = Contacts()

                findRequests = SMSInBox.query(SMSInBox.contact_id == thisContact.contact_id)
                thisInBoxMessagesList = findRequests.fetch()

                findRequests = SMSOutBox.query(SMSOutBox.contact_id == thisContact.contact_id)
                thisSMSOutBoxList = findRequests.fetch()



                findRequest = DeliveryReport.query(DeliveryReport.cell == vstrCell, DeliveryReport.response_received == True)
                thisResponsesList = findRequest.fetch()

                template = template_env.get_template('templates/contacts/sub/sms.html')
                context = {'thisInBoxMessagesList':thisInBoxMessagesList,'thisSMSOutBoxList':thisSMSOutBoxList,
                           'thisContact':thisContact,'thisResponsesList':thisResponsesList}
                self.response.write(template.render(context))

        elif vstrChoice == "5":
            from mysms import SMSAccount,SMSPortalVodacom,SMSPortalBudget,DeliveryReport,ClickSendSMSPortal
            from myTwilio import MyTwilioPortal
            vstrMessage = self.request.get('vstrMessage')
            vstrContactID = self.request.get('vstrContactID')
            vstrCell = self.request.get('vstrCell')

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = Organization.query(Organization.strOrganizationID == thisMainAccount.organization_id)
                thisOrgList = findRequest.fetch()

                if len(thisOrgList) > 0:
                    thisOrg = thisOrgList[0]
                    if thisOrg.verified:

                        findRequest = SMSAccount.query(SMSAccount.organization_id == thisMainAccount.organization_id)
                        thisSMSAccountList = findRequest.fetch()
                        if len(thisSMSAccountList) > 0:
                            thisSMSAccount = thisSMSAccountList[0]
                        else:
                            thisSMSAccount = SMSAccount()

                        if thisSMSAccount.strUsePortal == "Vodacom":

                            findRequest = SMSPortalVodacom.query()
                            thisPortalList = findRequest.fetch()

                            if len(thisPortalList) > 0:
                                thisPortal = thisPortalList[0]
                            else:
                                thisPortal = SMSPortalVodacom()

                            i = 0

                            message = mail.EmailMessage()
                            message.sender = thisPortal.strSenderAddress
                            message.to = thisPortal.strEmailAddress
                            message.subject = vstrCell
                            message.body = vstrMessage
                            message.send()
                            thisPortal.strAvailableCredit = thisPortal.strAvailableCredit - 1

                            thisDeliveryReport = DeliveryReport()
                            thisDeliveryReport.writeGroupID(vstrContactID)
                            thisDeliveryReport.writeOrganizationID(strinput=thisSMSAccount.organization_id)
                            thisDeliveryReport.writeCell(vstrCell)
                            thisDeliveryReport.writeDelivered(strinput=True)
                            thisDate = datetime.datetime.now()
                            strThisDate = thisDate.date()
                            strThisTime = thisDate.time()
                            strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,second=strThisTime.second)
                            thisDeliveryReport.writeDate(strinput=strThisDate)
                            thisDeliveryReport.writeTime(strinput=strThisTime)
                            thisDeliveryReport.writeMessageID(strinput=vstrMessage)
                            thisDeliveryReport.put()
                            thisPortal.put()

                            thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - 1
                            thisSMSAccount.put()


                            thisOutBox = SMSOutBox()
                            thisOutBox.writeMessage(strinput=vstrMessage)
                            thisOutBox.writeContactID(strinput=vstrContactID)
                            thisOutBox.writeMessageID(strinput=thisOutBox.CreateMessageID())
                            thisOutBox.writeDateSent(strinput=strThisDate)
                            thisOutBox.writeTimeSent(strinput=strThisTime)
                            thisOutBox.put()

                            self.response.write("SMS Successfully sent")

                        elif thisSMSAccount.strUsePortal == "Budget":
                            findRequest = SMSPortalBudget.query()
                            thisPortalList = findRequest.fetch()

                            if len(thisPortalList) > 0:
                                thisPortal = thisPortalList[0]
                            else:
                                thisPortal = SMSPortalBudget()

                            i = 0
                            thisDate = datetime.datetime.now()
                            strThisDate = thisDate.date()
                            strThisTime = thisDate.time()
                            thisOutBox = SMSOutBox()
                            thisOutBox.writeMessage(strinput=vstrMessage)
                            thisOutBox.writeContactID(strinput=vstrContactID)
                            thisOutBox.writeMessageID(strinput=thisOutBox.CreateMessageID())
                            thisOutBox.writeDateSent(strinput=strThisDate)
                            thisOutBox.writeTimeSent(strinput=strThisTime)
                            thisOutBox.put()

                            ref = thisPortal.SendCronMessage(strMessage=vstrMessage,strCell=vstrCell)

                            if not(ref == None):

                                thisPortal.strAvailableCredit = thisPortal.strAvailableCredit - 1

                                thisDeliveryReport = DeliveryReport()
                                thisDeliveryReport.writeGroupID(vstrContactID)
                                thisDeliveryReport.writeOrganizationID(strinput=thisSMSAccount.organization_id)
                                thisDeliveryReport.writeCell(vstrCell)
                                thisDeliveryReport.writeDelivered(strinput=True)

                                thisDate = datetime.datetime.now()
                                strThisDate = thisDate.date()
                                strThisTime = thisDate.time()
                                strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,second=strThisTime.second)
                                thisDeliveryReport.writeDate(strinput=strThisDate)
                                thisDeliveryReport.writeTime(strinput=strThisTime)
                                thisDeliveryReport.writeMessageID(strinput=thisOutBox.message_id)
                                thisDeliveryReport.writeReference(strinput=ref)
                                thisDeliveryReport.put()
                                thisPortal.put()

                                thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - 1
                                thisSMSAccount.put()

                                self.response.write("SMS Successfully Sent")
                            else:
                                self.response.write("Unable to send SMS Message")

                        elif thisSMSAccount.strUsePortal == "ClickSend":
                            findRequest = ClickSendSMSPortal.query()
                            thisClickSendPortalList = findRequest.fetch()

                            if len(thisClickSendPortalList) > 0:
                                thisPortal = thisClickSendPortalList[0]
                            else:
                                thisPortal = ClickSendSMSPortal()

                            i = 0
                            thisDate = datetime.datetime.now()
                            strThisDate = thisDate.date()
                            strThisTime = thisDate.time()
                            thisOutBox = SMSOutBox()
                            thisOutBox.writeMessage(strinput=vstrMessage)
                            thisOutBox.writeContactID(strinput=vstrContactID)
                            thisOutBox.writeMessageID(strinput=thisOutBox.CreateMessageID())
                            thisOutBox.writeDateSent(strinput=strThisDate)
                            thisOutBox.writeTimeSent(strinput=strThisTime)
                            thisOutBox.put()

                            ref = thisPortal.SendSMS(strMessage=vstrMessage,strCell=vstrCell)

                            if ref != None:

                                thisDeliveryReport = DeliveryReport()
                                thisDeliveryReport.writeGroupID(vstrContactID)
                                thisDeliveryReport.writeOrganizationID(strinput=thisSMSAccount.organization_id)
                                thisDeliveryReport.writeCell(vstrCell)
                                thisDeliveryReport.writeDelivered(strinput=True)

                                thisDate = datetime.datetime.now()
                                strThisDate = thisDate.date()
                                strThisTime = thisDate.time()
                                strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,
                                                            second=strThisTime.second)
                                thisDeliveryReport.writeDate(strinput=strThisDate)
                                thisDeliveryReport.writeTime(strinput=strThisTime)
                                thisDeliveryReport.writeMessageID(strinput=thisOutBox.message_id)
                                thisDeliveryReport.writeReference(strinput=ref)
                                thisDeliveryReport.put()
                                thisPortal.put()

                                thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - 1
                                thisSMSAccount.put()

                                self.response.write("SMS Successfully Sent")
                            else:
                                self.response.write("Unable to send SMS Message")

                        elif thisSMSAccount.strUsePortal == "Twilio":
                            findRequest = MyTwilioPortal.query()
                            thisTwilioPortalList = findRequest.fetch()

                            if len(thisTwilioPortalList) > 0:
                                thisPortal = thisTwilioPortalList[0]
                            else:
                                thisPortal = MyTwilioPortal()

                            i = 0
                            thisDate = datetime.datetime.now()
                            strThisDate = thisDate.date()
                            strThisTime = thisDate.time()
                            thisOutBox = SMSOutBox()
                            thisOutBox.writeMessage(strinput=vstrMessage)
                            thisOutBox.writeContactID(strinput=vstrContactID)
                            thisOutBox.writeMessageID(strinput=thisOutBox.CreateMessageID())
                            thisOutBox.writeDateSent(strinput=strThisDate)
                            thisOutBox.writeTimeSent(strinput=strThisTime)
                            thisOutBox.put()

                            ref = thisPortal.SendSMS(strMessage=vstrMessage,strCell=vstrCell)

                            if ref != None:

                                thisDeliveryReport = DeliveryReport()
                                thisDeliveryReport.writeGroupID(vstrContactID)
                                thisDeliveryReport.writeOrganizationID(strinput=thisSMSAccount.organization_id)
                                thisDeliveryReport.writeCell(vstrCell)
                                thisDeliveryReport.writeDelivered(strinput=True)

                                thisDate = datetime.datetime.now()
                                strThisDate = thisDate.date()
                                strThisTime = thisDate.time()
                                strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,
                                                            second=strThisTime.second)
                                thisDeliveryReport.writeDate(strinput=strThisDate)
                                thisDeliveryReport.writeTime(strinput=strThisTime)
                                thisDeliveryReport.writeMessageID(strinput=thisOutBox.message_id)
                                thisDeliveryReport.writeReference(strinput=ref)
                                thisDeliveryReport.put()
                                thisPortal.put()

                                thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - 1
                                thisSMSAccount.put()

                                self.response.write("SMS Successfully Sent")
                            else:
                                self.response.write("Unable to send SMS Message")

                    else:
                        self.response.write("Please verify your organization before sending SMS Messages")

        elif vstrChoice == "6":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrCell = self.request.get('vstrCell')
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                findRequest = Contacts.query(Contacts.cell == vstrCell)
                thisContactList = findRequest.fetch()

                if len(thisContactList) > 0:
                    thisContact = thisContactList[0]
                else:
                    thisContact = Contacts()


                findRequest = EmailInBox.query(EmailInBox.contact_id == thisContact.contact_id)
                thisEmailInboxList = findRequest.fetch()

                findRequest = EmailOutBox.query(EmailOutBox.contact_id == thisContact.contact_id)
                thisEmailOutBoxList = findRequest.fetch()

                template = template_env.get_template('templates/contacts/sub/email.html')
                context = {'vstrCell':vstrCell,'thisEmailInboxList':thisEmailInboxList,'thisEmailOutBoxList':thisEmailOutBoxList}
                self.response.write(template.render(context))

        elif vstrChoice == "7":

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')



            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):
                vstrCell = self.request.get('vstrCell')
                vstrSubject = self.request.get('vstrSubject')
                vstrMessage = self.request.get('vstrMessage')

                findRequest = Organization.query(Organization.strOrganizationID == thisMainAccount.organization_id)
                thisOrgList = findRequest.fetch()

                if len(thisOrgList) > 0:
                    thisOrg = thisOrgList[0]

                    if thisOrg.verified:


                        findRequest = Contacts.query(Contacts.cell == vstrCell)
                        thisContactList = findRequest.fetch()

                        if len(thisContactList) > 0:
                            thisContact = thisContactList[0]
                        else:
                            thisContact = Contacts()

                        findRequest = EmailOutBox.query(EmailOutBox.subject == vstrSubject, EmailOutBox.message == vstrMessage)
                        thisEmailOutBoxList = findRequest.fetch()

                        if len(thisEmailOutBoxList) > 0:
                            thisEmailOutBox = thisEmailOutBoxList[0]
                        else:
                            thisEmailOutBox = EmailOutBox()

                        thisEmailOutBox.writeContactID(strinput=thisContact.contact_id)
                        thisEmailOutBox.writeMessageID(strinput=thisEmailOutBox.CreateMessageID())
                        thisEmailOutBox.writeMessage(strinput=vstrMessage)
                        thisDate = datetime.datetime.now()
                        thisDate = thisDate.date()
                        thisTime = datetime.datetime.now()
                        thisTime = datetime.time(hour=thisTime.hour,minute=thisTime.minute,second=thisTime.second)
                        if thisEmailOutBox.sendEmail():
                            thisEmailOutBox.writeIsSent(strinput=True)
                            thisEmailOutBox.writeTimeSent(strinput=thisTime)
                            thisEmailOutBox.writeDateSent(strinput=thisDate)

                            thisEmailOutBox.put()
                            self.response.write("Successfully sent an Email")
                        else:
                            self.response.write("Error Sending Email")
                    else:
                        self.response.write("Please verify your organization before sending emails")

app = webapp2.WSGIApplication([
    ('/admin/contacts', ContactsHandler),
    ('/admin/contacts/.*', ThisContactHandler)
], debug=True)

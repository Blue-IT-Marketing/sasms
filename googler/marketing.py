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
import urllib
from google.cloud import ndb
from userRights import UserRights
from accounts import Accounts
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
import logging
import requests
import re


class ShortenURL(object):
    """ A class that defines the default URL Shortener.

    TinyURL is provided as the default and as an example helper class to make
    URL Shortener calls if/when required. """

    def __init__(self,
                 userid=None,
                 password=None):
        """Instantiate a new ShortenURL object. TinyURL, which is used for this
        example, does not require a userid or password, so you can try this
        out without specifying either.

        Args:
            userid:   userid for any required authorization call [optional]
            password: password for any required authorization call [optional]
        """
        self.userid = userid
        self.password = password

    def Shorten(self, long_url):
        """ Call TinyURL API and returned shortened URL result.
        Args:
            long_url: URL string to shorten
        Returns:
            The shortened URL as a string
        Note:
            long_url is required and no checks are made to ensure completeness
        """

        result = None
        f = requests.get("http://tinyurl.com/api-create.php?url={0}".format(
            long_url))
        try:
            result = f.read()
        finally:
            f.close()

        # The following check is required for py2/py3 compatibility, since
        # urlopen on py3 returns a bytes-object, and urlopen on py2 returns a
        # string.
        if isinstance(result, bytes):
            return result.decode('utf8')
        else:
            return result

class FacebookMessages(ndb.Model):
    message_id = ndb.StringProperty()
    message = ndb.TextProperty()
    message_status = ndb.StringProperty(default="Ready") # Sent
    date_sent = ndb.DateProperty()
    time_sent = ndb.TimeProperty()

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
    def writeMessageStatus(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ["Sent","sent","Ready","ready"]:
                self.message_status = strinput
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
            for i in range(26):
                strMessageID += random.SystemRandom().choice(string.digits + string.ascii_lowercase)
            return strMessageID
        except:
            return None

class FacebookGroups(ndb.Model):
    group_id = ndb.StringProperty()
    group_state = ndb.StringProperty(default="Open") # Closed
    blocked = ndb.BooleanProperty(default=False)
    failed_attempts = ndb.IntegerProperty(default=0)

    def writeGroupID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.group_id = strinput
                return True
            else:
                return False
        except:
            return False
    def writeGroupState(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ["Open","Closed","open","closed"]:
                self.group_state = strinput
                return True
            else:
                return False
        except:
            return False

    def writeBlocked(self,strinput):
        try:
            if strinput in [True,False]:
                self.blocked = strinput
                return True
            else:
                return False
        except:
            return False

    def writeFailedAttempts(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) > 0):
                self.failed_attempts += int(strinput)
                return True
            else:
                return False
        except:
            return False

class FaceGroupAutoPosterSettings(ndb.Model):
    api = ndb.StringProperty(os.environ.get('FACEBOOK_GRAPH_API_KEY'))
    last_message_sent = ndb.StringProperty()
    start_run = ndb.BooleanProperty(default=False)
    retry = ndb.IntegerProperty(default=5)
    first_run = ndb.BooleanProperty(default=True)


    def writeAPI(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.api = strinput
                return True
            else:
                return False
        except:
            return False

    def writeStartRun(self,strinput):
        try:
            if strinput in [True,False]:
                self.start_run = strinput
                return True
            else:
                return False
        except:
            return False

    def writeRetry(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) > 0):
                self.retry = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeFirstRun(self,strinput):
        try:
            if strinput in [True,False]:
                self.first_run = strinput
                return True
            else:
                return False
        except:
            return False

class TwitterSettings(ndb.Model):
    #api = TwitterAPI(consumer_key,consumer_secret,auth_type='oAuth2')
    settings_id = ndb.StringProperty()
    consumer_api = ndb.StringProperty(default=os.environ.get('TWITTER_CONSUMER_API'))
    consumer_secret = ndb.StringProperty(default=os.environ.get('TWITTER_CONSUMER_SECRET'))
    access_token_key = ndb.StringProperty(default=os.environ.get('TWITTER_ACCESS_TOKEN_KEY'))
    access_token_secret = ndb.StringProperty(default=os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'))

    call_back_url = ndb.StringProperty(default="https://sa-sms.appspot.com")
    app_only_authentication = ndb.StringProperty(default="https://api.twitter.com/oauth2/token")
    request_token_url = ndb.StringProperty(default="https://api.twitter.com/oauth/request_token")
    authorize_url = ndb.StringProperty(default="https://api.twitter.com/oauth/authorize")
    access_token_url = ndb.StringProperty(default="https://api.twitter.com/oauth/access_token")

    rate_limit = ndb.IntegerProperty(default=0) # Rate at which tweets can be sent
    credentials_worked = ndb.BooleanProperty(default=True)



    def writeConsumerAPI(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.consumer_api = strinput
                return True
            else:
                return False
        except:
            return False

    def writeConsumerSecret(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.consumer_secret = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAccessTokenKey(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.access_token_key = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCredentialsWorks(self,strinput):
        try:
            if strinput in [True,False]:
                self.credentials_worked = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAccessTokenSecret(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.access_token_secret = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCallBackURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.call_back_url = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAPPOnlyAuthenticationURL(self,strinput):
        try:
            strinput = str(strinput)

            if strinput != None:
                self.app_only_authentication = strinput
                return True
            else:
                return False
        except:
            return False

    def writeRequestTokenURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.request_token_url = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAuthorizeURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.authorize_url = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAccessTokenURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.access_token_url = strinput
                return True
            else:
                return False
        except:
            return False

class TwitterMessages(ndb.Model):
    message_id = ndb.StringProperty()

    message = ndb.StringProperty(default="Business Messaging, Serious About Marketing Send SMS Adverts, Surveys and Bulk SMS Messages start today https://sa-sms.appspot.com")
    media_url = ndb.StringProperty(default="https://sa-sms.appspot.com/static/dist/img/sms.jpeg")
    message_status = ndb.StringProperty(default="Ready") # Sent
    date_sent = ndb.DateProperty()
    time_sent = ndb.TimeProperty()


    def CreateMessageID(self):
        import random,string
        try:
            strMessageID = ""
            for i in range(26):
                strMessageID += random.SystemRandom().choice(string.digits + string.ascii_lowercase)
            return strMessageID
        except:
            return None

    def writeMessageID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None :
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

    def writeMediaURL(self,strinput):

        try:
            strinput = str(strinput)
            if strinput != None:
                self.media_url = strinput
                return True
            else:
                return False
        except:
            return False

    def writeMessageStatus(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ["Ready", "Sent","ready","sent"]:
                self.message_status = strinput.capitalize()
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


def FacebookGroupAutoPoster():

    native_facebook_groups = ['538342933008320', '1102533313090105', '164489826895912', '1484049628524039',
    '1603928069926995', '950322191651738','711364268938701', '274441032766829', '146876972149386', '1547776405444325',
    '784297738345030', '1511575495781679','755692847910950', '262238687211695', '1664864617114927', '1723905861222063',
    '251957491804488', '174191025183','1486373431626775', '343159492474520', '885227164831542', '578127695539798',
    '471072349663119', '1098883566843151','879486452078688', '931491813597939', '490154967827123', '177688965660272',
    '56538832229', '722960411120468', '1463758510550402','392378173668', '1456901304560845', '576508995745651', '110232907716',
    '927120324005475', '325338070893306', '790034754371631','8435656980', '280574585289376', '677089919009723', '368749976523903', '128388737052',
    '695720603784600', '170506956490414','158639990958633', '367572560012674', '355615061175037', '701170026628303',
    '534788106622337', '368085513254028', '606025329524125','1630663117178377', '1517180231872532', '343928159012007',
    '479117102273081','1637455066482964', '1244089915607083', '1533599940269521','1631550350457988', '1720682281477923',
    '1685430391674558', '1545276862466917','578454355638033', '1072733022748070', '221536938197594','446778575529751',
    '1013873848655762','1115710995106134','1772069786356199','1598112443796217','467001136828976','671898842944619',
    '941668412537650','906556536065387','1640610469529320','329568040468750','1657793177785586','2474481925','1430391003916153',
    '727573637323817','1656947441202089','155324307866118','149506018740280','130172024017663','1449934281907579',
    '730837800336990','107126572963627','712176562219634','1627920250768831','243523489167838','111904830976','285860561619633',
    '230409830494491','587959551257227','1473216516263475','528137823866443','553467354681667','187517217990286',
    '606612136070473','151973274960633','284094691733585','140653645705','439672099472239','594714773881988','111193713672',
    '164104306956514','184103631696012','197538603706948','664240323606427','442232432519601','197774950382493','1407264492828426',
    '810829005693798','940318179419497','502320243132747','132802300453356','203786410058693','1637041589892908','1468664553160531',
    '198420500600522','891061780929581','848005738647762','614040405377838','872057319590582','547028591978991','123188094404370',
    '1688641051393706','1668569696790345','165768552491','1443778175891838','440686002617339','260239120726390','925986950783070',
    '1732481493746128','965010596942476','892875597476035','1893927924176512','1283427078363484','307379289380149','928783137200701',
    '4977473396','1510134682579854','100408726061','1089485814411535','545385115636321','997649333587035','603722176454062',
    '1543606095889586','160144424187088','1658489027701931','594209814060335','833200753363714','1428541787397755',
    '122248708135673','1706888759556063','465747676834716','592182754291599','1593232564275059','295650563943353',
    '603486743007117','224400727696059','710022769113385','582394958530735','1506510342986982','264850663631929',
    '1604802029807500','25601192554','1136778453013720','873874819289292','1701505993461696','1637490423203745',
    '148952955185461','1466973543578470','1407091979553310','1127393483986104','1156035977769819','1658539847762726',
    '1397113697191012','508801575862447','182305425135221','1534239730146847','363820700131','1746086708950541','693574467384316',
    '858125590921398','286635168161978','257278007747757','1449148772062684','175065069242399','240585582781522','599676956830835',
    '490674444415347','1674245802857616','424212554263176','315648031795904','919904734702356','408304439288997','932349213503882',
    '536587376495659','1424456921151976','459410427435175','102447169409','1201403736608902','1749737425263201','333780066677674',
    '195944513749408','450401991813658','152188814704','142218919148258','646685465422603','170315496348208','384510588304355',
    '142131742543914','523185731048873','680800761979419','1779077192323084','233197526773710','304261556348945','504558616231170',
    '1430109333891514','1659027771007020','767077376635822','191466331052830','640301292740952','686560551374180','1800203813539596',
    '539442972773185','107783820425','1655264228059761','1475140182718128','1612700025646277','189358431227615','150242608485563',
    '289602997904342','108798822613610','500940936729937','243941079016400','991255834224016','3391455157','1671111996494128',
    '828876950477339','301236770215087','529249277151153','179240855474784','189862404438781','204688026241326','449390561822511',
    '1668059363426647','507436076008625','310026072398295','472075392822777','563017063728296','233122546849309','1461469420768211',
    '2292539667','321161591353779','975601132536207','679206288859405','369893076477765','1659705697632881','103520569687440',
    '490679154473739','1594147557481160','28677307798','196071440407513','185041218180436','225642780952806','322352291276016',
    '257846404276208','380931315446756','386363811511995','317914378291866','142387942535037','209813225819521','1732317317014456',
    '133527986816712','29593013279','904213339661769','697832600270981','1633642200225514','320054581486654','696681767084560',
    '2589935026','599922293488350','123360237824437','1534291620144249','486770048108063','1628507944078356','581633288604367','235073923239979',
    '483795721673233','1422200781411407','422644721123231','917930858246383','953491894739573','227490057271104','148987911950101',
    '530854860312927','181474265226850','439436016112485','488870704597498','343473102333010','1494619354148670','488312691218223',
    '832271583463424','111197075591922','101597333515011','1625000364380794','1627849460831788','112159512077','1591385517796417',
    '279060572129079','550401341791811','1460122770970778','155001380737','125884654163145','286913978167041','157582414428974',
    '1571510353060324','247908098718875','1045168405519076','129242607801','640616389408190','693810073989433','902134456512819',
    '503933759632352','333850896703700','933409900058855','410964029065245','275386869304367','417492461702401']


    findRequest = FaceGroupAutoPosterSettings.query()
    FaceGroupAutoPosterList = findRequest.fetch()

    if len(FaceGroupAutoPosterList) > 0:
        FaceGroupAutoSettings = FaceGroupAutoPosterList[0]
    else:
        FaceGroupAutoSettings = FaceGroupAutoPosterSettings()


    if FaceGroupAutoSettings.first_run == True:
        thisFaceGroupsList = []
        for thisID in native_facebook_groups:
            thisFaceGroup = FacebookGroups()
            thisFaceGroup.writeGroupID(strinput=thisID)
            thisFaceGroup.writeGroupState(strinput="Open")
            thisFaceGroup.put()
            thisFaceGroupsList.append(thisFaceGroup)
    else:
        findRequest = FacebookGroups.query(FacebookGroups.blocked == False)
        thisFaceGroupsList = findRequest.fetch()


    findRequest = FacebookMessages.query(FacebookMessages.message_status == "Ready")
    thisMessagesList = findRequest.fetch()

    if (len(thisMessagesList) > 0) and (FaceGroupAutoSettings.start_run == True):
        try:
            from facepy import GraphAPI
            graph = GraphAPI(FaceGroupAutoSettings.api)
            import random
            for i in range(5):
                thisFaceGroup = random.SystemRandom().choice(thisFaceGroupsList)
                thisMessage = random.SystemRandom().choice(thisMessagesList)
                try:

                    graph.post(path=str(thisFaceGroup.group_id) + '/feed', retry=FaceGroupAutoSettings.retry, message=thisMessage)
                except:
                    thisFaceGroup.writeFailedAttempts(strinput=1)
                    if thisFaceGroup.failed_attempts > 5:
                        thisFaceGroup.writeBlocked(strinput=True)
                        thisFaceGroup.writeGroupState(strinput="Closed")
                    thisFaceGroup.put()
        except:
            #TODO- try and alternate graph API here
            pass

    FaceGroupAutoSettings.writeFirstRun(strinput=False)
    FaceGroupAutoSettings.put()


def TweetMessages():
    """
        Send Tweets from Tweets Messages
    :return: 
    """
    try:
        from urllib.request import urlopen
    except:
        from urllib2 import urlopen

    import re
    try:
        from twitter.twitter_utils import URL_REGEXP
        from twitter import Api
    except:
        from urlmarker import URL_REGEXP
        logging.error("Error with python-twitter module not found")
    import random

    findRequest = TwitterMessages.query(TwitterMessages.message_status == "Ready")
    thisTwitterMessagesList = findRequest.fetch()

    findRequest = TwitterSettings.query()
    thisTwitterSettingsList = findRequest.fetch()

    if (len(thisTwitterSettingsList) > 0):
        thisTwitterSetting = thisTwitterSettingsList[0]
    else:
        thisTwitterSetting = TwitterSettings()

    try:
        myapi = Api(consumer_key=thisTwitterSetting.consumer_api, consumer_secret=thisTwitterSetting.consumer_secret, access_token_key=thisTwitterSetting.access_token_key, access_token_secret=thisTwitterSetting.access_token_secret)

        if len(thisTwitterMessagesList) > 0:
            thisMessage = random.SystemRandom().choice(thisTwitterMessagesList)
        else:
            thisMessage = TwitterMessages()

        shortener = ShortenURL()
        urls = re.findall(URL_REGEXP, thisMessage.message)
        for url in urls:
            thisMessage.message = thisMessage.message.replace(url, shortener.Shorten(url), 1)

        myapi.PostUpdate(status=thisMessage.message)

        thisMessage.writeMessageStatus(strinput="Sent")
        vstrThisDateTime = datetime.datetime.now()
        vstrThisDate = datetime.date(year=vstrThisDateTime.year,month=vstrThisDateTime.month,day=vstrThisDateTime.day)
        vstrThisTime = datetime.time(hour=vstrThisDateTime.hour,minute=vstrThisDateTime.minute,second=vstrThisDateTime.second)

        thisMessage.writeDateSent(strinput=vstrThisDate)
        thisMessage.writeTimeSent(strinput=vstrThisTime)
        thisMessage.put()
    except:
        logging.info("We are getting an Error While Sending Twitter Messages")



def SubmitSitemap():
    #TODO- this method requires authorization
    #TODO- Consider building a dynamic sitemap
    headers = {}
    strSiteMapURL = "https://www.googleapis.com/webmasters/v3/sites/https://sa-sms.appspot.com/sitemaps/https://sa-sms.appspot.com/sitemap.xml"
    try:
        result = urlfetch.fetch(url=strSiteMapURL ,payload=None,method=urlfetch.PUT,headers=headers,validate_certificate=True)
    except:
        pass



class RouterHandler(webapp2.RequestHandler):
    def get(self):
        """
            /marketing-cron/facebook-groups
            /marketing-cron/twitter-feeds
            /marketing-cron/linkedin-crawler

        :return:
        """
        URL = self.request.url
        strURLlist = URL.split("/")

        strFunction = strURLlist[4]

        if strFunction == "facebook-groups":
            FacebookGroupAutoPoster()
        elif strFunction == "twitter-feeds":
            TweetMessages()
        elif strFunction == "linkedin-crawler":
            pass
        elif strFunction == "submit-sitemap":
            SubmitSitemap()
            #PUT https://www.googleapis.com/webmasters/v3/sites/siteUrl/sitemaps/feedpath


app = webapp2.WSGIApplication([
    ('/marketing-cron/.*', RouterHandler)
    #TODO- Create Advertising Endpoints and also Surveys End Points---Refine this idea its prooving to be difficult
], debug=True)
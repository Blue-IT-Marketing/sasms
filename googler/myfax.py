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

import json

Country_Codes = [
    {
        "Country": "AFGHANISTAN",
        "Code": "AF"
    },
    {
        "Country": "ALAND ISLANDS",
        "Code": "AX"
    },
    {
        "Country": "ALBANIA",
        "Code": "AL"
    },
    {
        "Country": "ALGERIA",
        "Code": "DZ"
    },
    {
        "Country": "AMERICAN SAMOA",
        "Code": "AS"
    },
    {
        "Country": "ANDORRA",
        "Code": "AD"
    },
    {
        "Country": "ANGOLA",
        "Code": "AO"
    },
    {
        "Country": "ANGUILLA",
        "Code": "AI"
    },
    {
        "Country": "ANTARCTICA",
        "Code": "AQ"
    },
    {
        "Country": "ANTIGUA AND BARBUDA",
        "Code": "AG"
    },
    {
        "Country": "ARGENTINA",
        "Code": "AR"
    },
    {
        "Country": "ARMENIA",
        "Code": "AM"
    },
    {
        "Country": "ARUBA",
        "Code": "AW"
    },
    {
        "Country": "AUSTRALIA",
        "Code": "AU"
    },
    {
        "Country": "AUSTRIA",
        "Code": "AT"
    },
    {
        "Country": "AZERBAIJAN",
        "Code": "AZ"
    },
    {
        "Country": "BAHAMAS",
        "Code": "BS"
    },
    {
        "Country": "BAHRAIN",
        "Code": "BH"
    },
    {
        "Country": "BANGLADESH",
        "Code": "BD"
    },
    {
        "Country": "BARBADOS",
        "Code": "BB"
    },
    {
        "Country": "BELARUS",
        "Code": "BY"
    },
    {
        "Country": "BELGIUM",
        "Code": "BE"
    },
    {
        "Country": "BELIZE",
        "Code": "BZ"
    },
    {
        "Country": "BENIN",
        "Code": "BJ"
    },
    {
        "Country": "BERMUDA",
        "Code": "BM"
    },
    {
        "Country": "BHUTAN",
        "Code": "BT"
    },
    {
        "Country": "BOLIVIA, PLURINATIONAL STATE OF",
        "Code": "BO"
    },
    {
        "Country": "BONAIRE, SINT EUSTATIUS AND SABA",
        "Code": "BQ"
    },
    {
        "Country": "BOSNIA AND HERZEGOVINA",
        "Code": "BA"
    },
    {
        "Country": "BOTSWANA",
        "Code": "BW"
    },
    {
        "Country": "BOUVET ISLAND",
        "Code": "BV"
    },
    {
        "Country": "BRAZIL",
        "Code": "BR"
    },
    {
        "Country": "BRITISH INDIAN OCEAN TERRITORY",
        "Code": "IO"
    },
    {
        "Country": "BRUNEI DARUSSALAM",
        "Code": "BN"
    },
    {
        "Country": "BULGARIA",
        "Code": "BG"
    },
    {
        "Country": "BURKINA FASO",
        "Code": "BF"
    },
    {
        "Country": "BURUNDI",
        "Code": "BI"
    },
    {
        "Country": "CAMBODIA",
        "Code": "KH"
    },
    {
        "Country": "CAMEROON",
        "Code": "CM"
    },
    {
        "Country": "CANADA",
        "Code": "CA"
    },
    {
        "Country": "CAPE VERDE",
        "Code": "CV"
    },
    {
        "Country": "CAYMAN ISLANDS",
        "Code": "KY"
    },
    {
        "Country": "CENTRAL AFRICAN REPUBLIC",
        "Code": "CF"
    },
    {
        "Country": "CHAD",
        "Code": "TD"
    },
    {
        "Country": "CHILE",
        "Code": "CL"
    },
    {
        "Country": "CHINA",
        "Code": "CN"
    },
    {
        "Country": "CHRISTMAS ISLAND",
        "Code": "CX"
    },
    {
        "Country": "COCOS (KEELING) ISLANDS",
        "Code": "CC"
    },
    {
        "Country": "COLOMBIA",
        "Code": "CO"
    },
    {
        "Country": "COMOROS",
        "Code": "KM"
    },
    {
        "Country": "CONGO",
        "Code": "CG"
    },
    {
        "Country": "CONGO, THE DEMOCRATIC REPUBLIC OF THE",
        "Code": "CD"
    },
    {
        "Country": "COOK ISLANDS",
        "Code": "CK"
    },
    {
        "Country": "COSTA RICA",
        "Code": "CR"
    },
    {
        "Country": "COTE DIVOIRE",
        "Code": "CI"
    },
    {
        "Country": "CROATIA",
        "Code": "HR"
    },
    {
        "Country": "CUBA",
        "Code": "CU"
    },
    {
        "Country": "CURACAO",
        "Code": "CW"
    },
    {
        "Country": "CYPRUS",
        "Code": "CY"
    },
    {
        "Country": "CZECH REPUBLIC",
        "Code": "CZ"
    },
    {
        "Country": "DENMARK",
        "Code": "DK"
    },
    {
        "Country": "DJIBOUTI",
        "Code": "DJ"
    },
    {
        "Country": "DOMINICA",
        "Code": "DM"
    },
    {
        "Country": "DOMINICAN REPUBLIC",
        "Code": "DO"
    },
    {
        "Country": "ECUADOR",
        "Code": "EC"
    },
    {
        "Country": "EGYPT",
        "Code": "EG"
    },
    {
        "Country": "EL SALVADOR",
        "Code": "SV"
    },
    {
        "Country": "EQUATORIAL GUINEA",
        "Code": "GQ"
    },
    {
        "Country": "ERITREA",
        "Code": "ER"
    },
    {
        "Country": "ESTONIA",
        "Code": "EE"
    },
    {
        "Country": "ETHIOPIA",
        "Code": "ET"
    },
    {
        "Country": "FALKLAND ISLANDS (MALVINAS)",
        "Code": "FK"
    },
    {
        "Country": "FAROE ISLANDS",
        "Code": "FO"
    },
    {
        "Country": "FIJI",
        "Code": "FJ"
    },
    {
        "Country": "FINLAND",
        "Code": "FI"
    },
    {
        "Country": "FRANCE",
        "Code": "FR"
    },
    {
        "Country": "FRENCH GUIANA",
        "Code": "GF"
    },
    {
        "Country": "FRENCH POLYNESIA",
        "Code": "PF"
    },
    {
        "Country": "FRENCH SOUTHERN TERRITORIES",
        "Code": "TF"
    },
    {
        "Country": "GABON",
        "Code": "GA"
    },
    {
        "Country": "GAMBIA",
        "Code": "GM"
    },
    {
        "Country": "GEORGIA",
        "Code": "GE"
    },
    {
        "Country": "GERMANY",
        "Code": "DE"
    },
    {
        "Country": "GHANA",
        "Code": "GH"
    },
    {
        "Country": "GIBRALTAR",
        "Code": "GI"
    },
    {
        "Country": "GREECE",
        "Code": "GR"
    },
    {
        "Country": "GREENLAND",
        "Code": "GL"
    },
    {
        "Country": "GRENADA",
        "Code": "GD"
    },
    {
        "Country": "GUADELOUPE",
        "Code": "GP"
    },
    {
        "Country": "GUAM",
        "Code": "GU"
    },
    {
        "Country": "GUATEMALA",
        "Code": "GT"
    },
    {
        "Country": "GUERNSEY",
        "Code": "GG"
    },
    {
        "Country": "GUINEA",
        "Code": "GN"
    },
    {
        "Country": "GUINEA-BISSAU",
        "Code": "GW"
    },
    {
        "Country": "GUYANA",
        "Code": "GY"
    },
    {
        "Country": "HAITI",
        "Code": "HT"
    },
    {
        "Country": "HEARD ISLAND AND MCDONALD ISLANDS",
        "Code": "HM"
    },
    {
        "Country": "HOLY SEE (VATICAN CITY STATE)",
        "Code": "VA"
    },
    {
        "Country": "HONDURAS",
        "Code": "HN"
    },
    {
        "Country": "HONG KONG",
        "Code": "HK"
    },
    {
        "Country": "HUNGARY",
        "Code": "HU"
    },
    {
        "Country": "ICELAND",
        "Code": "IS"
    },
    {
        "Country": "INDIA",
        "Code": "IN"
    },
    {
        "Country": "INDONESIA",
        "Code": "ID"
    },
    {
        "Country": "IRAN, ISLAMIC REPUBLIC OF",
        "Code": "IR"
    },
    {
        "Country": "IRAQ",
        "Code": "IQ"
    },
    {
        "Country": "IRELAND",
        "Code": "IE"
    },
    {
        "Country": "ISLE OF MAN",
        "Code": "IM"
    },
    {
        "Country": "ISRAEL",
        "Code": "IL"
    },
    {
        "Country": "ITALY",
        "Code": "IT"
    },
    {
        "Country": "JAMAICA",
        "Code": "JM"
    },
    {
        "Country": "JAPAN",
        "Code": "JP"
    },
    {
        "Country": "JERSEY",
        "Code": "JE"
    },
    {
        "Country": "JORDAN",
        "Code": "JO"
    },
    {
        "Country": "KAZAKHSTAN",
        "Code": "KZ"
    },
    {
        "Country": "KENYA",
        "Code": "KE"
    },
    {
        "Country": "KIRIBATI",
        "Code": "KI"
    },
    {
        "Country": "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF",
        "Code": "KP"
    },
    {
        "Country": "KOREA, REPUBLIC OF",
        "Code": "KR"
    },
    {
        "Country": "KUWAIT",
        "Code": "KW"
    },
    {
        "Country": "KYRGYZSTAN",
        "Code": "KG"
    },
    {
        "Country": "LAO PEOPLE'S DEMOCRATIC REPUBLIC",
        "Code": "LA"
    },
    {
        "Country": "LATVIA",
        "Code": "LV"
    },
    {
        "Country": "LEBANON",
        "Code": "LB"
    },
    {
        "Country": "LESOTHO",
        "Code": "LS"
    },
    {
        "Country": "LIBERIA",
        "Code": "LR"
    },
    {
        "Country": "LIBYA",
        "Code": "LY"
    },
    {
        "Country": "LIECHTENSTEIN",
        "Code": "LI"
    },
    {
        "Country": "LITHUANIA",
        "Code": "LT"
    },
    {
        "Country": "LUXEMBOURG",
        "Code": "LU"
    },
    {
        "Country": "MACAO",
        "Code": "MO"
    },
    {
        "Country": "MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF",
        "Code": "MK"
    },
    {
        "Country": "MADAGASCAR",
        "Code": "MG"
    },
    {
        "Country": "MALAWI",
        "Code": "MW"
    },
    {
        "Country": "MALAYSIA",
        "Code": "MY"
    },
    {
        "Country": "MALDIVES",
        "Code": "MV"
    },
    {
        "Country": "MALI",
        "Code": "ML"
    },
    {
        "Country": "MALTA",
        "Code": "MT"
    },
    {
        "Country": "MARSHALL ISLANDS",
        "Code": "MH"
    },
    {
        "Country": "MARTINIQUE",
        "Code": "MQ"
    },
    {
        "Country": "MAURITANIA",
        "Code": "MR"
    },
    {
        "Country": "MAURITIUS",
        "Code": "MU"
    },
    {
        "Country": "MAYOTTE",
        "Code": "YT"
    },
    {
        "Country": "MEXICO",
        "Code": "MX"
    },
    {
        "Country": "MICRONESIA, FEDERATED STATES OF",
        "Code": "FM"
    },
    {
        "Country": "MOLDOVA, REPUBLIC OF",
        "Code": "MD"
    },
    {
        "Country": "MONACO",
        "Code": "MC"
    },
    {
        "Country": "MONGOLIA",
        "Code": "MN"
    },
    {
        "Country": "MONTENEGRO",
        "Code": "ME"
    },
    {
        "Country": "MONTSERRAT",
        "Code": "MS"
    },
    {
        "Country": "MOROCCO",
        "Code": "MA"
    },
    {
        "Country": "MOZAMBIQUE",
        "Code": "MZ"
    },
    {
        "Country": "MYANMAR",
        "Code": "MM"
    },
    {
        "Country": "NAMIBIA",
        "Code": "NA"
    },
    {
        "Country": "NAURU",
        "Code": "NR"
    },
    {
        "Country": "NEPAL",
        "Code": "NP"
    },
    {
        "Country": "NETHERLANDS",
        "Code": "NL"
    },
    {
        "Country": "NEW CALEDONIA",
        "Code": "NC"
    },
    {
        "Country": "NEW ZEALAND",
        "Code": "NZ"
    },
    {
        "Country": "NICARAGUA",
        "Code": "NI"
    },
    {
        "Country": "NIGER",
        "Code": "NE"
    },
    {
        "Country": "NIGERIA",
        "Code": "NG"
    },
    {
        "Country": "NIUE",
        "Code": "NU"
    },
    {
        "Country": "NORFOLK ISLAND",
        "Code": "NF"
    },
    {
        "Country": "NORTHERN MARIANA ISLANDS",
        "Code": "MP"
    },
    {
        "Country": "NORWAY",
        "Code": "NO"
    },
    {
        "Country": "OMAN",
        "Code": "OM"
    },
    {
        "Country": "PAKISTAN",
        "Code": "PK"
    },
    {
        "Country": "PALAU",
        "Code": "PW"
    },
    {
        "Country": "PALESTINE, STATE OF",
        "Code": "PS"
    },
    {
        "Country": "PANAMA",
        "Code": "PA"
    },
    {
        "Country": "PAPUA NEW GUINEA",
        "Code": "PG"
    },
    {
        "Country": "PARAGUAY",
        "Code": "PY"
    },
    {
        "Country": "PERU",
        "Code": "PE"
    },
    {
        "Country": "PHILIPPINES",
        "Code": "PH"
    },
    {
        "Country": "PITCAIRN",
        "Code": "PN"
    },
    {
        "Country": "POLAND",
        "Code": "PL"
    },
    {
        "Country": "PORTUGAL",
        "Code": "PT"
    },
    {
        "Country": "PUERTO RICO",
        "Code": "PR"
    },
    {
        "Country": "QATAR",
        "Code": "QA"
    },
    {
        "Country": "REUNION",
        "Code": "RE"
    },
    {
        "Country": "ROMANIA",
        "Code": "RO"
    },
    {
        "Country": "RUSSIAN FEDERATION",
        "Code": "RU"
    },
    {
        "Country": "RWANDA",
        "Code": "RW"
    },
    {
        "Country": "SAINT BARTHELEMY",
        "Code": "BL"
    },
    {
        "Country": "SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA",
        "Code": "SH"
    },
    {
        "Country": "SAINT KITTS AND NEVIS",
        "Code": "KN"
    },
    {
        "Country": "SAINT LUCIA",
        "Code": "LC"
    },
    {
        "Country": "SAINT MARTIN (FRENCH PART)",
        "Code": "MF"
    },
    {
        "Country": "SAINT PIERRE AND MIQUELON",
        "Code": "PM"
    },
    {
        "Country": "SAINT VINCENT AND THE GRENADINES",
        "Code": "VC"
    },
    {
        "Country": "SAMOA",
        "Code": "WS"
    },
    {
        "Country": "SAN MARINO",
        "Code": "SM"
    },
    {
        "Country": "SAO TOME AND PRINCIPE",
        "Code": "ST"
    },
    {
        "Country": "SAUDI ARABIA",
        "Code": "SA"
    },
    {
        "Country": "SENEGAL",
        "Code": "SN"
    },
    {
        "Country": "SERBIA",
        "Code": "RS"
    },
    {
        "Country": "SEYCHELLES",
        "Code": "SC"
    },
    {
        "Country": "SIERRA LEONE",
        "Code": "SL"
    },
    {
        "Country": "SINGAPORE",
        "Code": "SG"
    },
    {
        "Country": "SINT MAARTEN (DUTCH PART)",
        "Code": "SX"
    },
    {
        "Country": "SLOVAKIA",
        "Code": "SK"
    },
    {
        "Country": "SLOVENIA",
        "Code": "SI"
    },
    {
        "Country": "SOLOMON ISLANDS",
        "Code": "SB"
    },
    {
        "Country": "SOMALIA",
        "Code": "SO"
    },
    {
        "Country": "SOUTH AFRICA",
        "Code": "ZA"
    },
    {
        "Country": "SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS",
        "Code": "GS"
    },
    {
        "Country": "SOUTH SUDAN",
        "Code": "SS"
    },
    {
        "Country": "SPAIN",
        "Code": "ES"
    },
    {
        "Country": "SRI LANKA",
        "Code": "LK"
    },
    {
        "Country": "SUDAN",
        "Code": "SD"
    },
    {
        "Country": "SURINAME",
        "Code": "SR"
    },
    {
        "Country": "SVALBARD AND JAN MAYEN",
        "Code": "SJ"
    },
    {
        "Country": "SWAZILAND",
        "Code": "SZ"
    },
    {
        "Country": "SWEDEN",
        "Code": "SE"
    },
    {
        "Country": "SWITZERLAND",
        "Code": "CH"
    },
    {
        "Country": "SYRIAN ARAB REPUBLIC",
        "Code": "SY"
    },
    {
        "Country": "TAIWAN, PROVINCE OF CHINA",
        "Code": "TW"
    },
    {
        "Country": "TAJIKISTAN",
        "Code": "TJ"
    },
    {
        "Country": "TANZANIA, UNITED REPUBLIC OF",
        "Code": "TZ"
    },
    {
        "Country": "THAILAND",
        "Code": "TH"
    },
    {
        "Country": "TIMOR-LESTE",
        "Code": "TL"
    },
    {
        "Country": "TOGO",
        "Code": "TG"
    },
    {
        "Country": "TOKELAU",
        "Code": "TK"
    },
    {
        "Country": "TONGA",
        "Code": "TO"
    },
    {
        "Country": "TRINIDAD AND TOBAGO",
        "Code": "TT"
    },
    {
        "Country": "TUNISIA",
        "Code": "TN"
    },
    {
        "Country": "TURKEY",
        "Code": "TR"
    },
    {
        "Country": "TURKMENISTAN",
        "Code": "TM"
    },
    {
        "Country": "TURKS AND CAICOS ISLANDS",
        "Code": "TC"
    },
    {
        "Country": "TUVALU",
        "Code": "TV"
    },
    {
        "Country": "UGANDA",
        "Code": "UG"
    },
    {
        "Country": "UKRAINE",
        "Code": "UA"
    },
    {
        "Country": "UNITED ARAB EMIRATES",
        "Code": "AE"
    },
    {
        "Country": "UNITED KINGDOM",
        "Code": "GB"
    },
    {
        "Country": "UNITED STATES",
        "Code": "US"
    },
    {
        "Country": "UNITED STATES MINOR OUTLYING ISLANDS",
        "Code": "UM"
    },
    {
        "Country": "URUGUAY",
        "Code": "UY"
    },
    {
        "Country": "UZBEKISTAN",
        "Code": "UZ"
    },
    {
        "Country": "VANUATU",
        "Code": "VU"
    },
    {
        "Country": "VENEZUELA, BOLIVARIAN REPUBLIC OF",
        "Code": "VE"
    },
    {
        "Country": "VIETNAM",
        "Code": "VN"
    },
    {
        "Country": "VIRGIN ISLANDS, BRITISH",
        "Code": "VG"
    },
    {
        "Country": "VIRGIN ISLANDS, U.S.",
        "Code": "VI"
    },
    {
        "Country": "WALLIS AND FUTUNA",
        "Code": "WF"
    },
    {
        "Country": "WESTERN SAHARA",
        "Code": "EH"
    },
    {
        "Country": "YEMEN",
        "Code": "YE"
    },
    {
        "Country": "ZAMBIA",
        "Code": "ZM"
    },
    {
        "Country": "ZIMBABWE",
        "Code": "ZW"
    }]


class AvailableFaxNumbers(ndb.Expando):
    strFaxNumberRef = ndb.StringProperty()
    strFaxNumber = ndb.StringProperty()
    strCountryCode = ndb.StringProperty(default="ZA")
    strCountryName = ndb.StringProperty(default="South Africa")
    strAssigned = ndb.BooleanProperty(default=False)
    strOrganizationID = ndb.StringProperty()

    def writeFaxNumberReference(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strFaxNumber = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateFaxNumberReference(self):
        import random, string
        try:
            strFaxReference = ""
            for i in range(13):
                strFaxReference += random.SystemRandom().choice(string.ascii_uppercase + string.digits)

            return strFaxReference
        except:
            return None

    def writeFaxNumber(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strFaxNumber = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCountryCode(self, strinput):
        try:
            strinput = str(strinput)
            strinput = strinput.strip()
            strinput = strinput.upper()

            if strinput in Country_Codes:
                self.strCountryCode = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCountryName(self, strinput):
        try:
            strinput = str(strinput)
            strinput = strinput.strip()
            if strinput in Country_Codes:
                self.strCountryName = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAssigned(self, strinput):
        try:
            if strinput in [True, False]:
                self.strAssigned = strinput
                return True
            else:
                return False
        except:
            return False

    def writeOrganizationID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strOrganizationID = strinput
                return True
            else:
                return False
        except:
            return False


class AvailableEmailEndPoints(ndb.Expando):
    strEmailReference = ndb.StringProperty()
    strEmailAddress = ndb.StringProperty()
    strAssigned = ndb.BooleanProperty(default=False)
    strOrganizationID = ndb.StringProperty()

    def writeOrganizationID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strOrganizationID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeEmailReference(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strEmailReference = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateEmailReference(self):
        import random,string
        try:
            strEmailReference = ""
            for i in range(32):
                strEmailReference += random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            return strEmailReference
        except:
            return None

    def writeEmailAddress(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strEmailAddress = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateEmailAddress(self):
        import random,string
        try:
            strEmailAddress = ""
            for i in range(8):
                strEmailAddress += random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            strEmailAddress += "@sa-sms.appspotmail.com"
            return strEmailAddress
        except:
            return None

    def writeAssigned(self, strinput):
        try:
            if strinput in [True, False]:
                self.strAssigned = strinput
                return True
            else:
                return False
        except:
            return False


class FaxSettings(ndb.Expando):
    strOrganizationID = ndb.StringProperty()
    strFaxNumber = ndb.StringProperty()
    strSMSNotifyOnSend = ndb.BooleanProperty(default=False)
    strSMSCreditNotify = ndb.BooleanProperty(default=False)
    strSMSNotifyOnReceive = ndb.BooleanProperty(default=False)
    strEmailToFax = ndb.StringProperty()
    strAPIKey = ndb.StringProperty()
    strSecretCode = ndb.StringProperty()

    def writeOrganizationID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strOrganizationID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeFaxNumber(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strFaxNumber = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSMSNotifyOnSend(self, strinput):
        try:
            if strinput in [True, False]:
                self.strSMSNotifyOnSend = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSMSCreditNotify(self, strinput):
        try:
            if strinput in [True, False]:
                self.strSMSCreditNotify = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSMSNotifyOnReceive(self, strinput):
        try:
            if strinput in [True, False]:
                self.strSMSNotifyOnReceive = strinput
                return True
            else:
                return False
        except:
            return False

    def writeEmailToFax(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strEmailToFax = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAPIKey(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strAPIKey = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSecretCode(self, strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSecretCode = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateAPIKey(self):
        import random, string
        try:
            strAPIKey = ""
            for i in range(24):
                strAPIKey += random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            return strAPIKey
        except:
            return None

    def CreateSecretCode(self):
        import random, string
        try:
            strSecretCode = ""
            for i in range(24):
                strSecretCode += random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            return strSecretCode
        except:
            return None


class FaxAccount(ndb.Expando):
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strTel = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strWebsite = ndb.StringProperty()

    strOrganizationID = ndb.StringProperty()
    strCreditInPages = ndb.IntegerProperty(default=0)
    strCostPerPage = ndb.IntegerProperty(default=60)
    strDateLastCredit = ndb.DateProperty()
    strTimeLastCredit = ndb.TimeProperty()
    strUsePortal = ndb.StringProperty(default="ClickSend")
    strDepositReference = ndb.StringProperty()
    strSuspended = ndb.BooleanProperty(default=False)

    strTotalTopUpCost = ndb.IntegerProperty(default=0)
    strTopUpCredit = ndb.IntegerProperty(default=0)
    strTopUpReference = ndb.StringProperty()
    strTopUpInvoiceLink = ndb.StringProperty()
    strPayByDate = ndb.DateProperty()
    strDateInvoiceCreated = ndb.DateProperty()
    strDepositSlipFileName = ndb.StringProperty()


    def writeTotalTopUpCost(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) > 0):
                self.strTotalTopUpCost = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeTopUpCredit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTopUpCredit = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeTopUpReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTopUpReference = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateTopUpInvoiceLink(self,strinput):
        """
            strinput should be TopUpReference
        :param strinput:
        :return:
        """
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTopUpInvoiceLink = "/fax/topup/invoice/" + strinput
                return True
            else:
                return False
        except:
            return False
    def writePayByDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strPayByDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateInvoiceCreated(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateInvoiceCreated = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDepositSlipFilename(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strDepositSlipFileName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNames(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strNames = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateTopUpReference(self):
        import random,string
        try:
            strTopUpReference = ""
            for i in range(12):
                strTopUpReference += random.SystemRandom().choice(string.digits + string.ascii_uppercase)

            return strTopUpReference
        except:
            return None

    def writeSurname(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strSurname = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCell(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTel(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strTel = strinput
                return True
            else:
                return False

        except:
            return False

    def writeEmail(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strEmail = strinput
                return True
            else:
                return False
        except:
            return False

    def writeWebsite(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strWebsite = strinput
                return True
            else:
                return False
        except:
            return False

    def writeOrganizationID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strOrganizationID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCreditInPages(self, strinput):
        try:
            strinput = str(strinput)
            if (strinput.isdigit() and (int(strinput) >= 0)):
                self.strCreditInPages = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeCostPerPage(self, strinput):
        try:
            strinput = str(strinput)
            if (strinput.isdigit() and (int(strinput) >= 0)):
                self.strCostPerPage = strinput
                return True
            else:
                return False

        except:
            return False

    def writeDateLastCredit(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.strDateLastCredit = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeLastCredit(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.strTimeLastCredit = strinput
                return True
            else:
                return False
        except:
            return False

    def writeUsePortal(self, strinput):
        try:

            strinput = str(strinput)
            if not (strinput == None):
                self.strUsePortal = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDepositReference(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strDepositReference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSuspended(self, strinput):
        try:
            if strinput in [True, False]:
                self.strSuspended = strinput
                return True
            else:
                return False
        except:
            return False


class SentFax(ndb.Expando):
    strUserID = ndb.StringProperty()
    strOrganizationID = ndb.StringProperty()
    strFaxReference = ndb.StringProperty()
    strFaxNumber = ndb.StringProperty()
    strSubject = ndb.StringProperty()
    strCoverPage = ndb.StringProperty()
    strFaxFilename = ndb.StringProperty()
    strDateCreated = ndb.DateProperty()
    strTimeCreated = ndb.TimeProperty()
    strFaxSent = ndb.BooleanProperty(default=False)
    strDateSent = ndb.DateProperty()
    strTimeSent = ndb.TimeProperty()
    strStatus = ndb.StringProperty(default="Received"),  # Engaged,
    strNumberPages = ndb.IntegerProperty(default=1)

    strResponseFilename = ndb.StringProperty()
    strDateResponse = ndb.DateProperty()
    strTimeResponse = ndb.TimeProperty()

    def writeSubject(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strSubject = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCoverPage(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strCoverPage = strinput
                return True
            else:
                return False
        except:
            return False

    def writeUserID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeOrganizationID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strOrganizationID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeFaxReference(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strFaxReference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeFaxNumber(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strFaxNumber = strinput
                return True
            else:
                return False
        except:
            return False

    def writeFaxFilename(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strFaxFilename = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateCreated(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.strDateCreated = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeCreated(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.strTimeCreated = strinput
                return True
            else:
                return False
        except:
            return False

    def writeFaxSent(self, strinput):
        try:
            if strinput in [True, False]:
                self.strFaxSent = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateSent(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.strDateSent = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeSent(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.strTimeSent = strinput
                return True
            else:
                return False
        except:
            return False

    def writeStatus(self, strinput):
        try:
            strinput = str(strinput)
            if strinput in ["Sent", "Received", "Engaged", "Not Sent", "Not Received"]:
                self.strStatus = strinput
                return True
            else:
                return False
        except:
            return False

    def writeNumberPages(self, strinput):
        try:
            strinput = str(strinput)
            if (strinput.isdigit() and (int(strinput) > 0)):
                self.strNumberPages = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def CreateFaxReference(self):
        import random, string
        try:
            strFaxReference = ""
            for i in range(12):
                strFaxReference += random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            return strFaxReference
        except:
            return None

    def writeResponseFilename(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strResponseFilename = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateResponse(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.strDateResponse = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeResponse(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.strTimeResponse = strinput
                return True
            else:
                return False
        except:
            return False


class ReceivedFax(ndb.Expando):
    strUserID = ndb.StringProperty()
    strOrganizationID = ndb.StringProperty()
    strFaxReference = ndb.StringProperty()
    strFaxNumber = ndb.StringProperty()
    strSubject = ndb.StringProperty()
    strCoverPage = ndb.StringProperty()
    strFaxFilename = ndb.StringProperty()
    strDateReceived = ndb.DateProperty()
    strTimeReceived = ndb.TimeProperty()
    strFaxReceived = ndb.BooleanProperty(default=False)
    strNumberPages = ndb.IntegerProperty(default=0)

    def writeUserID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeOrganizationID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strOrganizationID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeFaxReference(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strFaxReference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeFaxNumber(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strFaxNumber = strinput
                return True
            else:
                return False
        except:
            return False

    def writeFaxFilename(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strFaxFilename = strinput
                return True
            else:
                return False

        except:
            return False

    def writeDateReceived(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.strDateReceived = strinput
                return True
            else:
                return False

        except:
            return False

    def writeTimeReceived(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.strTimeReceived = strinput
                return True
            else:
                return False
        except:
            return False

    def writeFaxReceived(self, strinput):
        try:
            if strinput in [True, False]:
                self.strFaxReceived = strinput
                return True
            else:
                return False
        except:
            return False

    def writeNumberPages(self, strinput):
        try:
            strinput = str(strinput)
            if (strinput.isdigit() and (int(strinput) > 0)):
                self.strNumberPages = int(strinput)
                return True
            else:
                return False
        except:
            return False


from firebaseadmin import VerifyAndReturnAccount

class MyFaxHandler(webapp2.RequestHandler):
    def get(self):
        try:
            template = template_env.get_template('templates/fax/fax.html')
            context = {}
            self.response.write(template.render(context))
        except:
            template = template_env.get_template('templates/fax/fax.html')
            context = {}
            self.response.write(template.render(context))



    def post(self):

        from accounts import Accounts
        from mysms import ClickSendSMSPortal
        from myTwilio import MyTwilioPortal

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            #'&vstrUserID=' + struid + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrAccessToken = self.request.get('vstrAccessToken')
            vstrEmail = self.request.get('vstrEmail')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = FaxAccount.query(FaxAccount.strOrganizationID == thisMainAccount.organization_id)
                thisFaxAccountList = findRequest.fetch()

                if len(thisFaxAccountList) > 0:
                    thisFaxAccount = thisFaxAccountList[0]
                else:
                    thisFaxAccount = FaxAccount()

                template = template_env.get_template('templates/fax/account.html')
                context = {'thisFaxAccount': thisFaxAccount}
                self.response.write(template.render(context))

        elif vstrChoice == "1":
            #'&vstrUserID=' + struid + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrAccessToken = self.request.get('vstrAccessToken')
            vstrEmail = self.request.get("vstrEmail")

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrNames = self.request.get("vstrNames")
                vstrSurname = self.request.get("vstrSurname")
                vstrCell = self.request.get("vstrCell")
                vstrTel = self.request.get("vstrTel")

                vstrWebsite = self.request.get("vstrWebsite")

                findRequest = FaxAccount.query(FaxAccount.strOrganizationID == thisMainAccount.organization_id)
                thisFaxAccountList = findRequest.fetch()

                if len(thisFaxAccountList) > 0:
                    thisFaxAccount = thisFaxAccountList[0]
                else:
                    thisFaxAccount = FaxAccount()

                thisFaxAccount.writeOrganizationID(strinput=thisMainAccount.organization_id)
                thisFaxAccount.writeNames(strinput=vstrNames)
                thisFaxAccount.writeSurname(strinput=vstrSurname)
                thisFaxAccount.writeCell(strinput=vstrCell)
                thisFaxAccount.writeTel(strinput=vstrTel)
                thisFaxAccount.writeEmail(strinput=vstrEmail)
                thisFaxAccount.writeWebsite(strinput=vstrWebsite)
                thisFaxAccount.put()
                self.response.write("Successfully updated account")

        elif vstrChoice == "2":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')


            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = SentFax.query(SentFax.strOrganizationID == thisMainAccount.organization_id)
                thisSentFaxesList = findRequest.fetch()

                findRequest = ReceivedFax.query(ReceivedFax.strOrganizationID == thisMainAccount.organization_id)
                thisReceivedFaxesList = findRequest.fetch()

                template = template_env.get_template('templates/fax/sub/myfaxes.html')
                context = {'thisSentFaxesList': thisSentFaxesList, 'thisReceivedFaxesList': thisReceivedFaxesList}
                self.response.write(template.render(context))

        elif vstrChoice == "3":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')


            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)

            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrToFaxNumber = self.request.get("vstrToFaxNumber")
                vstrSubject = self.request.get("vstrSubject")
                vstrCoverPage = self.request.get("vstrCoverPage")
                vstrFilename = self.request.get("vstrFilename")
                # TODO- find a way to count the pages in a pdf file with python
                # TODO- once that is done check if credit on the user account is enough to send the fax if yes send

                findRequest = FaxAccount.query(FaxAccount.strOrganizationID == thisMainAccount.organization_id)
                thisFaxAccountList = findRequest.fetch()

                if len(thisFaxAccountList) > 0:
                    thisFaxAccount = thisFaxAccountList[0]
                else:
                    thisFaxAccount = FaxAccount()

                if thisFaxAccount.strCreditInPages > 0:
                    findRequest = ClickSendSMSPortal.query()
                    thisClickSendPortalList = findRequest.fetch()
                    if len(thisClickSendPortalList) > 0:
                        thisClickSend = thisClickSendPortalList[0]
                    else:
                        thisClickSend = ClickSendSMSPortal()

                    if thisClickSend.sendFax(strFaxNumber=vstrToFaxNumber, strFaxFileName=vstrFilename,
                                             strSubject=vstrSubject, strCoverPage=vstrCoverPage):
                        self.response.write("Fax Successfully sent once delivered your credits will be subtracted...")
                    else:
                        self.response.write("Error sending fax we will keep retrying until we succeed")
                else:
                    self.response.write("You do not have sufficient credit to send a fax please recharge your account")

        elif vstrChoice == "4":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = FaxSettings.query(FaxSettings.strOrganizationID == thisMainAccount.organization_id)
                thisFaxSettingsList = findRequest.fetch()

                if len(thisFaxSettingsList) > 0:
                    thisFaxSettings = thisFaxSettingsList[0]
                else:
                    thisFaxSettings = FaxSettings()

                template = template_env.get_template('templates/fax/sub/settings.html')
                context = {'thisFaxSettings': thisFaxSettings}
                self.response.write(template.render(context))

        elif vstrChoice == "5":

            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')



            vstrTotalCredits = self.request.get("vstrTotalCredits")
            vstrAddCredits = self.request.get("vstrAddCredits")
            vstrPaymentMethod = self.request.get("vstrPaymentMethod")

            findRequest = MyTwilioPortal.query()
            thisTwilioPortalList = findRequest.fetch()

            if len(thisTwilioPortalList) > 0:
                thisTwilioPortal =  thisTwilioPortalList[0]
            else:
                thisTwilioPortal = MyTwilioPortal()

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                findRequest = FaxAccount.query(FaxAccount.strOrganizationID == thisMainAccount.organization_id)
                thisFaxAccountList = findRequest.fetch()

                if len(thisFaxAccountList) > 0:
                    thisFaxAccount = thisFaxAccountList[0]
                    if vstrPaymentMethod == "DirectDeposit":
                        vstrThisDate = datetime.datetime.now()
                        strThisDate = datetime.date(year=vstrThisDate.year,month=vstrThisDate.month,day=vstrThisDate.day)
                        vstrThisDate += datetime.timedelta(days=30)
                        strPayByDate = datetime.date(year=vstrThisDate.year, month=vstrThisDate.month, day=vstrThisDate.day)
                        strTotalCost = (thisTwilioPortal.strCostPerPage * int(vstrAddCredits))/100
                        thisFaxAccount.writeTotalTopUpCost(strinput=strTotalCost)
                        thisFaxAccount.writeTopUpCredit(strinput=vstrAddCredits)
                        thisFaxAccount.writeTopUpReference(strinput=thisFaxAccount.CreateTopUpReference())
                        thisFaxAccount.CreateTopUpInvoiceLink(strinput=thisFaxAccount.top_up_reference)
                        thisFaxAccount.writePayByDate(strinput=strPayByDate)
                        thisFaxAccount.writeDateInvoiceCreated(strinput=strThisDate)
                        thisFaxAccount.put()
                        self.response.write("""
                        Top up Credit Successfully processed please click on this link to view your 
                        <strong><a href=" """ + thisFaxAccount.top_up_invoice_link + """ ">Proforma Invoice</a></strong>""")

        elif vstrChoice == "6":

            # '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                findRequest = FaxAccount.query(FaxAccount.strOrganizationID == thisMainAccount.organization_id)
                thisFaxAccountList = findRequest.fetch()
                if len(thisFaxAccountList) > 0:
                    thisFaxAccount = thisFaxAccountList[0]
                else:
                    thisFaxAccount = FaxAccount()

                findRequest = FaxSettings.query(FaxSettings.strOrganizationID == thisMainAccount.organization_id)
                thisFaxSettingsList = findRequest.fetch()
                if len(thisFaxSettingsList) > 0:
                    thisFaxSettings = thisFaxSettingsList[0]
                else:
                    thisFaxSettings = FaxSettings()

                template = template_env.get_template('templates/fax/sub/submenu.html')
                context = {'thisFaxAccount': thisFaxAccount, 'thisFaxSettings': thisFaxSettings}
                self.response.write(template.render(context))



class SettingsHandler(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):

        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            #+ '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):


                findRequest = AvailableFaxNumbers.query(AvailableFaxNumbers.strAssigned == False)
                thisAvailableFaxNumbersList = findRequest.fetch()
                if len(thisAvailableFaxNumbersList) > 0:
                    thisAvailFax = thisAvailableFaxNumbersList[0]

                    thisAvailFax.writeAssigned(strinput=True)
                    thisAvailFax.writeOrganizationID(strinput=thisMainAccount.organization_id)
                    self.response.write(thisAvailFax.strFaxNumber)
                    thisAvailFax.put()
                else:
                    self.response.write("No Fax Numbers Available")

        elif vstrChoice == "1":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):



                findRequest = AvailableEmailEndPoints.query(AvailableEmailEndPoints.strAssigned == False)
                thisAvailableEmailsList = findRequest.fetch()
                if len(thisAvailableEmailsList) > 0:
                    thisEmailEndPoint = thisAvailableEmailsList[0]
                    thisEmailEndPoint.writeAssigned(strinput=True)
                    thisEmailEndPoint.writeOrganizationID(strinput=thisMainAccount.organization_id)
                    self.response.write(thisEmailEndPoint.strEmailAddress)
                    thisEmailEndPoint.put()
                else:
                    self.response.write("No Available Email Address at this time")

        elif vstrChoice == "2":
            #+ '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                thisFaxSettings = FaxSettings()
                strAPIKey = thisFaxSettings.CreateAPIKey()
                self.response.write(strAPIKey)

        elif vstrChoice == "3":
            #+ '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                thisFaxSettings = FaxSettings()
                strSecretCode = thisFaxSettings.CreateSecretCode()
                self.response.write(strSecretCode)

        elif vstrChoice == "4":
            #+ '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')
            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):

                vstrFaxNumber = self.request.get('vstrFaxNumber')
                vstrSMSNotifyOnSend = self.request.get('vstrSMSNotifyOnSend')
                vstrSMSCreditNotify = self.request.get('vstrSMSCreditNotify')
                vstrSMSNotifyOnReceive = self.request.get('vstrSMSNotifyOnReceive')
                vstrEmailToFax = self.request.get('vstrEmailToFax')
                vstrAPIKey = self.request.get('vstrAPIKey')
                vstrSecretCode = self.request.get('vstrSecretCode')

                findRequest = FaxSettings.query(FaxSettings.strOrganizationID == thisMainAccount.organization_id)
                thisFaxSettingsList = findRequest.fetch()

                if len(thisFaxSettingsList) > 0:
                    thisFaxSetting = thisFaxSettingsList[0]
                else:
                    thisFaxSetting = FaxSettings()
                thisFaxSetting.writeOrganizationID(strinput=thisMainAccount.organization_id)
                thisFaxSetting.writeFaxNumber(strinput=vstrFaxNumber)
                if vstrSMSNotifyOnSend == "YES":
                    thisFaxSetting.writeSMSNotifyOnSend(strinput=True)
                else:
                    thisFaxSetting.writeSMSNotifyOnSend(strinput=False)

                if vstrSMSCreditNotify == "YES":
                    thisFaxSetting.writeSMSCreditNotify(strinput=True)
                else:
                    thisFaxSetting.writeSMSCreditNotify(strinput=False)

                if vstrSMSNotifyOnReceive == "YES":
                    thisFaxSetting.writeSMSNotifyOnReceive(strinput=True)
                else:
                    thisFaxSetting.writeSMSNotifyOnReceive(strinput=False)

                thisFaxSetting.writeEmailToFax(strinput=vstrEmailToFax)
                thisFaxSetting.writeAPIKey(strinput=vstrAPIKey)
                thisFaxSetting.writeSecretCode(strinput=vstrSecretCode)
                thisFaxSetting.put()
                self.response.write("Fax Settings successfully saved")


class ThisTopUpInvoiceHandler(webapp2.RequestHandler):
    def get(self):

        from accounts import Organization
        from dashboard import AccountDetails

        URL = self.request.url
        strURLlist = URL.split("/")
        strTopUpReference = strURLlist[len(strURLlist) - 1]

        findRequest = FaxAccount.query(FaxAccount.strTopUpReference == strTopUpReference)
        thisFaxAccountList = findRequest.fetch()

        if len(thisFaxAccountList) > 0:
            thisFaxAccount = thisFaxAccountList[0]

            findRequest = Organization.query(Organization.strOrganizationID == thisFaxAccount.organization_id)
            thisOrgList = findRequest.fetch()

            if len(thisOrgList) > 0:
                thisOrg = thisOrgList[0]
            else:
                thisOrg = Organization()


            findRequest = AccountDetails.query()
            thisBlueITAccountList = findRequest.fetch()

            if len(thisBlueITAccountList) > 0:
                thisBlueITAccount = thisBlueITAccountList[0]
            else:
                thisBlueITAccount = AccountDetails()

            template = template_env.get_template('templates/fax/invoice/proforma.html')
            context = {'thisFaxAccount':thisFaxAccount,'thisOrg':thisOrg,'thisBlueITAccount':thisBlueITAccount}
            self.response.write(template.render(context))

    def post(self):
        from dashboard import TopUpVerifications
        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            #'&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
            vstrTopUpReference = self.request.get("vstrTopUpReference")
            vstrYourReferenceNumber = self.request.get("vstrYourReferenceNumber")
            vstrDepositSlipFile = self.request.get("vstrDepositSlipFile")

            vstrUserID = self.request.get('vstrUserID')
            vstrEmail = self.request.get('vstrEmail')
            vstrAccessToken = self.request.get('vstrAccessToken')

            thisMainAccount = VerifyAndReturnAccount(strUserID=vstrUserID, strAccessToken=vstrAccessToken)
            if (thisMainAccount != None) and (thisMainAccount.email == vstrEmail):
                findRequest = FaxAccount.query(FaxAccount.strOrganizationID == thisMainAccount.organization_id)
                thisFaxAccountList = findRequest.fetch()

                if len(thisFaxAccountList) > 0:
                    thisFaxAccount = thisFaxAccountList[0]
                    if vstrYourReferenceNumber == vstrTopUpReference:
                        thisFaxAccount.writeDepositSlipFilename(strinput=vstrDepositSlipFile)
                        thisFaxAccount.put()

                        thisVerifications = TopUpVerifications()
                        thisVerifications.writeOrganizationID(strinput=thisFaxAccount.organization_id)
                        strFax = "FAX"
                        thisVerifications.writeAccountName(strinput=strFax)
                        thisVerifications.writeCreditAmount(strinput=thisFaxAccount.total_top_up_cost)
                        thisVerifications.writeDepositSlipFileName(strinput=vstrDepositSlipFile)
                        thisVerifications.writeSMSCredits(strinput=thisFaxAccount.top_up_credit)
                        thisVerifications.writeTopUpReference(strinput=vstrYourReferenceNumber)
                        thisVerifications.writeVerified(strinput=False)
                        thisVerifications.put()

                        self.response.write("Successfully Uploaded Deposit slip file : " + vstrDepositSlipFile)
                    else:
                        thisFaxAccount.writeDepositSlipFilename(strinput=vstrDepositSlipFile)
                        thisFaxAccount.put()

                        thisVerifications = TopUpVerifications()
                        thisVerifications.writeOrganizationID(strinput=thisFaxAccount.organization_id)
                        strFax = "FAX"
                        thisVerifications.writeAccountName(strinput=strFax)
                        thisVerifications.writeCreditAmount(strinput=thisFaxAccount.total_top_up_cost)
                        thisVerifications.writeDepositSlipFileName(strinput=vstrDepositSlipFile)
                        thisVerifications.writeSMSCredits(strinput=thisFaxAccount.top_up_credit)
                        thisVerifications.writeTopUpReference(strinput=vstrTopUpReference)
                        thisVerifications.writeVerified(strinput=False)
                        thisVerifications.put()

                        self.response.write("Reference Verification Error, deposit will take longer to verify please use our support tickets to enquire if it takes more than three days")

app = webapp2.WSGIApplication([
    ('/fax', MyFaxHandler),
    ('/fax/settings', SettingsHandler),
    ('/fax/topup/invoice/.*', ThisTopUpInvoiceHandler)


], debug=True)

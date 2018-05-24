
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
import logging
def VerifyAndReturnAccount(strUserID, strAccessToken):
    """
        Myoptions = {"type": "service_account",
                         "project_id": "sa-sms-b",
                         "private_key_id": "b5a2df76c2222b83893b111c41e49bdf3fb2298a",
                         "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDogYEyuGH8Dxd2\nOt11WSlWxPL7bxKZd6F26NOmVQ+vWDqlthmGPWM1zAFW4l/+600VUMKqqcjAC39W\nm2kCQp+S95WyovzyZ7u4PVEBoYrQJq1oSI1zjxCtRC/u0kqI5iYLyN7ofpJRqjnu\nUCQyu/8AstoW1M88/xwwgRUbJqZxPpbrkBHQGakm+M8Q5ZvJwQPLpPeQLRD7Xjyt\nmgbHLqDaJy1iwEo1V8ypAyS0il0rfNx7TtxTgrBUEpjt9/rPrVSdkSwExyZeFTYS\nPZo2ls24irlHQC+MKVanbSyNFeT20Z9KM/Fl2v6XpwQZFqd4tf2k3U3U7CjJ2K4A\nhi8ABWLtAgMBAAECggEADIHANr+UWxVfaGIM552+4NwB9g8o1k3ecaG0ljidJLbU\n8MpgNR24PdHrgIZM2PmZ++Y259dE5TpjxH+M9oIpnfjozzh/7XTcXtzC2W5HI/Xw\nqLC+ayjsTLsOQ6/W3TuuxZODP3O6Nd+3ngom6FO/M9prFi9RtoZCje64+UJAUcxh\n2A9ZcpQNzjUScqhmJiy+HvKYnmRx7gRuxTLi7drKgFQJUY4qptMindVuTudBVTxZ\n8/gOuUv3cCg+WBgZrWIt9BFE6g0KbZYIJWC892cI22qwPlday+h99134J75fTG03\nAXKFfdvOYO4wv7xAhgwMIn/ewGQhHANw1G0Ah0qmQQKBgQD9u5C93GxnokSCoHSr\nEWm2VDRNQXJuMhrp8QCU2xFZbswOzzjE4IUZS01ac90upRhzuuaIv/mwCLJh9hfH\nRbaPj7Z/0Oy/Vf251oqsGKcZwjaQlLWGA+wFg/7x0D2N9xjNiao4uMx42zohCLG3\nT3U3a05J7rzs99IbYw0NSsu/qwKBgQDqlWGXM1/FCI/YdwMVncuQx/HbzyLLReVx\ny5VegQADOR06DiUJbDilvY+6cjuwIqOYwKYY/zNbM8YubF63mDUTOINEXGB3sCSf\nz2L6TnHQcZ4PQUm1TSHgcliTZmRqWpn5WmAqH/z672jkYGTrWMBsF2E5U5Q1OeB1\nxYWNc1kvxwKBgFl0BA57pJhQw/iNmzQoWm2WeC34ceBZt9VcSwkvxokSH8zkz63R\nPftx6d6G1Ka6O8mpTddOXzfpiQIyYaW2dStdzkh3ns/CAEbBVXhg5KCXMOd+FhUe\nUtqK85nLAbiIMe1cqG+A7014dKDq0MTAtaGJKju0eFTO9fsDy7kw8m4rAoGBAJNl\nd2OFEUkBnzi5VwPPGWiIaaze0xL8gTXmYJ132uUrjvS6jIUGLfXeTSAuxNhge4Dw\nk60jNUa6Gm1zBHTBu5+vI7Phg2/RCsIrkhqLDbKWoWUedczogT/BOWysqq207gii\nw8fUP6YAplzRQLgsFQQWEK3vmTF0g1gc21TMxJ5jAoGBALXq/qhnQOUHUnuPs5M3\n+waHg7mJgzQt1jbClB1AVc722Lp9KSFCIhzbr3AQmHDo/eSAm9OwTTd1I4NW4vY9\nieSp/Md16NCqMXqBP6uINKuEMURAW2gGbLHDxu55EopOly+2NdgYHZbcnaeadAix\nLZoX/XlMSSgtyei0GxS9dZai\n-----END PRIVATE KEY-----\n",
                         "client_email": "firebase-adminsdk-ov6wg@sa-sms-b.iam.gserviceaccount.com",
                         "client_id": "114948598379533240849",
                         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                         "token_uri": "https://accounts.google.com/o/oauth2/token",
                         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                         "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ov6wg%40sa-sms-b.iam.gserviceaccount.com"}
            try:

                import firebase_admin

                cred = firebase_admin.credentials.Certificate(Myoptions)

                default_app = firebase_admin.initialize_app(cred)

                from firebase_admin.auth import verify_id_token
            except:
                logging.error("Credentials error")


            findRequest = Accounts.query(Accounts.strUserID == strUserID)
            thisAccountList = findRequest.fetch()
            if len(thisAccountList) > 0:
                thisAccount = thisAccountList[0]

                try:
                    decode_token = verify_id_token(id_token=strAccessToken,app=default_app)
                    uid = decode_token['uid']
                except:
                    uid = None

                if (uid != None) and (uid == strUserID):
                    return thisAccount
                else:
                    return None  # Once firebase credentials is working properly then we should return none here
            else:
                return None

    """

    from accounts import Accounts


    findRequest = Accounts.query(Accounts.strUserID == strUserID)
    thisAccountList = findRequest.fetch()
    if len(thisAccountList) > 0:
        thisAccount = thisAccountList[0]
        return thisAccount
    else:
        return None



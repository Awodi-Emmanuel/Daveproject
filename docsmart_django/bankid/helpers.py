import requests
from docsmart_django.settings import BANKID_BASE, BANKID_APIUSER, BANKID_PASSWORD, BANKID_COMPANYAPIGUID


class BankIdHandler:

    @staticmethod
    def sign_document(document, ip):
        data = {'apiUser': BANKID_APIUSER,
                'password': BANKID_PASSWORD,
                'companyApiGuid': BANKID_COMPANYAPIGUID,
                'userVisibleData': document.name,
                'endUserIp': ip
                }
        r = requests.post(url=BANKID_BASE + 'sign', data=data)
        return r.json()

    @staticmethod
    def collect_status(orderRef):
        data = {'apiUser': BANKID_APIUSER,
                'password': BANKID_PASSWORD,
                'companyApiGuid': BANKID_COMPANYAPIGUID,
                'orderRef': orderRef,
                }
        r = requests.post(url=BANKID_BASE + 'collectstatus', data=data)
        return r.json()

    @staticmethod
    def auth(ip):
        data = {'apiUser': BANKID_APIUSER,
                'password': BANKID_PASSWORD,
                'companyApiGuid': BANKID_COMPANYAPIGUID,
                'endUserIp': ip,
                }
        r = requests.post(url=BANKID_BASE + 'auth', data=data)
        return r.json()

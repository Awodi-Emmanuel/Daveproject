import requests

from bankid.models import SignedDocuments
from docsmart_django.settings import BANKID_BASE, BANKID_APIUSER, BANKID_PASSWORD, BANKID_COMPANYAPIGUID


class BankIdHandler:

    @staticmethod
    def sign_document(offer, ip, customer):
        data = {'apiUser': BANKID_APIUSER,
                'password': BANKID_PASSWORD,
                'companyApiGuid': BANKID_COMPANYAPIGUID,
                'userVisibleData': offer.document.name,
                'endUserIp': ip
                }
        r = requests.post(url=BANKID_BASE + 'sign', data=data)
        data = r.json()
        if r.status_code == 200 and data['authResponse']['Success']:
            SignedDocuments.objects.create(
                company=offer.related_company,
                document=offer.document,
                customer=customer,
                status=data['authResponse']['Success'],
                ip_address=ip,
                data=data

            )
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

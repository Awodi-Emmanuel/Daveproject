from datetime import datetime

import chargebee
# from datetime import datetime, timedelta, date
from company.models import Company
from docsmart_django.settings import CHARGEBEE_API_KEY, CHARGEBEE_SITE
from django.urls import reverse
# from company.models import Company
# from plugins_base.models import Plugin, AppTypes, STATUS
# from plugins_base.models import Plugin, STATUS


class ChargebeeHandler:
    def __init__(self, api_key=CHARGEBEE_API_KEY, site=CHARGEBEE_SITE):
        chargebee.configure(api_key=api_key, site=site)

    @staticmethod
    def create_plan(plan):
        result = chargebee.Plan.create({
            "id": plan['plan_id'],
            "name": plan['name'],
            "description": plan['description'],
            "price": int(plan['price'] * 100),
            "period": plan['period'],
            "period_unit": plan['period_unit'],
            "currency_code": 'USD'
        })
        plan = result.plan
        print(plan)
        if plan:
            return True
        else:
            return False

    @staticmethod
    def update_plan(plan):
        result = chargebee.Plan.update(plan.plan_id, {
            "name": plan.name,
            "price": int(plan.price * 100),
        })
        plan = result.plan
        print(plan)
        if plan:
            return True
        else:
            return False

    @staticmethod
    def get_checkout_page(plan_id, user):
        result = chargebee.HostedPage.checkout_new({
            "subscription": {
                "plan_id": plan_id
            },
            "customer": {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email
            },
            "redirect_url": "http://127.0.0.1:8000/api/billing/hosted-page"
            # reverse('billing', kwargs={'target': 'subscription', 'action': 'confirm'})
        })
        return result

    @staticmethod
    def get_hosted_page(hosted_page_id):
        result = chargebee.HostedPage.retrieve(hosted_page_id)
        return result

    @staticmethod
    def update_customer(user):
        if user.chargebee_id:
            result = chargebee.Customer.update(user.chargebee_id, {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email
            })
            customer = result.customer

    @staticmethod
    def cancel_subscription(subscription):
        if subscription.status:
            result = chargebee.Subscription.cancel(subscription.subscription_id, {
                "end_of_term": True
            })
            subscription = result.subscription


# def start_trial(user):
#
#     company = Company.objects.get(user__id=user.id)
#     Plugin.objects.add_plugin(app=AppTypes.GENERAL.value,
#                               status=STATUS.TRIAL.value, company=company, last_payment_date=str(datetime.today()),
#                               next_expiry_date=str(date.today() + timedelta(days=15)))
#
#
# def end_trial(user):
#     company = Company.objects.get(user__id=user.id)
#     plugin = Plugin.objects.get(company=company, status=STATUS.TRIAL.value)
#     plugin.status = STATUS.EXPIRED
#     plugin.last_expiry_date = str(datetime.today())
#     plugin.save()

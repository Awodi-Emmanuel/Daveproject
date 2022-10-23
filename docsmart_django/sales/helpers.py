from datetime import date, timedelta, datetime

from sales.models import SentOffers
from user_auth.classes.email.send import SendMail


class Send:

    """
        related_company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, db_column='related_company', null=True, blank=True)
    related_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='related_user', null=True, blank=True)
    offer = models.ForeignKey(Sales, on_delete=models.DO_NOTHING, db_column='offer', null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, db_column='customer', null=True, blank=True)
    offer_status = (
        ('sent', 'Sent'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('signed', 'Signed'),
        ('lost', 'Lost'),
        ('expired', 'Expired'),
        ('won', 'Won'),
    )
    status = models.CharField(max_length=10, choices=offer_status)
    expires_at = models.DateTimeField()
    signed_at = models.DateTimeField()
    declined_at = models.DateTimeField()
    accepted_at = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True, null=True)
    """

    @staticmethod
    def offer(offer):
        customers = offer.customer.filter()
        for customer in customers:
            SendMail.send_reminder(customer, "New Offer From DocSmart", 'welcome.html', 'Sign Document')
            SentOffers.objects.create(
                related_company=offer.related_company,
                related_user=offer.owner,
                customer=customer,
                status='sent',
                expires_at=str(date.today() + timedelta(days=15)),
                created_at=str(datetime.today())
            )


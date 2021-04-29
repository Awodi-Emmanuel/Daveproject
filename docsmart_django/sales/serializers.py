from rest_framework import serializers

from payment_schedule.models import PaymentSchedule
from sales.models import Sales

"""
title = models.CharField(verbose_name="title", max_length=500)
    # template = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    status = models.CharField(
        max_length=5,
        choices=[(tag, tag.value) for tag in Status], default=Status.IN_PROGRESS
    )
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=3)
    discount = models.DecimalField(default=0.00, max_digits=9, decimal_places=3)
    vat = models.ForeignKey(VAT, on_delete=models.CASCADE, blank=True)
    signature_type = models.CharField(
        max_length=5,
        choices=[(tag, tag.value) for tag in SignatureType]
    )
    currency = models.CharField(
        max_length=5,
        choices=[(tag, tag.value) for tag in Currency]
    )
    customer = models.ManyToManyField(Customer, verbose_name="Customer", blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True)
    payment_schedule = models.ForeignKey(PaymentSchedule, on_delete=models.CASCADE, blank=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True)
"""


class CreateSalesOfferSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=255, min_length=8)
    status = serializers.CharField(max_length=255, min_length=4, required=False)
    total = serializers.DecimalField(max_digits=9, decimal_places=3, required=False)
    discount = serializers.DecimalField(max_digits=9, decimal_places=3, required=False)
    signature_type = serializers.CharField(
        max_length=255, min_length=3, required=False)
    currency = serializers.CharField(max_length=255, min_length=4, required=False)
    customer = serializers.CharField(required=False)
    owner = serializers.IntegerField(required=False, write_only=True)
    company = serializers.IntegerField(required=False)
    payment_schedule = serializers.IntegerField(required=False, write_only=True)
    document = serializers.IntegerField(required=False)

    class Meta:
        model = Sales
        fields = '__all__'

    def create(self, validated_data):

        return Sales.objects.create_sales_offer(**validated_data)


class CreatePaymentSchedule(serializers.ModelSerializer):
    """
    item = models.CharField(verbose_name="item", max_length=500)
    price = models.DecimalField(verbose_name="price", max_digits=9, decimal_places=3)
    start = models.DateTimeField(verbose_name="start")
    finish = models.DateTimeField(verbose_name="finish")
    """

    item = serializers.CharField(
        max_length=255, min_length=8, required=True)
    price = serializers.CharField(max_length=255, min_length=4, required=False)
    start = serializers.DateTimeField(required=False)
    finish = serializers.DateTimeField(required=False)

    class Meta:
        model = PaymentSchedule
        fields = ['item', 'price', 'start', 'finish']

    def create(self, validated_data):

        return PaymentSchedule.objects.create_schedule(**validated_data)


class RetrieveSalesOfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        depth = 1
        fields = '__all__'

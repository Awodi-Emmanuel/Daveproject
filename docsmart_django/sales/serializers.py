from rest_framework import serializers

from payment_schedule.models import PaymentSchedule
from sales.models import Sales


class OfferSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=255, min_length=8)
    status = serializers.CharField(max_length=255, min_length=4, required=False)
    total = serializers.DecimalField(max_digits=9, decimal_places=3, required=False)
    discount = serializers.DecimalField(max_digits=9, decimal_places=3, required=False)
    signature_type = serializers.CharField(
        max_length=255, min_length=3, required=False)
    currency = serializers.CharField(max_length=255, min_length=4, required=False)
    owner = serializers.IntegerField(required=False, write_only=True)
    related_company = serializers.IntegerField(required=False, write_only=True)
    payment_schedule = serializers.IntegerField(required=False, write_only=True)
    document = serializers.IntegerField(required=False)

    class Meta:
        model = Sales
        depth = 1
        fields = '__all__'

    def get_fields(self, *args, **kwargs):
        fields = super(OfferSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) == "PUT":
            fields['title'].required = False
        return fields

    def create(self, validated_data):
        return Sales.objects.create_sales_offer(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.status = validated_data.get('status', instance.status)
        instance.total = validated_data.get('total', instance.total)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.signature_type = validated_data.get('signature_type', instance.signature_type)
        instance.currency = validated_data.get('currency', instance.currency)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.related_company = validated_data.get('related_company', instance.related_company)
        instance.payment_schedule = validated_data.get('payment_schedule', instance.payment_schedule)
        instance.document = validated_data.get('document', instance.document)
        instance.save()
        return instance


class CreatePaymentSchedule(serializers.ModelSerializer):

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
        fields = '__all__'

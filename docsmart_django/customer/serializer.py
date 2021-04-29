from rest_framework import serializers

from customer.models import Customer

"""

    first_name = models.CharField(verbose_name="First Name", max_length=500, null=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=254, null=True)
    email = models.EmailField(verbose_name='Email', null=True)
    company_email = models.EmailField(verbose_name='Company Email', null=True)
    refernce = models.CharField(verbose_name="Reference", max_length=500,null=True)
    company_name = models.CharField(verbose_name="Comapny Name", max_length=500, null=True)
    company_number = models.CharField(verbose_name="Company Number", max_length=500, null=True)
    company_address = models.CharField(verbose_name="Company Address", max_length=1000,null=True)
    company_zipcode = models.CharField(verbose_name="Company Zipcode", max_length=1000,null=True)
    company_city = models.CharField(verbose_name="Company City", max_length=1000,null=True)
    company_country = models.CharField(verbose_name="Company Country", max_length=500,null=True)

"""


class CreateCustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        max_length=255)
    last_name = serializers.CharField(max_length=255,  required=False)
    email = serializers.EmailField()
    related_company = serializers.IntegerField(required=True, write_only=True)
    company_email = serializers.EmailField()
    refernce = serializers.CharField(
        max_length=255, min_length=3, required=False),
    company_name = serializers.CharField(max_length=255, min_length=4, required=True)
    company_number = serializers.CharField(required=True)
    company_address = serializers.CharField(max_length=1000, min_length=4, required=True)
    company_zipcode = serializers.CharField(max_length=255, min_length=4, required=True)
    company_city = serializers.CharField(max_length=255, min_length=4, required=True)
    company_country = serializers.CharField(max_length=255, min_length=4, required=True)

    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):

        return Customer.objects.create_customer(**validated_data)
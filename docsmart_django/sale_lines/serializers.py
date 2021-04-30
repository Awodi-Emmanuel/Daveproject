from rest_framework import serializers

from customer.models import Customer
from sale_lines.models import Lines

"""

    title = models.CharField(verbose_name="Title", max_length=500,null=True)
    item_number = models.CharField(verbose_name="Item Number", max_length=500, null=True)
    item_description = models.CharField(verbose_name="Item Description", max_length=500, null=True)
    item_type = models.CharField(verbose_name="Item Type", max_length=1000,null=True)

    item_manufacturer_id = models.CharField(verbose_name="Item Manufacturer ID", max_length=500,null=True)
    item_quantity = models.CharField(verbose_name="Item Quantity", max_length=500, null=True)

    related_user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    related_company= models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

"""


class CreateLinesSerializer(serializers.ModelSerializer):

    title = serializers.CharField(
        max_length=1000)
    item_number = serializers.CharField(max_length=255)
    item_description = serializers.CharField(
        max_length=1000, required=False)
    item_type = serializers.CharField(max_length=255, required = True)
    item_manufacturer_id = serializers.CharField(max_length=255, required = True)
    item_quantity = serializers.IntegerField(required=True),
    related_user = serializers.IntegerField(required=False, write_only=True)
    related_company = serializers.IntegerField(required=False, write_only=True)


    class Meta:
        model = Lines
        fields = '__all__'

    def create(self, validated_data):

        return Lines.objects.create_sales_lines(**validated_data)


class FetchLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lines
        fields = '__all__'
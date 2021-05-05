from rest_framework import serializers
from plugins_base.models import Plugin


class AddPluginSerializer(serializers.ModelSerializer):

    """
    app = models.CharField(
        max_length=5,
        choices=[(tag, tag.value) for tag in APP_TYPES]
    )
    status = models.CharField(
        max_length=5,
        choices=[(tag, tag.value) for tag in STATUS], default = STATUS.TRIAL
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True)
    users = models.ManyToManyField(User, verbose_name="Permission", blank=True)
    last_payment_date = models.DateTimeField(null = True)
    next_expiry_date = models.DateTimeField(null = True)
    last_expiry_date = models.DateTimeField(null = True)
    """


    app = serializers.CharField(
        max_length=255, min_length=8)
    status = serializers.CharField(max_length=255, min_length=4, required=False)
    company = serializers.IntegerField(required=False, write_only=True)
    users = serializers.IntegerField(required=False, write_only=True)


    class Meta:
        model = Plugin
        depth = 1
        fields = '__all__'

    def create(self, validated_data):

        return Plugin.objects.add_plugin(**validated_data)
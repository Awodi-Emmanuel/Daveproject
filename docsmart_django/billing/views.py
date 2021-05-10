from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from billing.helpers import ChargebeeHandler
from billing.serializers import FetchPlansSerializer
from roles.backends import OwnerPermission
from .models import BillingPlans


class GetHostedPage(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, OwnerPermission)

    @staticmethod
    def post(request):
        result = ChargebeeHandler().get_checkout_page(request.data.get("id"), request.user)
        hosted_page = result._response['hosted_page']
        return Response(hosted_page, status=200)


class FetchPlans(ListCreateAPIView):
    queryset = BillingPlans.objects.all()
    serializer_class = FetchPlansSerializer
    # permission_classes = [IsAdminUser]

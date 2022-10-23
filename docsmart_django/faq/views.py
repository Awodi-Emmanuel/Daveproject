from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import FAQ
from .serializers import FetchSerializer


# Create your views here.
class FetchFAQ(ListCreateAPIView):
    serializer_class = FetchSerializer

    def get_queryset(self):
        return FAQ.objects.all()

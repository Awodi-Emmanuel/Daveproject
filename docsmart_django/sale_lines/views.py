from django.shortcuts import render
from rest_framework import permissions, status
from .serializers import CreateLinesSerializer
from company.models import Company
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from sale_lines.serializers import FetchLinesSerializer
from sale_lines.models import Lines


# Create your views here.
class CreateLines(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CreateLinesSerializer

    @staticmethod
    def post(request):
        if not request.data.get('lines'):

            lines_serializer = CreateLinesSerializer(data=request.data)
            if lines_serializer.is_valid():
                related_company = Company.objects.get(user__id=request.user.id)
                lines_serializer.save(related_user=request.user, related_company=related_company)
                return Response(lines_serializer.data, status=status.HTTP_201_CREATED)

            return Response(lines_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        errors = []
        lines = []

        for l in request.data.get('lines'):

            lines_serializer = CreateLinesSerializer(data=l)
            if lines_serializer.is_valid():

                related_company = Company.objects.get(user__id=request.user.id)
                lines_serializer.save(related_user=request.user, related_company=related_company)
                lines.append(lines_serializer.data)

            else:

                errors.append(lines_serializer.errors)

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(lines, status=status.HTTP_201_CREATED)


class FetchLines(ListCreateAPIView):
    serializer_class = FetchLinesSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Lines.objects.filter(related_company__user__id=self.request.user.id)

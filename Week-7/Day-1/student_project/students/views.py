from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser, IsAuthenticated, AllowAny)
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST)
from .models import Student
from .serializers import StudentSerializer
from .mixins import StudentOperationsMixin
from rest_framework.generics import GenericAPIView



class StudentListMixin(StudentOperationsMixin, GenericAPIView):

    def get_queryset(self):
        queryset = super().get_queryset()
        date_joined = self.request.query_params.get('date_joined')
        if date_joined:
            print (date_joined)
            queryset = queryset.order_by('date_joined')
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)   


class StudentDetailMixin(StudentOperationsMixin, GenericAPIView):
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StudentSerializer(instance)
        return Response(serializer.data)
    

class StudentView(APIView):

    permission_classes = (AllowAny, )


    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if pk:
            try:
                instance = Student.objects.get(id=pk)
                serializer = StudentSerializer(instance)
            except Student.DoesNotExist:
                return Response({"detail": "Student not found"}, status=HTTP_400_BAD_REQUEST)
        else:
            queryset = Student.objects.all()
            serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


    def post(self, request, *args, **kwargs):

        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED) 
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


    @api_view(['GET', 'POST'])
    def student_list(request):
        if request.method == 'GET':
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


    @api_view(['GET', 'PUT', 'DELETE'])
    def student_detail(request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = StudentSerializer(student)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            student.delete()
            return Response(status=HTTP_204_NO_CONTENT)






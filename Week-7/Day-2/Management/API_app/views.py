from django.shortcuts import render, redirect
from .models import Department, Task, Project, Employee
from .serializers import TaskSerializer, ProjectSerializer, EmployeetSerializer, DepartmentSerializer
from .permissions import IsDepartmentAdmin
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth.models import Group

from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser,
                                        IsAuthenticated,
                                        AllowAny)
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_201_CREATED,
                                   HTTP_202_ACCEPTED,
                                   HTTP_400_BAD_REQUEST)

from rest_framework.generics import (GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView,
                                     DestroyAPIView, UpdateAPIView)

# CRUD - CREATE - RETRIEVE - UPDATE - DELETE/DESTROY


class DepartmentListAPIView(ListAPIView):
    permission_classes = [IsDepartmentAdmin]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentCreateAPIView(CreateAPIView):
    permission_classes = (IsDepartmentAdmin,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeListAPIView(ListAPIView):
    permission_classes = (IsDepartmentAdmin,)
    queryset = Employee.objects.all()
    serializer_class = EmployeetSerializer

class EmployeeCreateAPIView(CreateAPIView):
    permission_classes = (IsDepartmentAdmin,)
    queryset = Department.objects.all()
    serializer_class = EmployeetSerializer


class ProjectListAPIView(ListAPIView):
    permission_classes = (IsDepartmentAdmin,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectCreateAPIView(CreateAPIView):
    permission_classes = (IsDepartmentAdmin,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsDepartmentAdmin,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'

class ProjectUpdateAPIView(UpdateAPIView):
    permission_classes = (IsDepartmentAdmin,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'

class ProjectDestroyAPIView(DestroyAPIView):
    permission_classes = (IsDepartmentAdmin,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'


class TaskListAPIView(ListAPIView):
    permission_classes = (IsDepartmentAdmin,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskCreateAPIView(CreateAPIView):
    permission_classes = (IsDepartmentAdmin,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsDepartmentAdmin,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'

class TaskUpdateAPIView(UpdateAPIView):
    permission_classes = (IsDepartmentAdmin,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'

class TaskDestroyAPIView(DestroyAPIView):
    permission_classes = (IsDepartmentAdmin,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'







# class DepartmentListAPIView(ListAPIView):

#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer

    # def get(self, request, *args, **kwargs):

    #     pk = kwargs.get('pk')

    #     if pk:
    #         try:
    #             instance = Department.objects.get(id=pk)
    #             serializer = DepartmentSerializer(instance)
    #         except Department.DoesNotExist:
    #             return Response({"detail": "Department not found"}, status=HTTP_400_BAD_REQUEST)
    #     else:
    #         queryset = Department.objects.all()
    #         serializer = DepartmentSerializer(queryset, many=True)
    #     return Response(serializer.data, status=HTTP_200_OK)


    # def post(self, request, *args, **kwargs):

    #     serializer = DepartmentSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=HTTP_201_CREATED) 
    #     return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


    # @api_view(['GET', 'POST'])
    # def department_list(request):
    #     if request.method == 'GET':
    #         departments = Department.objects.all()
    #         serializer = DepartmentSerializer(departments, many=True)
    #         return Response(serializer.data)

    #     elif request.method == 'POST':
    #         serializer = DepartmentSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=HTTP_201_CREATED)
    #         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


    # @api_view(['GET', 'PUT', 'DELETE'])
    # def department_detail(request, pk):
    #     try:
    #         department = Department.objects.get(pk=pk)
    #     except Department.DoesNotExist:
    #         return Response(status=HTTP_404_NOT_FOUND)

    #     if request.method == 'GET':
    #         serializer = DepartmentSerializer(department)
    #         return Response(serializer.data)

    #     elif request.method == 'PUT':
    #         serializer = DepartmentSerializer(department, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    #     elif request.method == 'DELETE':
    #         department.delete()
    #         return Response(status=HTTP_204_NO_CONTENT)



# # ---------------------APIView------------------
# class DepartmentView(APIView):

#     permission_classes = (AllowAny, )

#     def get(self, request, *args, **kwargs):

#         pk = kwargs.get('pk')
        
#         if pk:
#             try:
#                 instance = Department.objects.get(id=pk)
#                 serializer = DepartmentSerializer(instance)
#             except Department.DoesNotExist:
#                 return Response({"detail": "Department not found"}, status=HTTP_400_BAD_REQUEST)
#         else:
#             queryset = Department.objects.all()
#             serializer = DepartmentSerializer(queryset, many=True)
#         return Response(serializer.data, status=HTTP_200_OK)
    
#     def post(self, request, *args, **kwargs):

#         serializer = DepartmentSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = HTTP_201_CREATED)
        
#         return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, *args, **kwargs):

#         pk = kwargs.get('pk')
        
#         if pk:
#             try:
#                 department = Department.objects.get(id=pk)
#                 department.delete()
#                 return Response({"detail": "Department was deleted!"}, status=HTTP_202_ACCEPTED)
#             except Department.DoesNotExist:
#                 return Response({"detail": "Department not found"}, status=HTTP_400_BAD_REQUEST)

#         else:
#             return redirect('post-list')

#     def put(self, request, *args, **kwargs):

#         pk = kwargs.get('pk')

#         if pk:
#             try:
#                 department = Department.objects.get(id=pk)
#                 serializer = DepartmentSerializer(department, data=request.data)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data)
                
#             except Department.DoesNotExist:
#                 return Response({"detail": "Department not found"}, status=HTTP_400_BAD_REQUEST)
#         else:
#            return Response({"detail": "pk wasn't found"}, status=HTTP_400_BAD_REQUEST) 



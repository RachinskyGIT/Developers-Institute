from django.contrib import admin
from django.urls import path
from API_app.views import (DepartmentListAPIView, DepartmentCreateAPIView, 
                            EmployeeListAPIView, EmployeeCreateAPIView,
                            ProjectDestroyAPIView, ProjectUpdateAPIView, ProjectRetrieveAPIView,
                            ProjectCreateAPIView, ProjectListAPIView,
                            TaskDestroyAPIView, TaskUpdateAPIView, TaskRetrieveAPIView,
                            TaskCreateAPIView, TaskListAPIView
                            )

urlpatterns = [
    path("admin/", admin.site.urls),

    path('department/', DepartmentListAPIView.as_view(), name='department-list'),
    path("department/<int:pk>", DepartmentListAPIView.as_view(), name = 'department'),
    path('create_department/', DepartmentCreateAPIView.as_view(), name='department-create'),

    path('employee/', DepartmentListAPIView.as_view(), name='employee-list'),
    path("employee/<int:pk>", EmployeeListAPIView.as_view(), name = 'employee'),
    path('create_employee/', EmployeeCreateAPIView.as_view(), name='employee-create'),

    path('project/', ProjectListAPIView.as_view(), name='project-list'),
    path('project/create/', ProjectCreateAPIView.as_view(), name='project-create'),
    path('project/<int:id>/', ProjectRetrieveAPIView.as_view(), name='project-detail'),
    path('project/<int:id>/update/', ProjectUpdateAPIView.as_view(), name='project-update'),
    path('project/<int:id>/delete/', ProjectDestroyAPIView.as_view(), name='project-delete'),

    path('task/', TaskListAPIView.as_view(), name='task-list'),
    path('task/create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('task/<int:id>/', TaskRetrieveAPIView.as_view(), name='task-detail'),
    path('task/<int:id>/update/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('task/<int:id>/delete/', TaskDestroyAPIView.as_view(), name='task-delete'),
]
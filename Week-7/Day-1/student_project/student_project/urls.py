from django.contrib import admin
from django.urls import path, include
from students.views import StudentView, StudentListMixin, StudentDetailMixin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include('rest_framework.urls')),
    # path("api-students/", StudentView.as_view(), name = 'student-list'),
    # path("api-students/<int:pk>", StudentView.as_view(), name = 'student'),
    path('students/', StudentListMixin.as_view(), name='student-list'),
    path('students/<int:id>/', StudentDetailMixin.as_view(), name='student-detail'),    
    
]

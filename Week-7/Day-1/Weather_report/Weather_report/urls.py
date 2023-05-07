from django.contrib import admin
from django.urls import path, include
from weatherapp.views import ReportView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include('rest_framework.urls')),
    path("api-reports/", ReportView.as_view(), name = 'report-list'),
    path("api-reports/<int:pk>", ReportView.as_view(), name = 'report'),
    
]

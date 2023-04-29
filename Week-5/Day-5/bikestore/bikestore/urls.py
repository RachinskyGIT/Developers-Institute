"""
URL configuration for bikestore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rent.views import All_rentals, Rental_detail, Customer_detail, All_customers, All_vehicles, Vehicle_detail


urlpatterns = [
    path("admin/", admin.site.urls),
    path("rental/", All_rentals),
    path("rental/<pk>", Rental_detail),
    path("customer/<pk>", Customer_detail),
    path("customer/", All_customers),
    path("vehicle/", All_vehicles),
    path("vehicle/<pk>", Vehicle_detail),

]

# from django.contrib import admin
# from django.urls import path
# from gifs.views import Homepage, add_gif_view, add_category_view


# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("rental/", All_rentals),
#     path("add_gif/", add_gif_view),
#     path("add_category/", add_category_view),
# ]

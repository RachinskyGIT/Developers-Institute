from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date



# Create your views here.
def index (request):
    current_time = date.today()
    context = {'current_date': current_time}
    return render(request, 'index.html',context)
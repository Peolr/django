from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import MyTable

def my_view(request):
    data = MyTable.objects.all()
    return render(request, 'my_template.html', {'data': data})
 
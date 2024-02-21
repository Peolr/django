from django.shortcuts import render

# Create your views here.

def my_view(request):
    context = {'message': "Hello, this is my static text!"}
    return render(request, 'template_name.html', context)
from django.shortcuts import render

# Create your views here.
def app1_hello(request):
    return render(request,'app1/app1.html')
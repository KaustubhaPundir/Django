from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("I am Django")

def contact(request):
    return HttpResponse("Contact me Django")
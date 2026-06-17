from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hi  resive the call ")
def name(request):
    return HttpResponse("hi this is my name")

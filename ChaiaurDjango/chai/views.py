from django.shortcuts import render

# Create your views here.
def chai_home(request):
    #return HttpResponse("Hello world!! This is Home page")
    return render(request,'chai/chai_home.html')
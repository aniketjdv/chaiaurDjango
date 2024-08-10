from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def chai_home(request):
    chais = ChaiVariety.objects.all()
    #return HttpResponse("Hello world!! This is Home page")
    return render(request,'chai/chai_home.html',{'chais':chais})

def chai_detail(request,chai_id):
    chai=get_object_or_404(ChaiVariety,pk=chai_id)
    #return HttpResponse("Hello world!! This is Home page")
    return render(request,'chai/chai_detail.html',{'chai':chai})
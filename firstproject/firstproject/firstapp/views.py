from os import name

from django.http import HttpResponse
from django.shortcuts import render
from .models import place, team


def demo(request):
    obj=place.objects.all()
    obj2=team.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})
#def operations(request):
#   x=int(request.GET['num1'])
#  y=int(request.GET['num2'])
#    res1=x+y
#    res2=x-y
#    res3=x*y
#    res4=x/y
#    return render(request,"result.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})


  #def about(request):
 #   return render(request,"about.html")
#def contact(request):
 #   return HttpResponse("Our Contacts")
#def detail(request):
 #   return render(request,"detail.html")
#def thanks(request):
 #   return HttpResponse("Thanks")
# Create your views here.

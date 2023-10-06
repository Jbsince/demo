from django.http import HttpResponse
from django.shortcuts import render
from . models import place,partners
# Create your views here.



def demo(request):
   name = place.objects.all()
   patner = partners.objects.all()
   return render(request, "index.html", {'obj': name, 'obj1': patner})






   # name="india"
   # return render(request,"index.html",{'obj':name})
#
# def about(request):
#    return render(request,'about.html')
#
# def contact(request):
#    return render(request,'contact.html')
#
# def details(request):
#    return render(request,'details.html')
#
# def thanks(request):
#    return HttpResponse("Thanks to visit the Page")


def operation(request):
   n1=int(request.GET['n1'])
   n2=int(request.GET['n2'])
   add=n1+n2
   sub=n1-n2
   mul=n1*n2
   div=n1/n2
   return render(request,'result.html',{'add':add,'sub':sub,'mul':mul,'div':div,'n1':n1,'n2':n2})
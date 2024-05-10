from django.shortcuts import render

# Create your views here.

def agregasi(input):
    result = input + 10
    return result

def page_landing(request):
    return render(request, "app_landing/index.html") #merequest ke templates

def page_about(request):
    context = {"NAMA": "Izzan",
               "AGREGASI" : agregasi(123),
               }
    return render(request,"app_landing/about.html", context)
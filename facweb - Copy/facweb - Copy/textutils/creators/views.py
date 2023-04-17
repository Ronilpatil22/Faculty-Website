from django.shortcuts import render

# Create your views here.


def creators(request):
    return render(request, "creators.html")
    
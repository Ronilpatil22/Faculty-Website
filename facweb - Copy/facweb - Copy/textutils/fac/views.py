from django.shortcuts import render
def index(request):
    return render(request, "index.html",{"var": "work"})
# Create your views here.

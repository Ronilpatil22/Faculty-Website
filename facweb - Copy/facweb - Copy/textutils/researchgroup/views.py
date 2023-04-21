from django.shortcuts import render
from fac.models import socialmediabar
from fac.models import Navbar
from fac.models import Navbar_icon
from .models import research_group_class
from .models import research_group_details

# Create your views here.
def research(request):
    socialmedia_list = socialmediabar.objects.all()
    Navbar_list = Navbar.objects.all()
    Navbar_icon_list = Navbar_icon.objects.all()
    research_group_class_list = research_group_class.objects.all()
    research_group_details_list = research_group_details.objects.all()
    return render(request, "research-group.html",{'socialmedia':socialmedia_list,'navbar':Navbar_list,'Navbar_icon':Navbar_icon_list,'research_group_class':research_group_class_list,'research_group_details':research_group_details_list})
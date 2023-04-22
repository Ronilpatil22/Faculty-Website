from django.shortcuts import render
from fac.models import socialmediabar
from fac.models import Navbar
from fac.models import Navbar_icon
from fac.models import socialmediabarmessage
from .models import current_research,current_btp,alumni_btech,alumni_ms,alumni_phd,interns
# Create your views here.
def research(request):
    socialmedia_list = socialmediabar.objects.all()
    Navbar_list = Navbar.objects.all()
    socialmediabarmessage_list = socialmediabarmessage.objects.all()
    Navbar_icon_list = Navbar_icon.objects.all()
    current_research_list = current_research.objects.all()
    current_btp_list = current_btp.objects.all()
    alumni_btech_list = alumni_btech.objects.all()
    alumni_ms_list = alumni_ms.objects.all()
    alumni_phd_list = alumni_phd.objects.all()
    interns_list = interns.objects.all()
    return render(request, "research-group.html",
                  {'socialmedia':socialmedia_list,
                   'navbar':Navbar_list,
                   'Navbar_icon':Navbar_icon_list,
                   'socialmediabarmessage':socialmediabarmessage_list,
                   'current_research':current_research_list,
                   'current_btp':current_btp_list,
                   'alumni_btech':alumni_btech_list,
                   'alumni_ms':alumni_ms_list,
                   'alumni_phd':alumni_phd_list,
                   'interns':interns_list,
                   })
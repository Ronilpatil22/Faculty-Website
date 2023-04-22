from django.shortcuts import render
from fac.models import socialmediabar
from fac.models import Navbar
from fac.models import Navbar_icon
from fac.models import socialmediabarmessage
from .models import current_employment,previous_employment,courses,projects,international_journal,conference_papers,patents,book_chapters,achievements_outreach,awards
# Create your views here.

def aboutme(request):
    socialmedia_list = socialmediabar.objects.all()
    Navbar_list = Navbar.objects.all()
    Navbar_icon_list = Navbar_icon.objects.all()
    socialmediabarmessage_list = socialmediabarmessage.objects.all()
    current_employment_list = current_employment.objects.all()
    previous_employment_list = previous_employment.objects.all()
    projects_list = projects.objects.all()
    international_journal_list = international_journal.objects.all()
    conference_papers_list = conference_papers.objects.all()
    patents_list = patents.objects.all()
    book_chapters_list = book_chapters.objects.all()
    achievements_outreach_list = achievements_outreach.objects.all()
    awards_list = awards.objects.all()
    courses_list = courses.objects.all()
    return render(request, "about-me (2).html",
                  {'socialmedia':socialmedia_list,
                   'navbar':Navbar_list,
                   'Navbar_icon':Navbar_icon_list,
                   'socialmediabarmessage':socialmediabarmessage_list,
                   'current_employment':current_employment_list,
                   'previous_employment':previous_employment_list,
                   'projects':projects_list,
                   'international_journal':international_journal_list,
                   'conference_papers':conference_papers_list,
                   'patents':patents_list,
                   'book_chapters':book_chapters_list,
                   'achievements_outreach':achievements_outreach_list,
                   'awards':awards_list,
                   'courses' : courses_list,
                   })
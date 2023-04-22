from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import current_employment,previous_employment,projects,international_journal,courses,conference_papers,patents,book_chapters,achievements_outreach,awards
# Register your models here.
admin.site.register(current_employment)
admin.site.register(previous_employment)
admin.site.register(projects)
admin.site.register(international_journal)
admin.site.register(conference_papers)
admin.site.register(patents)
admin.site.register(book_chapters)
admin.site.register(achievements_outreach)
admin.site.register(awards)
admin.site.register(courses)
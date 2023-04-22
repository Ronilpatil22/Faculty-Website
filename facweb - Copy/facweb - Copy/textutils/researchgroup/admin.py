from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import current_research,current_btp,alumni_btech,alumni_ms,alumni_phd,interns
# Register your models here.
class restricted_to_3(admin.ModelAdmin):
    def add_view(self, request, form_url='', extra_context=None):
        if self.model.objects.count() >= 3:
            self.message_user(request, 'Only three entries can exist at once - please remove others first or edit them', messages.ERROR)
            return HttpResponseRedirect(reverse(f'admin:{self.model._meta.app_label}_testimonials_changelist'))
        return super().add_view(request, form_url, extra_context)
class restricted_to_1(admin.ModelAdmin):
    def add_view(self, request, form_url='', extra_context=None):
        if self.model.objects.count() >= 1:
            self.message_user(request, 'Only One entry can exist at once - please remove it first or edit it', messages.ERROR)
            return HttpResponseRedirect(reverse(f'admin:{self.model._meta.app_label}_introduction_changelist'))
        return super().add_view(request, form_url, extra_context)
admin.site.register(current_research)
admin.site.register(current_btp)
admin.site.register(alumni_btech)
admin.site.register(alumni_ms)
admin.site.register(alumni_phd)
admin.site.register(interns)
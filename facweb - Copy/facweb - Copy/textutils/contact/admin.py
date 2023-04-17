from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import contacts
# Register your models here.
class restricted_to_1(admin.ModelAdmin):
    def add_view(self, request, form_url='', extra_context=None):
        if self.model.objects.count() >= 1:
            self.message_user(request, 'Only One entry can exist at once - please remove it first or edit it', messages.ERROR)
            return HttpResponseRedirect(reverse(f'admin:{self.model._meta.app_label}_introduction_changelist'))
        return super().add_view(request, form_url, extra_context)
    

admin.site.register(contacts,restricted_to_1)
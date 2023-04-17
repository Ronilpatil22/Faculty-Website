from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import socialmediabar
from .models import Navbar
from .models import Navbar_icon
# Register your models here.

class restricted_to_3(admin.ModelAdmin):
    def add_view(self, request, form_url='', extra_context=None):
        if self.model.objects.count() >= 3:
            self.message_user(request, 'Only three entries can exist at once - please remove others first or edit them', messages.ERROR)
            return HttpResponseRedirect(reverse(f'admin:{self.model._meta.app_label}_testimonials_changelist'))
        return super().add_view(request, form_url, extra_context)
admin.site.register(socialmediabar)
admin.site.register(Navbar)
admin.site.register(Navbar_icon)
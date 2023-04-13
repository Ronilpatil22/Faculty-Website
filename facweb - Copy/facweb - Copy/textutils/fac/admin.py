from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import testimonials
from .models import introduction
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    def add_view(self, request, form_url='', extra_context=None):
        if self.model.objects.count() >= 3:
            self.message_user(request, 'Only three entries can exist at once - please remove others first', messages.ERROR)
            return HttpResponseRedirect(reverse(f'admin:{self.model._meta.app_label}_testimonials_changelist'))
        return super().add_view(request, form_url, extra_context)

admin.site.register(testimonials,AboutAdmin)
admin.site.register(introduction)
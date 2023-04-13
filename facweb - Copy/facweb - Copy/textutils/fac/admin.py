from django.contrib import admin
from .models import testimonials
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    def add_view(self, request, form_url='', extra_context=None):
        if self.model.objects.count() >= 2:
            self.message_user(request, 'Only two entries can exist at once - please remove others first', messages.ERROR)
            return HttpResponseRedirect(reverse(f'admin:{self.model._meta.app_label}_about_changelist'))
        return super().add_view(request, form_url, extra_context)

admin.site.register(testimonials)
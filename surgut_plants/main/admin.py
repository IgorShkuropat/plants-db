from django.contrib import admin
from .models import Company


class OrgAdmin(admin.ModelAdmin):
    list_display = ('ur_lico', 'address')


admin.site.register(Company, OrgAdmin)

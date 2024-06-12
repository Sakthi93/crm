from django.contrib import admin
from .models import leads


admin.site.site_header = "CRM Admin Site"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to the Admin Portal"


class leadsAdmin(admin.ModelAdmin):
    list_display = ('company', 'contact_person', 'email', 'phone', 'website','confidence', 'estimated_value', 'status', 'created_by', 'created_at', 'modified_at')  
    search_fields = ('company', 'contact_person', 'email', 'phone', 'website','confidence', 'estimated_value', 'status', 'created_by', 'created_at', 'modified_at')               
    list_filter = ('company', 'contact_person', 'email', 'phone', 'website','confidence', 'estimated_value', 'status', 'created_by', 'created_at', 'modified_at')                  

admin.site.register(leads, leadsAdmin)

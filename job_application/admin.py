from django.contrib import admin
from .models import Form


# Data to display in the admin interface
class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("start_date", "position")
    ordering = ("last_name", )
    # readonly_fields = ("start_date", )


# Registers the form data available in admin interface
admin.site.register(Form, FormAdmin)
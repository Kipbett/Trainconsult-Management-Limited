from django.contrib import admin

# Register your models here.
from .models import Events, OrgBookEvents, MakePayment

class BookEventsAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "event",
        "attendance_mode",
        "email_address",
    )
    list_filter = ("first_name", "last_name", "attendance_mode")
    search_fields = ("first_name", "last_name")

admin.site.register(Events)
admin.site.register(OrgBookEvents, BookEventsAdmin)
admin.site.register(MakePayment)

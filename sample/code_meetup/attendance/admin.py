from django.contrib import admin
from .models import Attendance, Attendee


# Register your models here.
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("date", "get_attendees_count")
    model = Attendance

    def get_attendees_count(self, obj):
        return obj.attendees.count()

    get_attendees_count.short_description = "Ilan umattend?"



class AttendeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "middle_name", "last_name")
    model = Attendee

    

admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Attendee, AttendeeAdmin)
from django.contrib import admin
from .models import HostelUser
from .models import Profile
from .models import contact
from .models import Booking


# Register your models here.

class HostelUserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email')


admin.site.register(HostelUser,HostelUserAdmin)



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'dob', 'course', 'college', 'phone','profile_image')
    search_fields = ('full_name', 'college', 'course')





@admin.register(contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "message")






@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "first_name", "last_name", "email", "phone",
        "room_type", "room_number", "bed_number",
        "check_in", "check_out", "payment_method", "created_at"
    )
    search_fields = ("first_name", "last_name", "email", "phone", "room_number", "bed_number")
    list_filter = ("room_type", "payment_method", "check_in", "check_out")

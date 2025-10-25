from django.db import models
from .models import *
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

# Create your models here.
class HostelUser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    dob = models.DateField()
    address = models.TextField()
    course = models.CharField(max_length=100)
    college = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.png',blank=True,null=True)

    def __str__(self):
        return self.full_name




class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def _str_(self):
        return self.name 




class Booking(models.Model):
    # Personal Details
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)

    # Contact
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    # Booking Details
    check_in = models.DateField()
    check_out = models.DateField()
    room_type = models.CharField(max_length=100)
    room_number = models.CharField(max_length=50)
    bed_number = models.CharField(max_length=50)

    # Payment & ID Proof
    id_type = models.CharField(max_length=50)
    id_number = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    payment_reference = models.CharField(max_length=100, blank=True, null=True)

    # Additional Info
    special_requests = models.TextField(blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Consent
    terms_accepted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Room {self.room_number} (Bed {self.bed_number})"

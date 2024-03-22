import datetime
from collections import defaultdict

from django.db import models
from datetime import date

class Events(models.Model):
    event_id = models.CharField(max_length=100)
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_venue = models.CharField(max_length=100)
    event_time = models.CharField(max_length=100)
    event_image = models.ImageField(upload_to="pictures")

    def __str__(self):
        return self.event_name

class OrgBookEvents(models.Model):

    PAYMENT_CHOICES = (
        ('mpesa', 'M-Pesa'),
        ('visa', 'Visa')
    )

    EVENTS = (
        ('choose', 'Choose Event'),
        ('women-led', '1ST WOMEN LEAD CONFERENCE'),
    )

    MODE_OF_ATTENDANCE = (
        ('physical', 'Physical'),
        ('virtual', 'Virtual'),
        ('student', 'Student')
    )

    CURRENCY_CHOICES = (
        ('kes', 'KES'),
        ('usd', 'USD')
    )

    STUDY_YEAR = (
        ('first', '1ST YEAR'),
        ('second', '2ND YEAR'),
        ('third', '3RD YEAR'),
        ('fourth', '4TH YEAR'),
        ('fifth', '5TH YEAR')
    )

    event = models.CharField(max_length=100, choices=EVENTS)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100, blank=True)
    email_address = models.EmailField(max_length=100)
    attendance_mode = models.CharField(max_length=100, choices=MODE_OF_ATTENDANCE)
    phone_number = models.CharField(max_length=15, null=True)
    booking_status = models.CharField(max_length=20, default="Not Approved")
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    university = models.CharField(max_length=100,blank=True)
    year_of_study = models.CharField(max_length=10, choices=STUDY_YEAR, blank=True)
    date_booking = models.DateField(max_length=100, default=date.today)


    def __str__(self):
        return self.first_name

class MakePayment(models.Model):
    email_address = models.ForeignKey(OrgBookEvents, on_delete=models.PROTECT)
    payment_method = models.CharField(max_length=100)
    order_amount = models.IntegerField()
    confirmation_code = models.CharField(max_length=100, unique=True)
    status_code = models.CharField(max_length=5)
    order_currency = models.CharField(max_length=20)

    def __str__(self):
        return self.email_address
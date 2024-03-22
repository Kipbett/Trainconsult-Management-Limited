from django import forms

from .models import OrgBookEvents


class OrgBookingForm(forms.ModelForm):
    class Meta:
        model = OrgBookEvents
        fields = ['event', 'first_name', 'last_name', 'organization', 'email_address', 'phone_number', 'attendance_mode',
                  'currency', 'university', 'year_of_study']

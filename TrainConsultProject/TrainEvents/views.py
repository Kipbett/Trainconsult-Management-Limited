import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

from .forms import OrgBookingForm
from django_daraja.mpesa.core import MpesaClient
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from .models import OrgBookEvents, MakePayment
from Utils.pesapalpayment import submit_order_request, reg_ipn_url, transaction_status
from Utils.SendMail import send_custom_email

# from ..Utils.pesapalpayment import reg_ipn_url

ipn = reg_ipn_url()

j_result = (
    ipn.json()
)

ipn_id = j_result['ipn_id']


@csrf_exempt
def book_event(request):
    if request.method == 'POST':
        form = OrgBookingForm(request.POST)
        if form.is_valid():
            phone_number = request.POST['phone_number']
            attendance = request.POST['attendance_mode']
            email_address = request.POST['email_address']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            currency = request.POST['currency']

            if currency == 'KES':
                if attendance == "physical":
                    amount = 1
                elif attendance == "virtual":
                    amount = 1
                elif attendance == "student":
                    amount = 1
            else:
                if attendance == "physical":
                    amount = 1
                elif attendance == "virtual":
                    amount = 1
                elif attendance == "student":
                    amount = 1

            #Get order details.

            form_data = {}

            submit_order_request(amount, phone_number, email_address, first_name, last_name, ipn_id, currency)
            submit_order = submit_order_request(amount, phone_number, email_address, first_name, last_name, ipn_id,
                                                currency)
            j_response = (
                submit_order.json()
            )
            redirect_url = j_response['redirect_url']

            order_tracking_id = j_response['order_tracking_id']

            #Get payment details

            tracking_id = transaction_status(order_tracking_id)
            order_response = (
                tracking_id.json()
            )

            payment_method = order_response['payment_method'],
            order_amount = order_response['amount'],
            confirmation_code = order_response['confirmation_code'],
            status_code = order_response['status_code'],
            order_currency = order_response['currency'],
            status = ''

            if status_code == 0:
                status = 'INVALID'
            if status_code == 1:
                status = 'COMPLETED'
            if status_code == 2:
                status = 'FAILED'
            if status_code == 3:
                status = 'REVERSED'

            payment_data = {
                payment_method: order_response['payment_method'],
                order_amount: order_response['amount'],
                confirmation_code: order_response['confirmation_code'],
                status_code: order_response['status_code'],
                order_currency: order_response['currency'],
                status: status
            }

            form.save()

            MakePayment.objects.create(
                payment_data
            )
            messages.success(request, "Event Booked Successfully.")
            send_custom_email("Trainconsult Event Booking",
                              "Your Request To Attend Our Event Has Been Received.\n "
                              "Your booking will be confirmed within the 24 hours. \n "
                              f"Your transaction code for the payment is {confirmation_code}"
                              "Thank You.\n Regards\n "
                              "Trainconsult Management", "admin@trainconsult-management.co.ke",
                              [email_address])


            return HttpResponseRedirect(redirect_url)
    else:
        form = OrgBookingForm()
    return render(request, 'booking.html', {'form': form})


@login_required(login_url='/user-login')
def show_bookings(request):
    bookings = OrgBookEvents.objects.all()
    username = request.session['username']
    return render(request, 'bookings.html', {'bookings': bookings, 'username': username})


def delete(request, id):
    try:
        # data = OrgBookEvents.objects.get(id=id)
        data = get_object_or_404(OrgBookEvents, pk = id)
        if data:
            data.delete()
            messages.success(request, "Data Deleted Successfully.")
        else:
            messages.warning(request, "Data Not Found.")
    except OrgBookEvents.DoesNotExist:
        messages.warning(request, "Error!!! Data Not Found.")
    return HttpResponseRedirect(reverse('bookings'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, "Login Successful")
            request.session['username'] = request.POST['username']
            return redirect('bookings')
        else:
            messages.warning(request, "User Does Not Exist")
    form = AuthenticationForm()
    return render(request, 'user-login.html', {'form': form})

@login_required(login_url='/user-login')
def view_booking(request, id):
    try:
        data = get_object_or_404(OrgBookEvents, pk = id)
        username = request.session['username']
        if data:
            return render(request, 'booking-details.html', {'data': data, 'username': username})
        else:
            messages.warning(request, "Invalid Choice")
    except OrgBookEvents.DoesNotExist:
        messages.warning(request, "Invalid Choice")

def confirm_booking(request, id):
    data = get_object_or_404(OrgBookEvents, pk = id)
    email_address = data.email_address
    if data:
        data.booking_status = "Approved"
        data.save()
        send_custom_email("Trainconsult Event Booking Confirmation",
                          "Your Request To Attend Our Event Has Been APPROVED.\n "
                          "Thank You. Looking forward to seeing you.\n Regards.\n "
                          "Trainconsult Management", "admin@trainconsult-management.co.ke",
                          [email_address])
        return HttpResponse("Booking Is Approved")

@login_required(login_url='/user-login')
def confirmed_booking(request):
    data = OrgBookEvents.objects.all()
    username = request.session['username']
    if username:
        return render(request, "approved-bookings.html", {'data': data, 'username': username})
    else:
        return redirect('user_login')

def user_logout(request):
    try:
        del request.session['username']
    except:
        pass
    return redirect('user_login')

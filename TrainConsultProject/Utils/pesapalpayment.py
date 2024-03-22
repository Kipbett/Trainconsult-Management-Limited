import requests
import json
from . import random_id

unique_id = random_id.generate_random_string(20)

BASE_URL = "https://cybqa.pesapal.com/pesapalv3/api/"

def pesa_auth():
    url = f"{BASE_URL}Auth/RequestToken"
    payload = json.dumps({
        "consumer_key": "enter your consumer key",
        "consumer_secret": "Enter your consumer secret"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    j_response = (
        response.json()
    )
    access_token = j_response['token']
    return access_token

pesa = pesa_auth()

def reg_ipn_url():
    url = f"{BASE_URL}URLSetup/RegisterIPN"
    payload = json.dumps({
        "url": "https://trainconsult-management.co.ke/ipn",
        "ipn_notification_type": "GET"
    })
    headers = {
        "Authorization": "Bearer %s" % pesa,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response

def get_ipn_list():
    url = "https://cybqa.pesapal.com/pesapalv3/apiURLSetup/GetIpnList"
    payload = {}
    headers = {
        "Authorization": "Bearer %s" % pesa,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    ipn_id = response.text
    return ipn_id


def submit_order_request(amount, email_address, phone_number, first_name, last_name, ipn_id, currency):
    url = f"{BASE_URL}Transactions/SubmitOrderRequest"
    payload = json.dumps({
        "id": "%s" % unique_id,
        "currency": currency,
        "amount": amount,
        "description": "Payment for Trainconsult Event",
        "callback_url": "https://trainconsult-management.co.ke/events",
        "notification_id": ipn_id,
        "billing_address": {
            "email_address": email_address,
            "phone_number": phone_number,
            "country_code": "",
            "first_name": first_name,
            "middle_name": "",
            "last_name": last_name,
            "line_1": "",
            "line_2": "",
            "city": "",
            "state": "",
            "postal_code": None,
            "zip_code": None
        }
    })
    headers = {
        "Authorization": "Bearer %s" % pesa,
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response


def transaction_status(order_tracking_id):
    url = f"{BASE_URL}Transactions/GetTransactionStatus?orderTrackingId={order_tracking_id}"
    payload = {}
    headers = {
        "Authorization": "Bearer %s" % pesa,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response
import requests
from requests.auth import HTTPBasicAuth

from .access_token import generate_access_token
from .encode import generate_password
from .utils import get_timestamp
from . import keys


def lipa_na_mpesa(phone_number, amount):
    formatted_time = get_timestamp()
    decoded_password = generate_password(formatted_time)
    access_token = generate_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {"Authorization": "Bearer %s" % access_token}

    request = {
        "BusinessShortCode": keys.business_shortCode,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": keys.business_shortCode,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://mysterious-oasis-16355.herokuapp.com/api/payments/lnm/",
        "AccountReference": "test aware",
        "TransactionDesc": "Pay School Fees",
    }

    response = requests.post(api_url, json=request, headers=headers)

    return response.text


# print(lipa_na_mpesa())

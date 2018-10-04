import fitbit
import requests
import json
from configs import settings

token_file = 'token.json'

# http://python-fitbit.readthedocs.io/en/latest/

def read_token():
    with open(token_file, 'r') as f:
        t = json.load(f)
        return { "access_token": t['access_token'], 
            "refresh_token": t['refresh_token'] }


def authd_client(token):
    return fitbit.Fitbit(settings['consumer_key'], 
        settings['consumer_secret'], 
        access_token=token['access_token'], 
        refresh_token=token['refresh_token'])


def refresh_token(token):
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": token['refresh_token']
    }
    headers = {
        "Host": "api.fitbit.com",
        "Authorization": "Basic " + settings['authorization_id'],
        "Content-Type": "application/x-www-form-urlencoded"
    }
    return requests.get('https://api.fitbit.com/oauth2/token', 
        params=payload, headers=headers)


def call_fitbit(token):
    try:
        authd_resp = authd_client(token)
        # Basic check:
        activities_data = authd_resp.activities()
        return authd_resp
    except:
        token = refresh_token(token)
        f = open(token_file, 'w')
        f.write(str(token.json()))
        f.close()
        return authd_client(token)


token = read_token()
authd_client = call_fitbit(token)

data = ['caloriesOut', 'floors', 'restingHeartRate', 
    'sedentaryMinutes', 'steps', 'veryActiveMinutes']

activities_data = authd_client.activities()
a = activities_data['summary']
for d in data:
    print(f'{d}: {str(a[d])}')


import requests
from django.conf import settings

class Paystack: 
    SECRET_KEY = settings.SECRET_KEY
    BASE_URL = 'https://api.paystack.co'

    def verify(self, reference, *args, **kwargs):
        path = f'/transaction/verify/{reference}'

        headers = {
            "Authorization": f'Bearer {self.SECRET_KEY}',
            "Content-Type": "application/json",
        }

        url = self.BASE_URL + path
        
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            return response_data['status'], response_data['data']
        response_data = response.json()
        return response_data['status'], response_data['message']



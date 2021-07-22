import requests


class PetAuthorization:

    @staticmethod
    def get_token():
        client_id = '' # Put key here
        client_secret = '' # Put secret here

        data = {'grant_type': 'client_credentials', 'client_id': client_id, 'client_secret': client_secret}
        r = requests.post('https://api.petfinder.com/v2/oauth2/token', data=data)
        return r.json()['access_token']

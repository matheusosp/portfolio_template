import requests
import json
import getpass
#Creating URL, usr/pass and user agent variables

import requests
import json
import endpoints


endpoints = {
    'base': 'https://instagram.com/',
    'user_info': 'https://instagram.com/%s/?__a=1',
    'login': 'https://instagram.com/accounts/login/ajax/',
}
class VeslaInstaBot:
    def __init__(self):
        self.session = requests.Session()
        r = self.session.get(endpoints['base'])
        self.session.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
        self.user_id = None


    def login(self, credentials):      
        r = self.session.post(endpoints['login'], data=credentials)
        self.session.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
        r = json.loads(r.content.decode('utf-8'))
        if r['authenticated']:
            self.user_id = r['userId']
        return r


    def get_userid(self, username):
        url = endpoints['user_info'] % username
        r = self.session.get(url)
        if r.status_code == 200:
            r = json.loads(r.content.decode('utf-8'))
            return r['graphql']['user']['id']
        return None

start= VeslaInstaBot()  
credentials = {'username': 'tech_zone_produtos', 
               'password': '91128993'}     
r = start.login(credentials)
print(r)
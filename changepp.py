import requests
import random, time
from bs4 import BeautifulSoup

class ChangePP:
    mbasic = 'https://mbasic.facebook.com/'
    def __init__(self, cookie: str):
        # setup session
        self.session = requests.session()
        self.session.cookies['cookie'] = cookie

    def __main__(self, picture: bytes) -> bool:
        # get url for change profile picture
        source = BeautifulSoup(self.session.get(self.mbasic +'me').text, 'html.parser')
        try: url = source.find('a', href=lambda x: '/photos/change/profile_picture/' in x)['href']
        except Exception as e: url = source.find('a', href=lambda x: '/profile_picture/?returnuri=' in x)['href']
        
        # get parameter data 
        form = BeautifulSoup(self.session.get(self.mbasic + url).text, 'html.parser').find('form', {'method': 'post', 'action': True})
        data = {input_['name']: input_['value'] for input_ in form.find_all('input', {'name': True, 'value': True})}
        files = {'file1': picture}

        # upload
        send = self.session.post(form['action'], data=data, files=files)
        print(send.status_code)
        print(send.url)

        # conditions
        if 'm_upload_pic' in send.url: return True

# images using url
# images = requests.get('').content
# images form internal
images = open('images/profile.jpeg', 'rb').read()
cookie = '' # paste your cookies in here
ChangePP(cookoe=cookie).__main__(picture=images)

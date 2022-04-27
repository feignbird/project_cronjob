import requests
from django.contrib.auth import get_user_model

User = get_user_model()

URL = "https://randomuser.me/api/"

def make_user():
    r = requests.get(URL)
    data = r.json()
    username = data['results'][0]['login']['username']
    password = data['results'][0]['login']['password']
    first_name = data['results'][0]['name']['first']
    last_name = data['results'][0]['name']['last']
    email = data['results'][0]['email']
    user = User(username = username, first_name = first_name, last_name = last_name, email = email)
    user.set_password(password)
    user.save()


# def create_n_users(n):
#     for repeat in range(n):
#         make_user()


import requests
import sys
import os
import json
from copy import deepcopy
sys.path.append(os.path.abspath(os.path.join('..')))
from config import Config
from utils.utils import generate_object_id


params = {
    'apiKey': Config.API_KEY
}

headers = {
    'content-type': 'application/json'
}

posts = [
    {
        '_id': generate_object_id(),
        'image_url': '',
        'body': '',
        '_p_user': ''
    }
]


def insert(post):

    # resp = requests.post(Config.DB_POST_URL, params=params, data=json.dumps(post), headers=headers)
    # print resp.json()
    print post


def get_user_id(first_name):
    p = deepcopy(params)
    p['q'] = json.dumps({'first_name': first_name})
    resp = requests.get(Config.DB_USER_URL, params=p)
    if len(resp.json()) == 0:
        raise ValueError

    return resp.json()[0]['_id']

if __name__ == '__main__':
    user_id = get_user_id('Adil')
    for p in posts:
        p['_p_user'] = 'User$' + user_id
    map(insert, posts)

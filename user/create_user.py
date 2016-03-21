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

users = [
    {
        '_id': generate_object_id(),
        'first_name': 'Lionel',
        'last_name': 'Messi',
        'age': 28,
        'gender': 'MALE',
        'profile_image_url': 'http://res.cloudinary.com/hojviuaws/image/upload/v1458543242/profile_images/lionel_messi.jpg',
        'cover_image_url': 'http://res.cloudinary.com/hojviuaws/image/upload/v1458543402/cover_images/lionel_messi.jpg'
    },
    {
        '_id': generate_object_id(),
        'first_name': 'Eva',
        'last_name': 'Mendes',
        'age': 42,
        'gender': 'FEMALE',
        'profile_image_url': 'http://res.cloudinary.com/hojviuaws/image/upload/v1458543822/profile_images/eva_mendes.jpg',
        'cover_image_url': 'http://res.cloudinary.com/hojviuaws/image/upload/v1458543912/cover_images/eva_mendes.jpg'
    },
    {
        '_id': generate_object_id(),
        'first_name': 'Stephen',
        'last_name': 'Curry',
        'age': 28,
        'gender': 'MALE',
        'profile_image_url': 'http://res.cloudinary.com/hojviuaws/image/upload/v1458544022/profile_images/stephen_curry.jpg',
        'cover_image_url': 'http://res.cloudinary.com/hojviuaws/image/upload/v1458544110/cover_images/stephen_curry.jpg'
    },
    {
        '_id': generate_object_id(),
        'first_name': 'Aziz',
        'last_name': 'Ansari',
        'age': 33,
        'gender': 'MALE',
        'profile_image_url': 'http://res.cloudinary.com/hojviuaws/image/upload/v1458544230/profile_images/aziz_ansari.jpg',
        'cover_image_url': 'http://res.cloudinary.com/hojviuaws/image/upload/v1458544165/cover_images/aziz_ansari.jpg'
    },
    {
        '_id': generate_object_id(),
        'first_name': 'Maria',
        'last_name': 'Sharapova',
        'age': 28,
        'gender': 'FEMALE',
        'profile_image_url': 'http://res.cloudinary.com/hojviuaws/image/upload/v1458543032/profile_images/maria_sharapova.jpg',
        'cover_image_url': 'http://res.cloudinary.com/hojviuaws/image/upload/v1458542798/cover_images/maria_sharapova.jpg'
    }
]


def insert(user):
    if not user_exists(user):
        print 'FAILED', user['first_name'], 'already exists'
        return

    resp = requests.post(Config.DB_USER_URL, params=params, data=json.dumps(user), headers=headers)
    print resp.json()


def user_exists(user):
    p = deepcopy(params)
    p['q'] = json.dumps({'first_name': user['first_name'], 'last_name': user['last_name']})
    resp = requests.get(Config.DB_USER_URL, params=p)
    return len(resp.json()) == 0

if __name__ == '__main__':
    map(insert, users)

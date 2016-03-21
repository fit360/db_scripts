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

healthy = [
    'https://c1.staticflickr.com/3/2343/2233024002_bf65da29b2_b.jpg',
    'https://c2.staticflickr.com/4/3811/14267529834_6c4a71b519_o.jpg',
    'https://c2.staticflickr.com/8/7282/8903261552_532aac1bc4_b.jpg',
    'https://c2.staticflickr.com/8/7419/14186795735_ac50ff4ded_b.jpg',
    'https://c2.staticflickr.com/6/5492/11087468846_71931b5bd4_o.jpg'
]
workout = [
    'https://c2.staticflickr.com/4/3765/12336066195_1f5f36f8d1_o.jpg',
    'http://www.caloriesecrets.net/wp-content/uploads/2014/09/results-to-fitness-addiction.jpg',
    'http://cdn04.cdn.justjared.com/wp-content/uploads/2013/12/manganiello-muscle/joe-manganiello-gives-inside-look-at-his-shirtless-gym-workout-photos-10.jpg',
    'http://cdn1.theodysseyonline.com/files/2016/01/17/635886596101501921791037009_running.jpg',
    'http://daylol.com/nw/wp-content/uploads/2014/01/ball-fitness-fail.jpg'
]
body = [
    'http://www.directlyfitness.com/wordpress/wp-content/uploads/2013/01/Julie-Bonnet4.jpg',
    'http://www.alux.com/wp-content/uploads/2014/06/James-Ellis2.jpg',
    'https://dwaynejohnsoncentral.files.wordpress.com/2010/09/dwayne-johnson-golds-gym.jpg',
    'http://s9.favim.com/orig/130813/funny-pictures-funny-jokes-funny-pic-humor-Favim.com-851641.jpeg',
    'http://www.freakingnews.com/pictures/88500/Tom-Cruise-Training-at-the-Gym--88937.jpg'
]
transformation = [
    'http://media1.popsugar-assets.com/files/2015/01/09/254/n/28443503/edit_img_image_15904640_1420777274_THUMB.xxxlarge/i/Before-After-Photos-From-Kayla-Itsines-Bikini-Body-Guide.jpg',
    'https://media.licdn.com/mpr/mpr/shrinknp_800_800/AAEAAQAAAAAAAAX0AAAAJGY1ZGI3MGU2LTgzZGYtNGMwZC1iNjRkLTJlZjBjM2ViYTM2Nw.jpg',
    'https://toneeveryzone.files.wordpress.com/2015/04/wpid-fitness-funny-w630.jpg',
    'http://www.comebackmomma.com/wp-content/uploads/2013/10/funny-fitness-transformation.jpg',
    'https://s-media-cache-ak0.pinimg.com/736x/4c/a6/68/4ca668c2b93b3a1f79df8c25e26d5b31.jpg',
]

mutual = [
    'http://cdn-maf1.heartyhosting.com/sites/muscleandfitness.com/files/styles/full_node_image_1090x614/public/hit-on-girls-workout.jpg',
    'http://blog.walkjogrun.net/wp-content/uploads/2013/08/tips-for-couples-who-run-together.jpg',
    'http://images.veer.com/stock-photos/Young-naked-couple-running-and-MWP0057638.jpg',
    'http://imgfave-herokuapp-com.global.ssl.fastly.net/image_cache/1426516239570277.jpg',
    'http://data3.whicdn.com/images/69919170/large.png'
]


posts = [
    {
        '_id': generate_object_id(),
        'image_url': healthy[1],
        'body': 'This is what is getting me bankrupt for real.',
        '_p_user': ''
    },
    {
        '_id': generate_object_id(),
        'image_url': body[1],
        'body': "No gains only pains",
        '_p_user': ''
    },
    {
        '_id': generate_object_id(),
        'image_url': workout[1],
        'body': 'Join us @clubSPott',
        '_p_user': ''
    },
    {
        '_id': generate_object_id(),
        'image_url': mutual[1],
        'body': 'This is so happening',
        '_p_user': ''
    },
    {
        '_id': generate_object_id(),
        'image_url': transformation[1],
        'body': 'I am that guy doing stupid stuff always.',
        '_p_user': ''
    },
]


def insert(post):
    if is_new_image(post['image_url']):
        resp = requests.post(Config.DB_POST_URL, params=params, data=json.dumps(post), headers=headers)
        print resp.json()
    else:
        print 'exists'


def is_new_image(image_url):
    p = deepcopy(params)
    p['q'] = json.dumps({'image_url': image_url})
    resp = requests.get(Config.DB_POST_URL, params=p)
    return len(resp.json()) == 0


def get_user_id(first_name):
    p = deepcopy(params)
    p['q'] = json.dumps({'first_name': first_name})
    resp = requests.get(Config.DB_USER_URL, params=p)
    if len(resp.json()) == 0:
        raise ValueError

    return resp.json()[0]['_id']

if __name__ == '__main__':
    user_id = get_user_id('Lionel')
    for p in posts:
        p['_p_user'] = 'User$' + user_id
    map(insert, posts)

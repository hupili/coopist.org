import jinja2
import json
from db_mongo import *
from collections import Counter
from os import path
import sys


def render_one(project):
    dir_root = '/var/www/'
    dir_project = path.join(dir_root, project)
    fn_template = path.join(dir_root, 'project.tpl.html')
    fn_output = path.join(dir_project, 'index.html')

    status_list = mongo_client[project].status_list
    template = jinja2.Template(open(fn_template).read())
    recent = status_list.find().sort('time', -1)[:10]
    #recent = status_list.find().sort()
    photos = dict([(s['user']['profile_image_url'], s['user']['screen_name']) for s in status_list.find()])
    wall = photos.items()[:100]
    #print wall
    _tags = []
    for s in status_list.find():
        _tags.extend(s['text'].split())
    l = len(_tags)
    c = Counter(_tags)
    tag = json.dumps([[k, float(v) / l] for (k,v) in c.iteritems()])
    description = open(path.join(project, 'description'))
    result = template.render(recent=recent, wall=wall, tag=tag, description=description)
    open(fn_output, 'w').write(result)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        project = sys.argv[1]
        render_one(project)
    else:
        print "usage: %s project" % sys.argv[0]

'''
> db.status_list.findOne()
{
    "_id" : NumberLong("396612281863131136"),
    "favorited" : false,
    "truncated" : false,
    "text" : "The first #coopist tag?",
    "created_at" : "Sat Nov 02 12:18:31 +0000 2013",
    "hashtags" : [
        "coopist"
    ],
    "retweeted" : false,
    "source" : "web",
    "user" : {
        "lang" : "en",
        "profile_background_tile" : false,
        "statuses_count" : 65,
        "description" : "I'm back",
        "friends_count" : 250,
        "url" : "http://t.co/zvGhRoonba",
        "profile_link_color" : "0084B4",
        "created_at" : "Thu Oct 21 09:21:28 +0000 2010",
        "profile_sidebar_fill_color" : "http://abs.twimg.com/images/themes/theme1/bg.png",
        "utc_offset" : 28800,
        "profile_image_url" : "https://pbs.twimg.com/profile_images/378800000283621712/a5b897c6161ddaea540276d94e0842d4_normal.jpeg",
        "name" : "HU Pili",
        "profile_text_color" : "333333",
        "followers_count" : 20,
        "protected" : false,
        "location" : "Hongkong",
        "profile_background_color" : "C0DEED",
        "time_zone" : "Beijing",
        "id" : 205640689,
        "screen_name" : "hupili"
    },
    "id" : NumberLong("396612281863131136")
'''

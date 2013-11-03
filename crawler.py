import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('snsapi')

import snsapi
from snsapi.snspocket import SNSPocket
from db_mongo import *

def crawl_one(tag):
    sp = SNSPocket()
    sp.load_config(fn_channel=tag+'/channel.json')

    status_list = mongo_client[tag].status_list
    sl = sp.home_timeline()
    for s in sl:
        try:
            r = s.raw
            #print r
            if 'urls' in r:
                r.urls = [[k, v] for (k, v) in r['urls'].items()]
            r['_id'] = r['id']
            r['time'] = s.parsed['time']
            ret = status_list.insert(r)
            print ret
        except Exception as e:
            print str(e)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        tag = sys.argv[1]
        crawl_one(tag)
    else:
        print "usage: %s tag" % sys.argv[0]

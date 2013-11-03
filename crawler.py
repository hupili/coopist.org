import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('snsapi')

import snsapi
from snsapi.snspocket import SNSPocket

sp = SNSPocket()
sp.load_config(fn_channel='channel.json')

from db_mongo import *

sl = sp.home_timeline()
for s in sl:
    try:
        r = s.raw
        r['_id'] = r['id']
        r['time'] = s.parsed['time']
        ret = status_list.insert(r)
        print ret
    except Exception as e:
        print str(e)

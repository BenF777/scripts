#!usr/bin/env python
# -*- coding: utf-8 -*-


import collections
import pycurl
import pprint
import json
import sys
import unicodedata
import yaml
from io import BytesIO
from datetime import datetime
now = datetime.now()

print 'Request Time: %s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

reload(sys)
sys.setdefaultencoding('utf-8')

c = pycurl.Curl()
data = BytesIO()

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

if sys.argv[1] == "gene":
    gene = sys.argv[2]
    c.setopt(c.URL, "https://civic.genome.wustl.edu/api/genes/"+gene+"?identifier_type=entrez_symbol")
    c.setopt(c.WRITEFUNCTION, data.write)
    c.perform()
    dictionary = json.loads(data.getvalue())
    if sys.argv[3:]:
        parameter = sys.argv[3]
        pprint.pprint(dictionary[parameter])
    else:
        pprint.pprint(dictionary)
elif sys.argv[1] == "variant":
    variant = sys.argv[2]
    c.setopt(c.URL, "https://civic.genome.wustl.edu/api/variants/"+variant)
    c.setopt(c.WRITEFUNCTION, data.write)
    c.perform()
    dictionary = json.loads(data.getvalue())
    dictionary = convert(dictionary)
    #pprint.pprint(dictionary)
    for key, value in dictionary.items():
        print "######"
        print key
        print value

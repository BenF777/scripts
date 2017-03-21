#!usr/bin/env python
# -*- coding: utf-8 -*-


import pycurl
import pprint
import json
import sys
import unicodedata
import yaml
from io import BytesIO

c = pycurl.Curl()
data = BytesIO()

gene = sys.argv[1]

c.setopt(c.URL, "https://civic.genome.wustl.edu/api/genes/"+gene+"?identifier_type=entrez_symbol")
c.setopt(c.WRITEFUNCTION, data.write)
c.perform()
dictionary = json.loads(data.getvalue())

if sys.argv[2:]:
    parameter = sys.argv[2]
    pprint.pprint(dictionary[parameter])
else:
    pprint.pprint(dictionary)
#c.setopt(c.URL, "https://civic.genome.wustl.edu/api/genes/")
#c.setopt(c.URL, "https://civic.genome.wustl.edu/api/variant_groups")

#pprint.pprint(dictionary["records"])
#pprint.pprint(dictionary)

"""
possible parameters for gene searches:
aliases
description
sources
entrez_id
variants
variant_groups
type
lifecycle_actions
"""

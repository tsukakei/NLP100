# coding: UTF-8
import json
import codecs
with open("jawiki-country.json", "r") as wiki, open("jawiki-uk.txt", "w") as eng:
    country = wiki.readline()
    while country:
        content = json.loads(country)
        if content["title"] == u"イギリス":
            eng = codecs.lookup('utf-8')[-1](eng)
            eng.write(content["text"])
            break
        country = wiki.readline()

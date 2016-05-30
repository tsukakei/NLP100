# coding: UTF-8
import json
with open("jawiki-country.json", "r") as wiki, open("jawiki-uk.txt", "w") as eng:
    country = wiki.readline()
    while country:
        content = json.loads(country)
        if content["title"] == u"イギリス":
            eng.write(content["text"])
            break
        country = wiki.readline()

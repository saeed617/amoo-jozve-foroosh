# scripts/add_counties_provinces.py

import json
from ..models import County, Province

with open('./Province.json', 'r') as f:
    datas = json.load(f)


def run():
    for object in datas:
        province_name = object["name"]
        province = Province.objects.create(name=province_name)
        for obj in object["Cities"]:
            county = County(name=obj["name"], province=province)
            county.save()

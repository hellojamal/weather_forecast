#! /urs/bin/env python flask
# _*_ coding: utf-8

# Load city information

import json


def load_json():
    """get city code"""
    city_dict = dict()
    with open("citycode.json", encoding="utf-8") as f:
        file = json.load(f)
        for item in file:
            if item["city_code"]:
                city_dict[item["city_name"]] = item["city_code"]
    return city_dict


if __name__ == '__main__':
    print(load_json())

#! /urs/bin/env python flask
# _*_ coding: utf-8

# project pytest file


import pytest
import yaml
import requests


def get_weather_info():
    """get weather information"""
    file_path = "app/tests/city.yaml"
    with open(file_path, 'r') as f:
        # 读取内容
        weather_info = yaml.load(f, Loader=yaml.FullLoader)
    args_list = []
    for k, v in weather_info.items():
        args_list.append(v)
    return args_list


class TestWeather(object):
    """ test basic class"""

    def setup_method(self):

        print('setUp')

    def teardown_method(self):
        print('tearDown')

    @pytest.mark.parametrize('weather_info', get_weather_info())
    def test_weather1(self, weather_info):
        self.do_weather_info()


    def do_weather_info(self):
        test_city= "北京"
        result = requests.get("0.0.0.0/5000/?= %s" % test_city)
        print('search the weather of specific city',result)


if __name__ == '__main__':
    pytest.main()



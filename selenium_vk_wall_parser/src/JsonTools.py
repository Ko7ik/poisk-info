# -*- coding: utf-8 -*-

import json


class JsonTools:

    @staticmethod
    def parse(filename):
        with open(filename, 'r') as f:
            return json.loads(f.read())

    @staticmethod
    def save(data):
        with open('data.json', 'w', encoding='utf-8') as json_file:
            # Записываем данные в файл в формате JSON
            json.dump(data, json_file, indent=4)

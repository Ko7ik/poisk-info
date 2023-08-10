import json


class JsonTools:

    @staticmethod
    def parse(filename):
        with open(filename, 'r') as f:
            return json.loads(f.read())

import json


class JSONLoader:
    @staticmethod
    def load(filename):
        with open(filename, 'r') as f:
            return json.loads(f.read())

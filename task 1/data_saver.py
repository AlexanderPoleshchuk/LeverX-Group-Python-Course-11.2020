import json
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString


class JSONSaver:
    @staticmethod
    def save(data: dict, filename: str):
        with open(filename, 'w') as f:
            f.write(json.dumps(data, indent=4))


class XMLSaver:
    @staticmethod
    def save(data: dict, filename: str):
        xml = parseString(dicttoxml(data)).toprettyxml()
        with open(filename, 'w') as f:
            f.write(xml)

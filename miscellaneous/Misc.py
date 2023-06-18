import json

class Misc:

    @staticmethod
    def tryparse(test_text):
        try:
            return int(test_text)
        except:
            return False
        
    @staticmethod
    def objecttojsonfile(object,file_name):
        jsonFile = open(file_name, "w")
        objecttojson = json.dumps(object,ensure_ascii=False)
        jsonFile.write(objecttojson)
        jsonFile.close()

    @staticmethod
    def jsonfiletoobject(file_name):
        file = open(file_name)
        return json.load(file)
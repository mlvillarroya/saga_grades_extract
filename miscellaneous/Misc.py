import json

class Misc:

    @staticmethod
    def try_parse(test_text):
        try:
            return int(test_text)
        except:
            return False
        
    @staticmethod
    def object_to_json_file(object,file_name):
        jsonFile = open(file_name, "w")
        object_to_json = json.dumps(object,ensure_ascii=False)
        jsonFile.write(object_to_json)
        jsonFile.close()

    @staticmethod
    def json_file_to_object(file_name):
        file = open(file_name,mode='r')
        return json.load(file)
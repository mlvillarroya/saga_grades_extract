class Misc:

    @staticmethod
    def tryparse(test_text):
        try:
            return int(test_text)
        except:
            return False
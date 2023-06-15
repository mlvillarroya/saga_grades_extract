class DifferentPageException(Exception):
    
    def __init__(self, url, message="The URL expected is not the one found"):
        self.url = url
        self.message = message
        super().__init__(self.message)
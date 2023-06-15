class ElementNotFoundException(Exception):
    
    def __init__(self, element, message="The element searched is not been found"):
        self.element = element
        self.message = message
        super().__init__(self.message)
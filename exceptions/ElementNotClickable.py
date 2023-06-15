class ElementNotClickable(Exception):
    
    def __init__(self, element, message="The element is not clickable"):
        self.element = element
        self.message = message
        super().__init__(self.message)
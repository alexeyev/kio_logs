__author__ = 'alexeyev'

import utils

# constant values
none = 0
yellow = 1
green = 2
blue = 3
red = 4

class Model:
    """
    Hardcoded model of the solution space.
    """
    global red, yellow, blue, red

    def set_config(self):
        self.space = [
            [yellow, yellow, yellow, yellow, red, red, red, red],
            [green, green, green, green, blue, blue, blue, blue]
        ]
        self.pointer = 0

    def __init__(self):
        self.set_config(self)

    def check_code(self, code):
        error_message = "errors:"
        if not utils.check_brackets(code):
            error_message += "brackets:"
        #todo: more checks
        return error_message

    def config_after_running(self,code):
        config = (self.space, self.pointer)
        #todo: run code
        return config
__author__ = 'alexeyev'

import heuristics

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
    global red, yellow, blue, red, none

    def set_config(self):
        self.space = [
            [yellow, yellow, yellow, yellow, red, red, red, red],
            [green, green, green, green, blue, blue, blue, blue],
            [none, none, none, none, none, none, none, none],
            [none, none, none, none, none, none, none, none]
        ]
        self.pointer = 0

    def __init__(self):
        self.set_config()

    def check_code(self, code):
        # quick checks
        error_message = ""
        if not heuristics.check_brackets(code):
            error_message += "brackets:"
        if not heuristics.check_tp(code):
            error_message += "tp_wrapping:"
        if heuristics.has_k_t(code):
            error_message += "conseq_takes:"
        if heuristics.has_k_p(code):
            error_message += "conseq_puts:"
        if error_message == "":
            return "OK"
        return "errors:" + error_message + "end"

    def config_after_running(self, code):
        """
        Emulating machine's actions.
        """
        space = self.space
        ponter = self.pointer
        #todo: run code
        return space, ponter

#test
#model = Model()
#print model.check_code("TPTR(R)(8(R))P")
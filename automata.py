"""
State automata remembering stuff.
Any sort of additional actions is done by it.
"""
import re

class Automata:
    def __init__(self, rules):
        self.rules = rules
        print "Automata created."

    def process(self, line):
        for pattern in self.rules:
            match = re.search(re.compile(pattern), line)
            if match:
                print "recognized:" + line
                # hardcode begin
                if line.startswith("blocks: new record"):
                    prefix = "click:record:" + match.group(1) + ":" + match.group(2) + ":" + match.group(3)
                    if match.group(4):
                        return prefix + ":" + match.group(4)
                    return prefix
                if line.startswith("blocks: button num"):
                    num = match.group(1)
                    return "click:" + num
                    # hardcode end
            else:
                if line.startswith('blocks'):
                    print "unrecognized:" + line
        return "unrecognized"
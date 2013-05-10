__author__ = 'alexeyev'

def chunk(code):
    chunked = []
    if code <> "":
        index = 0
        buffer = ""
        while index < len(code):
            # a number is a single chunk
            if code[index].isdigit() and buffer.isdigit():
                buffer += code[index]
            else:
                chunked += [buffer]
                # managing brackets
                if code[index] == "(":
                    start = index
                    index += 1
                    stack_height = 1
                    while stack_height > 0:
                        if code[index] == "(":
                            stack_height += 1
                        if code[index] == ")":
                            stack_height -= 1
                        index += 1
                    index -= 1
                    buffer = code[start: index + 1]
                # one-symbol case
                else:
                    buffer = code[index]
            index += 1
        chunked += [buffer]
    return chunked[1:]

def remove_brackets(code):
    if code.startswith("(") and code.endswith(")"):
        return code[1:len(code) - 1]
    return code

class Tree:
    def __init__(self, code, value, postfix):
        self.id = value + postfix
        self.label = value
        self.out = []
        if code <> "":
            chunked = chunk(code)
            index = 0
            while index < len(chunked):
                if chunked[index].isdigit():
                    self.out +=\
                    [Tree(chunk(remove_brackets(chunked[index + 1])),
                        chunked[index],
                        postfix + "." + str(index))]
                    index += 2
                else:
                    self.out += [Tree("", chunked[index], postfix + "." + str(index))]
                    index += 1

    def __repr__(self):
        return str(self.label) + (str(self.out) if self.out <> [] else "")

    def to_graphviz_format(self):
        #todo:
        pass

print Tree("T2R45L31(R7L)P", "1", "")
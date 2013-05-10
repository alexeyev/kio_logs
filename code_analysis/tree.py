__author__ = 'alexeyev'
"""
    Usage of prog="dot" with graphviz representation is highly recommended.
"""
import pygraphviz

def chunk(code):
    """
        Chunking code into parts for further processing.
    """
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
    """
        If unit is wrapped in brackets, removes them.
    """
    if code.startswith("(") and code.endswith(")"):
        return code[1:len(code) - 1]
    return code

class Tree:
    def __init__(self, code, value, postfix):
        """
            Given the code, the tree is built.
        """
        self.id = "@" + value + postfix
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

    def visit(self, handler):
        """
            Traverses the nodes of a tree.
        """
        handler(self)
        for child in self.out:
            child.visit(handler)

    def to_graphviz_format(self):
        tree = pygraphviz.AGraph()

        def pusher(t):
            tree.add_node(t.id)
            tree.get_node(t.id).attr['label'] = t.label
            for child in t.out:
                tree.add_edge(t.id, child.id)
        self.visit(pusher)
        return tree
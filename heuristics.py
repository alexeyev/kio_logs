__author__ = 'alexeyev'

import re

def has_k_t(code):
    match = re.search(re.compile(".*\\D(\\d+)T.*"), code)
    if match:
        if int(match.group(1)) > 1:
            return True
    return False

def has_k_p(code):
    match = re.search(re.compile(".*\\D(\\d+)P.*"), code)
    if match:
        if int(match.group(1)) > 1:
            return True
    return False

def check_brackets_general(code, open, close):
    op_brackets = 0
    for char in code:
        if char == open:
            op_brackets += 1
        if char == close:
            op_brackets -= 1
        if op_brackets < 0:
            return False
    if op_brackets > 0:
        return False
    return  True

def check_brackets(code):
    return check_brackets_general(code, "(", ")")

def check_tp(code):
    state = ""
    for char in code:
        if char == state:
            return False
        if char == "T" or char == "P":
            state = char
    return True
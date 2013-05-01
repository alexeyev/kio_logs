__author__ = 'alexeyev'

import nltk

def check_brackets(code):
    op_brackets = 0
    for char in code:
        if char == '(':
            op_brackets += 1
        if char == ')':
            op_brackets -= 1
        if op_brackets < 0:
            return False
    return  True

def calc_tree_edit_distance(tree0, tree1):
    #todo:
    pass

def calc_code_edit_distance(old_code, new_code):
    return nltk.metrics.edit_distance(old_code, new_code)

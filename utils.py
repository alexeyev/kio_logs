__author__ = 'alexeyev'

import nltk

def calc_tree_edit_distance(tree0, tree1):
    #todo:
    pass

def calc_code_edit_distance(old_code, new_code):
    return nltk.metrics.edit_distance(old_code, new_code)

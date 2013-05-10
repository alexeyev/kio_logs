__author__ = 'alexeyev'

import nltk

def calc_code_edit_distance(old_code, new_code):
    return nltk.metrics.edit_distance(old_code, new_code)


#include <string>
import string


def reverse_string(s):
    str = ''
    for x in s:
        str = x+str
    return str

def capitalize_words(s):
    str = ''
    for x in s:
        x = x.capitalize()
        str = str+x
    return str

def remove_puncuation(s):
    n = ''
    for x in s:
        if(char in string.punctuation for char in x):
            x = n
    return s


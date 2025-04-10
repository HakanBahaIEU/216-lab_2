def count_char(s):
    return len(s)

def count_words(s):
    a = int(0)
    for x in s:
        if(x == ' '):
            a = a+1
    return a

def average_word_length(s):
    
    a = int(0)
    b = int(0)
    c = int(0)

    for x in s:
        if(x == ' '):
            c = c + a
            b = b+1
            a = 0
        else:
            a = a +1
    return c/b

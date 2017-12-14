#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# https://developers.google.com/edu/python/exercises/basic

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###


def print_words( filepath ):
    with open( filepath ) as f:
        txt = f.read()
    words = txt.split()
    count = len( words )
    print 'word count, `%s`' % count
    return


def print_top( filepath ):
    import operator, pprint
    with open( filepath ) as f:
        txt = f.read()
    words = txt.split()
    ## get counts
    word_dct = {}
    for word in words:
        if word in word_dct.keys():
            word_dct[word] +=1
        else:
            word_dct[word] = 1
    ## sort on keys: https://stackoverflow.com/a/613218
    sorted_by_val_lst_of_tuples = sorted(word_dct.items(), key=operator.itemgetter(1))
    print( 'sorted_by_val_lst_of_tuples, ```%s```' % pprint.pformat(sorted_by_val_lst_of_tuples) )
    ## grab highest 20
    start = len(sorted_by_val_lst_of_tuples) - 20
    highest_tuples = sorted_by_val_lst_of_tuples[start:]
    print( 'highest_tuples, ```%s```' % pprint.pformat(highest_tuples) )
    ## make list of words
    top_words = []
    for word_tuple in highest_tuples:
        top_words.append(word_tuple[0])
    print( 'top_words, ```%s```' % pprint.pformat(top_words) )
    top_words.reverse()
    print( 'reverse_words, ```%s```' % pprint.pformat(top_words) )
    return


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py {--count | --topcount} file'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)

if __name__ == '__main__':
    main()

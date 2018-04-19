#!/usr/bin/env python

import click

@click.command()
@click.argument('filename')


def count_words(filename):
    f = open(filename)
    file = f.readlines() # file is a list
    new_file = "\n".join(file)
    word_split = new_file.split()
    word_count = dict()
    for word in word_split:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    for word in word_count:
        print (word, word_count[word])

if __name__ == '__main__':
  count_words()

import string
import sys
import itertools

def minion(str):
    person_a_name = 'Stuart'
    person_b_name = 'Kevin'
    letter_list = [a for a in str]
    l = len(letter_list)
    vowel = ['A','E','I','O','U']
    consonants = ['Q','W','R','T','Y','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    all_word = []
    person_a_words = []
    person_b_words = []
    all_word = [letter_list[start:end+1] for start in xrange(l) for end in xrange(start, l)]
    print all_word
    for array in all_word:
        if array[0] in vowel:
            person_b_words.append(array)
    for array in all_word:
        if array[0] in consonants:
            person_a_words.append(array)
    if len(person_a_words) == len(person_b_words):
        print 'Draw'
    if len(person_a_words) > len(person_b_words):
        print person_a_name, len(person_a_words)
    if len(person_b_words) > len(person_a_words):
        print person_b_name, len(person_b_words)


def main():
    str = raw_input()
    minion(str.upper())

if __name__ == '__main__':
    main()
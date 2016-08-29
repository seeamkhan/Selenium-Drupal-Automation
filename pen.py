import string
import sys
import itertools


def minion(str):
    person_a_name = 'Stuart'
    person_b_name = 'Kevin'
    vowels = ['A','E','I','O','U']
    consonants = ['Q','W','R','T','Y','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    char_list = list(str)
    # print (char_list)
    total_char = len(char_list)
    # print (total_char)

    all_words = []
    for count in xrange(total_char):
        # temp_array = []
        for i in xrange(count, total_char):
            temp_array = []
            for j in xrange(count, i+1):
                 temp_array.append(char_list[j])
            # print temp_array
            all_words.append(temp_array)
    print all_words



def main():
    str = raw_input()
    minion(str.upper())

if __name__ == '__main__':
    main()
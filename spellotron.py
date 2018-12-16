# This Python file uses the following encoding: utf-8
"""
if you use the python command(not python3 or 3.7), it will raise an error
but the line above fixes that problem

File_name: spellotron.py
Name: Ayobami Adewale <aea8506@rit.edu>
Class: CSCI 141
Assignment: Project
Language: Python 3

"""
import sys
from solvers import *

LEGAL_WORD = "american-english.txt"
KEYBOARD_LETTERS = "keyboard-letters.txt"
alphabet = "abcdefghijklmnopqrstuvwxyz"


def american_set(filename):
    """
    Takes in the American Dictionary,
    and creates a set out of it.
    Time complexity: O(1)
    :param filename: The name of a file(American Dictionary)
    :return: a set of words
    """
    local_set = set()
    with open(filename) as inFile:
        for line in inFile:
            line = line.strip()
            local_set.add(line)
    return local_set


def adjacent_dict(filename):
    """
    Takes in the Keyboard letter,
    and creates a dictionary out of it.
    letter -> adjacent letter
    Time complexity: O(1)
    :param filename: The name of a file(Adjacent keys)
    :return: a dictionary
    """
    local_dict = dict()
    with open(filename) as inFile:
        for line in inFile:
            line = line.strip().split()
            local_dict[line[0]] = line[1:]
    return local_dict


def adjacent_letter(word):
    """
    This function loops through the word, and
    replaces every letter with its adjacent letter.
    if one of the words is in the dictionary, it
    returns the new word, if not it returns the
    old word.
    :param word: a single word(with error or not)
    :return: new word or old word depending on the original word
    """

    dicks = adjacent_dict(KEYBOARD_LETTERS)
    penis = american_set(LEGAL_WORD)
    if word in penis:
        return word
    for i in range(0, len(word)):
        orig = word[i]
        if orig in dicks:
            for bal in dicks[orig]:
                new_balls = word[0:i] + bal + word[i + 1:]
                if new_balls in penis:
                    return new_balls
    return word


def double_letter(word):
    """
    This function loops through the word, and
    temporally removes the current letter and
    search in the dictionary.
    if one of the words is in the dictionary, it
    returns the new word, if not it returns the
    old word.
    :param word: a single word(with error or not)
    :return: new word or old word depending on the original word
    """

    local_set = american_set(LEGAL_WORD)
    if word in local_set:
        return word
    for i in range(len(word)):
        new_word = word[:i] + word[i + 1:]
        if new_word in local_set:
            return new_word
    return word


def missingLetter(word):
    """
    This function loops through the word, and
    at every index, it adds the alphabet(loops through it)
    in that spot.
    if one of the words is in the dictionary, it
    returns the new word, if not it returns the
    old word.
    :param word: a single word(with error or not)
    :return: new word or old word depending on the original word
    """
    local_set = american_set(LEGAL_WORD)
    if word in local_set:
        return word
    for i in range(0, len(word)):
        for j in alphabet:
            new_word = word[:i] + j + word[i:]
            if new_word in local_set:
                return new_word
    return word


def correct(word):
    """
    This function puts together all the solver function.
    it will check each function to see if the word can be fixed
    in one fo the function. if it can't, it means the word is unknown
    and it returns 0
    :param word: each word
    :return: return 1 if the word is fixed and 0 if the word doesn't exist
    """
    #1 means fixed, 0 means non existing
    word_idk = adjacent_letter(word)
    word_missing = missingLetter(word)
    doubleletter = double_letter(word)
    local_set = american_set(LEGAL_WORD)

    if word_idk in local_set:
        return word_idk, 1
    elif word_missing in local_set:
        return word_missing, 1
    elif doubleletter in local_set:
        return doubleletter, 1
    else:
        return word, 0


def open_file(filename):
    """
    Reads a file and puts each line in a list
    :param filename: text file
    :return: list of lines
    """
    # check if it is a file
    with open(filename.strip()) as inFile:
        lst = []
        for line in inFile:
            lst.append(line)
        return lst


def main():
    """
    Using sys.argv, if the length is less than 2 or greater than 3,
    it prints out an error. if the length is 2, it will fix the inputted
    words or text file according to the mode specified.
    :return:
    """
    if len(sys.argv) < 2:
        print("Error")
        print("Usage: python3.7 spellotron.py words/lines [filename]")
    elif len(sys.argv) == 2:
        words = sys.stdin.readline()
        if sys.argv[1] == "words":
            console_helper(words, 0)
        elif sys.argv[1] == "lines":
            console_helper(words, 1)
        else:
            print("Wrong Mode")
            print("Available modes -> words/lines")
    elif len(sys.argv) == 3:
        filename = sys.argv[2]
        if sys.argv[1] == "words":
            main_helper(filename, 0)
        elif sys.argv[1] == "lines":
            main_helper(filename, 1)
    elif len(sys.argv) > 3:
        print("Error")
        print("Usage: python3.7 spellotron.py words/lines [filename]")


if __name__ == '__main__':
    main()

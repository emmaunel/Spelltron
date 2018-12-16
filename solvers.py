"""
File_name: solvers.py
Name: Ayobami Adewale <aea8506@rit.edu>
Class: CSCI 141
Assignment: Project
Language: Python 3
"""

from spellotron import *

def capital_solve(word):
    """
    This function checks if the word is in the dictionary
    and return the word and 0(which means it is in the dictionary)
    if it return 1, it is not in the dictionary
    :param word: lower case version of the original word
    :return:
    """
    temp = american_set(LEGAL_WORD)
    if word in temp:
        return word, 0
    else:
        new_word, stat = punctuation_checker(word)
        if stat == 0:
            return new_word, 0
        else:
            return new_word, 1


def punctuation_checker(word):
    """
    This function checks a word for any punctuation.
    if the word has a punctuation in the first and second index,
    it ignores that word.
    else, it strips out the punctuation and solve the word.
    :param word:
    :return: fixed word
    """
    # 0 in the dict
    # -1 doesn't existed
    if word.isdigit():
        return word, -2

    puncWord = "_-[]{}()\"@#ˆ&,.!?: ;\\'*+=/’"
    word_lst = []
    id = american_set(LEGAL_WORD)
    for i in word:
        word_lst.append(i)

    if word[0] in puncWord and word[1] in puncWord:
        return word, -2
    else:
        if word[0] in puncWord and word[len(word) - 1] in puncWord:
            correct_word, result = correct(word[1: len(word) - 1])
            return word[0] + correct_word + word[len(word) - 1], 1
        elif word[0] in puncWord:
            correct_word, result = correct(word[1:])
            return word[0] + correct_word, 1
        elif word[0] is not puncWord:
            if word_lst[-1] in puncWord:
                word_lst.pop(-1)

            if ''.join(word_lst) is not id:
                correct_word, result = correct(''.join(word_lst))
                if result == 0:
                    return word, 0
                elif result == 1:
                    return correct_word, 1

            for letter in word_lst:
                if letter in puncWord:
                    return word, -1
                else:
                    continue
        elif word[len(word) - 1] in puncWord:
            if word[:len(word) - 1] in id:
                return word, 0
            else:
                correct_word, result = correct(word[:len(word) - 1])
                return correct_word, 1
        else:
            correct_word, result = correct(word)
            if result == 0:
                return word, 0
            elif result == 1:
                return correct_word, 1


def console_helper(words, mode):
    """
    This function takes in a list of words and loops through them.
    if the word has a upper case, it changes it to lower case and
    solves it.
    It also prints the results in a pretty way.
    :param words: list of words
    :param mode: results changes based on mode(lines or words)
    :return: fixed word
    """
    line_sum = 0
    lines = words.split()
    for i in lines:
        line_sum += 1

    valid_words = []
    invalid_words = []
    corrected_words = dict()
    fuck_cs = []
    temp = american_set(LEGAL_WORD)

    for word in lines:
        if word[0].isupper():
            word_lower = word[0].lower()
            new_word = word_lower + word[1:]
            fixed_word, stats = capital_solve(new_word)
            new_word_fix = fixed_word[0].upper() + fixed_word[1:]
            if stats == 0:
                valid_words.append(new_word_fix)
            else:
                corrected_words[word] = new_word_fix
        else:
            if word in temp:
                valid_words.append(word)
                continue
            else:
                new_word, stat = punctuation_checker(word)
                if stat == 0 or stat == -1:
                    if new_word in temp:
                        fuck_cs.append(word)
                        corrected_words[word] = new_word
                    else:
                        invalid_words.append(new_word)
                elif stat == -2:
                    continue
                else:
                    fuck_cs.append(word)
                    corrected_words[word] = new_word

    if mode == 0:
        for word, corrected in corrected_words.items():
            print(word + " -> " + corrected)

        print("\n" + str(line_sum) + " words read from file.\n")

        print(str(len(fuck_cs)) + " Corrected Words")
        print(fuck_cs)

        print("\n" + str(len(invalid_words)) + " Unknown words")
        print(invalid_words)
    else:
        local_line = lines
        new_line = " ".join(local_line)
        for word in local_line:
            if word in corrected_words.keys():
                new_line = new_line.replace(word, corrected_words[word])

        print(new_line)
        print(str(line_sum) + " words read from file.\n")

        print(str(len(fuck_cs)) + " Corrected Words")
        print(fuck_cs)

        print("\n" + str(len(invalid_words)) + " Unknown words")
        print(invalid_words)


def main_helper(filename, mode):
    """
    This function takes in a list of words and loops through them.
    if the word has a upper case, it changes it to lower case and
    solves it.
    It also prints the results in a pretty way.
    :param words: list of words
    :param mode: results changes based on mode(lines or words)
    :return: fixed word
    """
    line_sum = 0
    lines = open_file(filename)
    valid_words = []
    invalid_words = []
    corrected_words = dict()
    correct = []
    temp = american_set(LEGAL_WORD)

    for line in lines:
        line = line.strip().split()
        for word in line:
            line_sum += 1
            if word[0].isupper():
                word_lower = word[0].lower()
                new_word = word_lower + word[1:]
                fixed_word, stats = capital_solve(new_word)
                new_word_fix = fixed_word[0].upper() + fixed_word[1:]
                if stats == 0:
                    valid_words.append(new_word_fix)
                else:
                    corrected_words[word] = new_word_fix
            else:
                if word in temp:
                    valid_words.append(word)
                    continue
                else:
                    new_word, stat = punctuation_checker(word)
                    if stat == 0 or stat == -1:
                        if new_word in temp:
                            correct.append(word)
                            corrected_words[word] = new_word
                        else:
                            invalid_words.append(new_word)
                    elif stat == -2:
                        continue
                    else:
                        correct.append(word)
                        corrected_words[word] = new_word
                    # if test == 0:
                    #     invalid_words.append(word)
                    # else:
                    #     correct.append(word)
                    #     corrected_words[word] = test
                    # print(test)
    if mode == 0:
        for word, corrected in corrected_words.items():
            print(word + " -> " + corrected)

        print("\n" + str(line_sum) + " words read from file.\n")

        print(str(len(correct)) + " Corrected Words")
        print(correct)

        print("\n" + str(len(invalid_words)) + " Unknown words")
        print(invalid_words)
    else:
        local = lines
        for line in local:
            line = line.split()
            for i in line:
                if i in corrected_words.keys():
                    line[line.index(i)] = corrected_words[i]
                    # new = [w.replace(i, corrected_words[i]) for w in line]
                    # print(new)
                # if i in corrected_words.keys():
                #     print(i)
                # print(i.replace(i, corrected_words[i]))
            print(' '.join(line))

        print("\n" + str(line_sum) + " words read from file.\n")

        print(str(len(correct)) + " Corrected Words")
        print(correct)

        print("\n" + str(len(invalid_words)) + " Unknown words")
        print(invalid_words)

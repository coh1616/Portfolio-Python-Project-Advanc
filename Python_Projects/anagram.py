"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dict_lst = []                 # all words in the dictionary


def main():
    read_dictionary()
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    while True:
        word = input('Find anagrams for: ')
        word = word.lower()  # Case-insensitive
        if word == EXIT:
            break
        find_anagrams(word)


def read_dictionary():
    global dict_lst
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            dict_lst.append(line)
        return dict_lst


def find_anagrams(s):
    """
    :param s: str, the word to find anagrams
    """
    s_lst = list(ele for ele in s)
    word_lst = []  # a list includes all anagrams
    helper(s, s_lst, '', word_lst)
    print('Searching...\n', len(word_lst), 'anagrams:', word_lst)


def helper(s, s_lst, new_word, word_lst):
    if len(new_word) == len(s):
        if new_word in dict_lst:  # check new_word existing in the dictionary
            if new_word not in word_lst:  # To prevent the word added repeatedly
                word_lst.append(new_word)
                print('Searching...\nFound:', new_word)
    else:
        for i in range(len(s_lst)):
            new_word += s_lst[i]
            if has_prefix(new_word):
                ch = s_lst.pop(i)
                helper(s, s_lst, new_word, word_lst)
                s_lst.insert(i, ch)
            new_word = new_word[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: str, part of newly arranged word to check if it's an anagram
    :return: bool, if it's an anagram, return True; if not, return False
    """
    for i in range(len(dict_lst)):
        if dict_lst[i].startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()

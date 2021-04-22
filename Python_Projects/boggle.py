"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dict_lst = []  # all words in the dictionary
check_duplicate = []  # Create a list to record the position of all used words


def main():
	"""
	TODO: To find all words in the checkerboard
	"""
	read_dictionary()
	input_letter = []  # A list storing user-inputted letters
	for i in range(4):
		ch = input(str(i + 1) + ' row of letters: ').lower().strip().split(' ')
		if not test(ch):
			print('Illegal input')
			break
		input_letter.append(ch)
	find_word(input_letter)


def test(lst):  # Test if the user-inputted letters are legal
	"""
	:param lst: list, letters user inputted
	:return: bool, if the length of string is not equal to 1, return False; otherwise, return True
	"""
	for i in range(len(lst)):
		if len(lst[i]) != 1:
			return False
	return True


def find_word(lst):
	"""
	:param lst:list, storing user-inputted letters
	"""
	global check_duplicate
	count = []  # Count the number of words
	word_lst = []  # To check whether the word has existed in word_lst
	#  Determine the starting letter
	for x in range(len(lst)):
		for y in range(len(lst)):
			word = lst[x][y]
			check_duplicate.append((x, y))
			helper(lst, word, word_lst, count, x, y)
			check_duplicate = []
	print(f'There are {sum(count)} words in total')


def helper(input_letter, word, word_lst, count, x, y):
	"""
	:param input_letter: list, storing user-inputted letters
	:param word: str, words can be found on the checkerboard
	:param word_lst: list, to check whether the word has existed in word_lst
	:param count:list, count the number of words
	:return:
	"""
	global check_duplicate
	if word in dict_lst and len(word) >= 4 and word not in word_lst:
		word_lst.append(word)
		count.append(1)
		helper(input_letter, word, word_lst, count, x, y)
		print(f'Found \"{word}\"')
	else:
		# word += input_letter[x][y] 原本word = ''，決定好的字在上面沒有串，會從決定好的字當中找鄰居開始串
		# Find neighbors
		for i in range(-1, 2, 1):
			for j in range(-1, 2, 1):
				position_x = x + i
				position_y = y + j
				if 0 <= position_x < len(input_letter):
					if 0 <= position_y < len(input_letter):
						if (position_x, position_y) not in check_duplicate:
							word += input_letter[position_x][position_y]
							check_duplicate.append((position_x, position_y))
							if has_prefix(word):
								helper(input_letter, word, word_lst, count, position_x, position_y)
							check_duplicate.pop()
							word = word[:-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dict_lst
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()
			dict_lst.append(line)
		return dict_lst


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for i in range(len(dict_lst)):
		if dict_lst[i].startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()

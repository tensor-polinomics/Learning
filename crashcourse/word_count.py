from pathlib import Path

def count_words(path):
	try:
		contents = path.read_text(encoding='utf-8')
	except FileNotFoundError:
		print(f"File {path} not found.")
	else:
		# Count the approximate number of words in the file
		words = contents.split() # tokenization
		num_words = len(words)
		print(f"There are approximately {num_words} words in {path} file.")

def count_specific_word(path, specific_word):
	try:
		contents = path.read_text(encoding='utf-8')
	except FileNotFoundError:
		print(f"File {path} not found.")
	else:
		# Count the occurrences of a specific word
		word_count = contents.count(specific_word.lower())
		print(f"The word '{specific_word}' occurs {word_count} times in {path} file.")
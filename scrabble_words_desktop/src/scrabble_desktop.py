import os

WORD_LIST = "twl06.txt" # New word list, updated
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, WORD_LIST)

wordlist = open(file_path).readlines()
# Get rid of newlines
wordlist = [word.lower().strip() for word in wordlist]

scores = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
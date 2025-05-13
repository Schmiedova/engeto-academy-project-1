"""
text_analyzer.py: první projekt do Engeto Online Python Akademie

author: Michaela Schmiedová
email: michaela.schmiedova@email.cz
discord: misa_47996
"""

import sys
import string
from task_template import TEXTS

USERS = {
    'bob':   '123',
    'ann':   'pass123',
    'mike':  'password123',
    'liz':   'pass123'
}

# 1) User sign-in
username = input("username:")
password = input("password:")

if username not in USERS or USERS[username] != password:
    print("unregistered user, terminating the program..")
    sys.exit()

print('-' * 40)
print(f"Welcome to the app, {username}")
print(f"We have {len(TEXTS)} texts to be analyzed.")
print('-' * 40)

# 2) Text selection
selection = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
if not selection.isdigit():
    print("invalid input, terminating the program..")
    sys.exit()
selection = int(selection)
if selection < 1 or selection > len(TEXTS):
    print("invalid input, terminating the program..")
    sys.exit()

print('-' * 40)
text = TEXTS[selection - 1]

# 3) Text analysis
words = text.split()
total_words = len(words)

titlecase = 0
uppercase  = 0
lowercase  = 0
numeric    = 0
num_sum    = 0
lengths    = {}

for w in words:
    w_clean = w.strip(string.punctuation)
    if not w_clean:
        continue

    # word length
    l = len(w_clean)
    lengths[l] = lengths.get(l, 0) + 1

    # word cathegory
    if w_clean.isdigit():
        numeric += 1
        num_sum += int(w_clean)
    elif w_clean.istitle():
        titlecase += 1
    elif w_clean.isupper() and w_clean.isalpha():
        uppercase += 1
    elif w_clean.islower():
        lowercase += 1

# 4) Statistics output
print(f"There are {total_words} words in the selected text.")
print(f"There are {titlecase} titlecase words.")
print(f"There are {uppercase} uppercase words.")
print(f"There are {lowercase} lowercase words.")
print(f"There are {numeric} numeric strings.")
print(f"The sum of all the numbers {num_sum}")

# 5) Word length frequency chart
print('-' * 40)
print("LEN| OCCURENCES |NR.")
print('-' * 40)

max_count = max(lengths.values())

for length in sorted(lengths):
    count = lengths[length]
    bar   = '*' * count
    # šířka pole pro bar je max_count
    print(f"{length:>3}|{bar:<{max_count}}|{count}")
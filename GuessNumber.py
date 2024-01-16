import random

print('Welcome New Grey hacker')

words = ['hacker', 'bounty', 'random']

secret_word = random.choice(words)
display_word = []

for letter in secret_word:
    display_word += '-'
print(display_word)

guess = input('Guess a letter?\n').lower()
print(guess) 

for position in range(len(secret_word)):
    letter = secret_word[position]
    if letter == guess:
        display_word[position] = letter
    else:
        print('Letter not in word')
print(display_word)



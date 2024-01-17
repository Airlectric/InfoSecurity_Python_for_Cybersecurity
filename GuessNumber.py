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

num = 0
game_over = False

while not game_over:
    guess = input('Guess a letter?\n').lower()
    for position in range(len(secret_word)):
        letter = secret_word[position] 
        if letter == guess:
            display_word[position] = letter
    if guess not in secret_word:
        num += 1
        guesses_left = 5 - num
        print(f'You have {guesses_left} guesses left')
        if num >= 5:
            print('You lose')
            game_over = True
    print(display_word)

    if '-' not in display_word:
        print('You Win')
        game_over = True

         





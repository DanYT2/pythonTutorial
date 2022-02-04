secret_word = 'Giraffe'
guess = ''
limit = 3
guess_count = 0
outOfGuesses = False

while guess != secret_word and not outOfGuesses:
    if guess_count < limit:
        guess = input('Guess the secret word: ')
        guess_count += 1
    else:
        outOfGuesses = True

if outOfGuesses:
    print('You lose. You are out of guesses')
else:
    print('You win. The secret word was ' + secret_word)

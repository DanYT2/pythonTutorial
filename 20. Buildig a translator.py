# All vowels are replaced with the letter 'p'

def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter in 'AEIOUaeiou':
            translation = translation + 'g'
        else:
            translation = translation + letter
    return translation


print(translate(input('Enter a phrase: ')))


# Ferb latin trial

def word_actions(phrase):
    word = ''
    translation = ''
    if phrase == 'ok' or phrase == 'okay':
        print('Action: Reach to the sky')
    if phrase == 'goodbye':
        print('Action: Blow raspberries')
    if phrase == 'bless you':
        print('Action: Blow a flugelhorn and give away your left shoe')
    if word in phrase == 'hungry':
        print('Action: Cracked knuckles')
    if word in phrase == 'hi' or 'greetings':
        print('Action: Stomp feet')
    if word in phrase == 'bye' or 'goodbye':
        print('Action: Give a slab of meat')
    if word in phrase == 'smell bad' or 'offensive smell':
        print('Action: Jazz hands')

    if len(phrase.replace(' ', '')) <= 3:
        translation = phrase
    else:

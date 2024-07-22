def hey_hangman():
    from hangman_module import stages # importing this module that I made in my system
    from hangman_module import logo3 # importing this module that I made in my system
    from hangman_module import word_list
    import random
    print('Welcome to Hangman')
    print(logo3)
    print('You have 5 lives.')
    lives = 6

    list_of_word = word_list
    chosen_word = random.choice(list_of_word)

    # making the blanks same as the length of word
    blanks = []
    for i in range(len(chosen_word)):
        blanks += '_'
    print(blanks)

    end_game = False
    while not end_game:
        guess = input('Guess a letter: ')
        for position in range(len(chosen_word)):
            if guess in chosen_word[position]:
                blanks[position] = guess
        print(blanks)
        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                end_game = True
                print('You are out of lives\nYou Loose')
                print(f'The word was {chosen_word}')
        if '_' not in blanks:
            end_game = True
            print('You Win')
        print(stages[lives])

hey_hangman()

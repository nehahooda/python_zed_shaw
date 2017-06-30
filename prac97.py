#part 2 to hangman problem
if __name__ == '__main__':
    print("welcome to Hangman")
    word= "EVAPORATE"
    guessed = "_"* len(word)
    word = list(word)
    guessed = list(guessed)
    lstguessed = []
    letter =input("guessed letter")
    while True:
        if letter.upper() in lstguessed:
            letter= ''
            print "already guessed"
        elif letter.upper() in word:
            index = word.index(letter.upper())
            guessed[index]= letter.upper()
            word[index]= '_'
        else:
            print(''.join(guessed))
            if letter is not '':
                lstguessed.append(letter.upper())
            letter = input("guess letter")
            if '_' not in guessed:
                print "you won"
                break
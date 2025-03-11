import time

import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    num = input()
    # Add input control here!
    #while(int(num)>4):
        #num = input("Scegliere un'altra alternativa: \n")


    if int(num) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        sc.handleSentence(txtIn, "Italian")
        continue

    if int(num) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        sc.handleSentence(txtIn,"English")
        continue

    if int(num) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn,"Spanish")
        continue

    if int(num) == 4:
        break



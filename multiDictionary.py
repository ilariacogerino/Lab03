import dictionary as d
import richWord as rw
import time


class MultiDictionary:

    def __init__(self):
       pass

    def printDic(self, language):
        file = open(f'./resources/{language}.txt', "r", encoding="utf-8")
        righe = file.readlines()
        for riga in righe:
            print(riga)
        pass

    def searchWord(self, words, language):
        file = open(f'./resources/{language}.txt', "r", encoding="utf-8")
        parole = [] #LISTA CHE CONTIENE TUTTE LE PAROLE DEL DIZIONARIO
        righe = file.readlines()
        for riga in righe:
            parole.append(riga.lower().strip())

        print("______________________________")
        print(f'Using cointains')
        tempo1 = self.ricercaConContains(words, parole)

        print("______________________________")
        print(f'Using Linear search')
        self.ricercaLineare(words, parole, tempo1)

        pass

    def ricercaConContains(self, words, parole):
        paroleSbagliate = []
        for word in words:
            if parole.__contains__(word) is False:
                paroleSbagliate.append(word)
        for p in paroleSbagliate:
            print(p)

        tempo1 = time.process_time()
        print(f'Time elapsed {tempo1}')
        return tempo1

    def ricercaLineare(self, words, parole, tempo1):
        paroleCorrette = []
        for word in words:
            for p in parole:
                if p==word:
                    paroleCorrette.append(word)
        paroleSbagliate = []
        for word in words:
            if word not in paroleCorrette:
                paroleSbagliate.append(word)
        for p in paroleSbagliate:
            print(p)
        tempo2 = time.process_time()
        print(f'Time elapsed {tempo2-tempo1}')
        pass

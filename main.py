import random
import time

class Translator():
    def __init__(self):
        self.eng_words = ['Hi','Bye','Task', 'Programm']
        self.sp_words = ['Hola','Adiós','Tarea', 'Programa']
        self.score = 0
        self.initialize_Translator()
    
    def initialize_Translator(self):
        print("***Welcome to English Translator App***")
        time.sleep(2)
        lang = str(input("\nChoose a language (English or Spanish): "))
        if lang == "Spanish":
            self.translate_Words("Spanish")
        elif lang == "English":
            self.translate_Words("English")

    def translate_Words(self, lang):
        if lang == "Spanish":
            mode = input("\nElige un modo: 0 - añadir nuevas palabras, 1 - entrenamiento: \n")
            while ((mode != '0') and (mode != '1')):
             mode = input("Símbolo no válido. Elija 0 o 1. (0 añade nuevas palabras, mientras que 1 permite el entrenamiento) \n")

            if mode == "1":
                print("¡Traduce tantas palabras como puedas! ¡Tienes 10 intentos!")
                for i in range(10):
                    number = random.randint(0, len(self.eng_words)-1)
                    print("Cómo deberíamos traducirlo " + self.eng_words[number])
                if input() == self.sp_words[number]:
                    print("¡¡¡Genial!!!")
                    self.score += 1
                else:
                    print("No, no del todo... La palabra correcta es - " + self.eng_words[number])
            else:
                word = str(input("Escribe una palabra en español: "))
                translate = str(input("Escriba la traducción al inglés de esta palabra: "))
                if len(word) > 0 and len(translate) > 0:
                    self.sp_words.append(word)
                    self.eng_words.append(translate)
                    print("La palabra se ha añadido correctamente")

        elif lang == "English":
            mode = str(input("\nChoose a mode: 0 - add new words: 1 - training: \n"))
            # Security check
            while ((mode != '0') and (mode != '1')):
                mode = str(input("Not valid symbol. Choose 0 or 1 (0 add new words, while that 1 allows the training)"))

            if mode == "1":
                print("Translate as many words as you can! You have a 10 attempts!")
                for i in range(10):
                    number = random.randint(0, len(self.eng_words)-1)
                    print(f"How should we translate {self.eng_words[number]}")
                if input() == self.sp_words[number]:
                    print("Great!!!")
                    self.score += 1
                else:
                    print(f"No, not entirely...The correct word is - {self.eng_words[number]}")
            
            else:
                word = str(input("Write a word in Spanish: "))
                translate = str(input("Write the English translation of this word: "))
                if len(word) > 0 and len(translate) > 0:
                    print("The word has been added correctly")

englishTranslator = Translator()
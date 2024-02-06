# Developer dictionary app

dev_dict = {
    "Linux": "Administrador de hardware que funciona en todas los sistemas operativos basados en él",
    "Software": "Bloques inmensos de código que ejecutan diversas tareas que le indiquemos",
    "Python": "Lenguaje de programación sencillo y versátil que el más usado en el mundo de la informática",
    "Script": "Conjunto de código que cumple una función determinada dentro de un software"
}

def search_in_Dictionary():
    word = str(input("Write a word that you don't understand: "))
    # To ask a word in dictionary app
    if word in dev_dict.keys():
        print(dev_dict[word])
    else:
        print("¡Error!: The word is not in dictionary.")
        word = str(input("Write a word that you don't understand: "))
        
search_in_Dictionary()

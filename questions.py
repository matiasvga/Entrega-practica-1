import random
import string

ascii_string = string.ascii_lowercase
ascii_list = [letter for letter in ascii_string]
ascii_list.append("ñ")
finish = False

categories = {"Programación": ["python", "programa", "variable", "funcion",
                               "bucle", "cadena", "entero", "lista"],
              "Paises": ["argentina", "brasil", "estados unidos", "españa", 
                         "francia", "rusia", "suiza", "japon", "australia"],
              "Sistemas operativos": ["windows", "linux", "macos", "android"],
              "Marcas de auto": ["ford", "chevrolet", "volkswagen", "renault"],
}

# Menú de selección de categoría
print("¡Bienvenido al Ahorcado! ◝ (ᵔᗜ ᵔ) ◜")
print("Seleccione una de las categorías de palabras:")
for category in categories:
    print(f"\t- {category}")

selected = input()
while not(selected in categories):
    print("Categoría inválida. Intente nuevamente:")
    selected = input()
else:
    word = random.choice(categories[selected])

# Lógica del juego
while not finish:
    guessed = []
    attempts = 6
    score = 6

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
                
        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            print(f"Puntaje: {score}")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")
        if not(letter in ascii_list):
            print("Entrada no válida.")
            print("")
            continue
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            score -= 1
            print("Esa letra no está en la palabra.")

        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        print(f"Puntaje: {score}")
    
    round = input("¿Querés otra ronda?\n - Si \n - No\n ")
    match round:
        case "SI"|"Si"|"si":
            finish = False
        case "NO"|"No"|"no":
            finish = True
print("Gracias por jugar (๑•᎑•๑)")
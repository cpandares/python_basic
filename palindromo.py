def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra_invertida == palabra:
        return True
    else:
        return False

def run():
    palabra = input("Escribe tu palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print("Es Palindromo")
    else:
        print("No es palindromo")

if __name__ == '__main__':
    run()

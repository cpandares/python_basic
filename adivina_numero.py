import random

def run():
    num_rand = random.randint(1,100)
    numero = int(input("Elige un numero entre el 1 y el 100: "))
   
    while numero != num_rand:
        if  numero < num_rand:
            print("Buscas un numero mas grande")            
        else:
            print("Buca un numero mas pequeño")
        numero = int(input("Elige otro numero: "))

    print("Ganaste")






if __name__ == '__main__':
    run()


def conversor(moneda, valor_dolar):
     pesos = input("¿Cuantos pesos " + moneda + " tienes? ")
     pesos = float(pesos)
    
     dolares = pesos / valor_dolar
     dolares = round(dolares,2)
     dolares  = str(dolares)
     print("tienes $" + dolares+ " dolares en tu cuenta")


menu = """
    Bienvenido al conversor de monedas 

    1 - Pesos colombianos
    2 - Pesos argentinos
    3 - Pesos Mexicanos

    Elige una opcion: """

    

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 5000)
elif opcion == 2:
     conversor("argentinos", 65)
elif opcion ==3:
     conversor("mexicanos", 24)
else:
    print("Opcion no valida")

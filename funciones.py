""" 
Las funciones ayudan a optimizar el código. Es decir, utilizar la menor cantidad de líneas dentro del código y evitar escribir acciones repetitivas.

Esto nos sirve para entregar un código más limpio y con buenas prácticas, que no desperdicia recursos innecesariamente. En Python, para definir funciones empleamos def.

Gracias a def, podemos “definir” funciones que emplearemos más tarde. Una función, en programación, es un grupo de instrucciones con un objetivo en particular y que se ejecuta cuando es “invocada”.

Cuando la definimos, estamos dándole un conjunto de instrucciones o un algoritmo. Al ahorrar líneas de código con funciones logramos también que la legibilidad de este sea más fácil.


"""

""" def imprimir_funciones():
    print("Mensaje 1")
    print("Mensaje 2")

imprimir_funciones()
imprimir_funciones()
imprimir_funciones()
imprimir_funciones() """


def imprimir_mensaje(param):
    print("Hola")
    print("Como esta ")
    print(param)
    print("Adios")
opcion = int(input("Elige un numero (1,2,3): "))

if opcion == 1:
    imprimir_mensaje("Escojiste 1 ")
elif opcion == 2:
    imprimir_mensaje("Escojiste 2")
elif opcion == 3:
    imprimir_mensaje("Escojiste 3")
else:
    print("Opcion no valida")
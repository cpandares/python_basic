""" 
Los diccionarios en Python son una estructura de datos mutable las cuales almacenan diferentes tipos de valores sin darle importancia a su orden. Identifican a cada elemento por una clave (Key). Se escriben entre {}.

Operaciones en diccionarios
.keys():Retorna la clave de nuestro elemento.

.values(): Retorna una lista de elementos (valores del diccionario).

.items(): Devuelve lista de tuplas (primero la clave y luego el valor).

.clear(): Elimina todos los items del diccionario.

.pop(“n”): Elimina el elemento ingresado. 
"""


def run():
    mi_diccionario = {
        'llave1' : 1,
        'llave2' : 2,
        'llave3' : 3,
    }

""" Imprimir las llaves del diccionario utilizando un bucle for. Con ‘.keys()’ estamos llamando a imprimir las llaves, no los valores. """

mi_diccionario = {
        'llave1' : 1,
        'llave2' : 2,
        'llave3' : 3,
    }
for llave in mi_diccionario.keys():
    print(llave)

if __name__ == '__main__':
    run()
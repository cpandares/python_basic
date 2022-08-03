""" Un bucle es un ciclo continuo en todos los lenguajes de programación que nos permite iterar sobre nuestros pasos: magina un contador cíclico (1,2,3,4,5,6…) donde puedes agregar un paso más sobre tu programa principal. """


def potencia(numero):
    
    potencia = 1

    while (potencia <= 10):
        
        result = numero ** potencia
        print('Potencia de {} elevado a la {} es {}'.format(numero, potencia, result))
        potencia += 1
        

def run():
    numero = int(input('Escribe el numero al cual quieres averiguarle la potencia: '))
    potencia(numero)


if __name__ == "__main__":
    run()

""" 
Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición (es decir, mientras la condición tenga el valor True). 

while condicion:
    cuerpo del bucle

Python evalúa la condición:

Si el resultado es True, se ejecuta el cuerpo del bucle. Una vez ejecutado el cuerpo del bucle, se repite el proceso (se evalúa de nuevo la condición y, si es cierta, se ejecuta de nuevo el cuerpo del bucle) una y otra vez mientras la condición sea cierta.
Si el resultado es False, el cuerpo del bucle no se ejecuta y continúa la ejecución del resto del programa.

"""
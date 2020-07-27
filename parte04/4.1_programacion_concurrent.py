#el modulo gevent provee soporte para ejecución sincrónica de alto nivel, es una api que provee métodos para facilitar la ejecución sincrónica de elementos de programa, por ejemplo funciones

#gevent.sleep(0) : cuando indicamos 0 hacemos un switch a la otra funcion que esta para ejecutarse también de forma concurrente, aqui se hace la petición de transición a otro programa
import gevent

def fn1():
    print('Inicio: fn1')
    gevent.sleep(0)
    print('Fin: fn1')

def fn2():
    print('Inicio: fn2')
    gevent.sleep(0)
    print('Fin: fn2')

def fn3():
    print('Inicio: fn3')
    gevent.sleep(0)
    print('Fin: fn3')

#de forma concurrente es decir al mismo tiempo

#gevent.spawn(fn1) : esto permite la ejecución concurrente de la diversas funciones

funciones = [gevent.spawn(fn1), gevent.spawn(fn2), gevent.spawn(fn3)]

#esto permite pasar con argumento par ala ejecución concurrente
gevent.joinall(funciones)

print()

# Funciones concurrentes con solicitud de datos del usuario:
def cuadrado():
    print('Inicio función: cuadrado')
    numero = int(input('Ingrese un número para elevar al cuadrado: '))
    gevent.sleep(0)
    resultado = numero ** 2
    print('El cuadrado es: %i' % resultado)

def cubo():
    print('Inicio función: cubo')
    numero = int(input('Ingrese un número para elevar al cubo: '))
    gevent.sleep(0)
    resultado = numero ** 3
    print('El cubo es: %i' % resultado)

gevent.joinall([gevent.spawn(cuadrado), gevent.spawn(cubo)])
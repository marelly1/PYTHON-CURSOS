#el módulo cProfile provee funcionalidad para obtener toda la informacion acerca de la ejecución completa de un programa y cuántas veces se ha ejecutado una funcion que se específica como argumento de la función run del modulo cProfile
import cProfile

def insercion():
    arr = [64, 25, 12, 22, 11]
    for i in range(1, len(arr)): 
    
        key = arr[i] 
    
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key


cProfile.run('insercion()')

# ncalls  : especifica el número de llamadas que se han efectuado
# tottime : el tiempo total que se ha necesitado por la ejecución de la función
# percall : es un cociente de tottime entre ncalls (tottime/ncalls)
# cumtime : es el timpo total para la invocación de otras funciones por ejemplo range() o len()
# percall : es el cociente de cumtime entre percall (cumtime/percall)
# filename:lineno(function) : se refiere al lugar donde se ha hecho la invocación de la función

'''
Así se muestra el mandar a imprimir
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 3.2_perfilamiento_ejecucion_codigo.py:4(insercion)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects '''
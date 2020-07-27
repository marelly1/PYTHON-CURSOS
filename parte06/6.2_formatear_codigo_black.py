import numpy

numeros = [1, 4, 2, 3]

puntajes = {"Edward": 2, "Daniela": 3, "Oliva": 5}

arreglo = numpy.zeros((2, 6), dtype=numpy.int64)

print(
    "arreglo = ",
    arreglo,
    "\n\n",
    "list numeros = ",
    numeros,
    "\n\n",
    "puntajes = ",
    puntajes,
    "\n",
)

#Asi es como se debe hacer a través de la terminal para que 
#el archivo desordenado se ordene automaticamente utilizando 
#black

''' 
E:\PYTHON-CURSOS>black
"black" no se reconoce como un comando interno o externo,
programa o archivo por lotes ejecutable.

E:\PYTHON-CURSOS>Scripts\activate

(PYTHON-CURSOS) E:\PYTHON-CURSOS>black
No Path provided. Nothing to do 😴

(PYTHON-CURSOS) E:\PYTHON-CURSOS>black parte06\6.2_formatear_codigo_black.py
reformatted parte06\6.2_formatear_codigo_black.py
All done! ✨ 🍰 ✨
1 file reformatted.

(PYTHON-CURSOS) E:\PYTHON-CURSOS> 
'''
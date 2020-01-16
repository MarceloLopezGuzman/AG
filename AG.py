import datetime
from random import *

def main():
	
	tam_poblacion = 4  # En total serán 44
	bits = 12
	generaciones = 6
	contNumGen = 0
	fitnessGeneracion = 0
	ftg0 = 0
	aux = 0
	mejor_generacion = 0
	probMuatacion = 1/tam_poblacion

	poblacion = []
	nueva_gen = []

	print("\n Generación 0")
	poblacion = crear_poblacion(tam_poblacion,bits)
	for x in poblacion:
		ftg0 = ftg0 + calcFitness(x)
		print(str(x) + " " + str("Fitness: ") + str(calcFitness(x)))
	print("Fitness Total de la Generación 0  =  ", str(ftg0))
		
	# Inicia el Cruce de genes depués de la Generacion 0
	while (generaciones != 0):	#aqui se eligen a las parejas para el crossover
		contNumGen += 1
		nueva_gen = vaciar_lista(nueva_gen)

		for i in range(0,tam_poblacion):
			nueva_gen.append(crossover(seleccion(poblacion),seleccion(poblacion)))
		print("\nGeneración: ", (str(contNumGen)), "\n")
		
		# Es lo que aparece al lado de las cadenas
		for lista_nueva_gen in nueva_gen:
			fitnessGeneracion = fitnessGeneracion + calcFitness(lista_nueva_gen)
			print((str(lista_nueva_gen) + " Fitness = " + str(calcFitness(lista_nueva_gen))))
		print(("Fitness de la Generacion " + str(contNumGen) + ": " + str(fitnessGeneracion)))

		if fitnessGeneracion > aux:
			mejor_generacion = contNumGen
			aux = fitnessGeneracion
		fitnessGeneracion = 0
		#copiar nueva_gen a poblacion
		for posicion in range(0,tam_poblacion):
			poblacion[posicion] = nueva_gen[posicion]
		generaciones -= 1
	print(("\nMejor Generacion: " + str(mejor_generacion)))
	

def crear_poblacion(medida, elementos):
	poblacion = []
	pool = []
	inicio = 0
	primer = 1

	for x in range(inicio,medida):
		pool = llenarPoblacion(elementos)
		poblacion.append([])
		for y in range(inicio,elementos):
			poblacion[x].append(pool.pop(randint(inicio,len(pool)-1)))

	return poblacion

def llenarPoblacion(magnitud):
	pool = []
	for x in range(0,magnitud):
		pool.append(0)
		pool.append(1)
	return pool


def calcFitness(individuo):
	aptitud = 0
	for x in range(0,len(individuo)):
		if individuo[x] == x:
			aptitud += 1
	return aptitud

def seleccion(poblacion):
	ruleta = []
	boleto = 0

	for individuo in poblacion:
		boleto = calcFitness(individuo)
		for x in range(0,boleto + 1):
			ruleta.append(individuo)
	return choice(ruleta)

def crossover(ind1, ind2):
	A = []
	B = []
	Descendencia = []

	proba = random()
	punto = randint(0,len(ind1)) #Aca puede se ind1 o 2 tienen el mismo tamaño de la cadena
	print(proba, "----------------------------------------------------")
	#punto = random.randint(1, 23)
	
	if proba > 0.65 :
		A = ind1
		B = ind2
	else:
		A = ind2
		B = ind1

	if punto == 0:	#Si el punto de crossover esta en los
		punto += 1	#extremos, lo mueve una casilla.
	elif punto == len(ind1):
		punto -= 1
	
	if proba > 0.3 :
		for x in range(0,punto):
			Descendencia.append(A[x])
		for y in range(punto,len(ind2)):
			Descendencia.append(B[y])
		Descendencia = mutacion(Descendencia)
		
		return Descendencia
	else:
		A = mutacion(A)
		return A

def vaciar_lista(lista):
	if len(lista) > 0:
		for elemento in range(0,len(lista)):
			lista.pop()
	return lista

def mutacion(individuo):
	probMuatacion = random()
	mutar1 = randint(0,len(individuo)-1)
	mutar2 = randint(0,len(individuo)-1)
	aux = 0

	if probMuatacion < 0.05 :
		print("Hubo mutacion en: " + str(individuo))
		values = ','.join(str(v) for v in (individuo))
		binario = values.replace(",","")
		binDecimal = (int(str(binario), 2))
		valConsiderar = binDecimal * 0.1
		print("Valor puntuado de la mutación:  ", valConsiderar)

		if valConsiderar > 59:
			print("Mutación Falló alv")
			pass
		else:
			individuo[mutar1] = randint(0,len(individuo)-1)
			pass
	return(individuo)

main()

#Programa por Hugo Gonzalez
#10 palabras mas repetidas en un texto
#Para usarlo, debera crear un txt (claves.txt) que contenga el texto

def repeticiones(palabra, lista):
	cont = 0
	for i in lista:
		if palabra == i:
			cont += 1
	return cont

def main():
	linea3 = []
	with open('claves.txt') as f:
		for linea in f:
			linea2 = linea.split()
			if linea2 is not None:
				for i in linea2:
					linea3.append(i)

	final = []
	word = []
	repeticion = []
	for x in linea3:
		palabra = x
		if x not in word:
			word.append(palabra)
			repeticion.append(repeticiones(palabra, linea3))
	for j in range(len(repeticion)):
		final = list(zip(word,repeticion))

	
	res = sorted(final, key = lambda x: x[1], reverse=True)
	for i in range(10):
		print (res[i])

main()


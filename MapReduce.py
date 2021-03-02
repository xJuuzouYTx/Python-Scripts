#Funcion para ver las veces que una palabra se repite en una lista
def repeticiones(palabra, lista):
	#empezamos con 0 repeticiones
	cont = 0
	#Recorro la lista, i es un elemento dentro de la lista, es decir una palabra
	for i in lista:
		#Comparo la i con la palabra que estoy buscando
		if palabra == i:
			#Sumo 1 repeticion en caso de que las palabras coincidan
			cont += 1
	#retorno el contador
	return cont

def main():
	#Lista que contendrá la lista con las palabras obtenidas del txt
	linea3 = []
	#Leo el archivo txt
	with open('claves.txt') as f:
		#Recorro cada linea del txt
		for linea in f:
			#Separo cada cadedena por espacios, cada linea es una lista, y cada palabra un elemento en esta
			linea2 = linea.split()
			print (linea2)
			#Filtro las listas vacias
			if linea2 is not None:
				#Recorro las listas y creo una lista mas grande con los elementos de todas las listas
				for i in linea2:
					linea3.append(i)

			print(linea3)

	valores = []

	#Palabra a buscar en la lista
	palabra = 'ambiental'
	#Llamo a la funcion y le paso la palabra
	print(palabra,',',repeticiones(palabra, linea3))

main()


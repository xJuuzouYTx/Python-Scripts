import math
from colorama import init, Fore, Back, Style
init()
letra = 'y'
print(Fore.WHITE+Back.BLUE+"DESARROLLADO POR HUGO GONZALEZ"+Back.RESET)
def pFijo():
	n=int(input('Numero de iteraciones\n'))
	x = float(input('Valor de Inicial\n'))
	for i in range (0, n):
		var = math.exp(-1*(x))
		if (var==x):
			break
		x = var
		print (x, 'i: ',i)
	raiz = x
	print ('Raiz: ',x)
pFijo()
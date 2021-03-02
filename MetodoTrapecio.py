import math
from colorama import init, Fore, Back, Style
init()
letra = 'y'
print(Fore.WHITE+Back.BLUE+"DESARROLLADO POR HUGO GONZALEZ"+Back.RESET)
print()
def main():
	a=2
	b = 7
	print(Fore.YELLOW+"Integral de e^x^2  a=",2," b=",7)
	divisiones=int(input('Numero Divisiones:\n'))
	Dx = (b-a)/divisiones
	Dx2 = Dx/2
	sumatoria = 0
	Iniciosumatoria = math.exp(a**2)
	cont = 0
	for i in range(a,divisiones):
		varX = (Dx+a+cont)
		cont = cont+Dx
		sumatoria = sumatoria+2*(math.exp(varX**2))
	FinSumatoria = math.exp((b)**2)
	print (Fore.BLUE+"Resultado: ",(Iniciosumatoria+sumatoria+FinSumatoria)*Dx2)
	print()
while letra=='y':
	main()

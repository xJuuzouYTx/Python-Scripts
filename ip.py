n = 16
cont = 1
for i in range(0,256,n):
	print(str(cont)+':',i,'-', i+n-1)
	cont+=1
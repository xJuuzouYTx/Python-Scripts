
TnuevoPaciente = 5
Trevision = 7
espera = []
revision = []
inicioh = 9
iniciom = 0
finalh = 11
strInicioM = ''
strInicioH = ''

letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
boo = True
contLetras = 0
while boo:
	if iniciom%TnuevoPaciente == 0:
		if (len(espera)==0) and (len(revision)==0):
			espera.append("-")
			revision.append(letras[contLetras])
		elif (len(espera)>0) and (len(revision)>0):
			if "-" in espera:
				espera.pop(0)
			espera.append(letras[contLetras])
		
		strInicioM = str(iniciom)
		strInicioH = str(inicioh)
		if (len(strInicioM))==1 and (len(strInicioH))==1 :
			print("0"+str(inicioh)+":"+"0"+str(iniciom),espera, revision)
		elif (len(strInicioM))==1:
			print(str(inicioh)+":"+"0"+str(iniciom),espera, revision)
		elif (len(strInicioH))==1:
			print("0"+str(inicioh)+":"+str(iniciom),espera, revision)
		else:
			print(str(inicioh)+":"+str(iniciom),espera, revision)
		contLetras += 1
	if iniciom%Trevision == 0 and iniciom!=0:
		if len(espera)>0:
			revision.pop()
			revision.append(espera[0])
			espera.pop(0)
		if (len(espera)==0) and (len(revision)>0):
			espera.append("-")

		strInicioM = str(iniciom)
		strInicioH = str(inicioh)
		if (len(strInicioM))==1 and (len(strInicioH))==1 :
			print("0"+str(inicioh)+":"+"0"+str(iniciom),espera, revision)
		elif (len(strInicioM))==1:
			print(str(inicioh)+":"+"0"+str(iniciom),espera, revision)
		elif (len(strInicioH))==1:
			print("0"+str(inicioh)+":"+str(iniciom),espera, revision)
		else:
			print(str(inicioh)+":"+str(iniciom),espera, revision)

	if iniciom > 63:
		iniciom = 3
		inicioh +=1
	if (inicioh == finalh ):
		boo = False
	iniciom+=1


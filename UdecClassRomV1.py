import urllib, json
import requests
from bs4 import BeautifulSoup
import urllib3
from pathlib import Path
from colorama import init, Fore, Back, Style
import os
import sys

def asignaturas():
	asignaturas = []
	asignaturasId = []
	for i in range(len(materiasVerificadas)):
		var = str(materiasVerificadas[i])
		var2 = var.split('</a></h4>, <h4 class="h5"><a class="" ')
		var3 = var2[0].split('<h4 class="h5"><a class="" href="https://virtual.ucundinamarca.edu.co/course/view.php?id=')
		values = var3[1].split('">')
		values2 = values[1].split('</a></h4>')
		iD = values[0]
		curso = values2[0]
		asignaturas.append(curso)
		asignaturasId.append(iD)
	return asignaturas, asignaturasId

def temas1():
	temas1 = []
	for i in range(len(temas)):
		var = str(temas[i])
		var2 = var.split('[<span class="media-body">')
		var3 = var2[1].split('</span>]')
		temas1.append(var3[0])
	return temas1

def asignaciones1():
    asignaciones1 = []
    tipoAsignacion = []
    nueva_asignacion =[]
    for i in range(len(asignaciones)):
    	var = str(asignaciones[i])
    	var2 = var.split('</span></span>,')
    
    	for j in range(len(var2)):
    		var3 = var2[j].split('<span class="instancename">')
    		#print (var3)
    		var4 = var3[1].split('<span class="accesshide"> ')
    		var5 = var4[1].split('</span></span>')
    		#print (nueva_asignacion)
    		tipoAsignacion.append(var5[0])
    		asignaciones1.append(var4[0])
    return asignaciones1, tipoAsignacion


init()


print(Fore.WHITE+Back.BLUE+"                              "+Back.RESET)
print(Fore.WHITE+Back.BLUE+"DESARROLLADO POR HUGO GONZALEZ"+Back.RESET)
print(Fore.WHITE+Back.BLUE+"                              "+Back.RESET)

payload = {'username':'username', 'password':'password'}
url = "https://virtual.ucundinamarca.edu.co/login/index.php"

materias = []
materiasVerificadas = []
quitarEtiqueta=[]
materias2 = []
norepetir = ''
temas = []
asignaciones = []

with requests.Session() as s:
    p = s.post(url, data=payload)
    html = BeautifulSoup(p.text, "html.parser")
    entradas = html.find_all('h4', {'class': 'h5'})
    for i, entrada in enumerate(entradas):
        if entrada != norepetir:
            norepetir = entrada
            materias.append(entrada)

    for i in materias:
        if i not in materiasVerificadas:
            materiasVerificadas.append(i)
    asignaturas1, asignaturasId1 = asignaturas()
    if len(asignaturas1) < 1:
        print("No hay asignaciones")
        sys.exit()
    print(Fore.YELLOW+'>>SELECCIONE UNA ASIGNATURA')
    for i in range(len(asignaturas1)):
    	print ('[',i,']','=>',asignaturas1[i])
    curso = int(input('>'))
    idCurso = asignaturasId1[curso]
    print ('====================================================================')
    print ('Accediendo a: ',asignaturas1[curso])
    print ('====================================================================')
    urlCurso = "https://virtual.ucundinamarca.edu.co/course/view.php?id="+idCurso
    req = s.get(str(urlCurso))
    cont = 0
    status_code = req.status_code
    if status_code == 200:
        html = BeautifulSoup(req.text, "html.parser")
        entradas = html.find_all('a', {'class': 'list-group-item'})
        for i, entrada in enumerate(entradas):
            titulo = entrada.find_all('span', {'media-body'})
            enlace = entrada.find_all('title=', 'tab_content')
            if titulo:
            	temas.append(titulo)
            	cont += 1        
        listatemas = temas1()
        print(Fore.YELLOW+'>>SELECCIONE UN TEMA')

        for i in range(len(listatemas)):
        	if i != 0:
        		print ('[',i,']','=>',listatemas[i])
        temaSeleccionado = int(input('>'))
        print ('====================================================================')
        print ('Accediendo a: ',listatemas[temaSeleccionado])
        print ('====================================================================')
        idCursoStr = str(idCurso)
        print(Fore.YELLOW+'>>TIENE LAS SIGUIENTES ASIGNACIONES')
        temaSeleccionadoStr = str(temaSeleccionado+1)
        urlTema = "https://virtual.ucundinamarca.edu.co/course/view.php?id="+idCursoStr+'&'+'section='+temaSeleccionadoStr
        reqTema = s.get(str(urlTema))
        status_code = reqTema.status_code
        codigoAsignacion = []
        if status_code == 200:
            html = BeautifulSoup(reqTema.text, "html.parser")
            entradas1 = html.find_all('li', {'class': 'activity'})
            for i, entrada1 in enumerate(entradas1):
                asignaciones = html.find_all('span', {'instancename'})
                codigo = html.find_all('div', {'activityinstance'})
            try:
                asignaciones2 = str(entradas1).split('onclick="window.open(\'')
                asignaciones3 = asignaciones2[1].split("', '',")
            except:
            	print()
            try:
                var = str(codigo)
                #print (entradas1)
                var2 = var.split('href="')

                for j in range(len(var2)):
                    var3 = var2[j].split('" onclick="">')
                    codigoAsignacion.append(var3[0])
                nuevo_codigoAsignacion = []
                for k in range(len(codigoAsignacion)):
                    if k > 0:
                        nuevo_codigoAsignacion.append(codigoAsignacion[k])
                #print (nuevo_codigoAsignacion)
                asignacion, tipoAsignacion = asignaciones1()  
                for j in range(len(asignacion)):
                    print ('[',j,']  (',tipoAsignacion[j],')','==>',asignacion[j])
                print(Fore.YELLOW+'Digite el numero de asignacion:')
                asignacionSeleccionada = int(input('>'))
                asignacionSeleccionadaStr = str(asignacionSeleccionada)
                print ('====================================================================')
                print ('Accediendo a: ',asignacion[asignacionSeleccionada])
                print ('====================================================================')
                urlAsignacion = nuevo_codigoAsignacion[asignacionSeleccionada]
                urlAsignacionStr = str(urlAsignacion)
                #print(urlAsignacion)
                try:
                    urlAsignacion3 = str(asignaciones3[0])
                    urlAsignacion2 = urlAsignacion3.replace('amp;','')
                except:
                    urlAsignacion2 = str(asignacion)
                reqAsignacion = s.get(str(urlAsignacionStr))
                status_code = reqAsignacion.status_code
                if status_code == 200:
                    html = BeautifulSoup(reqAsignacion.text, "html.parser")
                    foro = html.find_all('table', {'class': 'forumheaderlist'})

                    if tipoAsignacion[asignacionSeleccionada] == 'Foro':
                        print ('Actualmente no hay soporte para foros')
                    elif tipoAsignacion[asignacionSeleccionada] == 'Archivo':
                        try:
                            myfile = s.get(urlAsignacion)
                            myfile3 = s.get(urlAsignacion2)
                            if not myfile.history:
                                #print ("Request was redirected")
                                for resp in myfile.history:
                                    #print (resp.status_code, resp.url)
                                    #print ("Final destination:")
                                    #print (myfile.status_code, myfile.url)
                                    myfile2 = s.get(myfile.url)
                                    home = str(Path.home())
                                    #print(home)
                                    open(home,'/','file.pdf', 'wb').write(myfile2.content)
                                    print("**************************************************")
                                    print('El archivo se guardo en ',home,'\Downloads')
                            if myfile3.history:             
                                myfile4 = s.get(myfile3.url)
                                home = str(Path.home())
                                ruta = home+'\file2.pdf' 
                                '''print(ruta)
                                print("**************************************************")
                                open(home,ruta, 'wb').write(myfile4.content)
                                print("**************************************************")
                                print('El archivo se guardo en ',home,'\Downloads')'''
                                print ('El archivo se encuentra en la siguiente ruta:')
                                print(myfile3.url)
                            else:
                                print("pagina")
                        except:
                            print('Error al descargar')
                    elif tipoAsignacion[asignacionSeleccionada] == 'Carpeta':
                        print('Soporte Carpeta')
                    elif tipoAsignacion[asignacionSeleccionada] == 'Pagina':
                        print ('pagina')
                    elif tipoAsignacion[asignacionSeleccionada] == 'Tarea':
                        print ('Tarea')
                    else:
                        print('Desconocido:'+tipoAsignacion[asignacionSeleccionada])
                else:
                    print (status_code)

            except:
                try:
                    urlTema = "https://virtual.ucundinamarca.edu.co/course/view.php?id="+idCursoStr+'&'+'section='+temaSeleccionadoStr
                    reqTema = s.get(str(urlTema))
                    html = BeautifulSoup(reqTema.text, "html.parser")
                    entradas1 = html.find_all('div', {'class': 'summary'})
                    texto1 = str(entradas1[0]).split('<div class="summary"><div class="no-overflow">')
                    indice = texto1[1]
                    indice1 = indice[1]
                    indice2 = indice[2]
                    h = indice1+indice2
                    print('--TEXTO--')
                    if h == 'h1':
                        var = indice.split('<h1>')
                        var2 = str(var[1]).split('</h1></div></div>')
                        print(var2[0])
                    elif h == 'h2':
                        var = indice.split('<h2>')
                        var2 = str(var[1]).split('</h3></div></div>')
                        print(var2[0])
                    elif h == 'h3':
                        var = indice.split('<h3>')
                        var2 = str(var[1]).split('</h3></div></div>')
                        print(var2[0])
                    elif h == 'h4':
                        var = indice.split('<h4>')
                        var2 = str(var[1]).split('</h4></div></div>')
                        print(var2[0])
                    else:
                        var = indice.split('<h5>')
                        var2 = str(var[1]).split('</h5></div></div>')
                        print(var2[0])
                except:
                    print('No hay asignaciones')
        else:
    	    print (status_code)
    else:
    	print (status_code)

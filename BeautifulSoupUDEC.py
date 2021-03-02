from bs4 import BeautifulSoup
import requests
from constants import *

payload = {'username':'username', 'password':'password'}
url = "https://virtual.ucundinamarca.edu.co/login/index.php"

tagsH = []
tagsHsinRepetir = []
enlaces = []
temasCurso = []
enlacesTemas = []
with requests.Session() as solicitud:
	print (requests.Session())
	respuesta = solicitud.post(url, data=payload)
	contenido = BeautifulSoup(respuesta.content, "html.parser")
	div = contenido.find("div", {"id": "pc-for-in-progress"})
	for tag in div.find_all("h4", {"class": "h5"}):
		tagsH.append(str(tag.text))
		link = tag.a['href'] 
		for i in tagsH:
			if i not in tagsHsinRepetir:
				tagsHsinRepetir.append(i)
				if link not in enlaces:
					enlaces.append(str(link))

	print("Tiene los siguientes cursos:")
	for curso in tagsHsinRepetir:
		print(curso)
	print("Seleccione un curso: ")
	cursoSeleccionado = 2
	temas = solicitud.get(enlaces[cursoSeleccionado])
	temas = BeautifulSoup(temas.content, "html.parser")
	tema = temas.find_all("ul", {"class": "nav"})
	for tem in tema:
		for litag in tem.find_all('li'):
			texto = litag.text.strip()
			temasCurso.append(texto)
		for atag in tem.find_all('a',href=True):
			enlacesTemas.append(atag['href'])

	print("Tiene los siguientes Temas:")
	for team in temasCurso:
		print(team)
	print("Seleccione un Tema: ")
	temaSeleccionado = 1
	tarea = solicitud.get(enlacesTemas[temaSeleccionado])
	tarea = BeautifulSoup(tarea.content, "html.parser")
	div = tarea.find("div", {"class":"content"})
	tarea = div.find_all("ul", {"class": "section"})
	for t in tarea:
		for task in t.find_all('li',{"class": "activity"}):
			print(task)
    
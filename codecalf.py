#!/usr/bin/env/ python
import random as rd
import csv
def variables_iniciales():
	nombres = 'Maria,Luis,Rodrigo,Monica,Ruben,Gaby,Irma,Ofelia'.split(',')
	apellidos = 'Fernandez,Carmona,Marquez,Santana,Lopez,Nunez,Ortega,Mancera'.split(',')
	materias = 'Fisica,Espanol,Matematicas,Quimica,Geografia'.split(',')
	puntajes_max =[20,20,30,50,50]
	return nombres, apellidos, materias, puntajes_max
def nombre_completo(nombres=str,apellidos=str):
	full_names = []
	for i in range (len(nombres)):
		full_name = nombres[i] + ' ' + apellidos[i]
		full_names.append(full_name)
	return full_names
def calificaciones(puntajes_max,full_names):
	calif = []
	for name in full_names:
		calif_alumno=[]
		for i in range(len(puntajes_max)):
			nota = puntajes_max[i]
			calif_rd = rd.randint(0,nota)
			calif_alumno.append(calif_rd)
		calif.append(calif_alumno)
	return calif

def creacion_de_datos(full_names, materias, calif):
	lista = []

	for x in range (len(full_names)):
		dictionario_mamalon={'Nombre':'', 'Fisica':'', 'Español':'','Matematicas':'','Quimica':'', 'Geografia': ''}
		name = full_names[x]
		calificacion_estudiante = calif[x]
		if name not in dictionario_mamalon.keys():
			dictionario_mamalon['Nombre'] = name
			dictionario_mamalon['Fisica'] = calificacion_estudiante[0]
			dictionario_mamalon['Español'] = calificacion_estudiante[1]
			dictionario_mamalon['Matematicas'] = calificacion_estudiante[2]
			dictionario_mamalon['Quimica'] = calificacion_estudiante[3]
			dictionario_mamalon['Geografia'] = calificacion_estudiante[4]
			lista.append(dictionario_mamalon)

	return lista
def sheet_card(lista):
	keys = ['Nombre', 'Fisica', 'Español', 'Matematicas','Quimica', 'Geografia']
	with open('reporte_calificacion.csv', 'w') as file:
		writer = csv.DictWriter(file, fieldnames=keys)
		writer.writeheader()
		writer.writerows(lista)
def main():
	nombres, apellidos, materias, puntajes_max = variables_iniciales()
	full_names =nombre_completo(nombres, apellidos)
	calif =calificaciones(puntajes_max,full_names)
	lista = creacion_de_datos(full_names,materias, calif)
	sheet_card(lista)
if __name__ == '__main__':
	main()

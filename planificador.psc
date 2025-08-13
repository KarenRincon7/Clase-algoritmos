Algoritmo planificador 
	definir hora Como Entero
	Escribir "que hora es hoy"
	leer hora
		si hora mod 8=0 entonces 
			escribir hora, " Tiene que comer"//cada 8 horas el usuario tiene que comer
		FinSi
		si hora= 12 Entonces
			escribir hora, " Tiene que ir aestudiar"
		FinSi
		si hora= 18
			Escribir hora, " Es hora de ir al gimnasio"
		FinSi
		si hora > 20 o hora <8
			Escribir hora," deberias estar durmiendo"
		sino 
			Escribir "estas libre"
		FinSi
FinAlgoritmo

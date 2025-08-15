Algoritmo cronograma
	Escribir "----- Cronograma de hoy ----"
	Repetir
		libre<-Verdadero
		Escribir "¿Que hora es?"
		Leer num
		Si num >= 25 Entonces
            Escribir "La hora que ha ingresado no es valida"
        Sino
            libre <- Verdadero  // variable para controlar si está libre
			Segun num Hacer
				12,13,14,15:
					Escribir "deberia estar estudiando"
					libre<-falso
				4,24:
					Escribir "usted deberia estar durmiendo"
					libre<-falso
				De Otro Modo:
					si num mod 4=0
						Escribir "deberia comer algo"
						libre<-falso
					FinSi
					Si num>0 y num<6 o num>20 Y num<=24 Entonces
						Escribir 'Usted deberia estar durmiendo'
						libre<-falso
					FinSi
			Fin Segun
			si libre = Verdadero Entonces
				escribir "esta libre"
			FinSi
		FinSi
	Hasta Que num >= 25
FinAlgoritmo
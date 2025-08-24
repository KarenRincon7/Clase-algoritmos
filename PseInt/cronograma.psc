Algoritmo cronograma
	Escribir "----- Cronograma de hoy ----"
	Repetir // bucle, se repite hasta que cumple la condicion >= 25 o menor <=0//
		libre<-Verdadero
		Escribir "¿Que hora es?"
		Leer num
		Si num >= 25 o num <=0 Entonces
            Escribir "La hora que ha ingresado no es valida"
        Sino
            libre <- Verdadero  // variable para controlar si esta libre
			Segun num Hacer // si el numero que ingresaste es uno de los dados hacer lo siguiente//
				12,13,14,15:
					Escribir "deberia estar estudiando"
					libre<-falso
				4,24:
					Escribir "usted deberia estar durmiendo"
					libre<-falso
				De Otro Modo: // si no es ninguno de esos numeros hacer lo siguiente//
					si num mod 4=0 //cada 4 horas comer algo,exeptuando 4, 24 colocados en el segun//
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
	Hasta Que num >= 25 o num <= 0
FinAlgoritmo

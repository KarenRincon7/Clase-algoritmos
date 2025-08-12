Algoritmo clavem
	intentos=3
	Clavecorrexta = 1234
	leer clave
	Mientras clave <> Clavecorrexta y intentos <=4 Hacer
		Escribir "escribe otra vez tu contraseña" 
		leer Clave
		intentos <- intentos+1
	Fin Mientras
	si Clave = Clavecorrexta Entonces
		escribir "bienvenido"
	SiNo
		escribir "lo sentimos, estas bloqueado"
	FinSi
FinAlgoritmo


Algoritmo muralla// es un codigo en el cual voy a utilizar variable
	definir num Como Entero
	pares <- 0
	impares <- 0
	para i <- 1 hasta 10 con paso 1
		leer num 
		si num Mod 2=0 Entonces//primera condicion
			pares <- pares+1
		sino //segunda condicion
			impares <- impares +1
		FinSi
	FinPara
	escribir "pares:", pares, "  impares:", impares
FinAlgoritmo

Algoritmo mostrar_segmentos_while
	
	Definir a, b, c, d, e, f, g Como Entero
	Dimension a[10], b[10], c[10], d[10], e[10], f[10], g[10]
	a[1] <- 1; b[1] <- 1; c[1] <- 1; d[1] <- 1; e[1] <- 1; f[1] <- 1; g[1] <- 0  
	a[2] <- 0; b[2] <- 1; c[2] <- 1; d[2] <- 0; e[2] <- 0; f[2] <- 0; g[2] <- 0  
	a[3] <- 1; b[3] <- 1; c[3] <- 1; d[3] <- 0; e[3] <- 1; f[3] <- 0; g[3] <- 1  
	a[4] <- 1; b[4] <- 1; c[4] <- 1; d[4] <- 1; e[4] <- 0; f[4] <- 0; g[4] <- 1  
	a[5] <- 0; b[5] <- 1; c[5] <- 1; d[5] <- 0; e[5] <- 0; f[5] <- 1; g[5] <- 1  
	a[6] <- 1; b[6] <- 1; c[6] <- 1; d[6] <- 1; e[6] <- 0; f[6] <- 1; g[6] <- 1  
	a[7] <- 1; b[7] <- 0; c[7] <- 1; d[7] <- 1; e[7] <- 1; f[7] <- 1; g[7] <- 1  
	a[8] <- 1; b[8] <- 0; c[8] <- 1; d[8] <- 0; e[8] <- 0; f[8] <- 1; g[8] <- 1  
	a[9] <- 1; b[9] <- 1; c[9] <- 1; d[9] <- 1; e[9] <- 1; f[9] <- 1; g[9] <- 1  
	a[10] <- 1; b[10] <- 1; c[10] <- 1; d[10] <- 0; e[10] <- 0; f[10] <- 1; g[10] <- 1 
	
	Definir segmento Como Entero
	segmento <- 1
	
	Mientras segmento <= 10 Hacer
		Escribir "Número ", segmento - 1, " = A=", a[segmento], " B=", b[segmento], " C=", c[segmento], " D=", d[segmento], " E=", e[segmento], " F=", f[segmento], " G=", g[segmento]
		segmento <- segmento + 1
	FinMientras
	
FinAlgoritmo

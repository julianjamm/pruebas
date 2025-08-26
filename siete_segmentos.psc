Algoritmo siete_segmentos 
	a = 1
	b = 1
	c = 1
	d = 1
	e = 0
	f = 0
	g = 1
	Si 	a == 1 y b == 1 y c == 1 y d == 1 y e == 1 y f == 1 y g == 0 entonces;
		Escribir "su numero es 0";
	sino Si 	a == 0 y b == 1 y c == 1 y d == 0 y e == 0 y f == 0 y g == 0 entonces;
		Escribir "su numero es 1";
	sino Si 	a == 1 y b == 1 y c == 1 y d == 0 y e == 1 y f == 0 y g == 1 entonces;
		Escribir "su numero es 2";
	sino Si 	a == 1 y b == 1 y c == 1 y d == 1 y e == 0 y f == 0 y g == 1 entonces;
		Escribir "su numero es 3";
	sino Si 	a == 0 y b == 1 y c == 1 y d == 0 y e == 0 y f == 1 y g == 1 entonces;
		Escribir "su numero es 4";
	SiNo Si 	a == 1 y b == 1 y c == 1 y d == 1 y e == 0 y f == 1 y g == 1 entonces;
		Escribir "su numero es 5";
	sino Si 	a == 1 y b == 0 y c == 1 y d == 1 y e == 1 y f == 1 y g == 1 entonces;
		Escribir "su numero es 6";
	sino Si 	a == 1 y b == 0 y c == 1 y d == 0 y e == 0 y f == 1 y g == 1 entonces;
		Escribir "su numero es 7";
	sino Si 	a == 1 y b == 1 y c == 1 y d == 1 y e == 1 y f == 1 y g == 1 entonces;
		Escribir "su numero es 8";
	sino Si 	a == 1 y b == 1 y c == 1 y d == 0 y e == 0 y f == 1 y g == 0 entonces;
		Escribir "su numero es 9";
	SiNo
		escribir "el numero no existe";
	FinSi
FinSi
FinSi
FinSi
FinSi
FinSi
FinSi
FinSi
FinSi
FinSi

	
	
FinAlgoritmo

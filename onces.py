#from validaciones import TestOpcion
import calendar
import datetime
def TestOpcion(n):
    while n!=("1") and n!=("2"):
        n=input("Selecciona solo \'1\' o \'2\' segun su opción: ")
    return n
def ValidYearIni(n):
    while n<1 or n>9999:
        n=ValidYearIni(int(input("Introduzca un año valido: ")))
    return n
def ValidYearFin(n,m):
    while n<1 or n>9999 or n<m:
        n=ValidYearFin(int(input("Introduzca un año valido y posterior al inicial: ")),m)
    return n	
while True:
	print("1.- 11´s por año")
	print("2.- Coincidencias de natalidad ")

	opcion=TestOpcion(input("Escoge una opción:"))
	if opcion=="1":
		yearIni=ValidYearIni(int(input("Año inicial:")))
		yearFin=ValidYearFin(int(input("Año Final:")),yearIni)
		yearFin+=1
		cal= calendar.Calendar()
		for y in range(yearIni,yearFin):
			all=0
			for n in  range(1,13):
				for x in cal.itermonthdates(y, n):
					nd=0
					o=0
					x=str(x)
					a=x.rsplit("-")
					nd+=int(a[1])+int(a[2])+int(x[0])+int(x[1])+int(x[2])+int(x[3])
					s=str(nd)
					o=int(s[0])+int(s[1])
					if o==11:
						all+=1
						print("Fecha: "+x+" Número de destino: "+s)
			print("Totales por año: "+str(all))
	elif opcion=="2":
		print("hola mundo")
else:
        subprocess.call(["cmd.exe","/C","cls"])

print(opcion)
#cal= calendar.Calendar()
#for y in range(1981,1998):
#	all=0
#	for n in  range(1,13):
#		for x in cal.itermonthdates(y, n):
#			nd=0
#o=0
			
#			x=str(x)
#			a=x.rsplit("-")
#			nd+=int(a[1])+int(a[2])+int(x[0])+int(x[1])+int(x[2])+int(x[2])
#			s=str(nd)
#			o=int(s[0])+int(s[1])
#			if o==11:
#				all+=1
#	print(all)
		

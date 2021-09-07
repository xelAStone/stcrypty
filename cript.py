import hashlib
import sys
import os
import base64
import time
sys=sys.platform
print('Este es un ejercico con el modulo hashlib, os, y sys\nxela-stone')
print(time.ctime())
def funcion():
	a=input('ingresa el mensaje a continuacion --> : ')
	if a == '':
		return 'este campo esta vacio'
	elif a != '':
		x=hashlib.sha256(a.encode()).hexdigest()
		#return x
		print(x,' --> este es el mensaje')
def funcion2():
	a=input('introduce la ruta del archivo => : ')
	b=input('introduce el nombre del archivo => : ')
	if a == '' and sys == 'linux': os.getcwd() + "/home/kali/Desktop/"
	manejo=open(a+b,'r')
	leer=manejo.readlines()
	var=str(leer[0])
	x=hashlib.sha256(var.encode()).hexdigest()
	print(x)
	manejo.close()

def base64():
	a=input('ingresa el texto : ')
	y=base64.b64encode(a.encode())
	print(y)


if __name__=='__main__':
	a=input('elige b si quires ingresar el mensaje manual\nelige c para subir un archivo ya creado\nelige d para encriptar en base64 \n--> : ')
	if a == 'b' or a=='B':
		funcion()
	elif a == 'c' or a== 'C':
		funcion2()
	elif a == 'd' or a=='D':
		base64()
	elif a == '':
		print('el codigo esta terminado')

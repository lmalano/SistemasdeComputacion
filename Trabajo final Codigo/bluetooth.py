#!/usr/bin/env python
import bluetooth
from io import open

host = ""
port = 1

server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('Socket de Bluetooth creado')

try:
	server.bind((host, port))
	print("Binding completo")
except:
	print("Binding incompleto")

server.listen(1)
cliente, direccion = server.accept()
print("Conectado a:", direccion)
print("Cliente:", cliente)

try:
	while True:
		dato = cliente.recv(1024)
		print(dato)
		
		with open("/proc/hello", "w") as hello:
			hello.write(unicode(dato))
		
		if dato == 'A':
			print "Escribi una A"
		elif dato == 'B':
			print "Escribi una B"
		else:
			print("Otra letra")
			
except KeyboardInterrupt:
	client.close()
	server.close()

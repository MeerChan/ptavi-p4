#!/usr/bin/python3
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys
# Constantes. Dirección IP del servidor,Puerto del servidor y
# Linea
try:
    IPSERVER = sys.argv[1]
    PORTSERVER = int(sys.argv[2])
    # Une las palabras con lo que hay entre ' ',
    LINE = ' '.join(sys.argv[3:])
except IndexError:
    sys.exit("Usage: client.py ip puerto register sip_address expires_value")

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((IPSERVER, PORTSERVER))
    print("Enviando:", LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")

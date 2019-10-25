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
    PETICION = sys.argv[3]
    ADDRESS = sys.argv[4]
    EXPIRES = sys.argv[5]
except IndexError:
    sys.exit("Usage: client.py ip puerto register sip_address expires_value")

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((IPSERVER, PORTSERVER))
    print("Enviando:", PETICION.upper() + ' sip:' + ADDRESS + ' SIP/2.0')
    print("Expires: " + EXPIRES)
    #Se lo enviamos al servidor
    my_socket.send(bytes(PETICION.upper() + ' sip:' + ADDRESS + ' SIP/2.0\r\n '
                            + EXPIRES, 'utf-8') + b'\r\n\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")

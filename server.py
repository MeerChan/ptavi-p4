#!/usr/bin/python3
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import time
import json

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    dicc = {}

    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        milinea = ''
        for line in self.rfile:
            milinea += line.decode('utf-8')
        if milinea != '\r\n':
            print("El cliente nos manda ", milinea)
            (peticion, address, sip) = milinea.split()
            if peticion == 'REGISTER':
                IP = self.client_address[0]
                user = address.split(':')[1]
                self.dicc[user] = {'address': IP}



if __name__ == "__main__":
    # Listens at localhost ('') port 6001
    # and calls the EchoHandler class to manage the request
    if len(sys.argv) != 2:
        sys.exit("Usage: server.py port")
    try:
        PORTSERVER = int(sys.argv[1])
    except ValueError:
        sys.exit("Port must be a number")
    except IndexError:
        sys.exit("Usage: server.py port")
    serv = socketserver.UDPServer(('', PORTSERVER), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")

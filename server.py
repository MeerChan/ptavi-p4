#!/usr/bin/python3
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """

        for line in self.rfile:
            print("El cliente nos manda ", self.client_address, line.decode('utf-8'))
            self.wfile.write(line)

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
    serv = socketserver.UDPServer(('', PORTSERVER), EchoHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")

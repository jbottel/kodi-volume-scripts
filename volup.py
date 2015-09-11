#!/usr/bin/python

from jsonrpclib.jsonrpc import TransportMixIn, XMLTransport
from jsonrpclib import Server

class Transport(TransportMixIn, XMLTransport):
    """Replaces the json-rpc mixin so we can specify the http headers."""
    def send_content(self, connection, request_body):
        connection.putheader("Content-Type", "application/json")
        connection.putheader("Content-Length", str(len(request_body)))
        connection.endheaders()
        if request_body:
            connection.send(request_body)


import jsonrpclib
xbmc = jsonrpclib.Server('http://192.168.1.2:8080/jsonrpc', transport=Transport())
volume = xbmc.Application.GetProperties(properties=['volume'])['volume']
print "Current Volume: " + volume
volume = volume + 2
print "Setting Volume: " + volume
xbmc.Application.SetVolume(volume=volume)

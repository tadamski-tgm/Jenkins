'''
Created on 30.10.2014

@author: ilendemli
'''

from Control.Connection import Connection

class Diagram:
    objs = []
    
    @staticmethod
    def getData(session):
        return Connection.getMIBs(session, 'NETSCREEN-ZONE-MIB', Diagram.objs)
        
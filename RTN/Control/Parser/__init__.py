'''
Created on 18.10.2014

@author: ilendemli
'''

class Parser:    
    def parseData(self, errorIndication, errorStatus, errorIndex, varBindTable, om):
        
        if errorIndication:
            return None
        
        else:
            if errorStatus:
                return None
                # return '%s at %s' % ( errorStatus.prettyPrint(), errorIndex and varBindTable[-1][int(errorIndex)-1] or '?' )
            
            else:
                results = None
                
                if om == 0:
                    results = []
                    
                    for varBindTableRow in varBindTable:
                        for name, val in varBindTableRow:
                            results.append('%s' % val)
                            
                elif om == 1:
                    for name, val in varBindTable:
                        results = '%s' % val
                    
                return results
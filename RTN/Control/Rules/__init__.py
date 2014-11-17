'''
Created on 18.10.2014

@author: ilendemli
'''

from flask import Flask, render_template, logging, session, request, abort, redirect, url_for
from flask_classy import FlaskView, route

from Control.Connection import Connection
from Control.Connection.SNMPv3 import SNMPv3
from Control.Connection.SNMPv2 import SNMPv2

from Control.Objects.Zones import Zones
from Control.Objects.Services import Services
from Control.Objects.Rules import Rules
from Control.Objects.Diagram import Diagram

class Listener(FlaskView):
    route_base = '/'
    musthaveparams = ['ipAddress', 'ipPort', 'communityName', 'snmp_version']
    
    debug = False
    host = '127.0.0.1'
    port = 5000
    
    app = Flask(__name__)
    
    def __init__(self):
        self.app.template_folder = '../../View/templates'
        self.app.static_folder = '../../View/static'
        self.app.secret_key = 'averysecurekey'
        
    def checkSessions(self):
        logged_in = False
        
        count = 0
        for word in self.musthaveparams:
            if word in session: 
                count += 1
        
        if count == len(self.musthaveparams):
            logged_in = True
            
        return logged_in
    
    def index(self):
        return render_template('index.html', logged_in=self.checkSessions())
    
    @route('/login', methods=['GET', 'POST'])
    def login(self):
        error = None
        
        loginstate = self.checkSessions()
    
        if request.method == 'POST':
            session.pop('ipAddress', None)
            session.pop('ipPort', None)
            session.pop('communityName', None)
            session.pop('snmp_version', None)
        
            ipAddress = request.form.get("ip")
            ipPort = request.form.get("port")
            communityName = request.form.get("cname")
            
            result = Connection.getSNMPVersion(ipAddress, ipPort, communityName)

            if (result == -2):
                error = 'Counldn\'t access the community'
                
            elif (result == -1):
                error = 'Invalid IP and/or IP-PORT number...'
                
            elif (result > 0):
                session['ipAddress'] = ipAddress
                session['ipPort'] = ipPort
                session['communityName'] = communityName
                session['snmp_version'] = result
                
                loginstate = True
            
        if loginstate:
            url = url_for('Listener:zones')
            return redirect(url)
        
        else:
            return render_template('login.html', error=error)
        
    @route('/zones', methods=['GET'])
    def zones(self):
        return self.dataRetriever('zones.html', Zones)
    
    @route('/rules', methods=['GET'])
    def rules(self):
        return self.dataRetriever('rules.html', Rules)
    
    @route('/services', methods=['GET'])
    def services(self):
        return self.dataRetriever('services.html', Services)
    
    @route('/diagram', methods=['GET'])
    def diagram(self):
        return self.dataRetriever('diagram.html', Diagram)
                
    def dataRetriever(self, page, obj):
        loginstate = self.checkSessions()
        
        if (loginstate == False):
            if (request.args.get('json') == None):
                url = url_for('Listener:index')
                return redirect(url)
            
            else:
                return Connection.renderJSON({"error": "You aren't logged in"})
        
        else:
            if (request.args.get('json') == None):
                return render_template(page, logged_in=loginstate)
        
            else:
                return obj.getData(session)

    def logout(self):
        session.pop('ipAddress', None)
        session.pop('ipPort', None)
        session.pop('communityName', None)
        session.pop('snmp_version', None)
        
        url = url_for('Listener:index')
        return redirect(url)
    
    def registerApp(self):
        self.register(self.app)
        
    def setDebug(self, debug):
        self.debug = debug
        
    def setPort(self, port):
        self.port = port
        
    def setHost(self, host):
        self.host = host
        
    def run(self):
        self.app.run(host=self.host, port=self.port, debug=self.debug)

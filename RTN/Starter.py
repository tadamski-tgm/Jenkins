from Control.Rules import Listener
from Control.Logger import Logger

Logger.enableLogging();

listener = Listener()

listener.setDebug(True)
listener.setHost('0.0.0.0')
listener.setHost('25.42.250.176')

# listener.setHost('80.109.113.100')

listener.registerApp()
listener.run()

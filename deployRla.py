import deployApplication
import createJAASAuthData
import createDatasources
import restartServer

from properties import Properties

# First stop the application
#stopApplication.main()

properties = Properties()
serverNames = properties.getPropertyList("servers")
print "****************************************************************************************"
print "*                                                                                      *"
print serverNames
print "*                                                                                      *"
print "****************************************************************************************"
for currentServer in serverNames:
    print "****************************************************************************************"
    print "*                                                                                      *"
    print "*   Current Server in Cluster: " +currentServer
    print "*                                                                                      *"
    print "****************************************************************************************"

    splitServer = currentServer.split(".")
    Properties().setProperty("server",splitServer[1])
    Properties().setProperty("nodeName",splitServer[0])
    print "Cluster Server Details:" + Properties().getProperty("server") + " On Node: " + Properties().getProperty("nodeName")
    # Init

deployApplication.main()

#restartServer.main()

print "========================================================================================"
print "=                                                                                      ="
print "=                  Undeploying Application                                             ="
print "=                                                                                      ="
print "========================================================================================"


appName=sys.argv[0]

'''
Check to see if App is deployed
'''
def isAppExists(appName):
    return len(AdminConfig.getid("/Deployment:" + appName + "/" )) > 0

if isAppExists(appName):
    print 'Removing Application "%s"...' %(appName)
    AdminApp.uninstall(appName)
    print 'Application "%s" removed successfully!' %(appName)
    AdminConfig.save()
    AdminNodeManagement.syncActiveNodes()

else:
    print "Application Not Found..Deploy Imminent"

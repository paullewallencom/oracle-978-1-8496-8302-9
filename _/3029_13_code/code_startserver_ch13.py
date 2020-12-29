# Connect WLST to the running server
connect('weblogic','<password WebLogic>',’Admin URL>’);

#The following command will print the state of the servers
print 'Status',state('AdminServer','Server');
serverRuntime()
a = get('State')
if a == 'RUNNING'
print 'Status',state('<Managed Server Name 1>','Server');
print 'Status',state('<Managed Server Name 2>','Server');

startServer('AdminServer','mydomain',’<Admin URL>',
'weblogic','<password weblogic>', >,‘<domain dir>','true’)

# Disconnect the WLST from Adminserver
disconnect();

#Create and Configure a Cluster and assign the Managed Servers to that cluster

cd('/')
create('appcluster','Cluster')
assign('Server', 'app01,app02','Cluster','appcluster')
cd('Clusters/appcluster')
set('MulticastAddress','237.0.0.101')
set('MulticastPort',7204)

#Write the domain and Close the domain template

updateDomain()
closeDomain()

exit()
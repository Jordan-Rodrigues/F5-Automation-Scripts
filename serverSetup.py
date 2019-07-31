from f5.bigip import ManagementRoot

#Connect to account
f5_account = ManagementRoot("10.80.191.92", "admin", "cC50KXf1=rmOxdp")

#Creating a monitor to be used for the pool
f5_account.tm.ltm.monitor.https.http.create(name="health_monitor", partition="Common")


#Creating a pool (deletes it if it exists already)
if f5_account.tm.ltm.pools.pool.exists(name="pool1", partition="Common"):
    f5_account.tm.ltm.pools.pool.delete(name="pool1", partition="Common")
    pool1 = f5_account.tm.ltm.pools.pool.create(name="pool1", partition="Common")
else: 
    pool1 = f5_account.tm.ltm.pools.pool.create(name="pool1", partition="Common", monitor="health_monitor")

#Testing message
pool1.description = "This pool was configured using Python"
pool1.update()

#Adding the nodes to the pool
node1 = pool1.members_s.members.create(partition="Common", name = "10.90.75.131:80")
node2 = pool1.members_s.members.create(partition="Common", name = "10.90.75.240:80")

#Testing Message
node1.description = "This node was configured using Python"
node2.description = "This node was configured using Python"
node1.update()
node2.update()

#Creating a VIP
VIP1 = f5_account.tm.ltm.virtuals.virtual.create(partition="Common", name ="VIP1", pool="pool1")

#assigning the default VIP to a server



#Creating a pool object and assigning it to the existing pool
#pool_obj = f5_account.tm.ltm.pools.pool
#pool_obj.load(partition='Common', name='pool1')

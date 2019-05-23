from f5.bigip import ManagementRoot

mgmt = ManagementRoot("10.80.191.92","admin","cC50KXf1=rmOxdp")
pools = mgmt.tm.ltm.pools
pool = mgmt.tm.ltm.pools.pool
print(mgmt.tm.ltm.pools.pool.exists(name="Pool-1", parition="Common"))

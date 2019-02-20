## Docker EE Engine Tuning Details

We have found the settings outlined here to aid performance and stability of clusters both in
Docker’s internal clusters as well as at many of our clients. None of them are required but may
provide benefits to your team’s workloads.

---
```
vm.swappiness=0
vm.overcommit_memory=1
```
These settings should be used together to force the kernel to use RAM instead of swap
memory.
  * vm.swappiness=0 ​Prevents memory swapping except in the case of an OOM
(OutOfMemory) condition
  * vm.overcommit_memory=1​ Sets the kernel to always allow memory allocations
until there is actually zero memory remaining.

Additional information at:
https://success.docker.com/article/node-using-swap-memory-instead-of-host-memory

---
```
net.ipv4.neigh.default.gc_thresh1 = 80000
net.ipv4.neigh.default.gc_thresh2 = 90000
net.ipv4.neigh.default.gc_thresh3 = 100000
```
Increasing ARP caches for situations with very large networks where the limits of the
hosts ARP cache are exceeded (as evidenced by errors such as `neighbour: arp_cache:
neighbor table overflow!`` in dmesg).

Additional details on these settings is available at:
https://success.docker.com/article/how-to-increase-the-arp-cache-collection-threshold

---
```
net.ipv4.tcp_keepalive_time=600
```
Lowering the IPVS timeout to below that of the TCP session to avoid IPVC connections
being cleared from the connection table.

Additional details available at:
https://success.docker.com/article/ipvs-connection-timeout-issue

---
```
net.ipv4.ip_forward=1
```
This setting enables Linux IP forwarding, it is the default setting on RHEL

---
```
fs.may_detach_mounts=1
```
This setting is required for host mount points on RHEL 7.4 and is the default setting on
RHEL

---
```
fs.inotify.max_user_instances=8192
```
This specifies an upper limit on the number of inotify instances that can be created per
real user ID.

---
```
fs.inotify.max_user_watches=1048576
```
This specifies an upper limit on the number of watches that can be created per real user
ID.

# Docker EE Install Cheat Sheet

## Get a Trial

30 day trial : [https://hub.docker.com/search/?q=&type=edition&offering=enterprise&operating_system=linux](https://hub.docker.com/search/?q=&type=edition&offering=enterprise&operating_system=linux)

## Node Sizing - Port Requirements

* UCP - 4 core(vcpu) x 16GB Ram X 100GB free in `/var/lib/` for `kubelet` and `docker`. *Increase CPU and RAM as cluster grows.*
* DTR - 4 core(vcpu) x 16GB Ram X 250GB free in `/var/lib/` for `kubelet` and `docker`. *Increase CPU and RAM to improve CVE Scanning.*
  * Storage is dependent on if external storage for DTR is used.
* Worker - 4 core(vcpu) x 16GB Ram X 100GB free in `/var/lib/` for `kubelet` and `docker`. *Increase as container workload increases.*

Make sure the ports are open between ALL nodes.

* [Docker UCP System Requirements](https://docs.docker.com/ee/ucp/admin/install/system-requirements/)

## Get Docker EE RPMS, License, and Offline CVE

Get RPMS from your **PRIVATE** storebits url. The url location is located on [hub.docker.com](https://hub.docker.com/) under "My Content". Example url https://hub.docker.com/u/$HUB_ID/content. Then click "Setup".

![setup](./img/setup.jpg)

Notice the `https://storebits.docker.com/ee/...` link in the lower right. This is where the rpms can be downloaded for offline use.
Example url for getting the YUM repo file `https://storebits.docker.com/ee/rhel/sub-.../docker-ee.repo`.

![storebits](./img/license_storebits.jpg)

Make sure to **DOWNLOAD** at least the License and CVE file.

## Install Docker EE Engine

If you are online follow the [Centos Engine Install docs](https://docs.docker.com/install/linux/docker-ee/centos/#set-up-the-repository).

If you are offline, download the RPMs to the node or setup a local http/nfs repo. OR local install with:

```bash
yum install -y docker-ee-18.09.2-3.el7.x86_64.rpm docker-ee-cli-18.09.2-3.el7.x86_64.rpm containerd.io-1.2.2-3.3.el7.x86_64.rpm
```

## Tune Docker EE Engine

[Kernel Tuning](https://github.com/clemenko/best_practices#kernel)

```bash
echo "vm.swappiness=0" >> /etc/sysctl.conf # turn off swapping unless necessary
echo "vm.overcommit_memory=1" >> /etc/sysctl.conf # allowing oversubscription
echo "net.ipv4.neigh.default.gc_thresh1 = 80000" >> /etc/sysctl.conf # arp cache fixes
echo "net.ipv4.neigh.default.gc_thresh2 = 90000" >> /etc/sysctl.conf # arp cache fixes
echo "net.ipv4.neigh.default.gc_thresh3 = 100000" >> /etc/sysctl.conf # arp cache fixes
echo "net.ipv4.tcp_keepalive_time=600" >> /etc/sysctl.conf # decrease the tcp timeout for ipvs
echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf # needed for iptables
echo "fs.may_detach_mounts=1" >> /etc/sysctl.conf # needed for host mountpoints with RHEL 7.4
echo "fs.inotify.max_user_instances=8192" >> /etc/sysctl.conf # monitor file system events
echo "fs.inotify.max_user_watches=1048576" >> /etc/sysctl.conf # monitor file system events
sysctl -p
```

[Daemon Tuning](https://github.com/clemenko/best_practices#daemon-)

```bash
docker plugin disable docker/telemetry:1.0.0.linux-x86_64-stable
echo -e "{\n \"selinux-enabled\": true, \n \"log-driver\": \"json-file\", \"log-opts\": {\"max-size\": \"10m\", \"max-file\": \"3\"}, \n}" > /etc/docker/daemon.json
 systemctl restart docker
 ```

## Install UCP

## Configure UCP

## Join Nodes to Cluster

## Install Docker Trusted Registry
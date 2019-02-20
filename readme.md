# Docker EE Install Cheat Sheet

## Get a Trial

30 day trial : [https://hub.docker.com/search?q=&type=edition&offering=enterprise](https://hub.docker.com/search?q=&type=edition&offering=enterprise)

## Node Sizing - Port Requirements

  * UCP - 4 core(vcpu) x 16GB Ram X 100GB free in `/var/lib/`
  * DTR - 4 core(vcpu) x 16GB Ram X 250GB free in `/var/lib/`
    * Storage is dependent on if external storage for DTR is used.
  * Worker - 4 core(vcpu) x 16GB Ram X 100GB free in `/var/lib/`

Make sure the ports are open between ALL nodes. 

  * [Docker UCP System Requirements](https://docs.docker.com/ee/ucp/admin/install/system-requirements/)

## Install Docker EE Engine

## Tune Docker EE Engine

## Install UCP

## Configure UCP

## Join Nodes to Cluster

## Install Docker Trusted Registry
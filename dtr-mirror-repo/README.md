## Setup mirroring for DTR repositories to another registry using Python

Docker Trusted Registry allows you to create mirroring policies for a repository. When an image gets pushed to a repository and meets a certain criteria, DTR automatically pushes it to a repository in a remote Docker Trusted or Hub registry.

This not only allows you to mirror images but also allows you to create image promotion pipelines that span multiple DTR deployments and datacenters.

### Usage
1. Install python packages 
   * `pip3 install requests configparser ast`
2. Prepare the `mirror.cfg`
3. Run the script
   * `python3 dtr-repo-mirror.py`

Reference: https://docs.docker.com/ee/dtr/user/promotion-policies/push-mirror/
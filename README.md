# COMP90024-Team30
uses to store the repo of our A2 project

## Team Member
Denny Pan - ziyang.pan@student.unimelb.edu.au
Humna Hussain - hussain1@student.unimelb.edu.au
Jonny Jiang - jonny.jiang@student.unimelb.edu.au
Xiongfei Guo  - 1196869
Zoe Wu -  xiongfeig@student.unimelb.edu.au



## Ansible structure for our couchdb and harvesters setup
```
hosts    # inventory file for hosts

host_vars/
    couchdb.yaml    # couchdb hosts variables
    env_vars.yaml   # environment variables setting


roles/
    couch-setup/
        tasks/
            main.yaml    # tasks for couchdb setup
    docker
        tasks/
            main.yaml   # tasks for docker install
        templates
            l_http-proxy.conf   # config for docker proxy (used proxy from unimelb)
        
    node_setup
        tasks/
            main.yaml   # tasks for install required dependencies for hosts and config hosts
    
    volume_mount
        tasks/
            main.yaml   # tasks for config the partition volume.

    harvester  
        tasks/
            main.yaml   # tasks for setup and running harvester
            
    historical-tweet-crawler
        tasks/
            main.yaml   # tasks for setup and running historical tweet crawler
    
    frontend
        tasks/
            main.yaml   # tasks for setup frontend web server
            
            
```

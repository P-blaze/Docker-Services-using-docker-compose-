# Docker-Services-using-docker-compose-

# Docker compose is used in this project to provide services for :
`Wordpress` `Joomla` `Owncloud`

Technoligies used :
1. Docker
2. Redhat8
3. pyhton3
4. wordpress
5. joomla
6. owncloud

Database used is : `mysql`

# Essentials for this project to run :

=> make sure you have `rhel8` installed with configured `yum` in it.
   + rhel8 can be installed by getting an image online that install it in Virtual box/ VM ware.
   + to configure yum :
     - add docker.repo and dvd.repo inside the `/etc/yum.repos.d` for local installation using `https://download.docker.com/linux/centos/docker-ce.repo`
     
=> make sure that on top of your base os, docker and docker-compose are installed in latest version.
    + to install docker : `yum install docker-ce --nobest`
    + to setup dokcer compose:
       - sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-  compose
       - sudo chmod +x /usr/local/bin/docker-compose

=> to start docker :     
    + permanently : `systemctl enable docker`
    + at a time: `systemctl start docker`
     
# now to get any services using program :

=> run the program using python3 :  `# python3 docker-run.py`

=> before executing the above cmd, make sure you have cloned this project in `/root` folder.

=> all the images used inside this project will be downloaded automatically, but you can also install them manually using:
  ` 1.docker pull joomlan:latest`
   `2.docker pull owncloud:latest`
  ` 3.docker pull mysql:5.7 `
   `4.docker pull wordpress:5.1.1-php7.3-apache`
   
=> to start docker-compose env inside wordpress, joomlan , owncloud folder manuallty you can use :
   + `docker-compose start`
   
=> to stop docker-compose services:
   + `docker-compose stop`
   
   

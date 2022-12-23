
#!/bin/sh

#make sure docker is running
service docker start
#remove containers and images due to limited space in AWS
#docker-compose rm $(docker ps -a -q)
#docker-compose rmi $(docker ps -a -q)
#delete production folder
rm -rf /home/ubuntu/git_clone
mkdir /home/ubuntu/git_clone
cd /home/ubuntu/git_clone
git clone git@github.com:marjanovic93/emse-sppm.git
cd /home/ubuntu/git_clone/emse-sppm
#take down current composition if running
docker-compose down
#replace dev settings with prod db settings
mv /home/ubuntu/git_clone/emse-sppm/emse-sppm/sppm/settings.py /home/ubuntu/git_clone/emse-sppm/emse-sppm/sppm/settings_dev.py
mv /home/ubuntu/git_clone/emse-sppm/emse-sppm/sppm/settings_aws.py /home/ubuntu/git_clone/emse-sppm/emse-sppm/sppm/settings.py
#completely rebuild and run composition
docker-compose build --no-cache
docker-compose up




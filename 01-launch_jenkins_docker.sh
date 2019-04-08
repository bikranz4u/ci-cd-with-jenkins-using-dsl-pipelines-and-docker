#!/bin/bash
docker run \
  -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /Users/bikrdas/Desktop/DevOps/Jenkins/jenkins_home:/var/jenkins_home \
  --name jenkins \
  jenkins/jenkins:lts

echo 'Below is the Initial password to access Jenkins'
docker exec -it jenkins sh -c "cat /var/jenkins_home/secrets/initialAdminPassword"



echo '-------- For Best security practice Remove the Initial Password --------------- '
#docker exec -it jenkins sh -c "rm -rf /var/jenkins_home/secrets/initialAdminPassword"

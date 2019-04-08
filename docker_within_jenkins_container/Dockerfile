FROM jenkins/jenkins
USER root
RUN apt-get update && \
    apt-get install sudo -y

RUN mkdir -p /tmp/download && \
    curl -L https://download.docker.com/linux/static/stable/x86_64/docker-18.03.1-ce.tgz | tar -xz -C /tmp/download && \
    rm -rf /tmp/download/docker/dockerd && \
    mv /tmp/download/docker/docker* /usr/local/bin/ && \
    rm -rf /tmp/download && \
    groupadd -g 999 docker && \
 # For Mac 'Group 'staff is required'"
    usermod -aG staff,docker jenkins

USER jenkins

#docker run -d -p 8080:8080 -p 50000:50000 -v /Users/bikrdas/Desktop/DevOps/Jenkins/jenkins_home/:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --name _jenkins dockerwithinjenkins

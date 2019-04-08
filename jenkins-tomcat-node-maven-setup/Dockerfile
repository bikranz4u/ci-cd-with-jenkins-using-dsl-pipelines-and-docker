FROM ubuntu:18.04
LABEL Description="This image is used as base for running JAVA,TOMCAT,MAVEN,NODE" \
      Maintainer="Bikram" \
      Version="1.0"

#--------------   updating and installing requirequired packages --------------  #
RUN apt-get update && \
    apt-get install wget curl git inotify-tools openssh-server -y

#--------------- ARGs ---------------------------------------#
ARG JDK_URL="https://download.oracle.com/otn-pub/java/jdk/8u201-b09/42970487e3af4f5aa5bca3f542482c60/jdk-8u201-linux-x64.tar.gz"

#--------------   Installing Oracle Java 1.8 --------------  #
RUN mkdir -p /opt && \
    wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; \
    oraclelicense=accept-securebackup-cookie"  && \
    tar xzf jdk-8u201-linux-x64.tar.gz && \
    cd jdk1.8.0_201/ && \
    alternatives --install /usr/bin/java java /opt/jdk1.8.0_201/bin/java 200000 && \
    alternatives --install /usr/bin/javac javac /opt/jdk1.8.0_201/bin/javac 200000 && \
    alternatives --install /usr/bin/jar jar /opt/jdk1.8.0_201/bin/jar 200000 && \
    alternatives --set jar /opt/jdk1.8.0_201/bin/jar && \
    alternatives --set javac /opt/jdk1.8.0_201/bin/javac

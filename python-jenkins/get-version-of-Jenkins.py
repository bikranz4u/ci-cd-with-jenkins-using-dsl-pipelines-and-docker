import sys
import jenkins
import json
import credentials

username = credentials.login['username']
password = credentials.login['password']

server = jenkins.Jenkins('http://localhost:8080', username= username, password= password)
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

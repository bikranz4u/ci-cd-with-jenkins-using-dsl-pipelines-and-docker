import sys
import jenkins
import json
import credentials

# Credentails 
username = credentials.login['username']
password = credentials.login['password']


# Print the number of jobs present in jenkins
server = jenkins.Jenkins('http://localhost:8080', username=username, password=password)


# Get the installed Plugin info
plugins = server.get_plugins_info()
parsed = json.loads(plugins)   # take a string as input and returns a dictionary as output.
#parsed = json.dumps(plugins)    # take a dictionary as input and returns a string as output.
#print(json.dumps(parsed, indent=4, sort_keys=True))
#print(plugins)
print(parsed)

#This is an example showing how to create, configure and delete Jenkins jobs.
import sys
import jenkins
import json
import credentials


username = credentials.login['username']
password = credentials.login['password']


# Print the number of jobs present in jenkins
server = jenkins.Jenkins('http://localhost:8080', username=username, password=password)

print(server.jobs_count())


#  Let's create a sample JoB
server.create_job('demoooooo',jenkins.EMPTY_CONFIG_XML)
jobs = server.get_jobs()
print(jobs)


# Print XML configuration of a specific job named 'NodeJS example'
my_job = server.get_job_config('NodeJS example')
print(my_job) # prints XML configuration


# Build an existing Job
server.build_job('demoooooo')

# Disable/enable  a job
server.disable_job('demoooooo')
server.enable_job('demoooooo')

# Copy a Job
server.copy_job('demoooooo', 'demoooooo_copy')

server.reconfig_job('demoooooo_copy', jenkins.RECONFIG_XML)

#server.delete_job('demoooooo')
#server.delete_job('demoooooo_copy')

# build a parameterized job
# requires creating and configuring the api-test job to accept 'param1' & 'param2'

#server.build_job('api-test', {'param1': 'test value 1', 'param2': 'test value 2'})
#last_build_number = server.get_job_info('api-test')['lastCompletedBuild']['number']
#build_info = server.get_build_info('api-test', last_build_number)
#print(build_info)

# get all jobs from the specific view
jobs = server.get_jobs(view_name='my_view')
print(jobs)

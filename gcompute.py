import os
import google.auth
import googleapiclient.discovery
from pprint import pprint as p

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/gclouduser/zenpack creation-966e5c252fa3.json"
credentials, project = google.auth.default()
compute = googleapiclient.discovery.build('compute', 'v1')
zone="us-central1-c"
result = compute.instances().list(project=project, zone=zone).execute()
#p(result)

for i in result['items']:
    #p(i)
    if "labels" in i.keys():
        print "Label =",i['labels']['name']
    print "Name =",i['name']
    print "Status =",i['status']
    print "Private IP =",i['networkInterfaces'][0]['networkIP']
    if len(i['networkInterfaces'][0]['accessConfigs'][0]) > 3:
        print "Public IP =",i['networkInterfaces'][0]['accessConfigs'][0]['natIP']
    
    print "\n"

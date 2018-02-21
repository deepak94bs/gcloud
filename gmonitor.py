from google.cloud import monitoring
import os
import google.auth

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/gclouduser/zenpack creation-966e5c252fa3.json"
credentials, project = google.auth.default()

client = monitoring.Client(project=project)
#print client

#for descriptor in client.list_resource_descriptors():
#    print descriptor
#    print "\n\n"

#for descriptor in client.list_metric_descriptors():
#    print descriptor
#    print "\n\n"

METRIC = 'compute.googleapis.com/instance/cpu/utilization'
query = client.query(METRIC, minutes=5)
print query.as_dataframe()


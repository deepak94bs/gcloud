import os
import google.auth

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/gclouduser/zenpack creation-966e5c252fa3.json"
credentials, project = google.auth.default()
print credentials, project

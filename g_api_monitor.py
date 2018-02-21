import datetime
import pprint
import os
import google.auth
import googleapiclient.discovery
from pprint import pprint as p

def format_rfc3339(datetime_instance):
    """Formats a datetime per RFC 3339."""
    return datetime_instance.isoformat("T") + "Z"


def get_start_time():
    """ Returns the start time for the 5-minute window to read the custom
    metric from within.
    :return: The start time to begin reading time series values, picked
    arbitrarily to be an hour ago and 5 minutes
    """
    # Return an hour ago - 5 minutes
    start_time = (datetime.datetime.utcnow() -
                  datetime.timedelta(minutes=5))
    print start_time
    return format_rfc3339(start_time)


def get_end_time():
    """ Returns the end time for the 5-minute window to read the custom metric
    from within.
    :return: The start time to begin reading time series values, picked
    arbitrarily to be an hour ago, or 5 minutes from the start time.
    """
    end_time = datetime.datetime.utcnow()
    print end_time
    return format_rfc3339(end_time)


def list_monitored_resource_descriptors(client, project_resource):
    """Query the projects.monitoredResourceDescriptors.list API method.
    This lists all the resources available to be monitored in the API.
    """
    request = client.projects().monitoredResourceDescriptors().list(
        name=project_resource)
    response = request.execute()
    print('list_monitored_resource_descriptors response:\n{}'.format(
        pprint.pformat(response)))


def list_metric_descriptors(client, project_resource, metric):
    """Query to MetricDescriptors.list
    This lists the metric specified by METRIC.
    """
    request = client.projects().metricDescriptors().list(
        name=project_resource,
        filter='metric.type="{}"'.format(metric))
    response = request.execute()
    print(
        'list_metric_descriptors response:\n{}'.format(
            pprint.pformat(response)))


def list_timeseries(client, project_resource, metric):
    """Query the TimeSeries.list API method.
    This lists all the timeseries created between START_TIME and END_TIME.
    """
    request = client.projects().timeSeries().list(
        name=project_resource,
        filter='metric.type="{}"'.format(metric),
        pageSize=3,
        interval_startTime=get_start_time(),
        interval_endTime=get_end_time())
    response = request.execute()
    print('list_timeseries response:\n{}'.format(pprint.pformat(response)))


def main(project_id):
    client = googleapiclient.discovery.build('monitoring', 'v3')

    project_resource = "projects/{}".format(project_id)
    #list_monitored_resource_descriptors(client, project_resource)
    # Metric to list
    metric = 'compute.googleapis.com/instance/cpu/usage_time'
    #list_metric_descriptors(client, project_resource, metric)
    list_timeseries(client, project_resource, metric)

if __name__ == '__main__':
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/gclouduser/zenpack creation-966e5c252fa3.json"
    credentials, project = google.auth.default()
    main(project)


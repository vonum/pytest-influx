import os
import functools
import datetime
from influxdb_client import InfluxDBClient


DEFAULT_INFLUXDB_URL = "http://localhost:8086"
DEFAULT_INFLUXDB_TOKEN = "test"
DEFAULT_INFLUXDB_ORG = "test"
DEFAULT_INFLUXDB_BUCKET = "test"

def clean_db(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        url = os.getenv("INFLUXDB_URL", DEFAULT_INFLUXDB_URL)
        token = os.getenv("INFLUXDB_TOKEN", DEFAULT_INFLUXDB_TOKEN)
        org = os.getenv("INFLUXDB_ORG", DEFAULT_INFLUXDB_ORG)
        bucket = os.getenv("INFLUXDB_BUCKET", DEFAULT_INFLUXDB_BUCKET)

        client = InfluxDBClient(url=url, token=token, org=org)

        delete_api = client.delete_api()

        dt = datetime.datetime.now() + datetime.timedelta(seconds=1)
        start = "1970-01-01T00:00:00Z"
        stop = dt.strftime('%Y-%m-%dT%H:%M:%SZ')

        delete_api.delete(
            start,
            stop,
            "",
            bucket=bucket,
            org=org
        )

        f(*args, **kwargs)

    return wrapper

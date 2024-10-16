import os
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
from pytest_influx import clean_db
from pytest_influx import (
    DEFAULT_INFLUXDB_URL,
    DEFAULT_INFLUXDB_TOKEN,
    DEFAULT_INFLUXDB_ORG,
    DEFAULT_INFLUXDB_BUCKET
)

@clean_db
def test_clean_db():
    url = os.getenv("INFLUXDB_URL", DEFAULT_INFLUXDB_URL)
    token = os.getenv("INFLUXDB_TOKEN", DEFAULT_INFLUXDB_TOKEN)
    org = os.getenv("INFLUXDB_ORG", DEFAULT_INFLUXDB_ORG)
    bucket = os.getenv("INFLUXDB_BUCKET", DEFAULT_INFLUXDB_BUCKET)

    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    write_api = client.write_api(write_options=SYNCHRONOUS)

    points = []
    for i in range(50):
        p = influxdb_client.Point("my_measurement")
        p.tag("tag", "value")
        p.field("index", i)
        points.append(p)

    write_api.write(bucket, org, points)

    assert True == True

@clean_db
def test_db_empty_at_start():
    url = os.getenv("INFLUXDB_URL", DEFAULT_INFLUXDB_URL)
    token = os.getenv("INFLUXDB_TOKEN", DEFAULT_INFLUXDB_TOKEN)
    org = os.getenv("INFLUXDB_ORG", DEFAULT_INFLUXDB_ORG)
    bucket = os.getenv("INFLUXDB_BUCKET", DEFAULT_INFLUXDB_BUCKET)

    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    query_api = client.query_api()

    query = f"""
        from(bucket:"test")\
        |> range(start: -30y)\
    """

    tables = query_api.query(org=org, query=query)
    assert len(tables) == 0


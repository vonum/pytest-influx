# pytest-influx
[![Build Status](https://vonum.semaphoreci.com/badges/pytest-influx/branches/master.svg)](https://vonum.semaphoreci.com/projects/pytest-influx)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Pytest plugin for managing your influxdb instance between test runs.
Currently only removes all records from influx between tests.

## Installation
`pip install pytest-influx`

## Configuring Influx Client
Provide values through environment variables for:
1. `INFLUXDB_URL`       -> default: `http://localhost:8086`
2. `INFLUXDB_TOKEN`     -> default: `test`
3. `INFLUXDB_ORG`       -> default `test`
4. `INFLUXDB_BUCKET`    -> default `test`

## Usage
```python
from pytest_influx import clean_db

@clean_db
def test_influx_interraction():
    pass

@clean_db
def test_other_influx_interraction():
    pass
```

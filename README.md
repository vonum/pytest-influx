# pytest-influx
Pytest plugin for managing your influxdb instance between test runs.

## Installation
`pip install pytest-influx`

## Usage
```python
from pytest-influx import clean_db

@clean_db
def test_influx_interraction():
    pass

@clean_db
def test_other_influx_interraction():
    pass
```

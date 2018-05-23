locustor
========

Locustor is a simple Python scheduled worker which sends Locust load testing logs to InfluxDB.


Usage
-----

Just configure to LocustorConfig class

.. code-block:: python

    class LocustorConfig:
        'Locustor configuration'
        INFLUXDB_HOST = ''
        INFLUXDB_PORT = ''
        INFLUXDB_USER_NAME = ''
        INFLUXDB_PASSWORD = ''
        INFLUXDB_DATABASE = ''
        DELAY_IN_SEC = 5
        LOCUST_CSV_LOG_FILE_PATH = ''
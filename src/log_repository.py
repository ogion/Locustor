'log_repository.py'
from influxdb import InfluxDBClient
from locustor_config import LocustorConfig
from log_helper import LogHelper

class LogRepository:
    'Log repository.'
    influx_client = None

    def __init__(self):
        locustor_config = LocustorConfig()
        self.influx_client = InfluxDBClient(locustor_config.INFLUXDB_HOST,
                                            locustor_config.INFLUXDB_PORT,
                                            locustor_config.INFLUXDB_USER_NAME,
                                            locustor_config.INFLUXDB_PASSWORD,
                                            locustor_config.INFLUXDB_DATABASE)

    def add_log(self, log):
        'Add a log to InfluxDB'
        mapped_log = LogHelper().prepare_influx_insert_query(log)
        self.influx_client.write_points(mapped_log)

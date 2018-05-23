'locustor.py'

import sys
from datetime import datetime, timedelta
import time
import schedule
from locustor_config import LocustorConfig
from log_repository import LogRepository
from log_helper import LogHelper


class Locustor:
    'Start point'

    def __init__(self):
        self.end_date = datetime.now() + timedelta(minutes=int(sys.argv[1]))

    def job(self):
        'Locustor is a simple scheduled worker which sends Locust logs to InfluxDB.'

        print(datetime.now())
        log_output = LogHelper().parse_log_to_json(LocustorConfig.LOCUST_CSV_LOG_FILE_PATH)
        LogRepository().add_log(log_output)

    def is_runnable(self):
        'Function is runnable'
        if self.end_date < datetime.now():
            return False
        return True


LOCUSTOR = Locustor()

schedule.every(LocustorConfig.DELAY_IN_SEC).seconds.do(LOCUSTOR.job)

while LOCUSTOR.is_runnable():
    schedule.run_pending()
    time.sleep(1)

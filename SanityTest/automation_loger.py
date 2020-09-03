import logging
import time
import os


class AutomationLogger():
    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super(AutomationLogger, self).__new__(self)
            logging.basicConfig(filename='Commbox' + time.strftime('%Y_%m_%d') + '.log',
                                level=logging.DEBUG,
                                format='%(asctime)s:%(levelname)s:%(message)s')
            self.logger = logging
            return self._instance

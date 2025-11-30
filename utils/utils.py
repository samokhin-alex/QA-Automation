import configparser
import os
from pathlib import Path

config = configparser.RawConfigParser()

config_path = Path(__file__).parent.parent / 'support' / 'config_data.ini'
config.read(str(config_path))

class ReadConfig:
    @classmethod
    def get_url(cls):
        url = config.get('common value', 'url')
        return url
# -*- coding: UTF-8 -*
from os.path import dirname, abspath
import configparser


class Settings:
    """
    Class that reads the settings.cfg to get the db connection data and
    the JWT settings, with this data it builds and returns
    the following dictionaries: db_dict, token_dict, api_dict, limit_dict
    """
    def __init__(self):
        d = dirname(dirname(abspath(__file__)))
        _current_cfg = f"{d}/settings/settings.cfg"
        self.config = configparser.RawConfigParser()
        self.config.read(_current_cfg)

        self.db_dict = {'host': self.config.get('database', 'host'),
                        'user': self.config.get('database', 'user'),
                        'password': self.config.get('database', 'password'),
                        'db': self.config.get('database', 'db'),
                        'port': int(self.config.get('database', 'port'))}

        self.token_dict = {'secret_key': self.config.get('token',
                           'secret_key'),
                           'expires': self.config.get(
                                                      'token',
                                                      'access_token_expire')}

        self.api_dict = {'base_url': self.config.get('api', 'base_url'),
                         'key': self.config.get('api', 'key')}

        self.limit_dict = {'seconds': int(self.config.get('limit', 'seconds')),
                           'max_requests': int(self.config.get('limit', 'max_requests'))}  # noqa: E501

    @property
    def get_db_dict(self):
        return self.db_dict

    @property
    def get_token_dict(self):
        return self.token_dict

    @property
    def get_api_dict(self):
        return self.api_dict

    @property
    def get_limit_dict(self):
        return self.limit_dict

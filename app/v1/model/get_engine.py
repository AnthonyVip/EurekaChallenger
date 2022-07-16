from sqlmodel import create_engine
import os
import sys
bp = os.path.dirname(os.path.realpath('.')).split(os.sep)
modpath = os.sep.join(bp)
sys.path.insert(0, modpath)
try:
    from app.v1.settings.settings import Settings
    from app.v1.utils.singleton import singleton
except ImportError:
    from settings.settings import Settings
    from utils.singleton import singleton

"""
module used to open connection to database
"""


@singleton
class CreateEngine():
    def __init__(self) -> None:
        self._settings = Settings()
        self._db_dict = self._settings.get_db_dict

    def __open__(self):
        self.engine = create_engine('postgresql+psycopg2://'
                                    f'{self._db_dict["user"]}:'
                                    f'{self._db_dict["password"]}'
                                    f'@{self._db_dict["host"]}:'
                                    f'{self._db_dict["port"]}/'
                                    f'{self._db_dict["db"]}')
        return self.engine

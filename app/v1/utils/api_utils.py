"""
help module for validations
"""


def ValidatedFunction(func):
    _valids_funcs = ['TIME_SERIES_INTRADAY',
                     'TIME_SERIES_DAILY',
                     'TIME_SERIES_WEEKLY',
                     'TIME_SERIES_MONTHLY']

    if func not in _valids_funcs:
        return False
    return True


def ValidatedOutputsize(outputsize):
    _valids_outputsizes = ['compact', 'full']

    if outputsize not in _valids_outputsizes:
        return False
    return True

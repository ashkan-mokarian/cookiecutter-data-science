#!/usr/bin/env python
import datetime
import toml
import functools
import logging
logger = logging.getLogger(__name__)

def time_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t0 = datetime.now()
        ret = func(*args, **kwargs)
        logger.info('time %s: %s', func.__name__, str(datetime.now() - t0))
        return ret

    return wrapper

def merge_dicts(sink, source):
    if not isinstance(sink, dict) or not isinstance(source, dict):
        raise TypeError('Args to merge_dicts should be dicts')

    for k, v in source.items():
        if isinstance(source[k], dict) and isinstance(sink.get(k), dict):
            sink[k] = merge_dicts(sink[k], v)
        else:
            sink[k] = v

    return sink

def get_config(config_files):
    """Reading config files from the cli args input which comes in list,
    later config files overwrites previous ones, """
    config = {}
    if config_files is not None:
        try:
            for conf in config_files:
                config = merge_dicts(config, toml.load(conf))
        except:
            raise IOError('Could not read config file: {}'.format(conf))


    return config
import sys
import os
from configlib import getConfig


def include_mozdef():
    sys.path.append(os.path.join(get_mozdef_directory(), 'lib'))


def get_config_location():
    return os.path.join(os.path.dirname(__file__), '../config.txt')


def get_mozdef_directory():
    return getConfig('mozdef_src', '', get_config_location())


def get_es_server():
    return getConfig('es_server', '', get_config_location())

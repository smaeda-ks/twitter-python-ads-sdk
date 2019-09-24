# Copyright (C) 2015 Twitter, Inc.

VERSION = (6, 0, 0)
API_VERSION = '6'

from twitter_ads.utils import get_version
from twitter_ads.v2.client import Client  # noqa

__version__ = get_version()

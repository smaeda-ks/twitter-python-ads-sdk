"""Container for all helpers and utilities used throughout the Ads API SDK."""

import datetime
import json
import warnings
warnings.simplefilter('default', DeprecationWarning)
from email.utils import formatdate
from time import mktime
from functools import partial

from twitter_ads import VERSION
from twitter_ads.v2.enum import GRANULARITY
from twitter_ads.v2.resources import RESOURCE_TABLE


def get_version():
    """Returns a string representation of the current SDK version."""
    if isinstance(VERSION[-1], str):
        return '.'.join(map(str, VERSION[:-1])) + VERSION[-1]
    return '.'.join(map(str, VERSION))


def remove_minutes(time):
    """Sets the minutes, seconds, and microseconds to zero."""
    return time.replace(minute=0, second=0, microsecond=0)


def remove_hours(time):
    """Sets the hours, minutes, seconds, and microseconds to zero."""
    return time.replace(hour=0, minute=0, second=0, microsecond=0)


def to_time(time, granularity):
    """Returns a truncated and rounded time string based on the specified granularity."""
    if not granularity:
        if type(time) is datetime.date:
            return format_date(time)
        else:
            return format_time(time)
    if granularity == GRANULARITY.HOUR:
        return format_time(remove_minutes(time))
    elif granularity == GRANULARITY.DAY:
        return format_date(remove_hours(time))
    else:
        return format_time(time)


def format_time(time):
    """Formats a datetime as an ISO 8601 compliant string."""
    return time.strftime('%Y-%m-%dT%H:%M:%SZ')


def format_date(time):
    """Formats a datetime as an ISO 8601 compliant string, dropping time."""
    return time.strftime('%Y-%m-%d')


def http_time(time):
    """Formats a datetime as an RFC 1123 compliant string."""
    return formatdate(timeval=mktime(time.timetuple()), localtime=False, usegmt=True)


def validate_whole_hours(time):
    if type(time) is datetime.date:
        pass
    else:
        # Times must be expressed in whole hours
        if time.minute > 0 or time.second > 0:
            raise ValueError("'start_time' and 'end_time' must be expressed in whole hours.")


def split_list(list_, n):
    """Splits a list by a given number (n) and returns a generator object."""
    list_size = len(list_)
    for sp in range(0, list_size, n):
        yield list_[sp:min(sp + n, list_size)]


class Deprecated(object):
    def __init__(self, message):
        self._message = message

    def __call__(self, decorated, *args, **kwargs):
        def wrapper(*args, **kwargs):
            method = "{}.{}".format(str(args[0].__name__), str(decorated.__name__))
            warnings.warn(
                "{} => {}".format(method, self._message),
                DeprecationWarning,
                stacklevel=2
            )
            return decorated(*args, **kwargs)
        return wrapper


class FlattenParams(object):
    def __init__(self, function):
        self._func = function

    def __call__(self, instance, *args, **kwargs):
        # skip batch request
        if ('batch' in args) or (kwargs.get('endpoint_type') == 'batch'):
            return self._func(instance, *args, **kwargs)

        params = kwargs
        for i in params:
            if isinstance(params[i], list):
                params[i] = ','.join(map(str, params[i]))
            elif isinstance(params[i], bool):
                params[i] = str(params[i]).lower()
        return self._func(instance, *args, **kwargs)

    def __get__(self, instance, owner):
        return partial(self, instance)


class ResourceController(object):
    def __init__(self, resource, override=None, default_operation=None, has_batch=False):
        self._resource = resource
        self._override = override
        self._default_operation = default_operation
        self._has_batch = has_batch

    def __call__(self, decorated, *args, **kwargs):
        def wrapper(*args, **kwargs):
            params = kwargs
            instance = args[0]
            operation_types = ['all', 'load', 'update', 'create', 'batch', 'delete']
            if self._default_operation:
                if (len(args) > 1 and args[1] in operation_types) or\
                   (params.get('endpoint_type') is not None):
                    operation = params.get('endpoint_type') or args[1]
                else:
                    operation = self._default_operation
                    params['endpoint_type'] = operation
            else:
                operation = params.get('endpoint_type') or args[1]

            if operation not in operation_types:
                raise NotImplementedError

            if self._override is not None:
                if self._override.get('account_id'):
                    account_id = kwargs.get(self._override.get('account_id'))
            else:
                account_id = instance.account_id

            if operation in ['all', 'create']:
                base = RESOURCE_TABLE[self._resource]['RESOURCE_COLLECTION']
                resource = base.format(account_id=account_id)
            elif operation in ['load', 'delete', 'update']:
                base = RESOURCE_TABLE[self._resource]['RESOURCE']
                resource = base.format(
                    account_id=account_id,
                    id=kwargs.get('id', None)
                )
            elif operation == 'batch':
                params['data'] = json.dumps(params.get('data', []))
                headers = {'content-type': 'application/json'}
                base = RESOURCE_TABLE[self._resource]['BATCH']
                resource = base.format(account_id=account_id)
                return decorated(*args, resource=resource, headers=headers, **params)

            return decorated(*args, resource=resource, **kwargs)
        return wrapper

    def __get__(self, instance, owner):
        return partial(self, instance)

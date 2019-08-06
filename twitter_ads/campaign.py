# Copyright (C) 2015 Twitter, Inc.

"""Container for all campaign management logic used by the Ads API SDK."""

from twitter_ads.enum import TRANSFORM
from twitter_ads.resource import resource_property, Resource, Persistence, Batch, Analytics
from twitter_ads.http import Request
from twitter_ads.cursor import Cursor
from twitter_ads import API_VERSION


class TargetingCriteria(Resource, Persistence, Batch):

    PROPERTIES = []

    BATCH_RESOURCE_COLLECTION = '/' + API_VERSION + '/batch/accounts/{account_id}/\
targeting_criteria'
    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/targeting_criteria'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/targeting_criteria/{id}'
    RESOURCE_OPTIONS = '/' + API_VERSION + '/targeting_criteria/'

    @classmethod
    def all(klass, account, line_item_ids, **kwargs):
        """Returns a Cursor instance for a given resource."""
        params = {'line_item_ids': ','.join(map(str, line_item_ids))}
        params.update(kwargs)

        resource = klass.RESOURCE_COLLECTION.format(account_id=account.id)
        request = Request(account.client, 'get', resource, params=params)

        return Cursor(klass, request, init_with=[account])

    @classmethod
    def app_store_categories(klass, account, **kwargs):
        """Returns a list of supported app store categories"""
        resource = klass.RESOURCE_OPTIONS + 'app_store_categories'
        request = Request(account.client, 'get', resource, params=kwargs)
        return Cursor(None, request)

    @classmethod
    def behavior_taxonomies(klass, account, **kwargs):
        """Returns a list of supported behavior taxonomies"""
        resource = klass.RESOURCE_OPTIONS + 'behavior_taxonomies'
        request = Request(account.client, 'get', resource, params=kwargs)
        return Cursor(None, request)

    @classmethod
    def behaviors(klass, account, **kwargs):
        """Returns a list of supported behaviors"""
        resource = klass.RESOURCE_OPTIONS + 'behaviors'
        request = Request(account.client, 'get', resource, params=kwargs)
        return Cursor(None, request)

    @classmethod
    def conversations(klass, account, **kwargs):
        """Returns a list of supported conversations"""
        resource = klass.RESOURCE_OPTIONS + 'conversations'
        request = Request(account.client, 'get', resource, params=kwargs)
        return Cursor(None, request)

    @classmethod
    def devices(klass, account, **kwargs):
        """Returns a list of supported devices"""
        resource = klass.RESOURCE_OPTIONS + 'devices'
        request = Request(account.client, 'get', resource, params=kwargs)
        return Cursor(None, request)

    @classmethod
    def events(klass, account, **kwargs):
        """Returns a list of supported events"""
        resource = klass.RESOURCE_OPTIONS + 'events'
        request = Request(account.client, 'get', resource, params=kwargs)
        return Cursor(None, request)

    @classmethod
    def interests(klass, account, **kwargs):
        """Returns a list of supported interests"""
        resource = klass.RESOURCE_OPTIONS + 'interests'
        request = Request(account.client, 'get', resource, params=kwargs)
        return Cursor(None, request)

    @classmethod
    def languages(klass, account, **kwargs):
        """Returns a list of supported languages"""
        resource = klass.RESOURCE_OPTIONS + 'languages'
        request = Request(account.client, 'get', resource, params=kwargs)
        return Cursor(None, request)

    @classmethod
    def locations(klass, account, **kwargs):
        """Returns a list of supported locations"""
        resource = klass.RESOURCE_OPTIONS + 'locations'
        request = Request(account.client, 'get', resource, params=kwargs)
        return Cursor(None, request)

    @classmethod
    def network_operators(klass, account, **kwargs):
        """Returns a list of supported network operators"""
        resource = klass.RESOURCE_OPTIONS + 'network_operators'
        request = Request(account.client, 'get', resource, params=kwargs)
        return Cursor(None, request)

    @classmethod
    def platforms(klass, account, **kwargs):
        """Returns a list of supported platforms"""
        resource = klass.RESOURCE_OPTIONS + 'platforms'
        request = Request(account.client, 'get', resource, params=kwargs)
        return Cursor(None, request)

    @classmethod
    def platform_versions(klass, account, **kwargs):
        """Returns a list of supported platform versions"""
        resource = klass.RESOURCE_OPTIONS + 'platform_versions'
        request = Request(account.client, 'get', resource, params=kwargs)
        return Cursor(None, request)

    @classmethod
    def tv_markets(klass, account, **kwargs):
        """Returns a list of supported TV markets"""
        resource = klass.RESOURCE_OPTIONS + 'tv_markets'
        request = Request(account.client, 'get', resource, params=kwargs)
        return Cursor(None, request)

    @classmethod
    def tv_shows(klass, account, **kwargs):
        """Returns a list of supported TV shows"""
        resource = klass.RESOURCE_OPTIONS + 'tv_shows'
        request = Request(account.client, 'get', resource, params=kwargs)
        return Cursor(None, request)


# sdk-only
resource_property(TargetingCriteria, 'to_delete', transform=TRANSFORM.BOOL)


class FundingInstrument(Analytics, Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/funding_instruments'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/funding_instruments/{id}'


class PromotableUser(Resource):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/promotable_users'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/promotable_users/{id}'


class AppList(Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/app_lists'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/app_lists/{id}'

    def create(self, name, *ids):
        if isinstance(ids, list):
            ids = ','.join(map(str, ids))

        resource = self.RESOURCE_COLLECTION.format(account_id=self.account.id)
        params = self.to_params.update({'app_store_identifiers': ids, 'name': name})
        response = Request(self.account.client, 'post', resource, params=params).perform()

        return self.from_response(response.body['data'])

    def apps(self):
        if self.id and not hasattr(self, '_apps'):
            self.reload()
        return self._apps


class Campaign(Analytics, Resource, Persistence, Batch):

    PROPERTIES = []

    BATCH_RESOURCE_COLLECTION = '/' + API_VERSION + '/batch/accounts/{account_id}/campaigns'
    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/campaigns'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/campaigns/{id}'


# sdk-only
resource_property(Campaign, 'to_delete', transform=TRANSFORM.BOOL)


class LineItem(Analytics, Resource, Persistence, Batch):

    PROPERTIES = []

    BATCH_RESOURCE_COLLECTION = '/' + API_VERSION + '/batch/accounts/{account_id}/line_items'
    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/line_items'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/line_items/{id}'

    def targeting_criteria(self, id=None, **kwargs):
        """
        Returns a collection of targeting criteria available to the
        current line item.
        """
        self._validate_loaded()
        if id is None:
            return TargetingCriteria.all(self.account, self.id, **kwargs)
        else:
            return TargetingCriteria.load(self.account, id, **kwargs)


# sdk-only
resource_property(LineItem, 'to_delete', transform=TRANSFORM.BOOL)


class ScheduledPromotedTweet(Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/scheduled_promoted_tweets'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/scheduled_promoted_tweets/{id}'


class Tweet(object):

    TWEET_PREVIEW = '/' + API_VERSION + '/accounts/{account_id}/tweet/preview'
    TWEET_ID_PREVIEW = '/' + API_VERSION + '/accounts/{account_id}/tweet/preview/{id}'
    TWEET_CREATE = '/' + API_VERSION + '/accounts/{account_id}/tweet'

    def __init__(self):
        raise NotImplementedError(
            'Error! {name} cannot be instantiated.'.format(name=self.__class__.__name__))

    @classmethod
    def preview(klass, account, **kwargs):
        """
        Returns an HTML preview of a tweet, either new or existing.
        """
        params = {}
        params.update(kwargs)

        # handles array to string conversion for media IDs
        if 'media_ids' in params and isinstance(params['media_ids'], list):
            params['media_ids'] = ','.join(map(str, params['media_ids']))

        resource = klass.TWEET_ID_PREVIEW if params.get('id') else klass.TWEET_PREVIEW
        resource = resource.format(account_id=account.id, id=params.get('id'))
        response = Request(account.client, 'get', resource, params=params).perform()
        return response.body['data']

    @classmethod
    def create(klass, account, **kwargs):
        """
        Creates a "Promoted-Only" Tweet using the specialized Ads API end point.
        """
        params = {}
        params.update(kwargs)

        # handles array to string conversion for media IDs
        if 'media_ids' in params and isinstance(params['media_ids'], list):
            params['media_ids'] = ','.join(map(str, params['media_ids']))

        resource = klass.TWEET_CREATE.format(account_id=account.id)
        response = Request(account.client, 'post', resource, params=params).perform()
        return response.body['data']


class UserSettings(Resource, Persistence):

    PROPERTIES = []

    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/user_settings/{id}'


class TaxSettings(Resource, Persistence):

    PROPERTIES = []

    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/tax_settings'

    @classmethod
    def load(self, account):
        """
        Returns an object instance for a given account.
        """
        resource = self.RESOURCE.format(account_id=account.id)
        response = Request(account.client, 'get', resource).perform()
        return self(account).from_response(response.body['data'])

    def save(self):
        """
        Update the current object instance.
        """
        resource = self.RESOURCE.format(account_id=self.account.id)
        response = Request(
            self.account.client, 'put',
            resource, params=self.to_params()).perform()
        return self.from_response(response.body['data'])

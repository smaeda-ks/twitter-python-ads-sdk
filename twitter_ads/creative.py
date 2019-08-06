# Copyright (C) 2015 Twitter, Inc.

"""Container for all creative management logic used by the Ads API SDK."""

from requests.exceptions import HTTPError

from twitter_ads import API_VERSION
from twitter_ads.cursor import Cursor
from twitter_ads.enum import TRANSFORM
from twitter_ads.http import Request
from twitter_ads.resource import resource_property, Resource, Persistence, Analytics


class PromotedAccount(Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/promoted_accounts'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/promoted_accounts/{id}'


class PromotedTweet(Analytics, Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/promoted_tweets'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/promoted_tweets/{id}'

    def save(self):
        """
        Saves or updates the current object instance depending on the
        presence of `object.id`.
        """
        params = self.to_params()
        if 'tweet_id' in params:
            params['tweet_ids'] = [params['tweet_id']]
            del params['tweet_id']

        if self.id:
            raise HTTPError("Method PUT not allowed.")

        resource = self.RESOURCE_COLLECTION.format(account_id=self.account.id)
        response = Request(self.account.client, 'post', resource, params=params).perform()
        return self.from_response(response.body['data'][0])


class AccountMedia(Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/account_media'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/account_media/{id}'


class MediaCreative(Analytics, Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/media_creatives'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/media_creatives/{id}'


class WebsiteCard(Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/cards/website'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/cards/website/{id}'


class VideoWebsiteCard(Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/cards/video_website'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/cards/video_website/{id}'


class ImageAppDownloadCard(Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/cards/image_app_download'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/cards/image_app_download/{id}'


class VideoAppDownloadCard(Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/cards/video_app_download'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/cards/video_app_download/{id}'


class ImageConversationCard(Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/cards/image_conversation'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/cards/image_conversation/{id}'


class VideoConversationCard(Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/cards/video_conversation'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/cards/video_conversation/{id}'


class ScheduledTweet(Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/scheduled_tweets'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/scheduled_tweets/{id}'
    PREVIEW = '/' + API_VERSION + '/accounts/{account_id}/scheduled_tweets/preview/{id}'

    def preview(self):
        """
        Returns an HTML preview for a Scheduled Tweet.
        """
        if self.id:
            resource = self.PREVIEW
            resource = resource.format(account_id=self.account.id, id=self.id)
            response = Request(self.account.client, 'get', resource).perform()
            return response.body['data']


class DraftTweet(Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/draft_tweets'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/draft_tweets/{id}'
    PREVIEW = '/' + API_VERSION + '/accounts/{account_id}/draft_tweets/preview/{id}'

    def preview(self, draft_tweet_id=None):
        """
        Preview a Draft Tweet on a mobile device.
        """
        if not (draft_tweet_id is None):
            resource = self.PREVIEW.format(account_id=self.account.id, id=draft_tweet_id)
        elif self.id:
            resource = self.PREVIEW.format(account_id=self.account.id, id=self.id)
        else:
            raise AttributeError("object has no 'draft_tweet_id' to preview")

        response = Request(self.account.client, 'post', resource).perform()
        return response.body


class MediaLibrary(Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/media_library'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/media_library/{id}'

    def reload(self, **kwargs):
        if not self.media_key:
            return self

        resource = self.RESOURCE.format(account_id=self.account.id, id=self.media_key)
        response = Request(self.account.client, 'get', resource, params=kwargs).perform()

        return self.from_response(response.body['data'])

    def save(self):
        if self.media_key:
            method = 'put'
            resource = self.RESOURCE.format(account_id=self.account.id, id=self.media_key)
        else:
            method = 'post'
            resource = self.RESOURCE_COLLECTION.format(account_id=self.account.id)

        response = Request(
            self.account.client, method,
            resource, params=self.to_params()).perform()

        return self.from_response(response.body['data'])

    def delete(self):
        resource = self.RESOURCE.format(account_id=self.account.id, id=self.media_key)
        response = Request(self.account.client, 'delete', resource).perform()
        self.from_response(response.body['data'])


class PollCard(Resource, Persistence):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/cards/poll'
    RESOURCE = '/' + API_VERSION + '/accounts/{account_id}/cards/poll/{id}'


class CardsFetch(Resource):

    PROPERTIES = []

    FETCH_URI = '/' + API_VERSION + '/accounts/{account_id}/cards/all'
    FETCH_ID = '/' + API_VERSION + '/accounts/{account_id}/cards/all/{id}'

    def all(klass):
        raise AttributeError("'CardsFetch' object has no attribute 'all'")

    @classmethod
    def load(klass, account, card_uris=None, card_id=None, with_deleted=None):
        # check whether both are specified or neither are specified
        if all([card_uris, card_id]) or not any([card_uris, card_id]):
            raise ValueError('card_uris and card_id are exclusive parameters. ' +
                             'Please supply one or the other, but not both.')
        params = {}
        if with_deleted:
            params['with_deleted'] = 'true'

        if card_uris:
            params['card_uris'] = ','.join(map(str, card_uris))
            resource = klass.FETCH_URI.format(account_id=account.id)
            request = Request(account.client, 'get', resource, params=params)
            return Cursor(klass, request, init_with=[account])
        else:
            params['card_id'] = card_id
            resource = klass.FETCH_ID.format(account_id=account.id, id=card_id)
            response = Request(account.client, 'get', resource, params=params).perform()
            return klass(account).from_response(response.body['data'])

    def reload(self):
        if self.id:
            self.load(self.account, card_id=self.id)


class TweetPreview(Resource):

    PROPERTIES = []

    RESOURCE_COLLECTION = '/' + API_VERSION + '/accounts/{account_id}/tweet_previews'

    @classmethod
    def load(klass, account, tweet_ids=None, tweet_type=None):
        params = {}

        params['tweet_ids'] = ','.join(map(str, tweet_ids))
        params['tweet_type'] = tweet_type
        resource = klass.RESOURCE_COLLECTION.format(account_id=account.id)
        request = Request(account.client, 'get', resource, params=params)
        return Cursor(klass, request, init_with=[account])

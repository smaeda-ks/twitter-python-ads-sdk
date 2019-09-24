import json

from urllib.parse import urlparse
from twitter_ads.v2.http import Request
from twitter_ads.v2.utils import FlattenParams, ResourceController
from twitter_ads.v2.resources import RESOURCE_TABLE


class Base(object):

    METHOD_MAP = {
        'all': 'GET',
        'load': 'GET',
        'create': 'POST',
        'update': 'PUT',
        'delete': 'DELETE',
        'batch': 'POST'
    }

    @ResourceController('accounts', override={'account_id': 'id'})
    @FlattenParams
    def accounts(self, endpoint_type, *, resource=None, **kwargs):
        """Accounts
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/accounts

        Supported `endpoint_type`:
            `all`, `load`

        Args:
            endpoint_type (str): An endpoint type.
            id (:ojb:`str`, optional): An Ads Account ID to retrieve.
                Required when `endpoint_type` is `load`.
        """
        print('called accounts()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('authenticated_user_access')
    @FlattenParams
    def authenticated_user_access(self, endpoint_type, *, resource=None, **kwargs):
        """Authenticated User Access
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/authenticated-user-access

        Supported `endpoint_type`:
            `all`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called authenticated_user_access()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('bidding_rules')
    @FlattenParams
    def bidding_rules(self, endpoint_type, *, resource=None, **kwargs):
        """Bidding Rules
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/bidding-rules

        Supported `endpoint_type`:
            `all`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called bidding_rules()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('campaigns', has_batch=True)
    @FlattenParams
    def campaigns(self, endpoint_type, *, resource=None, headers={}, data=None, **kwargs):
        """Campaigns
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/campaigns

        Supported `endpoint_type`:
            `all`, `load`, `create`, `batch`, `update`, `delete`

        Args:
            endpoint_type (str): An endpoint type.
            data (:ojb:`list`, optional): A JSON POST body data to send.
                Required when `endpoint_type` is `batch`.
        """
        print('called campaigns()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource,
                       headers=headers, body=data, params=kwargs).perform()

    @ResourceController('content_categories')
    @FlattenParams
    def content_categories(self, endpoint_type, *, resource=None, **kwargs):
        """Content Categories
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/content-categories

        Supported `endpoint_type`:
            `all`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called content_categories()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('funding_instruments')
    @FlattenParams
    def funding_instruments(self, endpoint_type, *, resource=None, **kwargs):
        """Funding Instruments
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/funding-instruments

        Supported `endpoint_type`:
            `all`, `load`, `create`, `update`, `delete`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called funding_instruments()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('iab_categories')
    @FlattenParams
    def iab_categories(self, endpoint_type, *, resource=None, **kwargs):
        """IAB Categories
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/iab-categories

        Supported `endpoint_type`:
            `all`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called iab_categories()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('line_items', has_batch=True)
    @FlattenParams
    def line_items(self, endpoint_type, *, resource=None, headers={}, data=None, **kwargs):
        """Line Items
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/line-items

        Supported `endpoint_type`:
            `all`, `load`, `create`, `batch`, `update`, `delete`

        Args:
            endpoint_type (str): An endpoint type.
            data (:ojb:`list`, optional): A JSON POST body data to send.
                Required when `endpoint_type` is `batch`.
        """
        print('called line_items()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource,
                       headers=headers, body=data, params=kwargs).perform()

    @ResourceController('line_item_apps')
    @FlattenParams
    def line_item_apps(self, endpoint_type, *, resource=None, **kwargs):
        """Line Item Apps
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/line-item-apps

        Supported `endpoint_type`:
            `all`, `load`, `create`, `delete`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called line_item_apps()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('line_item_placements')
    @FlattenParams
    def line_item_placements(self, endpoint_type, *, resource=None, **kwargs):
        """Line Item Placements
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/line-item-placements

        Supported `endpoint_type`:
            `all`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called line_item_placements()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('media_creatives')
    @FlattenParams
    def media_creatives(self, endpoint_type, *, resource=None, **kwargs):
        """Media Creatives
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/media-creatives

        Supported `endpoint_type`:
            `all`, `load`, `create`, `delete`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called media_creatives()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('promoted_accounts')
    @FlattenParams
    def promoted_accounts(self, endpoint_type, *, resource=None, **kwargs):
        """Promoted Accounts
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/promoted-accounts

        Supported `endpoint_type`:
            `all`, `load`, `create`, `delete`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called promoted_accounts()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('promoted_tweets')
    @FlattenParams
    def promoted_tweets(self, endpoint_type, *, resource=None, **kwargs):
        """Promoted Tweets
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/promoted-tweets

        Supported `endpoint_type`:
            `all`, `load`, `create`, `delete`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called promoted_tweets()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('promotable_users')
    @FlattenParams
    def promotable_users(self, endpoint_type, *, resource=None, **kwargs):
        """Promotable Users
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/promotable-users

        Supported `endpoint_type`:
            `all`, `load`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called promotable_users()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('scheduled_promoted_tweets')
    @FlattenParams
    def scheduled_promoted_tweets(self, endpoint_type, *, resource=None, **kwargs):
        """Scheduled Promoted Tweets
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/scheduled-promoted-tweets

        Supported `endpoint_type`:
            `all`, `load`, `create`, `delete`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called scheduled_promoted_tweets()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('targeting_criteria')
    @FlattenParams
    def targeting_criteria(self, endpoint_type, *, resource=None, **kwargs):
        """Targeting Criteria
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-criteria

        Supported `endpoint_type`:
            `all`, `load`, `create`, `delete`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called targeting_criteria()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('targeting_suggestions')
    @FlattenParams
    def targeting_suggestions(self, endpoint_type, *, resource=None, **kwargs):
        """Targeting Suggestions
        https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-suggestions

        Supported `endpoint_type`:
            `all`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called targeting_suggestions()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('targeting_criteria_app_store_categories', default_operation='all')
    @FlattenParams
    def targeting_criteria_app_store_categories(self, endpoint_type, *, resource=None, **kwargs):

        print('called targeting_criteria_app_store_categories()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('targeting_criteria_behavior_taxonomies', default_operation='all')
    @FlattenParams
    def targeting_criteria_behavior_taxonomies(self, endpoint_type, *, resource=None, **kwargs):

        print('called targeting_criteria_behavior_taxonomies()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('targeting_criteria_behaviors', default_operation='all')
    @FlattenParams
    def targeting_criteria_behaviors(self, endpoint_type, *, resource=None, **kwargs):

        print('called targeting_criteria_behaviors()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('targeting_criteria_conversations', default_operation='all')
    @FlattenParams
    def targeting_criteria_conversations(self, endpoint_type, *, resource=None, **kwargs):

        print('called targeting_criteria_conversations()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('targeting_criteria_devices', default_operation='all')
    @FlattenParams
    def targeting_criteria_devices(self, endpoint_type, *, resource=None, **kwargs):

        print('called targeting_criteria_devices()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('targeting_criteria_events', default_operation='all')
    @FlattenParams
    def targeting_criteria_events(self, endpoint_type, *, resource=None, **kwargs):

        print('called targeting_criteria_events()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('targeting_criteria_interests', default_operation='all')
    @FlattenParams
    def targeting_criteria_interests(self, endpoint_type, *, resource=None, **kwargs):

        print('called targeting_criteria_interests()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('targeting_criteria_languages', default_operation='all')
    @FlattenParams
    def targeting_criteria_languages(self, endpoint_type, *, resource=None, **kwargs):

        print('called targeting_criteria_languages()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('targeting_criteria_locations', default_operation='all')
    @FlattenParams
    def targeting_criteria_locations(self, endpoint_type, *, resource=None, **kwargs):

        print('called targeting_criteria_locations()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('targeting_criteria_network_operators', default_operation='all')
    @FlattenParams
    def targeting_criteria_network_operators(self, endpoint_type, *, resource=None, **kwargs):

        print('called targeting_criteria_network_operators()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('targeting_criteria_platform_versions', default_operation='all')
    @FlattenParams
    def targeting_criteria_platform_versions(self, endpoint_type, *, resource=None, **kwargs):

        print('called targeting_criteria_platform_versions()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('targeting_criteria_platforms', default_operation='all')
    @FlattenParams
    def targeting_criteria_platforms(self, endpoint_type, *, resource=None, **kwargs):

        print('called targeting_criteria_platforms()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('targeting_criteria_tv_markets', default_operation='all')
    @FlattenParams
    def targeting_criteria_tv_markets(self, endpoint_type, *, resource=None, **kwargs):

        print('called targeting_criteria_tv_markets()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('targeting_criteria_tv_shows', default_operation='all')
    @FlattenParams
    def targeting_criteria_tv_shows(self, endpoint_type, *, resource=None, **kwargs):

        print('called targeting_criteria_tv_shows()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()







    @ResourceController('account_media')
    @FlattenParams
    def account_media(self, endpoint_type, *, resource=None, **kwargs):
        """Account Media
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/account-media

        Supported `endpoint_type`:
            `all`, `load`, `delete`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called account_media()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('scheduled_tweets')
    @FlattenParams
    def scheduled_tweets(self, endpoint_type, *, resource=None, **kwargs):
        """Scheduled Tweets
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/scheduled-tweets

        Supported `endpoint_type`:
            `all`, `load`, `create`, `update`, `delete`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called scheduled_tweets()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('draft_tweets')
    @FlattenParams
    def draft_tweets(self, endpoint_type, *, resource=None, **kwargs):
        """Draft Tweets
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/draft-tweets

        Supported `endpoint_type`:
            `all`, `load`, `create`, `update`, `delete`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called draft_tweets()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    def draft_tweets_preview(self, endpoint_type='create', *,
                             resource=None, draft_tweet_id):
        """Draft Tweets Preview
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/draft-tweets#post-accounts-account-id-draft-tweets-preview-draft-tweet-id

        Supported `endpoint_type`:
            `create` (default)

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
            draft_tweet_id (str): A Draft Tweet ID to preview.
        """
        print('called draft_tweets_preview()')
        base = RESOURCE_TABLE['draft_tweets_preview']['RESOURCE']
        resource = base.format(account_id=self.account_id, id=draft_tweet_id)
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params={}).perform()

    @FlattenParams
    def tweets(self, endpoint_type, *, resource=None, **kwargs):
        """Tweets
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/tweets

        Supported `endpoint_type`:
            `all`, `create`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called tweets()')
        if endpoint_type == 'all':
            base = RESOURCE_TABLE['tweets']['RESOURCE_GET']
        else:
            base = RESOURCE_TABLE['tweets']['RESOURCE_POST']
        resource = base.format(account_id=self.account_id)
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('tweet_previews', default_operation='all')
    @FlattenParams
    def tweet_previews(self, endpoint_type, *, resource=None, **kwargs):
        """Tweet Previews
        https://developer.twitter.com/en/docs/ads/creatives/api-reference/tweet-previews

        Supported `endpoint_type`:
            `all`

        Args:
            endpoint_type (:obj:`str`, optional): An endpoint type.
        """
        print('called tweet_previews()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()






    @ResourceController('active_entities', default_operation='all')
    @FlattenParams
    def active_entities(self, endpoint_type, *, resource=None, **kwargs):
        """Active Entities
        https://developer.twitter.com/en/docs/ads/analytics/api-reference/active-entities

        Supported `endpoint_type`:
            `all` (default)

        Args:
            endpoint_type (:ojb:`str`, optional): An endpoint type.
        """
        print('called active_entities()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('analytics_sync_stats', default_operation='all')
    @FlattenParams
    def analytics_sync_stats(self, endpoint_type, *, resource=None, **kwargs):
        """Synchronous Analytics
        https://developer.twitter.com/en/docs/ads/analytics/api-reference/synchronous

        Supported `endpoint_type`:
            `all` (default)

        Args:
            endpoint_type (:ojb:`str`, optional): An endpoint type.
        """

        # TODO: some helper functions here?
        print('called analytics_sync_stats()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('analytics_async_jobs')
    @FlattenParams
    def analytics_async_jobs(self, endpoint_type, *, resource=None, **kwargs):
        """Asynchronous Analytics
        Retrieve details for some or all asynchronous analytics jobs for the current account.
        https://developer.twitter.com/en/docs/ads/analytics/api-reference/asynchronous#get-stats-jobs-accounts-account-id
        Cancel an asynchronous analytics job for a given ads account.
        https://developer.twitter.com/en/docs/ads/analytics/api-reference/asynchronous#delete-stats-jobs-accounts-account-id-job-id

        Supported `endpoint_type`:
            `all`, `delete`

        Args:
            endpoint_type (str): An endpoint type.
        """

        # TODO: some helper functions here?
        print('called analytics_async_jobs()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    @ResourceController('analytics_async_create_job', default_operation='create')
    @FlattenParams
    def analytics_async_create_job(self, endpoint_type, *, resource=None, **kwargs):
        """Asynchronous Analytics
        Create an asynchronous analytics job for the current account.
        https://developer.twitter.com/en/docs/ads/analytics/api-reference/asynchronous#post-stats-jobs-accounts-account-id

        Supported `endpoint_type`:
            `create` (default)

        Args:
            endpoint_type (:ojb:`str`, optional): An endpoint type.
        """

        # TODO: some helper functions here?
        print('called analytics_async_create_job()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    def analytics_async_job_data(self, endpoint_type='load', *, url):
        """Returns the results of the specified async job data URL.

        Supported `endpoint_type`:
            `load`

        Args:
            endpoint_type (str): An endpoint type.
            url (str): A job data URL to download.
        """
        print('called analytics_async_job_data()')
        # TODO: some helper functions here?
        resource = urlparse(url)
        domain = '{0}://{1}'.format(resource.scheme, resource.netloc)
        print(domain)
        print(resource.path)
        return Request(
            self,
            self.METHOD_MAP[endpoint_type],
            resource.path,
            domain=domain,
            raw_body=True,
            stream=True).perform()





    @ResourceController('tailored_audiences')
    @FlattenParams
    def tailored_audiences(self, endpoint_type, *, resource=None, **kwargs):
        """Tailored Audiences
        https://developer.twitter.com/en/docs/ads/audiences/api-reference/tailored-audiences

        Supported `endpoint_type`:
            `all`, `load`, `create`, `delete`

        Args:
            endpoint_type (str): An endpoint type.
        """
        print('called tailored_audiences()')
        return Request(self, self.METHOD_MAP[endpoint_type], resource, params=kwargs).perform()

    def tailored_audiences_users(self, endpoint_type='create', *,
                                 resource=None, tailored_audience_id, data=[]):
        """Tailored Audiences Users
        https://developer.twitter.com/en/docs/ads/audiences/api-reference/audience

        Supported `endpoint_type`:
            `create`

        Args:
            endpoint_type (str): An endpoint type.
            tailored_audience_id (str): A Tailored Audience ID to update.
            data (list): A JSON POST body data to send.
        """
        print('called tailored_audiences_users()')
        base = RESOURCE_TABLE['tailored_audiences_users']['RESOURCE']
        resource = base.format(account_id=self.account_id, id=tailored_audience_id)
        return Request(
            self,
            self.METHOD_MAP[endpoint_type],
            resource,
            headers={'content-type': 'application/json'},
            params={},
            body=json.dumps(data)).perform()

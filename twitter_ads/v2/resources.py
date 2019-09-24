"""Container for all enum values used by the Ads API SDK."""


RESOURCE_TABLE = {
    'accounts': {
        'RESOURCE': 'accounts/{account_id}',
        'RESOURCE_COLLECTION': 'accounts'
    },
    'authenticated_user_access': {
        'RESOURCE_COLLECTION': 'accounts/{account_id}/authenticated_user_access'
    },
    'bidding_rules': {
        'RESOURCE_COLLECTION': 'bidding_rules'
    },
    'campaigns': {
        'BATCH': 'batch/accounts/{account_id}/campaigns',
        'RESOURCE': 'accounts/{account_id}/campaigns/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/campaigns'
    },
    'content_categories': {
        'RESOURCE_COLLECTION': 'content_categories'
    },
    'funding_instruments': {
        'RESOURCE': 'accounts/{account_id}/funding_instruments/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/funding_instruments'
    },
    'iab_categories': {
        'RESOURCE_COLLECTION': 'iab_categories'
    },
    'line_items': {
        'BATCH': 'batch/accounts/{account_id}/line_items',
        'RESOURCE': 'accounts/{account_id}/line_items/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/line_items'
    },
    'line_item_placements': {
        'RESOURCE_COLLECTION': 'line_items/placements'
    },
    'line_item_apps': {
        'RESOURCE': 'accounts/{account_id}/line_item_apps/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/line_item_apps'
    },
    'media_creatives': {
        'RESOURCE': 'accounts/{account_id}/media_creatives/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/media_creatives'
    },
    'promoted_accounts': {
        'RESOURCE': 'accounts/{account_id}/promoted_accounts/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/promoted_accounts'
    },
    'promoted_tweets': {
        'RESOURCE': 'accounts/{account_id}/promoted_tweets/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/promoted_tweets'
    },
    'promotable_users': {
        'RESOURCE': 'accounts/{account_id}/promotable_users/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/promotable_users'
    },
    'scheduled_promoted_tweets': {
        'RESOURCE': 'accounts/{account_id}/scheduled_promoted_tweets/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/scheduled_promoted_tweets'
    },
    'targeting_criteria': {
        'RESOURCE': 'accounts/{account_id}/targeting_criteria/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/targeting_criteria'
    },
    'targeting_suggestions': {
        'RESOURCE_COLLECTION': 'accounts/{account_id}/targeting_suggestions'
    },
    'targeting_criteria_app_store_categories': {
        'RESOURCE_COLLECTION': 'targeting_criteria/app_store_categories'
    },
    'targeting_criteria_behavior_taxonomies': {
        'RESOURCE_COLLECTION': 'targeting_criteria/behavior_taxonomies'
    },
    'targeting_criteria_behaviors': {
        'RESOURCE_COLLECTION': 'targeting_criteria/behaviors'
    },
    'targeting_criteria_conversations': {
        'RESOURCE_COLLECTION': 'targeting_criteria/conversations'
    },
    'targeting_criteria_devices': {
        'RESOURCE_COLLECTION': 'targeting_criteria/devices'
    },
    'targeting_criteria_events': {
        'RESOURCE_COLLECTION': 'targeting_criteria/events'
    },
    'targeting_criteria_interests': {
        'RESOURCE_COLLECTION': 'targeting_criteria/interests'
    },
    'targeting_criteria_languages': {
        'RESOURCE_COLLECTION': 'targeting_criteria/languages'
    },
    'targeting_criteria_locations': {
        'RESOURCE_COLLECTION': 'targeting_criteria/locations'
    },
    'targeting_criteria_network_operators': {
        'RESOURCE_COLLECTION': 'targeting_criteria/network_operators'
    },
    'targeting_criteria_platform_versions': {
        'RESOURCE_COLLECTION': 'targeting_criteria/platform_versions'
    },
    'targeting_criteria_platforms': {
        'RESOURCE_COLLECTION': 'targeting_criteria/platforms'
    },
    'targeting_criteria_tv_markets': {
        'RESOURCE_COLLECTION': 'targeting_criteria/tv_markets'
    },
    'targeting_criteria_tv_shows': {
        'RESOURCE_COLLECTION': 'targeting_criteria/tv_shows'
    },
    'account_media': {
        'RESOURCE': 'accounts/{account_id}/account_media/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/account_media'
    },
    'scheduled_tweets': {
        'RESOURCE': 'accounts/{account_id}/scheduled_tweets/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/scheduled_tweets'
    },
    'draft_tweets': {
        'RESOURCE': 'accounts/{account_id}/draft_tweets/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/draft_tweets'
    },
    'draft_tweets_preview': {
        'RESOURCE': 'accounts/{account_id}/draft_tweets/preview/{id}',
    },
    'tweets': {
        'RESOURCE_GET': 'accounts/{account_id}/tweets',
        'RESOURCE_POST': 'accounts/{account_id}/tweet',
    },
    'tweet_previews': {
        'RESOURCE_COLLECTION': 'accounts/{account_id}/tweet_previews'
    },
    'active_entities': {
        'RESOURCE_COLLECTION': 'stats/accounts/{account_id}/active_entities'
    },
    'analytics_sync_stats': {
        'RESOURCE_COLLECTION': 'stats/accounts/{account_id}'
    },
    'analytics_async_jobs': {
        'RESOURCE': 'stats/jobs/accounts/{account_id}/{id}',
        'RESOURCE_COLLECTION': 'stats/jobs/accounts/{account_id}'
    },
    'tailored_audiences': {
        'RESOURCE': 'accounts/{account_id}/tailored_audiences/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/tailored_audiences'
    },
    'tailored_audiences_users': {
        'RESOURCE': 'accounts/{account_id}/tailored_audiences/{id}/users'
    }
}

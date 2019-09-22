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
    'targeting_criteria_locations': {
        'RESOURCE_COLLECTION': 'targeting_criteria/locations'
    },
    'active_entities': {
        'RESOURCE_COLLECTION': 'stats/accounts/{account_id}/active_entities'
    },
    'tailored_audiences': {
        'RESOURCE': 'accounts/{account_id}/tailored_audiences/{id}',
        'RESOURCE_COLLECTION': 'accounts/{account_id}/tailored_audiences'
    },
    'tailored_audiences_users': {
        'RESOURCE': 'accounts/{account_id}/tailored_audiences/{id}/users'
    }
}

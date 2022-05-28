from tecton import batch_feature_view, Aggregation
from entities import user, merchant
from data_sources.transactions import transactions
from datetime import datetime, timedelta


@batch_feature_view(
    sources=[transactions],
    entities=[merchant],
    mode='snowflake_sql',
    aggregation_interval=timedelta(days=1),
    aggregations=[
        Aggregation(column='IS_FRAUD', function='mean', time_window=timedelta(days=1)),
        Aggregation(column='IS_FRAUD', function='mean', time_window=timedelta(days=3)),
        Aggregation(column='IS_FRAUD', function='mean', time_window=timedelta(days=7)),
        Aggregation(column='IS_FRAUD', function='mean', time_window=timedelta(days=40)),
    ],
    online=True,
    feature_start_time=datetime(2020, 10, 10),
    owner='david@tecton.ai',
    description='Merchant fraud rate over various time windows, updated daily.'
)
def merchant_fraud_rate(transactions):
    return f'''
        SELECT
            MERCHANT,
            IS_FRAUD,
            TIMESTAMP
        FROM
            {transactions}
        '''

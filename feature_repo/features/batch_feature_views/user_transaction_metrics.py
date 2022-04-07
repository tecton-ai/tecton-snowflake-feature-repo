from tecton import batch_feature_view, FeatureAggregation
from entities import user
from data_sources.transactions import transactions
from datetime import datetime


@batch_feature_view(
    sources=[transactions],
    entities=[user],
    mode='snowflake_sql',
    aggregation_slide_period='1d',
    aggregations=[
        FeatureAggregation(column='TRANSACTION', function='sum', time_windows=['24h','72h','168h', '960h']),
        FeatureAggregation(column='AMT', function='mean', time_windows=['24h','72h','168h', '960h']),
    ],
    online=True,
    feature_start_time=datetime(2020, 10, 10),
    owner='david@tecton.ai',
    description='User transaction totals over a series of time windows, updated daily.'
)
def user_transaction_metrics(transactions):
    return f'''
        SELECT
            USER_ID,
            1 as TRANSACTION,
            AMT,
            TIMESTAMP
        FROM
            {transactions}
        '''

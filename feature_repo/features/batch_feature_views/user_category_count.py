from tecton import batch_feature_view, Aggregation
from entities import user, category
from data_sources.transactions import transactions
from datetime import datetime, timedelta


@batch_feature_view(
    sources=[transactions],
    entities=[user, category],
    mode='snowflake_sql',
    aggregation_interval=timedelta(days=1),
    aggregations=[
        Aggregation(column='TRANSACTION', function='sum', time_window=timedelta(days=1)),
        Aggregation(column='TRANSACTION', function='sum', time_window=timedelta(days=3)),
        Aggregation(column='TRANSACTION', function='sum', time_window=timedelta(days=7)),
        Aggregation(column='TRANSACTION', function='sum', time_window=timedelta(days=40))
    ],
    online=True,
    feature_start_time=datetime(2020, 10, 10),
    owner='david@tecton.ai',
    description='User transaction totals over a series of time windows, updated daily.'
)
def user_category_count(transactions):
    return f'''
        SELECT
            USER_ID,
            CATEGORY,
            1 as TRANSACTION,
            TIMESTAMP
        FROM
            {transactions}
        '''

from tecton import batch_feature_view, Aggregation
from entities import user
from data_sources.transactions import transactions
from datetime import datetime, timedelta


@batch_feature_view(
    sources=[transactions],
    entities=[user],
    mode='snowflake_sql',
    aggregation_interval=timedelta(days=1),
    aggregations=[
        Aggregation(column='TRANSACTION', function='sum', time_window=timedelta(days=1)),
        Aggregation(column='TRANSACTION', function='sum', time_window=timedelta(days=3)),
        Aggregation(column='TRANSACTION', function='sum', time_window=timedelta(days=7)),
        Aggregation(column='TRANSACTION', function='sum', time_window=timedelta(days=40)),
        Aggregation(column='AMT', function='mean', time_window=timedelta(days=1)),
        Aggregation(column='AMT', function='mean', time_window=timedelta(days=3)),
        Aggregation(column='AMT', function='mean', time_window=timedelta(days=7)),
        Aggregation(column='AMT', function='mean', time_window=timedelta(days=40)),
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

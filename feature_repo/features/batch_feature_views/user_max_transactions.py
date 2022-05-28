from tecton import batch_feature_view, Aggregation
from entities import user
from data_sources.transactions import transactions
from datetime import datetime, timedelta


# @batch_feature_view(
#     sources=[transactions],
#     entities=[user],
#     mode='snowflake_sql',
#     online=True,
#     feature_start_time=datetime(2021, 5, 20),
#     description='Max transaction amounts for the user in various time windows',
#     aggregation_interval=timedelta(days=1),
#     aggregations=[
#         Aggregation(column='AMT', function='max', time_window=timedelta(days=1)),
#         Aggregation(column='AMT', function='max', time_window=timedelta(days=30)),
#         Aggregation(column='AMT', function='max', time_window=timedelta(days=180)),
#     ],)
# def user_max_transactions(transactions):
#     return f'''
#         SELECT
#             USER_ID,
#             AMT,
#             TIMESTAMP
#         FROM
#             {transactions}
#         '''

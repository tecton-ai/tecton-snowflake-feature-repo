from tecton import batch_feature_view, FeatureAggregation
from entities import user
from data_sources.transactions import transactions
from datetime import datetime


# @batch_feature_view(
#     sources=[transactions],
#     entities=[user],
#     mode='snowflake_sql',
#     online=True,
#     feature_start_time=datetime(2021, 5, 20),
#     description='Max transaction amounts for the user in various time windows',
#     aggregation_slide_period='1d',
#     aggregations=[FeatureAggregation(column='AMT', function='max', time_windows=['1d','30d','180d'])],
# )
# def user_max_transactions(transactions):
#     return f'''
#         SELECT
#             USER_ID,
#             AMT,
#             TIMESTAMP
#         FROM
#             {transactions}
#         '''

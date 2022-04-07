from tecton import batch_feature_view
from entities import user
from data_sources.transactions import transactions
from datetime import datetime


# @batch_feature_view(
#     sources=[transactions],
#     entities=[user],
#     mode='snowflake_sql',
#     online=True,
#     batch_schedule='1d',
#     ttl='30days',
#     feature_start_time=datetime(2021, 5, 20),
#     description='Last user transaction amount (batch calculated)'
# )
# def user_last_transaction_amount(transactions):
#     return f'''
#         SELECT
#             USER_ID,
#             AMT,
#             TIMESTAMP
#         FROM
#             {transactions}
#         '''

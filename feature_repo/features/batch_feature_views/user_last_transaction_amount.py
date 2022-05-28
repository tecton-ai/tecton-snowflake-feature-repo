from tecton import batch_feature_view
from entities import user
from data_sources.transactions import transactions
from datetime import datetime, timedelta


# @batch_feature_view(
#     sources=[transactions],
#     entities=[user],
#     mode='snowflake_sql',
#     online=True,
#     batch_schedule=timedelta(days=1),
#     ttl=timedelta(days=30),
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

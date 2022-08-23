from tecton import batch_feature_view, materialization_context
from datetime import datetime, timedelta
from entities import user
from data_sources.transactions import transactions


# This feature view must have materialization turned on. In order to test it, please apply to a live workspace.
@batch_feature_view(
    sources=[transactions],
    entities=[user],
    mode='snowflake_sql',
    online=True,
    offline=True,
    batch_schedule=timedelta(days=1),
    feature_start_time=datetime(2022, 3, 10),
    ttl=timedelta(days=1),
    incremental_backfills=True
)
def user_distinct_merchant_transaction_count_7d(transactions, context=materialization_context()):
    return f'''
        SELECT
            USER_ID,
            TO_TIMESTAMP('{context.end_time}') - INTERVAL '1 MICROSECOND' as TIMESTAMP,
            COUNT(DISTINCT MERCHANT) AS DISTINCT_MERCHANT_COUNT_7D
        FROM
            {transactions}
        WHERE TIMESTAMP >= TO_TIMESTAMP('{context.start_time}') - INTERVAL '6 DAYS' AND TIMESTAMP < TO_TIMESTAMP('{context.end_time}')
        GROUP by USER_ID'''

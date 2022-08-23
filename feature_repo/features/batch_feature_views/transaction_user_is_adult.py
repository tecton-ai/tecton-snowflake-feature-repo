from tecton import batch_feature_view, FilteredSource
from entities import user
from data_sources.users import users
from data_sources.transactions import transactions
from datetime import datetime, timedelta


# For every transaction, the following FeatureView precomputes a feature that indicates
# whether a user was an adult as of the time of the transaction
@batch_feature_view(
    sources=[FilteredSource(transactions), users],
    name="transaction_made_by_adult",
    entities=[user],
    mode='snowflake_sql',
    online=False,
    offline=False,
    feature_start_time=datetime(2022, 5, 1),
    batch_schedule=timedelta(days=1),
    ttl=timedelta(days=100),
    timestamp_field="TIMESTAMP",
    description='Whether the user performing the transaction is over 18 years old.'
)
def transaction_user_is_adult(transactions, users):
    return f'''
        select
          timestamp,
          t.user_id,
          IFF(datediff(day, timestamp, dob) > (18*365), TRUE, FALSE) as user_is_adult
        from {transactions} t join {users} u on t.user_id=u.user_id
    '''

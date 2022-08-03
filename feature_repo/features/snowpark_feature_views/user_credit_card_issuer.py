from tecton import batch_feature_view
from entities import user
from data_sources.users import users
from datetime import datetime, timedelta

@batch_feature_view(
    sources=[users],
    entities=[user],
    mode='snowpark',
    online=True,
    feature_start_time=datetime(2017, 1, 1),
    batch_schedule=timedelta(days=1),
    ttl=timedelta(days=3650),
)
def user_credit_card_issuer(users):
    from snowflake.snowpark.functions import when, col, substring
    from snowflake.snowpark.types import StringType

    cc_id = substring(col('CC_NUM').cast(StringType()), 0, 1)
    df = users.withColumn('CREDIT_CARD_ISSUER', when(cc_id == '3','AmEx') \
                                               .when(cc_id == '4','Visa') \
                                               .when(cc_id == '5','MasterCard') \
                                               .when(cc_id == '6','Discover')
                                               .otherwise('Other')) \
                .select('USER_ID', 'SIGNUP_TIMESTAMP', 'CREDIT_CARD_ISSUER')
    return df
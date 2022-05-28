from tecton import batch_feature_view
from entities import user
from data_sources.users import users
from datetime import datetime, timedelta


@batch_feature_view(
    sources=[users],
    entities=[user],
    mode='snowflake_sql',
    # online=True,
    # feature_start_time=datetime(2017,1, 1),
    batch_schedule=timedelta(days=1),
    ttl=timedelta(days=365 * 10),
    timestamp_field="SIGNUP_TIMESTAMP",
    description='User date of birth, entered at signup.',
)
def user_date_of_birth(users):
    return f'''
        SELECT
            USER_ID,
            TO_CHAR(DOB) as DATE_OF_BIRTH,
            SIGNUP_TIMESTAMP
        FROM
            {users}
        '''

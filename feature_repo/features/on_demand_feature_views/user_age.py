from tecton import RequestSource, on_demand_feature_view
from features.batch_feature_views.user_date_of_birth import user_date_of_birth
from tecton.types import String, Int64, Field

# On-Demand Feature Views require enabling Snowpark.
# Contact Tecton for assistance in enabling this feature.


# request = RequestSource(schema=[Field('timestamp', String)])
#
# @on_demand_feature_view(
#     sources=[request, user_date_of_birth],
#     mode='python',
#     schema=[Field('user_age', Int64)],
#     owner='matt@tecton.ai',
#     tags={'release': 'production'},
#     description="The user's age in days."
# )
# def user_age(request, user_date_of_birth):
#     from datetime import datetime, date
#
#     request_datetime = datetime.fromisoformat(request['timestamp']).replace(tzinfo=None)
#     dob_datetime = datetime.fromisoformat(user_date_of_birth['USER_DATE_OF_BIRTH'])
#
#     td = request_datetime - dob_datetime
#
#     return {'user_age': td.days}

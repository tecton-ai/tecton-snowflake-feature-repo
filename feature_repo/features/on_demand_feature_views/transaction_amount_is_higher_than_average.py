from tecton import RequestSource, on_demand_feature_view
from features.batch_feature_views.user_transaction_metrics import user_transaction_metrics
from tecton.types import Float64, Bool, Field

# On-Demand Feature Views require enabling Snowpark.
# Contact Tecton for assistance in enabling this feature.


# transaction_request = RequestSource(schema=[Field('AMT', Float64)])
#
# @on_demand_feature_view(
#     sources=[transaction_request, user_transaction_metrics],
#     mode='python',
#     schema=[Field('transaction_amount_is_higher_than_average', Bool)],
#     description='The transaction amount is higher than the 1 day average.'
# )
# def transaction_amount_is_higher_than_average(transaction_request, user_transaction_metrics):
#     amount_mean = 0 if user_transaction_metrics['AMT_MEAN_24H_1D'] == None else user_transaction_metrics['AMT_MEAN_24H_1D']
#     return {'transaction_amount_is_higher_than_average': transaction_request['AMT'] > amount_mean}

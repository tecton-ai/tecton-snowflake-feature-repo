from tecton import FeatureService
from features.batch_feature_views.user_transaction_metrics import user_transaction_metrics
from features.batch_feature_views.user_category_count import user_category_count
from features.batch_feature_views.merchant_fraud_rate import merchant_fraud_rate


fraud_detection_feature_service = FeatureService(
    name='fraud_detection_feature_service',
    features=[
        user_transaction_metrics,
        user_category_count
    ]
)

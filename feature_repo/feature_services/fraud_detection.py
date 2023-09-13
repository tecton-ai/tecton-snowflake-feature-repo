from tecton import FeatureService
from features.on_demand_feature_views.similarity import fuzzy_similarity


fraud_detection_feature_service = FeatureService(
    name='fraud_detection_feature_service',
    on_demand_environment="tecton-python-snowpark:0.1",
    online_serving_enabled=True,
    features=[
        fuzzy_similarity
    ]
)

from datetime import timedelta, datetime
from tecton import StreamFeatureView, BatchTriggerType, Aggregation,RedisConfig
from entities import user
from data_sources.users_push import users_push_source

users_city_pop_push_fv = StreamFeatureView(
    name="users_city_pop_push_fv",
    source=users_push_source,
    entities=[user],
    online=True,
    offline=False,
    feature_start_time=datetime(2023, 1, 1),
    ttl=timedelta(days=30),
    batch_schedule=timedelta(days=1),
    tags={'release': 'production'},
    owner='pooja@tecton.ai',
    description='City population for user'
)
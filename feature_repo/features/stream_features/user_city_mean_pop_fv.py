from datetime import timedelta, datetime
from tecton import StreamFeatureView, BatchTriggerType, Aggregation, RedisConfig
from entities import user
from data_sources.users_push import users_push_source

users_city_mean_pop_fv = StreamFeatureView(
    name="users_city_mean_pop_fv",
    source=users_push_source,
    entities=[user],
    online=True,
    offline=False,
    feature_start_time=datetime(2023, 1, 1),
    aggregations=[
         Aggregation(column='CITY_POP', function='mean', time_window=timedelta(days=1)),
         Aggregation(column='CITY_POP', function='mean', time_window=timedelta(days=30)),
         Aggregation(column='CITY_POP', function='mean', time_window=timedelta(days=60)),
    ],
    batch_schedule=timedelta(days=1),
    tags={'release': 'production'},
    owner='pooja@tecton.ai',
    description='City population for user'
)
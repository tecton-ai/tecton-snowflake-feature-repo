from tecton import SnowflakeConfig, PushSource
from tecton.types import Field, Int64, String, Timestamp

push_schema = [
    Field(name="USER_ID", dtype=String),
    Field(name="TIMESTAMP", dtype=Timestamp),
    Field(name="CITY_POP", dtype=Int64),
]

users_push_source = PushSource(
    name="users_push_source",
    schema=push_schema,
    batch_config=SnowflakeConfig(
        table="USERS",
        query="""
        select SIGNUP_TIMESTAMP AS TIMESTAMP,USER_ID, CITY_POP from TECTON_DEMO_DATA.FRAUD_DEMO.USERS
      """
    ),
)

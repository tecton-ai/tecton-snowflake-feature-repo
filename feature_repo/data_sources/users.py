from tecton import BatchSource, SnowflakeConfig
from datetime import datetime


users = BatchSource(
    name="users",
    batch_config=SnowflakeConfig(
      database="TECTON_DEMO_DATA",
      schema="FRAUD_DEMO",
      table="USERS",
    ),
)

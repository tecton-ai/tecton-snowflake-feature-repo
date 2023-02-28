from tecton import BatchSource, SnowflakeConfig
from datetime import datetime


transactions = BatchSource(
    name="transactions",
    batch_config=SnowflakeConfig(
      database="TECTON_DEMO_DATA",
      schema="FRAUD_DEMO",
      table="TRANSACTIONS",
      timestamp_field="TIMESTAMP"
    ),
)

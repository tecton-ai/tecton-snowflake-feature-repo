from tecton import BatchSource, SnowflakeConfig

snowflake_bve_batchsource = BatchSource(
    name="snowflake_bve_batchsource",
    batch_config=SnowflakeConfig(
        database="MONEYLION",
        schema="PUBLIC",
        table="BVE",
        timestamp_field="TRANSACTION_DATE"
    )
)
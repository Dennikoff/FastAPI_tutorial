import datetime
from sqlalchemy import TIMESTAMP, Column, Float, Integer, MetaData, String, Table

metadata = MetaData()

operations = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("tiker", String),
    Column("amount", Float),
    Column("created_at", TIMESTAMP, default=datetime.datetime.now(datetime.timezone.utc)),
)
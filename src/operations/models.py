from sqlalchemy import Column, Integer, MetaData, Table

metadata = MetaData()

operations = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("tiker", Integer, primary_key=True),
    Column("", Integer, primary_key=True),
    Column("id", Integer, primary_key=True),
    Column("id", Integer, primary_key=True),
    Column("id", Integer, primary_key=True),
)
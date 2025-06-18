from pyiceberg.catalog import load_catalog
import pyarrow.parquet as pq

warehouse_path = "iceberg-catalog"
catalog = load_catalog(
    "default",
    **{
        'type': 'sql',
        "uri": f"sqlite:///{warehouse_path}/pyiceberg_catalog.db",
        "warehouse": f"file://{warehouse_path}",
    },
)


#read
df = pq.read_table("data/fhvhv_tripdata_2023-05.parquet")

#create a table:
catalog.create_namespace("default")
table = catalog.create_table(
    "default.taxi_dataset",
    schema=df.schema,
)

# add data
table.append(df)
len(table.scan().to_arrow())


import pyarrow.compute as pc
df = df.append_column("tip_per_mile", pc.divide(df["tips"], df["trip_miles"]))

# Evolve the schema
with table.update_schema() as update_schema:
    update_schema.union_by_name(df.schema)

#write table
table.overwrite(df)
print(table.scan().to_arrow())

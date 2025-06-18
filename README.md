# rill-nyc-taxi

Rill demo project showing an interactive, exploratory dashboard of NYC Taxi and Limousine trip record data. This demo showcases Rill's capabilities for creating fast, interactive dashboards and is used for blog demonstrations on [rilldata.com/blog](https://rilldata.com/blog).

## Data Sources

This project uses two main data sources:

### NYC Taxi Trip Data (`sources/nyc_trips.yaml`)
- **Type**: Parquet file containing For-Hire Vehicle High Volume trip records
- **Data**: Trip data from May 2023 including request datetime, trip miles, trip time, driver pay, tips, and pickup/dropoff location IDs
- **Source**: NYC TLC trip record data
- Download data yourself: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- Use hosted data to directly query with DuckDB: https://github.com/toddwschneider/nyc-taxi-data/blob/master/setup_files/raw_data_urls.txt

### NYC Taxi Zones (`sources/zones.yaml`)
- **Type**: CSV file containing taxi zone lookup information
- **Data**: Mapping of LocationIDs to borough, zone, and service zone information
- **Source**: NYC TLC zone lookup data

## Local vs Remote Mode

The project is configured to work in both local and remote modes:

- **Remote Mode** (current): Data is loaded directly from cloud storage URLs for easy setup and sharing
- **Local Mode** (commented out): Data can be loaded from local files in the `data/` directory for offline development

To switch between modes, uncomment the local SQL queries and comment out the remote ones in the source YAML files.

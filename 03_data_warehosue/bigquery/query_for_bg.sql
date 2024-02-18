-- Creating external table referring to gcs path
--CREATE OR REPLACE EXTERNAL TABLE `macro-topic-412617.ny_taxi.external_green_tripdata`
--OPTIONS (
--  format = 'parquet',
--  uris = ['gs://mage_zoomcamp_bucket_02/green_taxi_data/2022_green_taxi_data/*.parquet']
--);

--SELECT COUNT(DISTINCT PULocationID) AS distinct_pu_location_count
--FROM `macro-topic-412617.ny_taxi.green_tripdata_2022`;

--SELECT COUNT(DISTINCT PULocationID) AS distinct_pu_location_count
--FROM `macro-topic-412617.ny_taxi.external_green_tripdata_2022`;

--SELECT COUNT(*) AS zero_fare_count
--FROM `macro-topic-412617.ny_taxi.external_green_tripdata_2022`
--WHERE fare_amount = 0;

--CREATE TABLE `macro-topic-412617.ny_taxi.partitioned_clustered_green_tripdata_2022`
--PARTITION BY DATE(lpep_pickup_datetime)
--CLUSTER BY PUlocationID AS
--SELECT * FROM `macro-topic-412617.ny_taxi.green_tripdata_2022`;

--This query will process 12.82 MB when run
--SELECT DISTINCT PULocationID
--FROM `macro-topic-412617.ny_taxi.green_tripdata_2022`
--WHERE lpep_pickup_datetime BETWEEN '2022-06-01T00:00:00' AND '2022-06-30T23:59:59';

--This query will process 1.12 MB when run.
SELECT DISTINCT PULocationID
FROM `macro-topic-412617.ny_taxi.partitioned_clustered_green_tripdata_2022`
WHERE lpep_pickup_datetime BETWEEN '2022-06-01T00:00:00' AND '2022-06-30T23:59:59';

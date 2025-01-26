# This script processes data using PySpark and stores cleaned data in S3
from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("DataProcessing").getOrCreate()

# Read data from S3
s3_bucket = 's3a://hotel-revenue-data/'
data = spark.read.json(s3_bucket)

def clean_data(df):
    return (
        df.na.drop()
          .withColumnRenamed("arrival_date_year", "year")
          .withColumnRenamed("arrival_date_month", "month")
          .filter(df["is_canceled"] == 0)
    )

# Clean and save data
cleaned_data = clean_data(data)
output_path = 's3a://cleaned-hotel-data/'
cleaned_data.write.parquet(output_path)
print(f"Cleaned data saved to {output_path}")

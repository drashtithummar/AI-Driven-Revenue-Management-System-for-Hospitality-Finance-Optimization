# This script forecasts demand using PySpark MLlib
from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler

# Initialize Spark Session
spark = SparkSession.builder.appName("DemandForecasting").getOrCreate()

# Read cleaned data from S3
data = spark.read.parquet('s3a://cleaned-hotel-data/')

# Feature Engineering
assembler = VectorAssembler(inputCols=['lead_time', 'length_of_stay'], outputCol='features')
data = assembler.transform(data)

# Train-Test Split
train, test = data.randomSplit([0.8, 0.2], seed=1234)

# Model Training
lr = LinearRegression(featuresCol='features', labelCol='adr')
model = lr.fit(train)

# Model Evaluation
predictions = model.transform(test)
predictions.select('adr', 'prediction').show()

# This script calculates optimal pricing using demand forecasts
import boto3
import pandas as pd

# Load Predictions from S3
s3 = boto3.client('s3')
predictions_file = 's3://cleaned-hotel-data/predictions.csv'
obj = s3.get_object(Bucket='hotel-revenue-data', Key='predictions.csv')

# Load Data
predictions = pd.read_csv(obj['Body'])

def optimize_price(demand, base_price=100):
    if demand > 80:
        return base_price * 1.2
    elif demand < 30:
        return base_price * 0.8
    else:
        return base_price

# Apply Optimization
predictions['optimized_price'] = predictions['demand'].apply(optimize_price)
predictions.to_csv('optimized_prices.csv', index=False)
s3.upload_file('optimized_prices.csv', 'hotel-revenue-data', 'optimized_prices.csv')
print("Optimized pricing saved to S3")

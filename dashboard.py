# This script provides a Streamlit dashboard for visualization
import streamlit as st
import pandas as pd
import boto3

# Load Data from S3
s3 = boto3.client('s3')
obj = s3.get_object(Bucket='hotel-revenue-data', Key='optimized_prices.csv')
data = pd.read_csv(obj['Body'])

# Streamlit Dashboard
st.title("Hotel Revenue Management Dashboard")
st.write("### Optimized Prices and Demand")
st.dataframe(data)

st.line_chart(data[['date', 'optimized_price']])
```

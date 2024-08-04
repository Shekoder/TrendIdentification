import os
from pymongo import MongoClient
import pandas as pd

# Use environment variable for Mongo URI if available, otherwise default to localhost
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/trenddb')

# Create a MongoDB client and connect to the database
client = MongoClient(MONGO_URI)
db = client.trenddb

# Specify the collection you want to insert data into
collection = db.trends  # Use 'trends' as the collection name

# Define the paths to your Excel files
base_path = 'C:/Users/HP8CG/OneDrive/Documents/PROJECTS/trend-identification-system/server'
myntra_file = os.path.join(base_path, 'SINGLE_20240730_144542(myntra).xlsx')
pinterest_file = os.path.join(base_path, 'SINGLE_20240730_144828(printest).xlsx')
instagram_file = os.path.join(base_path, 'SINGLE_20240730_145752(instagran).xlsx')

# Load Excel data
myntra_data = pd.read_excel(myntra_file)
pinterest_data = pd.read_excel(pinterest_file)
instagram_data = pd.read_excel(instagram_file)

# Convert DataFrames to dictionaries and insert into MongoDB
collection.insert_many(myntra_data.to_dict('records'))
collection.insert_many(pinterest_data.to_dict('records'))
collection.insert_many(instagram_data.to_dict('records'))

print("Data from all files inserted successfully.")


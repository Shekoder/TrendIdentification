import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt

# MongoDB configuration
client = MongoClient('mongodb://localhost:27017/')
db = client.trenddb
trends_cleaned_collection = db.trends_cleaned

def analyze_trends():
    print("Loading data from MongoDB...")
    data = pd.DataFrame(list(trends_cleaned_collection.find()))
    
    # Check if DataFrame is empty
    if data.empty:
        print("No data found in the collection.")
        return
    
    # Check columns
    print(f"Data columns: {data.columns}")
    
    # Example: Analyze brand popularity
    if 'brand' in data.columns:
        # Count occurrences of each brand
        brand_counts = data['brand'].value_counts()
        
        # Plot brand popularity
        brand_counts.plot(kind='bar', figsize=(12, 8))
        plt.title('Brand Popularity')
        plt.xlabel('Brand')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.show()
    else:
        print("Column 'brand' is missing in the dataset.")
    
    # Example: Analyze price distribution
    if 'price' in data.columns:
        # Plot price distribution
        plt.figure(figsize=(12, 8))
        plt.hist(data['price'].dropna(), bins=30, edgecolor='k')
        plt.title('Price Distribution')
        plt.xlabel('Price')
        plt.ylabel('Frequency')
        plt.show()
    else:
        print("Column 'price' is missing in the dataset.")
    
    # Example: Analyze occurrence of different LABEL columns
    label_columns = [col for col in data.columns if 'LABEL' in col]
    if label_columns:
        for label in label_columns:
            label_counts = data[label].value_counts()
            plt.figure(figsize=(12, 8))
            label_counts.plot(kind='bar')
            plt.title(f'Distribution of {label}')
            plt.xlabel('Category')
            plt.ylabel('Count')
            plt.xticks(rotation=45)
            plt.show()
    else:
        print("No LABEL columns found in the dataset.")

if __name__ == "__main__":
    analyze_trends()

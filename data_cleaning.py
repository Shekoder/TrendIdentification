from pymongo import MongoClient

# MongoDB configuration
client = MongoClient('mongodb://localhost:27017/')
db = client.trenddb
trends_collection = db.trends
cleaned_collection = db.trends_cleaned

def clean_data():
    try:
        # Check if there are any documents in the collection
        num_docs = trends_collection.count_documents({})
        print(f"Number of documents in 'trends': {num_docs}")

        if num_docs == 0:
            print("No documents found in the collection. Nothing to clean.")
            return

        # Clear the cleaned collection before inserting new cleaned data
        cleaned_collection.drop()

        # Remove duplicates based on a unique combination of fields
        pipeline = [
            # Convert fields to string to ensure compatibility with $concat
            {"$addFields": {
                "unique_id": {
                    "$concat": [
                        {"$toString": "$LABEL-1"},
                        "-",
                        {"$toString": "$_id"}
                    ]
                }
            }},
            {"$group": {
                "_id": "$unique_id",
                "doc": {"$first": "$$ROOT"}
            }},
            {"$replaceRoot": {"newRoot": "$doc"}}
        ]

        cursor = trends_collection.aggregate(pipeline)
        cleaned_docs = list(cursor)

        # Remove _id field to avoid duplicate key errors
        for doc in cleaned_docs:
            doc.pop('_id', None)

        # Insert cleaned documents into the cleaned collection
        cleaned_collection.insert_many(cleaned_docs)

        num_cleaned_docs = cleaned_collection.count_documents({})
        print(f"Number of documents in 'trends_cleaned': {num_cleaned_docs}")

        # Further cleaning: e.g., handle missing values
        print("Handling missing values...")
        update_result = cleaned_collection.update_many(
            {"$or": [{"price": {"$exists": False}}, {"price": ""}]},
            {"$set": {"price": "Unknown"}}
        )
        print(f"Updated {update_result.modified_count} documents for 'price'.")

        update_result = cleaned_collection.update_many(
            {"$or": [{"brand": {"$exists": False}}, {"brand": ""}]},
            {"$set": {"brand": "Unknown"}}
        )
        print(f"Updated {update_result.modified_count} documents for 'brand'.")

        print("Missing values handled successfully.")

        # Verify the data
        verify_data()

    except Exception as e:
        print(f"Error during data cleaning: {e}")

def verify_data():
    try:
        # Check for missing or empty 'price'
        missing_price_docs = cleaned_collection.count_documents({"price": {"$in": [None, ""]}})
        if missing_price_docs > 0:
            print(f"Documents with missing or empty price: {missing_price_docs}")
        else:
            print("No missing or empty 'price' values.")

        # Check for missing or empty 'brand'
        missing_brand_docs = cleaned_collection.count_documents({"brand": {"$in": [None, ""]}})
        if missing_brand_docs > 0:
            print(f"Documents with missing or empty brand: {missing_brand_docs}")
        else:
            print("No missing or empty 'brand' values.")

    except Exception as e:
        print(f"Error during data verification: {e}")

if __name__ == "__main__":
    clean_data()

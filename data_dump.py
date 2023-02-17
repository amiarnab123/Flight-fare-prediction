import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME = 'flight_fare'
TRAIN_COLLECTION_NAME = 'train_data'
TEST_COLLECTION_NAME = 'test_data'
TRAIN_DATA_FILE_PATH = '/config/workspace/Data_Train.xlsx'
TEST_DATA_FILE_PATH = '/config/workspace/Test_set.xlsx'

if __name__ == "__main__":
     train_df = pd.read_excel(TRAIN_DATA_FILE_PATH)
     test_df = pd.read_excel(TEST_DATA_FILE_PATH)
     print(f"Rows and columns: {train_df.shape}")
     print(f"Rows and columns: {test_df.shape}")

     ## convert dataframe to json format to dump the data into mongodb database
     train_df.reset_index(drop = True,inplace = True)
     test_df.reset_index(drop=True,inplace=True)
     train_json_record = list(json.loads(train_df.T.to_json()).values())
     test_json_record = list(json.loads(test_df.T.to_json()).values())
     print(train_json_record[0])
     print(test_json_record[0])

     ## insert converted record to mongodb database
     mongo_client[DATABASE_NAME][TRAIN_COLLECTION_NAME].insert_many(train_json_record)
     mongo_client[DATABASE_NAME][TEST_COLLECTION_NAME].insert_many(test_json_record)

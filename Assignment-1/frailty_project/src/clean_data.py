# Load necessary libraries
import pandas as pd

# Reading the raw_frailty_data csv file from the data_raw folder
raw_frailty_data = pd.read_csv("/Users/vanithakunta/Desktop/PDS/Assignment-1/frailty_project/data_raw/raw_frailty_data.csv")

# Clean the data by filtering the rows where "age" is between 20 and 50
clean_frailty_data = raw_frailty_data[raw_frailty_data['Age'].between(20, 50)]

# Write the cleaned data into a new csv file
clean_frailty_data.to_csv("/Users/vanithakunta/Desktop/PDS/Assignment-1/frailty_project/data_clean/clean_frailty_data.csv")



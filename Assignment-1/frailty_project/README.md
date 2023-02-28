The three stages of reproducible workflow are as follows:
1. Data Collection
2. Data Cleaning or Data Processing
3. Data Analysis

The given table reports the health conditions of people of various ages, in height, weight, grip strength.
1. Height: This column indicates the height of people in inches. All the values are of float type.
2. Weight: This column indicates the weight of people in pounds. All the values are of int type.
3. Age: It shows the age of people. All the values are of int type.
4. Grip strength: It shows the grip strength of the people. All the values are of int type.
5. Frailty: It refers to the condition of being weak and delicate. This column indicates whether a
given person is weak. Y indicates that the person is weak and N indicates that the person is
weak. All the values are either ‘Y’ or N’.

All the columns given have proper values. There are no unusual or missing values in the given data.

#### Stage 1 (Data Collection):

In this stage the data needs to be collected and saved into a CSV file with a proper name
(raw_frailty_data.csv).
1. Create a data_raw folder in the project folder and store the original dataset
(raw_frailty_data.csv) in the data_raw folder.
2. A metadata file needs to be created which has information about data source, columns, data
types, units of measurement, missing data, data transformations etc.,
   - Height is in inches 
   - Weight is in pounds 
   - Age is in digits 
   - Grip strength is in digits 
   - Frailty codes indicate the person is frail (Y) or the person isn’t (N)

##### Folder structure:
```
frailty_project/
    data_raw/
        raw_frailty_data.csv
        README.txt
    data_clean/
    results/
    src/
```

#### Stage 2 (Data Processing):
Inspection of the given data shows that the data is consistent and there are no unusual or missing
values. So, the data is good to be used for further analysis.

In this stage, we can clean data to remove any outliers, missing values, or normalize variables, filter
rows by age or filter rows by frailty status etc.,

Here, I want to focus only on people between 20 and 50 years old.
1. Create a folder “data_clean” in the project folder.
2. Create a folder “src” in the project folder.
3. Write a script “clean_data.py” to clean the data and store in the ‘src’ folder. Save the cleaned
data to data_clean folder as “clean_frailty_data.csv”.

##### Folder structure:
```
frailty_project/
    data_raw/
        raw_frailty_data.csv
        README.txt
    data_clean/
        clean_frailty_data.csv
    results/
    src/
        clean_data.py
```

#### Stage 3 (Data Analysis):
1. Create a script “analysis.py” and store it in “src” folder.
2. Create a folder called “results” in the project folder.
3. In this stage, perform the analysis, generate results and tables and save them to the “results”
folder.
4. Performed Welch Two Sample t-test of age by frailty, histogram of grip strength, box plot of grip_strength by frailty and saved the results to "results" folder.

##### Folder structure:
```
frailty_project/
    data_raw/
        raw_frailty_data.csv
        README.txt
    data_clean/
        clean_frailty_data.csv
    results/
        boxplot.png
        histogram.png
        welch_ttest_results.txt        
    src/
        analysis.py
        clean_data.py
```
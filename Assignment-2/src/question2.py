import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the diabetes dataset
diabetes_data = pd.read_csv("../data_raw/diabetes.csv")

# set the seed for reproducibility
np.random.seed(16326099)

# take a random sample of 25 observations
sample_data = diabetes_data.sample(n=25)

# Extract the population BMI data
population_bmi = diabetes_data['BMI']

# Extract the sample BMI data
sample_bmi = sample_data['BMI']

# calculate the 98th percentile of BMI for the sample
sample_98th_percentile = np.percentile(sample_data['BMI'], 98)
print("Sample 98th Percentile of BMI:", sample_98th_percentile)

# calculate the 98th percentile of BMI for the population
population_98th_percentile = np.percentile(diabetes_data['BMI'], 98)
print("Population 98th Percentile of BMI:", population_98th_percentile)

# Create a bar plot comparing the 98th percentile BMI of the population and sample
fig, ax = plt.subplots()
colors = ['tab:orange', 'tab:blue']
ax.bar(['Population', 'Sample'], [population_98th_percentile, sample_98th_percentile], color=colors)
ax.set_ylabel('98th Percentile BMI')
ax.set_title('Comparison of 98th Percentile BMI Between Population and Sample')
ax.figure.savefig('../results/result2.png')

""" The graph compares the 98th percentile BMI (Body Mass Index) between a population and a sample. 
The orange bar represents the population's 98th percentile BMI, and the blue bar represents the sample's 98th percentile BMI. 
The y-axis represents the 98th percentile BMI value, and the x-axis represents the population and sample groups. 
The graph shows that the population's 98th percentile BMI is higher than that of the sample. 
"""

# Create a histogram comparing the distribution of BMI in the population and sample
fig, ax = plt.subplots()
ax.hist([sample_bmi, population_bmi], bins=15, label=['Sample', 'Population'])
ax.axvline(x=sample_98th_percentile, color='green', linestyle='--', label='98th Percentile (Sample)')
ax.axvline(x=population_98th_percentile, color='red', linestyle='--', label='98th Percentile (Population)')
ax.set_xlabel('BMI')
ax.set_ylabel('Frequency')
ax.set_title('Comparison of BMI Distribution Between Population and Sample')
ax.legend()
ax.figure.savefig('../results/result3.png')

plt.show()

"""The above code generates a histogram with two datasets: the population's BMI distribution and a sample's BMI distribution. 
The histogram displays the frequency of BMI values in each dataset, and it uses 15 bins to group the data.
The graph also includes two vertical dashed lines to indicate the 98th percentile BMI values for both the sample and the population. 
The green dashed line represents the 98th percentile BMI value for the sample, while the red dashed line represents the 98th percentile BMI value for the population."""
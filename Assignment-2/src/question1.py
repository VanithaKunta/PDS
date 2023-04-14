import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# load the diabetes dataset
diabetes_data = pd.read_csv("../data_raw/diabetes.csv")

# set the seed for reproducibility
np.random.seed(16326099)

# take a random sample of 25 observations
sample_data = diabetes_data.sample(n=25)

# calculate the mean glucose value of the sample
sample_mean = sample_data['Glucose'].mean()
print("Sample Mean Glucose Value:", sample_mean)

# calculate the highest glucose value of the sample
sample_max = sample_data['Glucose'].max()
print("Sample Highest Glucose Value:", sample_max)

# calculate the population mean glucose value
population_mean = diabetes_data['Glucose'].mean()
print("Population Mean Glucose Value:", population_mean)

# calculate the highest glucose value of the population
population_max = diabetes_data['Glucose'].max()
print("Population Highest Glucose Value:", population_max)

# create a boxplot to compare the sample and population glucose levels
sns.boxplot(data=[diabetes_data['Glucose'], sample_data['Glucose']])
plt.xticks([0, 1], ['Population', 'Sample'])
plt.ylabel('Glucose')
plt.title('Comparison of Sample and Population Glucose Levels')
plt.annotate('Sample Mean = {:.2f}'.format(sample_mean), xy=(1, sample_mean), xytext=(1.1, sample_mean+5))
plt.annotate('Sample Max = {}'.format(sample_max), xy=(1, sample_max), xytext=(1.1, sample_max+5))
plt.annotate('Population Mean = {:.2f}'.format(population_mean), xy=(0, population_mean), xytext=(-0.25, population_mean+5))
plt.annotate('Population Max = {}'.format(population_max), xy=(0, population_max), xytext=(-0.25, population_max+5))
plt.savefig('../results/result1.png')
plt.show()

"""This code produces a boxplot that compares the distribution of glucose levels in the sample and population:
The blue box represents the distribution of glucose levels in the population, and the orange box represents the distribution of glucose levels in the sample. 
The sample mean and maximum glucose levels are also labeled on the chart.
This boxplot shows that while the sample mean glucose level is higher than the population mean glucose level, 
the maximum glucose level in the sample is lower than the maximum glucose level in the population.
"""
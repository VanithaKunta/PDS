import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the diabetes dataset
diabetes_data = pd.read_csv("../data_raw/diabetes.csv")

# set the seed for reproducibility
np.random.seed(16326099)

# create empty lists to store the samples means, standard deviations and percentiles
sample_means = []
sample_stds = []
sample_percentiles = []

# perform bootstrap sampling 500 times
for i in range(500):
    # Generate 500 samples of size 150 with replacement
    sample_data = diabetes_data['BloodPressure'].sample(n=150, replace=True)

    # calculate and add the sample mean to the list of sample means
    sample_means.append(np.mean(sample_data))

    # calculate and add the sample standard deviation to the list of sample stds
    sample_stds.append(np.std(sample_data))

    # calculate and add the sample 90th Percentile to the list of sample percentiles
    sample_percentiles.append(np.percentile(sample_data, 90))


# calculate the mean, standard deviation, and 90th percentile for BloodPressure for the population
population_mean = np.mean(diabetes_data['BloodPressure'])
population_std = np.std(diabetes_data['BloodPressure'])
population_90th_percentile = np.percentile(diabetes_data['BloodPressure'], 90)

# calculate the average mean, standard deviation, and percentile for BloodPressure for the samples
samples_average_mean = np.mean(sample_means)
samples_average_std = np.mean(sample_stds)
samples_average_90th_percentile = np.mean(sample_percentiles)

# print the population and sample mean, standard deviation, and percentile for BloodPressure
print("Population Mean of BloodPressure:", population_mean)
print("Population Standard Deviation of BloodPressure:", population_std)
print("Population 90th Percentile of BloodPressure:", population_90th_percentile)

print("Samples Average Mean of BloodPressure:", samples_average_mean)
print("Samples Average Standard Deviation of BloodPressure:", samples_average_std)
print("Samples Average 90th Percentile of BloodPressure:", samples_average_90th_percentile)

# Compare population and sample statistics with box plots
bp_data = [diabetes_data['BloodPressure'], sample_means, sample_stds, sample_percentiles]
fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(bp_data, labels=['Population', 'Sample Means', 'Sample SDs', 'Sample 90th Percentiles'])
ax.set_title('Comparison of BloodPressure Statistics')
ax.set_ylabel('BloodPressure')
plt.savefig('../results/result4.png')
plt.show()

"""The above code generates a boxplot to compare the BloodPressure statistics between the population and the samples. 
The boxplot displays the distribution of the BloodPressure values for each group (population and samples) in a visual format. 
The horizontal line inside the box represents the median of the data. 
The x-axis is labeled with the four groups being compared: population, sample means, sample standard deviations, and sample 90th percentiles. 
The y-axis represents the BloodPressure values.
The graph allows us to compare the spread and central tendency of the BloodPressure values between the population and the samples."""

# Compare population and sample statistics with histograms
fig, axs = plt.subplots(1, 3, figsize=(12, 4))
axs[0].hist(diabetes_data['BloodPressure'], bins=20)
axs[0].set_title('Population')
axs[0].set_xlabel('BloodPressure')
axs[0].set_ylabel('Frequency')
axs[0].axvline(population_mean, color='red', linestyle='dashed', linewidth=2, label='Population Mean')
axs[0].axvline(population_mean+population_std, color='orange', linestyle='dotted', linewidth=2, label='Population Mean + Std')
axs[0].axvline(population_90th_percentile, color='green', linestyle='solid', linewidth=2, label='Population 90th Percentile')
axs[0].legend()

axs[1].hist(sample_means, bins=20)
axs[1].set_title('Sample Mean')
axs[1].set_xlabel('BloodPressure')
axs[1].set_ylabel('Frequency')
axs[1].axvline(np.mean(sample_means), color='red', linestyle='dashed', linewidth=2, label='Sample Mean')
axs[1].axvline(np.mean(sample_means)+np.std(sample_means), color='orange', linestyle='dotted', linewidth=2, label='Sample Mean + Std')
axs[1].axvline(np.percentile(sample_means, 90), color='green', linestyle='solid', linewidth=2, label='Sample Mean 90th Percentile')
axs[1].legend()

axs[2].hist(sample_stds, bins=20)
axs[2].set_title('Sample Standard Deviation')
axs[2].set_xlabel('BloodPressure')
axs[2].set_ylabel('Frequency')
axs[2].axvline(np.mean(sample_stds), color='red', linestyle='dashed', linewidth=2, label='Sample Standard Deviation')
axs[2].axvline(np.mean(sample_stds)+np.std(sample_stds), color='orange', linestyle='dotted', linewidth=2, label='Sample Standard Deviation + Std')
axs[2].axvline(np.percentile(sample_stds, 90), color='green', linestyle='solid', linewidth=2, label='Sample Standard Deviation 90th Percentile')
axs[2].legend()

plt.tight_layout()
plt.savefig('../results/result5.png')
plt.show()

"""
This graph shows a comparison of the BloodPressure statistics between the population and sample. It consists of three histograms plotted side by side.
The first histogram shows the distribution of BloodPressure in the population. 
The red dashed line represents the population mean, the orange dotted line represents the population mean plus one standard deviation, and the green solid line represents the 90th percentile of the population BloodPressure.
The second histogram shows the distribution of sample means. The red dashed line represents the mean of the sample means, the orange dotted line represents the mean of the sample means plus one standard deviation, 
and the green solid line represents the 90th percentile of the sample means.
The third histogram shows the distribution of sample standard deviations. The red dashed line represents the mean of the sample standard deviations, 
the orange dotted line represents the mean of the sample standard deviations plus one standard deviation, and the green solid line represents the 90th percentile of the sample standard deviations.
Overall, the graph allows for a quick comparison between the population and sample statistics by visualizing their distributions side by side."""

# Create stacked bar plot
fig, ax = plt.subplots(figsize=(8, 6))
barWidth = 0.35

# Set positions of the bars on the x-axis
r1 = np.arange(len(['Mean', 'Standard Deviation', '90th Percentile']))
r2 = [x + barWidth for x in r1]

# Create the bars
ax.bar(r1, [population_mean, population_std, population_90th_percentile], color='tab:blue', width=barWidth, label='Population')
ax.bar(r2, [samples_average_mean, samples_average_std, samples_average_90th_percentile], color='tab:orange', width=barWidth, label='Bootstrap')

# Add labels and legend
ax.set_xlabel('BloodPressure Statistics')
ax.set_ylabel('Value')
ax.set_title('Comparison of BloodPressure Statistics')
ax.set_xticks([r + barWidth / 2 for r in range(len(['Mean', 'Standard Deviation', '90th Percentile']))])
ax.set_xticklabels(['Mean', 'Standard Deviation', '90th Percentile'])
ax.legend()
plt.savefig('../results/result6.png')
plt.show()

"""
The graph is a stacked bar plot that compares the population and bootstrap statistics for BloodPressure. 
The x-axis shows the three different statistics being compared, which are the Mean, Standard Deviation, and 90th Percentile. 
The y-axis shows the value of the statistic being compared."""
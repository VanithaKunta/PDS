# Load necessary libraries
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# Reading the clean_frailty_data csv file from the data_clean folder
clean_frailty_data = pd.read_csv("/Users/vanithakunta/Desktop/PDS/Assignment-1/frailty_project/data_raw/raw_frailty_data.csv")

# Split data into two groups based on frailty status
frailty_y = clean_frailty_data[clean_frailty_data['Frailty'] == 'Y']['Age']
frailty_n = clean_frailty_data[clean_frailty_data['Frailty'] == 'N']['Age']

# Perform t-test
t_stat, p_val = stats.ttest_ind(frailty_y, frailty_n, equal_var=False)

# Save results to welch_ttest_results text file in results folder
with open('/Users/vanithakunta/Desktop/PDS/Assignment-1/frailty_project/results/welch_ttest_results.txt', 'w') as f:
    f.write(f"t-statistic: {t_stat}\n")
    f.write(f"p-value: {p_val}\n")
    f.close()

# Create a histogram of grip strength
plt.hist(clean_frailty_data['Grip strength'], bins=10)

# Add labels and title
plt.xlabel('Grip Strength')
plt.ylabel('Frequency')
plt.title('Histogram of Grip Strength')

# Save histogram as PNG file
plt.savefig('/Users/vanithakunta/Desktop/PDS/Assignment-1/frailty_project/results/histogram.png')


# Create box plot of grip_strength by frailty
clean_frailty_data.boxplot(column='Grip strength', by='Frailty')

# Add labels and title
plt.xlabel('Frailty Status')
plt.ylabel('Grip Strength')
plt.title('Box Plot of Grip Strength by Frailty Status')

# Save box plot as PNG file
plt.savefig('/Users/vanithakunta/Desktop/PDS/Assignment-1/frailty_project/results/boxplot.png')
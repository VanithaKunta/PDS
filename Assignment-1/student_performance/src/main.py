# Load necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the raw_students_performance csv file from the data_raw folder
df = pd.read_csv("/Users/vanithakunta/Desktop/PDS/Assignment-1/student_performance/data_raw/raw_students_performance.csv")


# Bar Chart of students count by gender
gender_counts = df['gender'].value_counts()
plt.bar(gender_counts.index, gender_counts.values)
# Add labels and title
plt.title("Count of Students by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
# Save Bar Chart as PNG file
plt.savefig('/Users/vanithakunta/Desktop/PDS/Assignment-1/student_performance/results/bar_chart.png')
plt.show()


# Pie Chart of pass rate for each test
math_pass = df[df['math score'] >= 60]['math score'].count()
reading_pass = df[df['reading score'] >= 60]['reading score'].count()
writing_pass = df[df['writing score'] >= 60]['writing score'].count()
# Add labels and title
labels = ['Math', 'Reading', 'Writing']
values = [math_pass, reading_pass, writing_pass]
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Pass Rate for Each Test")
# Save Pie Chart as PNG file
plt.savefig('/Users/vanithakunta/Desktop/PDS/Assignment-1/student_performance/results/pie_chart.png')
plt.show()


# Scatter Plot of relationship between math and reading scores
plt.scatter(df['math score'], df['reading score'])
# Add labels and title
plt.title("Relationship Between Math and Reading Scores")
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
# Save Scatter Plot as PNG file
plt.savefig('/Users/vanithakunta/Desktop/PDS/Assignment-1/student_performance/results/scatter_plot.png')
plt.show()


# Box Plot of distribution of Writing Scores by Race/Ethnicity
sns.boxplot(x='race/ethnicity', y='writing score', data=df)
# Add labels and title
plt.title("Distribution of Writing Scores by Race/Ethnicity")
plt.xlabel("Race/Ethnicity")
plt.ylabel("Writing Score")
# Save Box Plot as PNG file
plt.savefig('/Users/vanithakunta/Desktop/PDS/Assignment-1/student_performance/results/box_plot.png')
plt.show()


# Histogram of distribution of Math Scores
plt.hist(df['math score'], bins=10)
# Add labels and title
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Frequency")
# Save Histogram as PNG file
plt.savefig('/Users/vanithakunta/Desktop/PDS/Assignment-1/student_performance/results/histogram.png')
plt.show()
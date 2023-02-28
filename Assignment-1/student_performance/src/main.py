import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#reading data from dataset
df = pd.read_csv("raw_students_performance.csv")


#Bar Chart
gender_counts = df['gender'].value_counts()
plt.bar(gender_counts.index, gender_counts.values)
plt.title("Count of Students by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()


#Pie Chart
math_pass = df[df['math score'] >= 60]['math score'].count()
reading_pass = df[df['reading score'] >= 60]['reading score'].count()
writing_pass = df[df['writing score'] >= 60]['writing score'].count()
labels = ['Math', 'Reading', 'Writing']
values = [math_pass, reading_pass, writing_pass]
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Pass Rate for Each Test")
plt.show()


#Scatter Plot
plt.scatter(df['math score'], df['reading score'])
plt.title("Relationship Between Math and Reading Scores")
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.show()


#Box Plot
sns.boxplot(x='race/ethnicity', y='writing score', data=df)
plt.title("Distribution of Writing Scores by Race/Ethnicity")
plt.xlabel("Race/Ethnicity")
plt.ylabel("Writing Score")
plt.show()


#Histogram
plt.hist(df['math score'], bins=10)
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.show()

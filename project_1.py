# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 19:47:03 2025

@author: Micaiah
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
df = pd.read_csv("C:/Users/27671/Downloads/student_depression_dataset.csv")

data = df.groupby(["Gender", "Family History of Mental Illness"]).size().unstack()
data.plot(kind="bar", stacked=True, color=["green", "yellow"])
plt.title("Students From Family With History of Mental Illness by Gender")
plt.ylabel("Number of Students")
plt.xlabel("Gender")
plt.legend(title="Family History")
plt.show()

print(data.head(30))

work = df.groupby("Gender")["Work Pressure"].mean()
work.plot(kind="bar", color="skyblue")
plt.title("Work Pressure by Gender")
plt.ylabel("Average Work Pressure")
plt.xlabel("Gender")
plt.show()

# Chart 3: Average Academic Pressure by Gender
academic = df.groupby("Gender")["Academic Pressure"].mean()
academic.plot(kind="bar", color="orange")
plt.title("Academic Pressure by Gender")
plt.ylabel("Average Academic Pressure")
plt.xlabel("Gender")
plt.show()


low_work = df[df["Work Pressure"] <= 2].groupby("Gender").size()
low_academic = df[df["Academic Pressure"] <= 2].groupby("Gender").size()

low = pd.DataFrame({
    "Low Work Pressure": low_work,
    "Low Academic Pressure": low_academic
})
low.plot(kind="bar", color=["purple", "lightgreen"])
plt.title("Students Resisting Pressure by Gender")
plt.ylabel("Number of Students")
plt.xlabel("Gender")
plt.show()

city=df["City"]
accademic=df["Academic Pressure"]
work=df["Work Pressure"]






# Breakdown of depression by family history
pd.crosstab(df['Family History of Mental Illness'], df['Depression'], normalize='index').plot(kind='bar')
plt.title('Depression Rate by Family History')
plt.ylabel('Percentage')

plt.show()
# Depression rate by gender
depression_gender = df.groupby('Gender')['Depression'].mean()
depression_gender.plot(kind='bar', color=['blue', 'pink'])
plt.title('Depression Rate by Gender')
plt.ylabel('Percentage Depressed')


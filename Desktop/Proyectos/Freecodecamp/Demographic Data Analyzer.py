import pandas as pd
df = pd.read_csv("dataset")  
#1. How many people of each race are represented in this dataset?
df["race"].unique()
race_counts = df["race"].value_counts()
print(race_counts)

# 2. What is the average age of men?
average_age_men = df[df["sex"] == "Male"]["age"].mean()
print(average_age_men)
# 3. What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (df["education"] == "Bachelors").mean() * 100
print(percentage_bachelors)

# 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
print(advanced_education)
percentage_advanced_education = (df[advanced_education]["salary"] == ">50K").mean() * 100
print(percentage_advanced_education)

# 5. What percentage of people without advanced education make more than 50K?
percentage_no_advanced_education = (df[~advanced_education]["salary"] == ">50K").mean() * 100
print(percentage_no_advanced_education)

# 6. What is the minimum number of hours a person works per week?
min_work_hours = df["hours-per-week"].min()
print(min_work_hours)

# 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
num_min_workers = df[df["hours-per-week"] == min_work_hours]
percentage_min_workers = (num_min_workers["salary"] == ">50K").mean() * 100
print(percentage_min_workers)

# 8. What country has the highest percentage of people that earn >50K and what is that percentage?

num = df[df["salary"] == ">50K"]["native-country"].value_counts()
den = df["native-country"].value_counts()

highest_earning_country = num/den
print(highest_earning_country)
highest_earning_percentage = (df[df["native-country"] == highest_earning_country]["salary"] == ">50K").mean() * 100
print(highest_earning_percentage)


# 9. Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].value_counts().idxmax()

print(top_IN_occupation)

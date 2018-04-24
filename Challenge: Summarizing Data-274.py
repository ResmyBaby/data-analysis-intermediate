## 2. Introduction to the Data ##

import pandas as pd
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
print(all_ages[0:4])
print(recent_grads[0:4])

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
major_category_unique = all_ages['Major_category'].unique()
for rows in major_category_unique :
    Major_category1 =all_ages[all_ages["Major_category"] == rows]
   
aa_cat_counts = dict()
rg_cat_counts = dict()
def calculate_major_cat_totals(df):
    cats = df['Major_category'].unique()
    counts_dictionary = dict()

    for c in cats:
        major_df = df[df["Major_category"] == c]
        total = major_df["Total"].sum()
        counts_dictionary[c] = total
    return counts_dictionary

aa_cat_counts = calculate_major_cat_totals(all_ages)
rg_cat_counts = calculate_major_cat_totals(recent_grads)

## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0
Low_wage_jobs_sum =recent_grads["Low_wage_jobs"].sum()
Total_sum =recent_grads["Total"].sum()
low_wage_proportion =Low_wage_jobs_sum/Total_sum 
print(low_wage_proportion)



## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0
for rows in majors :
    grads =recent_grads[recent_grads["Major"]==rows]
    ages =all_ages[all_ages["Major"]==rows]
    rg_unemp_rate = grads.iloc[0]['Unemployment_rate']
    aa_unemp_rate = ages.iloc[0]['Unemployment_rate']
    if rg_unemp_rate < aa_unemp_rate:
        rg_lower_count += 1

print(rg_lower_count)

    
    
    
    
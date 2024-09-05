### Go to test.py to run the Program!


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('adult.data.csv')

#Different race count
race_count = pd.Series(df['race'].value_counts())

#Average age of men
average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

#Percentage of people with bachelors degree
totaledu = (df['education']).count()
bachedu = (df['education'] == "Bachelors").sum()
percentage_bachelors = round((bachedu/totaledu)*100, 1)


mask1 = (df['education'] == "Bachelors") | (df['education'] == "Masters") | (df['education'] == "Doctorate")
mask2 = df['salary'] == ">50K"
mymask = mask1 & mask2
higher_education_rich = round(mymask.sum() / mask1.sum() * 100, 1)

mask3 = (df['education'] != "Bachelors") & (df['education'] != "Masters") & (df['education'] != "Doctorate")

lower_education_rich = round(len(df[mask3 & mask2]) / len(df[mask3]) * 100, 1)

min_work_hours = df['hours-per-week'].min()

rich_percentage = round(len(df[(df['hours-per-week'] == 1) & (df['salary'] == ">50K")]) / len(df[df['hours-per-week'] == 1]) * 100, 1)

highest_earning_country = (df['native-country'][mask2].value_counts() / df['native-country' ].value_counts()).idxmax()

highest_earning_country_percentage = round((df['native-country'][mask2].value_counts() / df['native-country'].value_counts()).max() * 100, 1)

top_IN_occupation = df[((df['native-country'] == "India") & mask2)]['occupation'].value_counts().idxmax()


def calculate_demographic_data():
    
    print("Number of each race:\n", race_count) 
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
    print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
    print(f"Min work time: {min_work_hours} hours/week")
    print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
    print("Country with highest percentage of rich:", highest_earning_country)
    print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
    print("Top occupations in India:", top_IN_occupation)

    return{
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
def plt_race_count():
    x = list(race_count.index)
    y = race_count.values
    plt.title("Num of People In Each Race")
    plt.bar(x,y, color='C0', edgecolor='black')
    plt.xticks(x, rotation=15)
    plt.show()
    return None

def plt_men_age():
    men_age = df[df['sex'] == 'Male']['age']
    plt.title("Men's Ages")
    plt.hist(men_age, color='C2', edgecolor='black')
    return None

def plt_bach_pie():
    fig,ax = plt.subplots()
    plt.style.use("ggplot")
    plt.title("Percentage of People with Bachelors")
    ax.pie([totaledu-bachedu,bachedu],labels=[f"W/O Bachelors({totaledu-bachedu})",f"Bachelors({bachedu})"], autopct='%.1f%%')
    plt.show()
    return None

def plt_salaries_50k():
    total_50k = len(df[df['salary']=='>50K'])
    total_50k
    normal_edu = mask3.sum()
    normal_edu_50k = (mask3 & mask2).sum()
    advanced_edu = mask1.sum()
    advanced_edu_50k = mymask.sum()
    
    fig,ax = plt.subplots()
    plt.title("Salaries Greater than 50K")
    x_labels =["NormalEdu","AdvancedEdu"] 
    y_counts1 = [normal_edu, advanced_edu]
    y_counts2 = [normal_edu_50k, advanced_edu_50k]
    colors1 = ['c', 'c']
    colors2 = ['r', 'g']
    bar1 = ax.bar(x_labels, y_counts1, color=colors1)
    bar2 = ax.bar(x_labels, y_counts2, color=colors2)
    ax.legend([bar2[0], bar2[1]], ['Normal Education > $50K', 'Advanced Education > $50K'])

    plt.show()
    

    return None


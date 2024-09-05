from main import *

#Function displaying data with prompts

calculate_demographic_data()


'''Change values of following variables to choose
which graphs you'd like to run
'''
run_race_count = True
run_men_age = False
run_bach_pie = False
run_salaries_50k = True

if run_race_count:
    plt_race_count()

if run_men_age:
    plt_men_age()

if run_bach_pie:
    plt_bach_pie()

if run_salaries_50k:
    plt_salaries_50k()
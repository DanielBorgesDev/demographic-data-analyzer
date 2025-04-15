import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load dataset
    df = pd.read_csv("adult.data.csv")

    # 1. Count of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # 4. Advanced education
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = round((higher_education['salary'] == '>50K').sum() / len(higher_education) * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').sum() / len(lower_education) * 100, 1)

    # 5. Minimum hours per week
    min_work_hours = df['hours-per-week'].min()

    # 6. Percentage of rich among those who work minimum hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').sum() / len(num_min_workers) * 100, 1)

    # 7. Country with highest percentage of >50K earners
    country_counts = df['native-country'].value_counts()
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_rich_percentage = (country_rich_counts / country_counts * 100).dropna()

    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)

    # 8. Most common occupation for >50K earners in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Output
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India for those who earn >50K:", top_IN_occupation)

    return {
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

import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")

    # 1. Número de pessoas por raça
    race_count = df["race"].value_counts()

    # 2. Média de idade dos homens
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Percentual com Bachelor's
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    # 4. Percentual com educação avançada que ganham >50K
    advanced_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_education = df[advanced_education]
    lower_education = df[~advanced_education]

    higher_education_rich = round(
        (higher_education["salary"] == ">50K").mean() * 100, 1
    )

    # 5. Percentual sem educação avançada que ganham >50K
    lower_education_rich = round(
        (lower_education["salary"] == ">50K").mean() * 100, 1
    )

    # 6. Mínimo de horas trabalhadas por semana
    min_work_hours = df["hours-per-week"].min()

    # 7. Percentual que trabalham mínimo de horas e ganham >50K
    num_min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_min_workers = round(
        (num_min_workers["salary"] == ">50K").mean() * 100, 1
    )

    # 8. País com maior percentual de >50K
    country_salary = (
        df[df["salary"] == ">50K"]["native-country"].value_counts() /
        df["native-country"].value_counts()
    ) * 100

    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(country_salary.max(), 1)

    # 9. Ocupação mais popular na Índia para >50K
    india_high_income = df[
        (df["native-country"] == "India") &
        (df["salary"] == ">50K")
    ]

    top_IN_occupation = india_high_income["occupation"].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_min_workers)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_min_workers,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }

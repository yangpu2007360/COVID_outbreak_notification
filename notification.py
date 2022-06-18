import pandas as pd
from datetime import datetime
from datetime import datetime, timedelta


df = pd.read_excel('Book.xlsx')

print(df)

# find current date

current_date = datetime.today().strftime('%Y-%m-%d')
fourteen_days_before = (
    datetime.today() - timedelta(days=14)).strftime('%Y-%m-%d')

print(current_date)
print("14 days before", fourteen_days_before)

# select dates in the past 14 days
in_range_df = df[df["Date"].isin(
    pd.date_range(fourteen_days_before, current_date))]

print(in_range_df)

count = len(in_range_df)

print(f"there are {count} casese during this peirod")


# cases in Area A
# area_A = in_range_df[df['Area']] == "A"
area_A = in_range_df.loc[df['Area'] == "A"]

areas = ["A", "B", "C"]

for area in areas:
    number_of_cases = len(in_range_df.loc[df['Area'] == area])
    print(f"the number of cases in {area} is {number_of_cases} ")

    if number_of_cases >= 20:
        print(f"There is an outbreak in {area}. Please take action!")

    elif number_of_cases >= 3:
        print(f"There is an outbreak in {area}. Please take action!")

import random
import pandas as pd


def birthdays(num, iterations):
    repeat = 0
    for i in range(iterations):
        birthdays = set()
        for j in range(num):
            r = random.randint(1,365)
            if r in birthdays:
                repeat += 1
                break
            else:
                birthdays.add(r)
    return repeat/iterations


def calc_birthday(num):
    days = 365
    total = 1
    denom = 365**num
    while num != 0:
        total *= (days)
        days -= 1
        num -= 1
    return round(1 - total/denom,4)


birthday_table = [[i, birthdays(i, 10000)] for i in [1,5,10,20,23,30,40,50,60,70,75,100]]
df = pd.DataFrame(birthday_table, columns=['n','Simulated p(n)'])
df['Calculated p(n)'] = df['n'].apply(calc_birthday)
print(df)

import datetime
import random

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def birthday_generator():
    start_date = datetime.date(2023,1,1)
    
    shift = datetime.timedelta(random.randint(1,365))
    numbered_bday = start_date + shift
            
    month_num = numbered_bday.month - 1
    date = numbered_bday.day
    month_name = months[month_num]
    birthday = month_name + " " + str(date)
        
    return birthday

def duplicate_checker(birthdays,birthdays_set,dupe_count):
    if len(birthdays) != len(birthdays_set):
        duplicates = []
        dupe_count += 1
            
        for i, birthday_a in enumerate(birthdays):
            for i, birthday_b in enumerate(birthdays[i+1:]):
                if birthday_a == birthday_b:
                    duplicates.append(birthday_a)
        
    return dupe_count
        
def probability(run_count,dupe_count,times):
    dupe_chance = (dupe_count / run_count) * 100
    r_dupe_chance = round(dupe_chance)
    print("")
    print(f"Out of {run_count} simulations of {times} people, there was a matching birthday in that group {dupe_count} times. This means that {times} people have a {r_dupe_chance}% chance of having a matching birthday in their group.") 

try:
    times = int(input("How many birthdays shall I generate? (Max 100): "))       
except ValueError:
    print("not a valid number")
else:
    print("Generating birthdays...")
    run_count = 100000
    dupe_count = 0
    for i in range(run_count):
        if 1 < times < 100:
            birthdays = []
            duplicates = []
        
            for i in range(times):
                birthday = birthday_generator()
            
                birthdays.append(birthday)
                birthdays_set = set(birthdays)
        
        dupe_count = duplicate_checker(birthdays,birthdays_set,dupe_count)
    
    probability(run_count,dupe_count,times)
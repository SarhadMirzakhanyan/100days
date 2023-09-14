age = int(input("What's your age"))

remaining_years = 90 - age
remaining_days = remaining_years*365 + remaining_years//4

print(f"Remaining days: {remaining_days}")
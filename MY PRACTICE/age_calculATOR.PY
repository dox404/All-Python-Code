# from datetime import datetime

# today=date.todat()

# date_of_birth=input('enter the date of birth: ')


from datetime import date

today = date.today()
# print("Today's date:", today)
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)
date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(day, month, year)
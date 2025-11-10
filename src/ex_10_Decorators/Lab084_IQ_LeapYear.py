
# checking a year is leap year or not


# first condition - multiple of 4
# 2. except for years evently by 100 but not by 400

# year is multiple for 400
# the year is multiple of  but not by 100

def check_leap_year(year):
    if(year%4==0 and year%100!=0) or yea%400==0:
        return True
    else:
        return False

year_1= int(input("Enter a valid year"))
if check_leap_year(year_1):
    print("Leap Year")
else:
    print("Not Leap Year")

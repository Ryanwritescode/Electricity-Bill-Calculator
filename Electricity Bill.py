import sys
import time
print("Please Enter Meter Reading For Present Month: ",end ="")
#The Above line is prompting the user to enter the meter reading for the previous month
presentmonth=int(input())
#The Above line is a variable declaration that allows the user to input his own figures for the presentmonth
print("Please Enter Meter Reading For Previous Month: ",end ="")
#The Above line is prompting the user to enter the meter reading for the Present month
previousmonth=int(input())
#The Above line is a variable declaration that allows the user to input his own figures for the previousmonth
if presentmonth<=previousmonth:
    print("Invalid Entry The Present Month Should Be Greater Than The Previous Month Please Try Again")
    time.sleep(2)
    sys.exit()
elif presentmonth<=0:
     print("Invalid Entry This Program Only Accepts Whole Numbers Please Try Again")
     time.sleep(2)
     sys.exit()
elif previousmonth<=0:
    print("Invalid Entry This Program Only Accepts Whole Numbers Please Try Again")
    time.sleep(2)
    sys.exit()
else:
    kwhused=(presentmonth - previousmonth)
#The Above line is calculating the Kilo-Watt-Hours Used For The Month by subtracting the previousmonth from the presentmonth
if kwhused <0:
    print("Invalid Entry This Program Only Accepts Whole Numbers Please Try Again")
    time.sleep(2)
    sys.exit()
else:
    print("The Kilo Watt Hours Used For This Month is:", kwhused)
low_kwh_rate=0.59
low_kwh_rate_range=50
mid_kwh_rate=0.65
mid_kwh_rate_range=150
high_kwh_rate=0.68
standing_charge=13
mid_kwh_rate_first_unit_fee=29.50
mid_kwh_rate_first_unit=50
high_kwh_rate_first_unit_fee=94.50
high_kwh_rate_first_unit=150
#The Above line is the declaration of rates, fees and charges that will be used for the calulation of the monthly bill
if kwhused <= low_kwh_rate_range:
    monthbill=(kwhused*low_kwh_rate)
    print("Monthly Bill Calculation:")
    print("The Kilo Watts Used Is Multiplied By The Rate For Users That Usage Don't Exceed 50 Kilo Watts=", kwhused, end="")
    print("*", end="")
    print(low_kwh_rate)
    print("$13 Which Is The Standing Charge Is Then Added To The Overall Result=", monthbill, end="")
    print("+", end="")
    print(standing_charge)
    monthbill=(monthbill+standing_charge)
    print("This Month Bill is: $", monthbill)
#The Above line is calculating the monthly bill within the 0-50 kilo watt range
elif kwhused <= mid_kwh_rate_range:
    monthbill=(kwhused-mid_kwh_rate_first_unit)
    print("Monthly Bill Calculation:")
    print("For Users Who's Usage Exceed 50 Kilo Watts But Is Less Than 150 The First 50 Is Subtracted From Your Overall Kilo Watts Used=", kwhused, end="")
    print("-", end="")
    print(mid_kwh_rate_first_unit)
    print("The Remainding Kilo Watts After The 50 Is Subtracted Is Then Multiplied By The Rate For Users Who Exceed 50 But Is Less Than 150=", monthbill, end="")
    print("*", end="")
    print(mid_kwh_rate)
    monthbill=(monthbill*mid_kwh_rate)
    print("The First 50 Is Charged As $29.50 Which Is Then Added To The Remainding Kilo Watts Which Was Multiplied By The Rate=", monthbill, end="")
    print("+", end="")
    print(mid_kwh_rate_first_unit_fee)
    monthbill=(monthbill+mid_kwh_rate_first_unit_fee)
    print("$13 Which Is The Standing Charge Is Then Added To The Overall Result=", monthbill, end="")
    print("+", end="")
    print(standing_charge)
    monthbill=(monthbill+standing_charge)
    print("This Month Bill is: $", monthbill)
elif kwhused > high_kwh_rate_first_unit:
    monthbill=(kwhused-high_kwh_rate_first_unit)
    print("Monthly Bill Calculation:")
    print("For Users Who's Usage Exceed 150 Kilo Watts The First 150 Is Subtracted From Your Overall Kilo Watts Used=", kwhused, end="")
    print("-", end="")
    print(high_kwh_rate_first_unit)
    print("The Remainding Kilo Watts After The 150 Is Subtracted Is Then Multiplied By The Rate For Users Who Exceed 150=", monthbill, end="")
    print("*", end="")
    print(high_kwh_rate)
    monthbill=(monthbill*high_kwh_rate)
    print("The First 150 Is Charged As $94.50 Which Is Then Added To The Remainding Kilo Watts Which Was Multiplied By The Rate=", monthbill, end="")
    print("+", end="")
    print(high_kwh_rate_first_unit_fee)
    monthbill=(monthbill+high_kwh_rate_first_unit_fee)
    print("$13 Which Is The Standing Charge Is Then Added To The Overall Result=", monthbill, end="")
    print("+", end="")
    print(standing_charge)
    monthbill=(monthbill+standing_charge)
    print("This Month Bill is: $", monthbill)
    

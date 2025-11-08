
#Name: Ayokunmi, Sodamola
#Course: MIS 5301 – Semester Year 
#Purpose: Sales Forcating
#File: MIS5301-PE3-Victorino Consultants.py
import datetime

#---Application Header --------------------------------------------

#CONSTANT
INDENT_1 = ' '*5
INDENT_2 = ' '*7
INDENT_3 = ' '*3
NAME = 'Marino Italian Ristorante'

#OUTPUT-----------------------------
print ()
print ('*'*58)
print (f'{"Victoriono Consultants - Sales Forecasting Tool":^58}')
print ('*'*58)
print ()

#  System Configuration
print (INDENT_1, 'Enter System Configuration')
ux_client_name = input('         Client Name: ')
ux_month_name = input('         Starting Month: ')
ux_number_forecast = int(input('         Number of Forecast Months: '))

#PROCESS-----------------------------
#Convert month name to month number

month_name_input = ux_month_name.strip()

if month_name_input in ['January', 'Jan']:
    month_num = 1
elif month_name_input in ['February', 'Feb']:
    month_num = 2
elif month_name_input in ['March', 'Mar']:
    month_num = 3
elif month_name_input in ['April', 'Apr']:
    month_num = 4
elif month_name_input == 'May':
    month_num = 5
elif month_name_input in ['June', 'Jun']:
    month_num = 6
else:
    month_num = 7

#-------------------------------------------------
#  Monthly Sales Data
print ()
print ('='*58)
print (f'{"MONTHLY SALES DATA":^58}')
print ('='*58)
print ()
total_units = 0
total_sales = 0.0
another ='y'
while another == 'y':
    date_obj = datetime.date(2025, month_num, 1)
    month_name = date_obj.strftime('%B')

    print(' '*5,'Enter Data for', month_name)
    units = int(input('        No. of units sold: '))
    sales = float(input('        Total sales: '))
    
    total_units += units
    total_sales += sales
    print()
    another = input("      >>> Enter Next Month's Data (y/n)? ")
    print()
    month_num += 1

#Display Sales Summary

print('         ------- Sales Summary -------')
print ()
print (f'{"":>14}{"Units":<10}{"Sales":>14}')
print (f'{"":>14}{"-----":<10}{"-----":>14}')
print (f'{"":>4} {"Total ":>12}{total_units:<8}   ${total_sales:,.2f}')
avg_units = total_units//2
avg_sales = total_sales/2

#-------------------------------------------------
#  Sales Forecast
print ('='*58)
print (f'{ux_number_forecast:>18}{" - Month Sales Forecast":<29}')
print(f'{"for " + ux_client_name.upper():^58}')
print ('='*58)
forecast_total = 0
forecast_sale = avg_sales * 1.05

for i in range(ux_number_forecast):
    forecast_month_num = month_num + i
    forecast_date = datetime.date(2025, (forecast_month_num - 1) % 12 + 1, 1)
    forecast_month = forecast_date.strftime('%b')
    
    rounded_forecast = int(forecast_sale)
    print(f'{forecast_month:>10}     ${rounded_forecast:>7,}')
    
    forecast_total += rounded_forecast
    forecast_sale *= 1.05  # Increase by 5%

print(f'{"":>10}     {"--------":>10}')
print(f'{"Total":>10}     ${forecast_total:>7,}')
print(f'{"Average":>10}     ${forecast_total // ux_number_forecast:>7,}')

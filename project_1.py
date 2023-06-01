########################################################################################################################
#                                       TOPIC : Spreadsheet Analysis
# CREATOR : Rupa-Rd
########################################################################################################################

# Importing the necessary libraries

import csv
import matplotlib.pyplot as plt

# Reading data from sales.csv file

def read_data():
    data = [] #Empty list to store the individual rows into the list
    with open('sales.csv', 'r') as sales_csv: # Opening the file in read mode
        spreadsheet = csv.DictReader(sales_csv) # Reading through sales.csv file
        for row in spreadsheet:
            data.append(row) # Adding the rows into the list
    return data
sales = [] # Empty list to store the sales column
months = [] # Empty list to store the month column

def run():

    data = read_data() # Function call

    for row in data: # Iterating through the data list
        sale = int(row['sales'])
        month = row['month']
        months.append(month)
        sales.append(sale)

    total = sum(sales) # Finding the total sales for the year
    month_with_high_sale = max(sales) # Finding which month has the maximum sales
    month_with_low_sale = min(sales) # Finding which month has the minimum sales
    index_high = sales.index(month_with_high_sale) # Finding the index of the highest sales month
    index_low = sales.index(month_with_low_sale) # Finding the index of the lowest sales month

    # Printing the total sales, highest sales month, lowest sales month.

    print('Total sales: {}'.format(total))
    print(f'{months[index_high]} has the highest sale of {month_with_high_sale}')
    print(f'{months[index_low]} has the lowest sale of {month_with_low_sale}')

run()

########################################################################################################################
                                        # DATA VISUALISATION
########################################################################################################################

# DEFINING PIE CHART TO SEE THE DISTRIBUTION OF SALES IN THE YEAR 2018

x_axis = months # Defining Label for the chart
slice = sales # Defining the source
cols = ['r','b','g','y','c','orange','r','b','g','y','c','orange'] # Defining the ccolors

# Creating a pie chart
plt.pie(slice,labels = x_axis,colors = cols,startangle=True,explode=(0,0.3,0,0,0,0,0.2,0,0,0,0,0))

# Defining a title for the chart
plt.title("Months Vs Sales")
plt.show()
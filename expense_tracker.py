#make an expense tracker
#categorise by type
#bar charts of category wise expenses
#highliht the most expenive item
import numpy as np
import matplotlib.pyplot as plt
import csv

with open("expenses.csv",'r') as file:
    reader=csv.reader(file)
    header=next(reader)#skip the first row as it is a header
    items=[]
    expenses=[]
    for row in reader:
        items.append(row[0])
        expenses.append(int(row[1]))
expense=np.array(expenses) 
print(items)       
print(expense)

#max & min expensive
min_exp=np.argmin(expense)
most_exp=np.argmax(expense)#np.argmax on a 1D array always gives the index of the highest value
#output
print(f'most expensive item:{items[most_exp]}')
print(f'amount spent:{expense[most_exp]}')
print(f'most cheap item:{items[min_exp]}')
print(f'amount spent:{expense[min_exp]}')

#graphs
plt.pie(expense,labels=items,autopct='%1.1f%%',startangle=90)
plt.title('Your expense Tracker')
plt.axis('equal')
plt.show()





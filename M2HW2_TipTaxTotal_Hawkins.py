#CTI-110
#M2HW2-Tip Tax Total
#Jalessa Hawkins
#September 9, 2017

#Get the total food cost
foodcost= float(input('Enter food cost: '))

#Calculate sales tax
salesTax= foodcost * 0.07
print('The amount of sales tax due is $', format(salesTax, ',.2f'))
                                                 
#Calculate tip amount (this tip amount is calculated before sales tax)
tipAmount= foodcost * 0.18
print('The tip amount due is $', format(tipAmount, ',.2f'))

#Calculate total meal cost
totalMealcost= foodcost + salesTax
print('The total amount of the meal not including the tip is $', format(totalMealcost, ',.2f'))

#Calculate meal cost including tip
finalMealcost= totalMealcost + tipAmount
print('The total meal amount including the tip is $', format(finalMealcost, ',.2f'))

#CTI-110
#P2HW2 - Tip Tax Total
#Brittany Lundy
#06/19/2018

#Write a program that calculates the total cost of a meal purchased at a restaurant
#The program should ask the user to enter the charge for the food. It should then calculate the amount ofthe tip and the amount for sales tax.
#(Assume 18% tip and 7% sales tax.)
#Display both of these amounts as well as the total cost of the meal.

food = float( input("Enter the charge of food: " ) )
total_cost = food + (food * 0.07) + (food * 0.18)

print("Total meal cost is:$ %.2f" % total_cost)



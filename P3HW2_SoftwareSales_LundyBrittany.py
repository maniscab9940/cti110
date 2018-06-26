#Brittany Lundy
#CTI-110
#6/25/2018
#P3HW2_Software Sales

# A software company sells a package that retails for $99.
#Quantity       Discount
# 10-19         10%
# 20-49         20%
# 50-99         30%
# 100 or more   40%

userNumberOfPackages = int( input ( "Please enter the number of packages bought: "))

packagePrice = 99

if userNumberOfPackages < 10:
    discount = 0;
elif userNumberOfPackages < 20:
    discount = 0.10
elif userNumberOfPackages < 50:
    discount = 0.20
elif userNumberOfPackages < 100:
    discount = 0.30
else:
    discount = 0.40

subTotal = userNumberOfPackages * packagePrice
discountAmount = discount * subTotal
total = subTotal - discountAmount

print( "\nAmount of discount: $ "+ format( discountAmount, ",.2f") + \
       "\nTotal amount: $" + format( total, ",.2f" ))

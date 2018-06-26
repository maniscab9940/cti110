#Brittany Lundy
#6/25/2018
#CTI-110
#P3T1_Area of Rectangles

#This program's logic should have 3 branches
#1. The first rectangle has the larger area
#2 The second rectangle has the larger area
#3 Both rectangles have equal area
#Area = length * width

rectangle1length = float(input ( "Please enter the length of rectangle 1: ") )
rectangle1width = float(input ( "Please enter the width of rectangle 1: ") )
rectangle2length = float(input ( "Please enter the length of rectangle 2: ") )
rectangle2width = float(input ( "Please enter the width of rectangle 2: ") )

rectangle1Area = rectangle1length * rectangle1width
rectangle2Area = rectangle2length * rectangle2width

if rectangle1Area > rectangle2Area:
    print ("\nRectangle 1 is bigger than Rectangle 2" )
elif rectangle2Area > rectangle1Area:
    print ("\nRectangle 2 is bigger than Rectangle 1" )
else: 
    print ("\nRectangle 1 is equal to Rectangle 2")

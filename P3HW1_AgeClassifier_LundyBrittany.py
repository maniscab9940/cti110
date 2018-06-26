#Brittany Lundy
#CTI-110
#6/25/2018
#P3HW1: Age Classifier

#Write a program that asks the user to enter a person's age.
#If the person is 1 year old or less, he or she is an infant
# If the person is older than 1, but younger than 13, he or she is a child
#If the person is at least 13, but less than 20, he or she is a teenager.
#If the person is at least 20, he or she is an adult.


userAge = int(input ("Please enter your age: ") )

if userAge <= 1:
    print ( "\nYou are an infant" )
elif userAge < 13:
    print ( "\nYou are a child" )
elif userAge < 20:
    print ("\nYou are a teenager")
elif userAge >= 20:
    print ("\nYou are an adult")

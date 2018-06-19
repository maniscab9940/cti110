#CTI-110
#P2T1 - Sales Prediction
#Brittany Lundy
#06/19/2018

#A company has determined that it's annual profit is typically 23% of total sales.

#0.23 = 23%

projectedTotalSales = float( input( "Enter the projected amount of total sales: " ) )

profit = 0.23 * projectedTotalSales

print( "The profit is $" + format( profit , ",.2f" ) )

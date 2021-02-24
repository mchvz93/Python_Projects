#Marco Chavez
#Student ID 913519
#CS 10
#HW2PS2

#input
total_profit = 0
stkname = input("Enter a stockname, enter -999 to quit: ")

while stkname!= "-999":
        numshar = int(input("Enter the number of shares: "))
        purpr = float(input("Enter the purchase price: "))
        sellpr = float(input("Enter the selling price: "))
        brkcom =  float(input("Enter the brokers commission: "))
        
        #calc
        amntpd = numshar*purpr
        brkcom1 = amntpd*brkcom
        soldstk =  numshar*sellpr
        brkcom2 = soldstk*brkcom
        profit = (soldstk-brkcom)-(amntpd+brkcom)
        
        #print
        print("The name of the stock is: ",stkname)
        print("The amount paid for stock is: ", format(amntpd, '.2f'))
        print("The amount paid to broker when bought the stock at first: ", format(brkcom1, '.2f'))
        print("The amount stock sold for: ", format(soldstk, '.2f'))
        print("The amount commission paid to broker after stock sold: ",format(brkcom2, '.2f'))
        print("The profit/loss of the stock is: ",format(profit, '.2f'))
        print("*****************************************************************")
        stkname = input("Enter a stockname, enter -999 to quit: ")
        total_profit += profit

print("The total profit is: ", format(total_profit, '.2f'))

#output
'''Enter a stockname, enter -999 to quit: schmo
Enter the number of shares: 20
Enter the purchase price: 2
Enter the selling price: 12
Enter the brokers commission: .10
The name of the stock is:  schmo
The amount paid for stock is:  40.00
The amount paid to broker when bought the stock at first:  4.00
The amount stock sold for:  240.00
The amount commission paid to broker after stock sold:  24.00
The profit/loss of the stock is:  199.80
*****************************************************************
Enter a stockname, enter -999 to quit: MK
Enter the number of shares: 2
Enter the purchase price: 33
Enter the selling price: 42
Enter the brokers commission: .2
The name of the stock is:  MK
The amount paid for stock is:  66.00
The amount paid to broker when bought the stock at first:  13.20
The amount stock sold for:  84.00
The amount commission paid to broker after stock sold:  16.80
The profit/loss of the stock is:  17.60
*****************************************************************
Enter a stockname, enter -999 to quit: -999
The total profit is:  217.40'''

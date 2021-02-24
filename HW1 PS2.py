#Marco Chavez
#Student ID 913519
#CS 10
#HW2PS2

#input
total_profit = 0.0
profit = 0
stkname = str(input("Enter a stockname, enter -999 to quit: "))
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
    profit = (soldstk - brkcom2) - (amntpd+brkcom1)

    #print
    print("The name of the stock is: ",stkname)
    print("The amount paid for stock is: $", format(amntpd, '.2f'))
    print("The amount paid to broker when bought the stock at first: $", format(brkcom1, '.2f'))
    print("The amount stock sold for: $", format(soldstk, '.2f'))
    print("The amount commission paid to broker after stock sold: $",format(brkcom2, '.2f'))
    print("The profit/loss of the stock is: $",format(profit, '.2f'))
    stkname = str(input("Enter a stockname, enter -999 to quit: "))

    total_profit += profit
print("The total profit is: $", format(total_profit, '.2f'))

'''
Enter a stockname, enter -999 to quit: schmoe
Enter the number of shares: 20
Enter the purchase price: 1
Enter the selling price: 10
Enter the brokers commission: .10
The name of the stock is:  schmoe
The amount paid for stock is: $ 20.00
The amount paid to broker when bought the stock at first: $ 2.00
The amount stock sold for: $ 200.00
The amount commission paid to broker after stock sold: $ 20.00
The profit/loss of the stock is: $ 158.00
Enter a stockname, enter -999 to quit: -999
The total profit is: $ 158.00
>>> 


    


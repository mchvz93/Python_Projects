total_profit = 0
profit = 0

num_stock = int(input("Enter the number of stocks you want to input: "))

for x in range(num_stock):
    stkname = str(input("Enter a stockname: "))
    numshar = int(input("Enter the number of shares: "))
    purpr = float(input("Enter the purchase price: "))
    sellpr = float(input("Enter the selling price: "))
    brkcom =  float(input("Enter the brokers commission: "))
    
    amntpd = numshar*purpr
    brkcom1 = amntpd*brkcom
    soldstk =  numshar*sellpr
    brkcom2 = soldstk*brkcom
    profit = (soldstk-brkcom) - (amntpd+brkcom)

    print("The name of the stock is: ",stkname)
    print("The amount paid for stock is: $", format(amntpd, '.2f'))
    print("The amount paid to broker when bought the stock at first: $", format(brkcom1, '.2f'))
    print("The amount stock sold for: $", format(soldstk, '.2f'))
    print("The amount commission paid to broker after stock sold: $",format(brkcom2, '.2f'))
    print("The profit/loss of the stock is: $",format(profit, '.2f'))
    print("****************************************************************")

    total_profit += profit
    

print("The total profit is: $",format(total_profit, '.2f'))

'''Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Enter the number of stocks you want to input: 3
Enter a stockname: schmoe
Enter the number of shares: 4
Enter the purchase price: 2.00
Enter the selling price: 4.00
Enter the brokers commission: .10
The name of the stock is:  schmoe
The amount paid for stock is: $ 8.00
The amount paid to broker when bought the stock at first: $ 0.80
The amount stock sold for: $ 16.00
The amount commission paid to broker after stock sold: $ 1.60
The profit/loss of the stock is: $ 7.80
****************************************************************
Enter a stockname: chubb
Enter the number of shares: 5
Enter the purchase price: 2.00
Enter the selling price: 6.00
Enter the brokers commission: .10
The name of the stock is:  chubb
The amount paid for stock is: $ 10.00
The amount paid to broker when bought the stock at first: $ 1.00
The amount stock sold for: $ 30.00
The amount commission paid to broker after stock sold: $ 3.00
The profit/loss of the stock is: $ 19.80
****************************************************************
Enter a stockname: scubs biz
Enter the number of shares: 8
Enter the purchase price: 2.00
Enter the selling price: 3.00
Enter the brokers commission: .1
The name of the stock is:  scubs biz
The amount paid for stock is: $ 16.00
The amount paid to broker when bought the stock at first: $ 1.60
The amount stock sold for: $ 24.00
The amount commission paid to broker after stock sold: $ 2.40
The profit/loss of the stock is: $ 7.80
****************************************************************
The total profit is: $ 35.40
>>> '''

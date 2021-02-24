#This is HW3 program set 1
#Marco Chavez
#Student ID 913519
#CS 10 Mon/Wed

def main():
    stock = (input("Enter the name of the stock, enter -999 to quit: "))
    while stock != "-999":
        stocknum, purpr, sellpr, bkr = load()
        amntpd, bkr1, soldstck, bkr2, totalpro = calc_stockinfo(stocknum, purpr, sellpr, bkr)
        prtprof(stock, amntpd, bkr1, soldstck, bkr2, totalpro)
        stock = (input("Enter the name of the stock, enter -999 to quit: "))
    
def load():  
    stocknum = int(input("Enter the number of shares Joe bought: "))
    purpr = float(input("Enter the purchase price of the stock: $" ))
    sellpr = float(input("Enter the selling price of the stock: $"))
    bkr = float(input("Enter the broker's commission: "))
    print("=====================================================")
    return stocknum, purpr, sellpr, bkr

def calc_stockinfo(stocknum, purpr, sellpr, bkr):
    amntpd = stocknum * purpr
    bkr1 = amntpd * bkr
    soldstck = stocknum * sellpr
    bkr2 = soldstck * bkr
    totalpro = (soldstck - bkr)- amntpd + bkr 
    return amntpd, bkr1, soldstck, bkr2, totalpro

def prtprof(stock, amntpd, bkr1, soldstck, bkr2, totalpro):
    print("The name of the stock is:                            ", stock)
    print("The amount paid for the stock:                      $", format(amntpd, '5.02f'))
    print("The amount paid to commission paid to broker:       $", format(bkr1,'5.02f'))
    print("The amount the stock sold for:                      $", format(soldstck, '5.02f'))
    print("The amount paid to broker after the stock was sold: $", format(bkr2, '5.02f'))
    print("The the total profit/loss is:                       $", format(totalpro, '5.02f'))
    if totalpro > 0:
        print("Joe made a profit")
        else totalpro < 0:
            print("Joe had lost money")
    
main ()
    

'''Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Enter the name of the stock, enter -999 to quit: Schmoe Inc
Enter the number of shares Joe bought: 20
Enter the purchase price of the stock: $1.00
Enter the selling price of the stock: $3.00
Enter the broker's commission: .10
=====================================================
The name of the stock is:                             Schmoe Inc
The amount paid for the stock:                      $ 20.00
The amount paid to commission paid to broker:       $  2.00
The amount the stock sold for:                      $ 60.00
The amount paid to broker after the stock was sold: $  6.00
The total commission paid for both stocks is:       $  8.00
The the total profit/loss is:                       $ 40.00
Enter the name of the stock, enter -999 to quit: '''
    


#This is HW3 PS1
'''Marco Chavez
Student ID 913519
CS 10 Mon, Wed'''

def main():
    totalpro = 0
    stock = input("Enter a stock name, -999 to quit: ")
    while stock != '-999':
         stocknum, purpr, sellpr, bkr = load()
         amntpd, bkr1, soldstck, bkr2, comm, totalpro = calc(stocknum, purpr, sellpr, bkr)
         
         

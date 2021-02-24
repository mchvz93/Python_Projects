import tkinter

class loan:
    def __init__(self):
        #Window form
        self.main_window = tkinter.Tk()

        #.....
        self.yearlyInt_frame = tkinter.Frame(self.main_window)
        self.numYear_frame = tkinter.Frame(self.main_window)
        self.loanAmount_frame = tkinter.Frame(self.main_window)
        self.borName_frame = tkinter.Frame(self.main_window)
        self.borNameshow_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        self.monthlyPay_frame = tkinter.Frame(self.main_window)
        self.totalPay_frame = tkinter.Frame(self.main_window)

        self.yearlyInt_label = tkinter.Label(self.yearlyInt_frame, text='Enter yearly interest rate:')
        self.yearlyInt_entry = tkinter.Entry(self.yearlyInt_frame, width=10)
        self.yearlyInt_label.pack(side='left')
        self.yearlyInt_entry.pack(side='left')

        self.numYear_label = tkinter.Label(self.numYear_frame, text='Enter number of years as an integer:')
        self.numYear_entry = tkinter.Entry(self.numYear_frame, width=10)
        self.numYear_label.pack(side='left')
        self.numYear_entry.pack(side='left')

        self.loanAmount_label = tkinter.Label(self.loanAmount_frame, text='Enter loan amount:')
        self.loanAmount_entry = tkinter.Entry(self.loanAmount_frame, width=10)
        self.loanAmount_label.pack(side='left')
        self.loanAmount_entry.pack(side='left')
        
        #find the way to make string print
        
        self.borName_label = tkinter.Label(self.borName_frame, text='Enter a borrower\'s name:')
        self.borName = tkinter.StringVar()
        self.borName_entry = tkinter.Entry(self.borName_frame, width=20)
        self.borName_label.pack(side='left')
        self.borName_entry.pack(side='left')
        

        self.result_label = tkinter.Label(self.borNameshow_frame, text='The loan is for: ')
        self.borNameshow = tkinter.StringVar()
        self.borNameshow_label = tkinter.Label(self.borNameshow_frame, textvariable=self.borNameshow)
        self.result_label.pack(side='left')
        self.borNameshow_label.pack(side='left')


        
        self.result_label = tkinter.Label(self.monthlyPay_frame, text='The monthly payment is: ')
        self.monthlyPay = tkinter.StringVar()
        self.monthlyPay_label = tkinter.Label(self.monthlyPay_frame, textvariable=self.monthlyPay)
        self.result_label.pack(side='left')
        self.monthlyPay_label.pack(side='left')

        self.result_label = tkinter.Label(self.totalPay_frame, text='The total payment is: ')
        self.totalPay = tkinter.StringVar()
        self.totalPay_label = tkinter.Label(self.totalPay_frame, textvariable=self.totalPay)
        self.result_label.pack(side='left')
        self.totalPay_label.pack(side='left')

        
        
        
        self.calc_button = tkinter.Button(self.button_frame, text='Calculate', command=self.calc_sum)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.yearlyInt_frame.pack()
        self.numYear_frame.pack()
        self.loanAmount_frame.pack()
        self.borName_frame.pack()
        self.borNameshow_frame.pack()
        self.monthlyPay_frame.pack()
        self.totalPay_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()


    def calc_sum(self):
        self.yearlyInt = float(self.yearlyInt_entry.get())
        self.numYear = float(self.numYear_entry.get())
        self.loanAmount = float(self.loanAmount_entry.get())
        self.borName = str(self.borName_entry.get())

        self.totalPayy = self.loanAmount * self.yearlyInt / (1 - (1 / (1 + self.yearlyInt) ** (self.numYear * 12)))
        self.monthlyPayy = self.yearlyInt * self.numYear * 12

        self.borNameshow.set(self.borName)
        self.monthlyPay.set(self.monthlyPayy)
        self.totalPay.set(self.totalPayy)

loan()
                                                             
                     
        
        

        

# Name: Sara Rydell
# P-uppgift: 145 Varuprisdatabas
# First date of revision: 2022-01-11 -> E
# Second date of revision: 2022-04-12 -> B
# Third date of revision: 2022-06-08 -> A

from tkinter import *
from GUI_Varuprisdatabas import *

class Window():
    def __init__(self,window):
        self.window=window
        self.original_stock = creating_original_stock() 

        #creating columns
        window.columnconfigure(0,weight=1) 
        window.columnconfigure(1,weight=1)

        #headding
        Label(window,text="Sara's General Store",font=("Helvetica", 17)).grid(column=0,row=0,padx=30,pady=15)
        
        #introduction
        Label(window,text="Welcome to Sara's General Store! :)").grid(column=0,row=1,padx=30,pady=15)
        
        #writing the product list
        product_list='''These are the products available, described in the following format:
        Product name, product code, quantity in stock, and product price.

        Buryan 100 53 68.98
        Banana 101 22 5.55
        Apple 102 95 2.7
        Pear 103 47 4.87
        Kebab 104 14 78.95
        Lemon 105 68 12.0
        Avocado 106 74 14.0
        Chips 107 352 14.99
        Orange 108 56 5.0
        Coffee 109 27 19.0
        Baklava 110 62 13.50
        Mango 111 51 14.0
        Sushi 112 74 55.75'''
        Label(window,text=product_list).grid(column=0,row=2,padx=30,pady=15)
        #instructions program
        instructions='''1. To add one product to your purchase: Write the product's product code, 
        then the wanted quantity seperated with blank space and press the "Add" button.

        2. To remove groceries from your purchase: Write a new order for that 
        product but with a minus sign before the ammount you want to return.

        3. To finish your purchase, print the receipt, and quit this program: 
        Press the "Finish" button.'''
        Label(window,text=instructions).grid(column=0,row=3,padx=30,pady=15)

        #writing an example order
        example='''Example order: 
        Buying two bags of chips and finishing the purchase: 107 2 "Add" "Finish"'''
        Label(window,text=example).grid(column=0,row=4,padx=30,pady=15)

        #starting order
        Label(window,text="Here starts your order: ").grid(column=1,row=0,sticky=W,padx=30,pady=15)

        #order entry
        self.order_entry=Entry(window)
        self.order_entry.grid(column=1,row=0,sticky=W,padx=160,pady=15)

        #order button
        Button(window,text="Add",command=self.when_add).grid(column=1,row=0,sticky=W,padx=300,pady=15)

        #finish button
        Button(window,text="Finish",command=self.when_finish).grid(column=1,row=0,sticky=W,padx=350,pady=15)

        self.message_text=Label(self.window)
        self.message_text.grid(column=1,row=1,sticky=W,padx=30,pady=15)

        self.receipt_text=Label(self.window)
        self.receipt_text.grid(column=1,row=2,sticky=W,padx=30,pady=15)

    def when_add(self):
        order_string=self.order_entry.get()
        self.order_entry.delete(0,"end")
        self.message_text.config(text="")
        message=ordering_products(self.original_stock,order_string)
        self.message_text.config(text=message)
        
    def when_finish(self):
        Label(self.window,text="Thank you for your visit!").grid(column=1,row=1,sticky=W,padx=30,pady=15)
        self.receipt_text.config(text="")
        self.message_text.config(text="")
        receipt=creating_receipt(self.original_stock)
        self.receipt_text.config(text=receipt)
        updating_file(self.original_stock)
    
def main():
    window = Tk() 
    mywindow=Window(window)
    window.title("145 Varuprisdatabas by Sara Rydell")
    window.geometry("1300x650")
    window.mainloop()

main()

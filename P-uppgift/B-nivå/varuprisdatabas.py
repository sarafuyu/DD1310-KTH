# Name: Sara Rydell
# P-uppgift: 145 Varuprisdatabas
# First date of revision: 2022-01-11 -> E
# Second day of revision: 2022-04-12 -> B

#original content from the text file databas.txt
'''
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
Sushi 112 74 55.75
'''

#classes and methods used in this program
class Stock:
    '''class for creating the stock of all products listed in databas.txt |
    IN: databas.txt | OUT: stock objects with the belonging attributes (name, code, quantity, and price)'''
    
    #attributes used for stock objects
    def __init__(self, name, code, quantity, price):
        '''creates all attributes belonging to the stock objects used in the program | 
        IN: - | OUT: product name as name, product code as code, the initial product quantity number as original_quantity, product quantity varibale used in the program as current_quantity, the product price as price
        '''
        self.name = name                    #product name
        self.code = code                    #product code
        self.original_quantity = quantity   #original product quantity: the original value of quantity when the file has been opened
        self.current_quantity = quantity    #current product quantity: the quantity that changes during the purchase depending on the user's inputs
        self.price = price                  #product price

    #methods returning the stock products' chosen attributes
    def give_name(self):
        '''IN: - | OUT: the choosen product's product name'''
        return self.name

    def give_code(self):
        '''IN: - | OUT: the choosen product's product code'''
        return self.code

    def give_original_quantity(self):
        '''IN: - | OUT: the choosen product's initial stock quantity'''
        return self.original_quantity

    def give_current_quantity(self):
        '''IN: - | OUT: the choosen product's updated stock quantity'''
        return self.current_quantity

    def give_price(self):
        '''IN: - | OUT: the choosen product's price'''
        return self.price

    def str_for_file(self):
        '''creates a string for updating the stock after ending a purchase | 
        IN: - | OUT: a string with all attributes of the choosen product used for updating the textfile databas.txt'''
        return self.name + " " + str(self.code) + " " + str(self.current_quantity) + " " + str(self.price)

    #methods used in the program
    def changing_quantity(self, order_quantity):
        '''changes the quantity of the stock based on user input | 
        IN: user input | OUT: changes product quantity in stock'''
        if self.current_quantity - order_quantity >= 0:
            if self.current_quantity - order_quantity > self.original_quantity:
                self.current_quantity = self.original_quantity
            else:
                self.current_quantity -= order_quantity
        else:
            self.current_quantity = 0
    
    def checking_stock(self, stock_quantity):
        '''checks if there's enough product in stock for an order by controlling the amount available | 
        IN: user input | OUT: True or False'''
        if stock_quantity <= self.current_quantity:
            return True
        else:
            return False

#functions used in the program
def creating_original_stock():
    '''reads the file, changes the information's format and creates stock objects of all listed products | 
    IN: - | OUT: list with all product objects with defined attributes'''
    #reads the file
    file = open("databas.txt")
    file_content = file.readlines()

    #changes the format of the file content
    stock_lines = []
    for line in file_content:
        stock_lines.append(line.replace("\n", ""))
    stock_products = []
    for attribute in stock_lines:
        stock_products.append(attribute.split(" "))

    #creates stock objects and returns them in a list
    original_stock = []
    for product in stock_products:
        stock_name = product[0]
        stock_code = product[1]
        stock_quantity = product[2]
        stock_price = product[3]
        stock_product = Stock(stock_name, int(stock_code), int(stock_quantity), float(stock_price))
        original_stock.append(stock_product)
    return original_stock

def introducing_program():
    '''writes an introduction for the program | 
    IN: - | OUT: program introduction'''
    print("\n145 Varuprisdatabas by Sara Rydell\n")
    print("Welcome to Sara's General Store! :)\n")
    print("1. To add one product to your purchase: Write the product's product code, and then the wanted quantity seperated with blank space.")
    print("2. To remove groceries from your purchase: Write a new order for that product but with a minus sign before the ammount you want to return.")
    print("3. To finish your purchase, print the receipt, and quit this program: Write hashtag. \n")

def showing_stock_menu(original_stock):
    '''IN: list with all product objects | OUT: product information (namne,code,quantity,price) and a "how to use" guide'''
    print("These are the products available described in the following format: \nProduct name, product code, quantiyt in stock, and product price.\n")
    for product in original_stock:
        print(product.str_for_file())
    print("\nThis example of an order would add two bags of chips to your order and finishes your purchase:")
    print("107 2")
    print("#\n")
    print("Here starts your order:")
    
def trying_integer(input):
    '''checks if the user's input is an integer | IN: user input | OUT: user input or error message'''
    try:
        return int(input)
    except:
        print("{} is not a valid input, please try again".format(input))
        return False

def ordering_products(original_stock):
    '''processes the user's inputs | 
    IN: list with all product objects | OUT: creates changes to the original_stock, gives error messages and user instructions based on the user's inputs'''
    while True:
        #receives the user's input and changes the format
        user_order = input(">>> ")
        split_user_order = user_order.split(" ")
        stock_code = None
        stock_quantity = None
        #prints the receipt
        if user_order == "#":
            creating_receipt(original_stock)
            break
        #if there's no input
        if user_order == "":
            print("Please enter an order.")
        #if the input is an integer, checks if the first number is a valid product code
        if split_user_order[0].isdigit():
            stock_code = trying_integer(split_user_order[0])
        #if only the product code is written the default quantity is one. otherwise the product quantity (an integer +/-) will be processed
        if len(split_user_order) == 1:
            stock_quantity = 1
        elif len(split_user_order) >= 2:
            if not split_user_order[1].strip("-").isdigit():
                print("The wanted quantity should be a number. Please only write digits")
            else:
                stock_quantity = trying_integer(split_user_order[1])
        #if the product exists and the wanted quantity is available, that amount is removed from the stock quantity
        product_exists = False
        for product in original_stock:
            if stock_code == product.give_code():
                product_exists = True
                if stock_quantity:
                    if product.checking_stock(stock_quantity):
                        product.changing_quantity(stock_quantity)
                        print("Your order changed with {} {}.".format(stock_quantity, product.give_name().lower()))
                    else:
                        print("We only have {} of the product {} in store, ".format(product.give_current_quantity(), product.give_name().lower()) + "please choose a smaller quantity or another product.")
        #asks for another input if code is invalid
        if not product_exists:
            print("Please enter another product code, we don't seem to have this product.")
    
def creating_receipt(original_stock):
    '''IN: list with all product objects (modified) | OUT: a receipt describing the user's purchase'''
    #prints the top of the receipt
    print("\nHere is your receipt!")
    print("\n       *** SARA'S GENERAL STORE ***\n")
    print("Stock\t      Quantity   A-price   Sum")
    print("__________________________________________")

    #creates the receipt based on the user's order
    quantity = 0
    sum = 0
    for product in original_stock:
        ordered_quantity = product.give_original_quantity() - product.give_current_quantity()
        product_sum = ordered_quantity * product.give_price()
        if ordered_quantity:
            quantity += ordered_quantity
            sum += product_sum
            print("{:<14}{:<11}{:<10}{}".format(product.give_name(), str(ordered_quantity), str(product.give_price()), str(round(product_sum, 2))))

    #creates the line for the total purchase 
    print("__________________________________________")
    print("{:<14}{:<21}{}".format("Total", str(quantity), str(round(sum, 2))))
    print("\nThank you for your visit!\n")

def updating_file(original_stock):
    '''the stock is updated in the list original_stock_rows and is written in the text file "databas.txt" | 
    IN: list with all product objects (modified) | OUT: updates the original text file "databas.txt"'''
    write = open("databas.txt", "w")
    for product in original_stock:
        write.write(product.str_for_file() + "\n")
    write.close()

def main():
    '''main function that runs the program | IN: - | OUT: the full program'''
    original_stock = creating_original_stock()
    introducing_program()
    showing_stock_menu(original_stock)
    ordering_products(original_stock)
    updating_file(original_stock)

#runs the program
main()

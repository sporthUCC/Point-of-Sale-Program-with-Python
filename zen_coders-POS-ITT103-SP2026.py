# I CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMENT 
# Signed: Saraijah Porth



#creating product catalog using a list of dictionaries 
#To make it simple for the cashier or user to add or update products during the sale, I'm storing product data in a list.
#Each dictionary has 4 key value pairs:
#Product ID: Unique identifier used to search or select items
#ItemName: The name of the product that was displayed to the cashier
#Price: The cost of the item/s
#stock" The amount of items that are available in the inventory

product_catalog = [
    {"productId": 0,
    "itemName":"Grace coconut milk",
    "price":250,
    "stock":200
    },
    {"productId": 1,
    "itemName":"Bigga Soda",
    "price":100,
    "stock":156
    },
    {"productId": 2,
    "itemName":"Tastee cheese",
    "price":2000,
    "stock":250
    },
    {"productId": 3,
    "itemName":"Maggi seasoning",
    "price":100,
    "stock":85
    },
    {"productId": 4,
    "itemName":"Excelsior crackers",
    "price":150,
    "stock":79
    },
    {"productId": 5,
    "itemName":"Condensed milk",
    "price":500,
    "stock":40
    },
    {"productId": 6,
    "itemName":"Kiss Cake",
    "price":120,
    "stock":250
    },
    {"productId": 7,
    "itemName":"Foska Oats",
    "price":250,
    "stock":50
    },
    {"productId": 8,
    "itemName":"2 litre Tropicana",
    "price":350,
    "stock":87
    },
    {"productId": 9,
    "itemName":"Dettol Soap",
    "price":600,
    "stock":56
    },
    {"productId": 10,
    "itemName":"Downy fabric softener",
    "price":210,
    "stock":56
    },
]

#initializing empty cart so that we can use it later in functions such as adding items, removing item and viewing the carts
cart = []


#The purpose of this function is to show the product catalog. At the beginning of the program, to the cashier
#We used print statement for the product catalog header
#Using the f string and :< :> to maintain orderly and tidy values for user experience
def display_catalog():
    print("================================================")
    print("|                PRODUCT CATALOG                |")
    print("================================================")
    print(f"{'ID':<5}|{'Product':<25}|{'Price':<10} |{'Stock':<10}")
    #Looping through each product in the dictionary and print it values
    for product in product_catalog:
        print(f"{product['productId']:<5}|{product['itemName']:<25}|${product['price']:>10}|{product['stock']:>10}")

#calling the "display catalog" function, so that the cashier sees the catalog as soon as the program
#it is the first thing the cashier will see
display_catalog()


#This function will be responsible for adding items to the cart
#We will utilize a while loop which will remain running, until the cashier enters E to exit.
#The while loop allows multiple items to be added during one session without restarting the function
def add_to_cart():
    #Here, a loop is used to ensure that the menu continues to appear until the cashier has completed adding products.
    while True:
      #Found is always false at the start of the loop and reset to false at the start of the loop
      #helps us to track whether product ID entered by the cashier exist.
      found= False
      itemName_id = input("Enter Product ID to add to cart (Press E to exit): ")
      #checking for blank input and removing accidental spaces using the strip method()
      if itemName_id.strip() == "":
       print("ID input cannot be blank")
       continue
      #This "if" statement allows the cashier to exit the loop and return to the main menu
      if itemName_id.upper() == "E":
        break
      
      #This is to handle the values type that is entered by the cashier
      # try/except is used here due the fact that the input python method return a string
      #If a user accidentally writes a letter rather than an ID, prevent the software from crashing.
      #with the except  Value Error, which alerts the cashier to try again if the wrong data type was entered.
      try:
        itemName_id = int(itemName_id)
      except ValueError:
         print("Please Enter a valid ID Number ")
         continue 
         
     
      #---------------------------- start of the for loop------------------------------------
      #searching for product 
      #created a loop that allows the cashier to add multiple items at once.
      for product in product_catalog:
            if product["productId"]==itemName_id:
             #Checking if the product ID that was found in catalog if it still has units available.
             #If the stock is less than 0 or less than that mean we do not have any available stocks for that item
             if product['stock'] <=0:
                print(f"SORRY! {product['itemName']} is currently OUT OF STOCK and cannot be added")
                #This tracks if the product was found.
                found = True
                #Once a match is found we use the break keyword to exit the loop entirely.
                break
             #Confirming with the cashier/user that the product was found
             print(f"This product ID has been found: \nItem:{product['itemName']}\nPrice:${product['price']}")
             found = True
             #Entering the quantity 
             amount_of_item = input("Enter the quantity amount : ")
             #Ensuring blank values cannot be entered by the cashier
             if amount_of_item.strip()=="":
                print("QUANTITY CANNOT BE BLANK, PLEASE ENTER AN AMOUNT")
                continue
             
             #converting string input to a int and and ensurint that the cashier didn't type a letter by mistake
             #try/except catches any invalid data type that was entered
             try:
                amount_of_item = int(amount_of_item)
             except ValueError:
                print("Please Enter Valid number")
                continue
             
             #Validating quantity to ensure that the values entered are not equal to or less than zero.
             #A quantity of zero would add nothing to the cart, and the data would have been corrupted
             if amount_of_item <= 0:
                print("Quantity must be greater than zero")
                continue
             #checking stock
             #Helps to notify the user the stock availability.
             #Prevents selling more items than what is available in the catalog
             if amount_of_item > product['stock']:
                print(f"Sorry only, {product['stock']} items are available") 
                continue  
            
             #adding item to the cart dictionary using the python append () method
             #storing information such as product_id, itemName, quantity and price
             #The key value pairs in the cart will help us during checkout and receipt generation
             cart.append({
                "product_id":product["productId"],
                "itemName": product['itemName'],
                "quantity": amount_of_item,
                "price": product['price']
             })
            
            #reducing the stock by the quantity that was purchased
            #This helps to keep track of the items during the session
             product['stock'] =  product['stock'] - amount_of_item

             #checking stock amount after purchases
             #Notifying the cashier when items are running low 
             #0 means we are out of stock and below 5 means we are running low
             if product['stock'] == 0:
                print(f"{product['itemName']} is now out of Stock")
             elif product['stock'] < 5:
                print(f"{product['itemName']} Stocks are running low. Only {product['stock']} left")      
             #confirmation that the items were added successfully
             print(f"{amount_of_item}: {product['itemName']} successfully added to cart")

             #stop looking once we find and process the item
             break
      #-----------------------------------------------------End of the For loop----------------------------
      #error handling if product ID is not available in catalog
      # if found remains false after the loop, the product ID does not exist
      if not found:
        print("Sorry that Product ID does not exist****Please check catalog*****")
        print("Please check the Product Catalog")
        display_catalog()


#This function display all items currently in the cart
def view_cart():
    # checking if cart is empty before attempting to display it
    #if we tried to iterate over an empty list it would just show nothing
    # This helps to prevent confusion and give clear message to the cashier, if the cart is empty
    if cart == []:
        print("CART IS EMPTY")
        return
    print("================================================")
    print("                    YOUR CART                   ")
    print("================================================")
    #for loop so that we iterate over all the items in your cart
    for item in cart:
        #calculating the item total by multiplying quantity * the price of each item
        item_total = item['quantity'] * item['price']
        #Using print to display the results
        #the usage of the f string helps with the formatting which keep the output aligned and neat
        print(f"{item['product_id']:<5}:{item['itemName']:>20} x {item['quantity']:<10} | ${item['price']:<10} = ${item_total:<10}")


#--------------------------------------------------------------------------
#remove function was revised and updated
#receipt generation handled in generate receipt()
#clear cart resets for new customer transactions
#----------------------------------------------------------------------------

#function to remove item from cart
#when an item is removed from the cart, its quantity is added back to the product catalog inventory
#This ensures that we are updating the stocks when item are removed from cart
def remove_item():
    #The while loop keeps the function running until the user press E to exit
    while True:
      #checking if the cart is empty at the start of the loop
      if cart == []:
         print("CART IS EMPTY!!! ")
         # #If empty we exist the loop immediately using the break keyword
         break
      else:
        #checking items in the current cart so that the cashier know what can be removed
        view_cart()
      #Initializing the found value
      #This tracks whether the entered ID exist in the product catalog
      #resets to false on each individual search
      found = False
      #prompting the user to enter the product ID they would like to remove from cart
      item_to_be_removed = input("Enter the product ID to remove from the cart (Press E to exit):  ")
      #strip method removes any accidental spaces, it ensures that inputs cannot be empty
      if item_to_be_removed.strip() == "":
         print("ID cannot be blank")
         #If the values is empty, the loop restarts
         continue
      #allows the user to return to the main menu
      if item_to_be_removed.upper()=="E":
         break
      #Error Handling
      #Try/except was added to prevent the application from crashing in the event that the cashier unintentionally hits a letter rather than a number.
      #without this the program could crash when the int tries to convert a letter
      try:
        item_to_be_removed = int(item_to_be_removed)
      except ValueError:
        print("Please Enter a valid ID number")
        continue
      #searching for the matching product ID that the user  would like to remove
      for product in product_catalog:
         if item_to_be_removed == product['productId']:
            print(f"This product ID has been found: \nItem:{product['itemName']}\nPrice:${product['price']}")
            found = True

            #The loop will keep iterating once the condition is met
            while True:
               #Asking the user if they would like to remove item
               #helps to prevent accidental removal of cart items
               item_check = input("Do you want to remove this item completely? (Y/N)")
               item_check = item_check.upper()
               #Error handling
               #validating that only Y or N is accepted 
               if item_check not in ["Y", "N"]:
                  print('Please Enter valid input (Y/N)')
                  continue
               #checking to see if the Y was entered, if y was entered, this means that the user would like to remove item
               if item_check == "Y":
                  #searching for item in cart
                  for item in cart:
                     if item['itemName'] == product['itemName']:
                      #adding back the stock to the catalog/inventory
                      #this keeps the inventory accurate after removal
                      product['stock'] += item['quantity']
                      cart.remove(item)
                      print(f"{product['itemName']} removed from cart!")
                      #exiting the loop for searching and removing item
                      break
                  break
               elif item_check == "N":
                  #If the user changed their mind, cancelling the removal of an item and return to the cart view
                  print("Remove Cancelled...returning to cart")
                  break     
      #If still false after the loop this means the product ID was never in the catalog
      if not found:
        print("Product ID is not found")

#checkout function   
# This function handles the checkout for the user which generate a receipt once it  is called.
def checkout():
   #checking if the cart is empty before processing
   #no point in calculating a total if nothing was added to the cart
   if cart == []:
      print("Your cart is empty")
      return
   #initializing running subtotal to 0
   #As the cashier adds more items, the running_total keeps track of the total
   running_subtotal = 0
   for item in cart:
      #calculating the total of each item by multiplying the quantity * price 
      subtotal = item['quantity'] * item['price']
      #adding each item total to the running subtotal
      ##+= is the shorthand for running_subtotal = running_subtotal + subtotal
      running_subtotal +=subtotal
   #Initializing discounted_amount to 0 so it can be passed to generate_receipt
   #even if no discount is applied, this initialization helps to keep track
   discounted_amount = 0
   #prevents overwriting of the subtotal when doing the running_subtotal > 5000
   origin_subtotal = running_subtotal
   #applying if condition to check if the customer total is greater than 5000JMD
   #This is a fixed business rule for this POS system
   if running_subtotal> 5000:
      #applying 5% discount of the sub total as the discount_amount
      discounted_amount = running_subtotal * 0.05
      #substracting the discount from the subtotal before tax is applied
      #discount is applied first so that the tax is calculated on the discounted_amount
      running_subtotal = running_subtotal - discounted_amount
   #calculating 10% tax on the discounted amount
   #tax is calculated outside the loop because we only need one tax value on the final total 
   tax = running_subtotal * 0.10
   #adding tax to the discounted amount to get the final amount that should be paid
   total = running_subtotal + tax
   #:.2f calculates the final total to 2 decimal places
   print("==========================================")
   print(f"       The total is ${total:.2f}"         )
   print("==========================================")

   #Initializing change to 0 before the payment while loop
   change = 0
   #The while loops keeps true until a valid payment amount is entered
   while True:
      try:
         #user enter the the payment amount
         #using float instaed to allow decimal payment amount e.g 123.45JMD
         payment_amount = float(input("Enter the cash amount received: "))
         #If statement here is used to check that the payment is not less than the total amount due
         #This ensures that the customer cannot pay less because it is enforced by the program/application
         if payment_amount < total:
            print(f"Incomplete payment!Customer still owes ${total - payment_amount:.2f} ")
            continue
         #If the payment is valid the payment is process and the calculated change is returned to the customer
         if payment_amount >= total:
           change = payment_amount - total
           print(f"Customer change is ${change:.2f}")
         break
      except ValueError:
         #Catches the cases when the user enters an invalid data type
         #This helps to prevent the program from crashing, when the float() tries to convert it
         print("Invalid input. Please enter numeric amount")
   #passing all the calculated values as arguments in the generate_receipt function
   #The arguments must be passed in order to effectively generate the receipt
   generate_receipt(origin_subtotal, running_subtotal, discounted_amount, tax, total, payment_amount,change)
        
#This function generates a receipt at the end  of each transaction
#Parameters contain calculated values from the checkout() function
def generate_receipt(origin_subtotal,running_subtotal, discounted_amount, tax, total, payment_amount,change ):
   #printing the store header so the customer know which store the receipt is from
   print("=======================================================")
   print("|                BEST BUY RETAIL STORE                |")
   print("=======================================================")

   #looping through cart for receipt details using the for loop and this will give the customer a breakdown of each individual item of their purchase
   print('------------------------------------------------------' )
   for item in cart:
      #calculating item total
      item_total = item['quantity'] * item['price']
      #printing the name, quantity, unit price and total for each item and using :< which aligns the items 
      print(f"{item['itemName']:<20} x {item['quantity']} | {item['price']} = ${item_total}")
   print("-----------------------------------------------------")
   #generating the data for the receipt output using.
   print(f'Subtotal:                      ${origin_subtotal:.2f}')
   #Only printing the discount if a discount was actually applied this is if the item are over 5000 JMD dollars
   if  discounted_amount>0:
         print(f"Discount 5%                -${discounted_amount:.2f}")
         print(f"After Discount              ${running_subtotal:.2f}")
   #printing the 10% tax amount that was applied to the discounted amount
   print(f"Tax (10%)                    ${tax:.2f}")
  
   print('------------------------------------------------------')
   print(f"Total:                        ${total:.2f}")
   #printing the payment details so  the customer can verify
   print(f"Amount Paid:                 ${payment_amount:.2f}")
   #printing the change returned to the customer
   # if there was no change left it will display $0:00
   print(f"Change:                      ${change:.2f}")
   print("=======================================================")
   print("               THANK YOU FOR YOUR PURCHASE             ")
   print("=======================================================")



#clear cart Function
#This function clears all the item from the cart to prepare for new customer transaction and  prevents us from restarting the entire program and loosing session data
#Display catalog after clearing so the cashier can see the updated stock level before serving another customer
def clear_cart():
    #checking if the cart if empty
    #no point in asking the cashier to confirm clearing an empty cart
    if cart == []:
        print("Cart is already empty!")
        return
    #loop keeps running until a valid Y or N is enteres
    while True:
      #asking the cashier to confirm before clearing
      #This prevents accidental loss of all cart data
      #.upper()method ensures that either upper or lower case values are accepted
      confirm = input("Are you sure you want to clear the cart? (Y/N): ").upper()
      #cart.clear() removes all the items from the cart list
      if confirm not in ["Y", "N"]:
        print("Invalid input. Please enter Y or N only.")
        continue
      #this modifies the cart by using the existing list than creating a new one
      if confirm == "Y":
         cart.clear()
         print("Cart has been successfully cleared")
         #Displaying the catalog after clearing so the user can see 
         #the current stocks before starting a new transaction
         display_catalog()
         #exiting the loop
         break
      elif confirm == "N":
         #cashier change their mind and the cart remains unchanged
         print("Cart was not cleared.")
         #exiting the loop
         break





#menu for user selection, so that they can have full control of which function they would like to carry out
#This is the entry point of the program after the catalog is displayed
# A while loop keep the menu running
#The cashier can perform multiple operations without restarting due to the while loop.
#The loop stops when the cashier/user selects option 6
def main_menu():
    while True:
        #displaying the menu where the cashier can choose from
        print("\n1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Clear Cart")
        print("6. Exit     ")
        choice = input("Enter choice: ")

        #each option is mapped directly to one function in the program
        #the appropriate function will be called based on the cashier/user selection
        if choice == "1":
            add_to_cart()
        elif choice == "2":
           remove_item()
        elif choice == "3":
           view_cart()
        elif choice == "4":
           checkout()
        elif choice == "5":
            clear_cart()
        elif choice == "6":
           #break exits the while True loop and the program ends
           print("SEE YAH LATER..................")
           break
        else:
         #handling input that is not between 1-6
         print("Invalid Choice, please enter 1-6")
         



#calling the main_menu function to start the program which triggers the functions withing the method
main_menu()
 

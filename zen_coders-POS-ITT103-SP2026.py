from datetime import datetime


#Creating a class for a color
class Color:
    boldOne= '\033[1m'
    boldTwo = '\033[0m'

#creating product product catalog for product
#using a list within a dictionary/set

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

#initializing empty cart 
cart = []

#Displaying Product Catalog
def display_catalog():
    print("================================================")
    print("|                PRODUCT CATALOG                |")
    print("================================================")
    print(f"{Color.boldOne}{'ID':<5}|{'Product':<25}|{'Price':<10} |{'Stock':<10}{Color.boldTwo}")
    for product in product_catalog:
        print(f"{product['productId']:<5}|{product['itemName']:<25}|${product['price']:>10}|{product['stock']:>10}")

#Invoking the "display catalog function"
display_catalog()


#adding itemName to cart

def add_to_cart():
    #asking for itemName name
    while True:
      found= False
      itemName_id = input("Enter Product ID to add to cart (Press E to exit): ")
      #checking for blank for blank input and removing accidental spaces
      if itemName_id.strip() == "":
       print("ID input cannot be blank")
       continue
      if itemName_id.upper() == "E":
        break
      #If Cashier enters a letter when ask for id, 
      try:
        itemName_id = int(itemName_id)
      except ValueError:
         print("Please Enter a valid ID Number ")
         continue 
         
      #searching for product 
      #---------------------------- start of the for loop------------------------------------
      for product in product_catalog:
            if product["productId"]==itemName_id:
             if product['stock'] <=0:
                print(f"SORRY! {product['itemName']} is currently OUT OF STOCK and cannot be added")
                found = True
                break
             #Displaying product name and the price
             print(f"This product ID has been found: \nItem:{product['itemName']}\nPrice:${product['price']}")
             found = True
             #Enter the amount of item would 
             amount_of_item = input("Enter the quantity amount : ")
             if amount_of_item.strip()=="":
                print("QUANTITY CANNOT BE BLANK, PLEASE ENTER AN AMOUNT")
                continue
             
             #converting string input to a int and validating the data type
             try:
                amount_of_item = int(amount_of_item)
             except ValueError:
                print("Please Enter Valid number")
                continue
             
             #validating quantity to ensure that the valiues entered is not equal or less than zero
             if amount_of_item <= 0:
                print("Quantity must be greater than zero")
                continue
             #checking stock
             if amount_of_item > product['stock']:
                print(f"Sorry only, {product['stock']} items are available") 
                continue  
            
             #adding item to the cart using the python append method
             cart.append({
                "product_id":product["productId"],
                "itemName": product['itemName'],
                "quantity": amount_of_item,
                "price": product['price']
             })
            
            #reducing the stock
             product['stock'] =  product['stock'] - amount_of_item

             #checking stock amount after purchases
             if product['stock'] == 0:
                print(f"{product['itemName']} is now out of Stock")
             elif product['stock'] < 5:
                print(f"{product['itemName']} Stocks are running low. Only {product['stock']} left")      
             #confirmation that the items were added successfully
             print(f"{amount_of_item}: {product['itemName']} successfully added to cart")

             #stop looking once we find the item 
             break
      #-----------------------------------------------------End of the For loop----------------------------
      #error handling if prodcut ID is not available in catalog
      if not found:
        print("Sorry that Product ID does not exist****Please check catalog*****")
        print("Please check the Product Catalog")
        display_catalog()


#view cart function
def view_cart():
    # checking if cart is empty
    if cart == []:
        print("CART IS EMPTY")
        return
    print("================================================")
    print("                    YOUR CART                   ")
    print("================================================")
    #for loop so than we iterate over all the items in your cart
    for item in cart:
        item_total = item['quantity'] * item['price']
        print(f"{item['product_id']:<5}:{item['itemName']:>20} x {item['quantity']:<10} | ${item['price']:<10} = ${item_total:<10}")


#--------------------------------------------------------------------------
#remove function was revised and updated
#receipt generation handled in generate receipt()
#clear cart resets for new customer transactions
#----------------------------------------------------------------------------

#function to remove item from cart
def remove_item():
    while True:
      #checking if the cart is empty
      if cart == []:
         print("CART IS EMPTY!!! ")
         break
      else:
        #checking items in cart
        view_cart()
      #intitializing the found value
      found = False
      #prompting the user to enter the product ID they would like to remove from cart
      item_to_be_removed = input("Enter the product ID to remove from the cart (Press E to exit):  ")

      if item_to_be_removed.strip() == "":
         print("ID cannot be blank")
         continue
      if item_to_be_removed.upper()=="E":
         break
      #Error Handling
      try:
        item_to_be_removed = int(item_to_be_removed)
      except ValueError:
        print("Please Enter a valid ID number")
        continue
      #searching for the product that they would like to remove
      for product in product_catalog:
         if item_to_be_removed == product['productId']:
            print(f"This product ID has been found: \nItem:{product['itemName']}\nPrice:${product['price']}")
            found = True

            #Asking the user if they would like to remove item
            item_check = input("Do you want to remove this item completely? (Y/N)")
            item_check = item_check.upper()
            #Error handling
            if item_check not in ["Y", "N"]:
               print('Please Enter valid input (Y/N)')
               continue
            #checking to see if the Y was entered, if y was entered, this means that the user would like to remove item
            if item_check == "Y":
               #searching for item in cart
               for item in cart:
                  if item['itemName'] == product['itemName']:
                   #adding back the stock to the catalog/inventory
                   product['stock'] += item['quantity']
                   cart.remove(item)
                   print(f"{product['itemName']} removed from cart!")
                   #exiting the loop for searching and removing item
                   break
               break
            elif item_check == "N":
               print("Remove Cancelled...returning to cart")
               break     
      if not found:
        print("Product ID is not found")

#checkout function   
def checkout():
   if cart == []:
      print("Your cart is empty")
      return
   #initializing running  subtotal
   running_subtotal = 0
   for item in cart:
      #calculating the total of each item
      subtotal = item['quantity'] * item['price']
      running_subtotal +=subtotal
      #print(f"\nSubtotal: ${running_subtotal}")
   discounted_amount = 0
   if running_subtotal> 5000:
      #applying 5% discount
      discounted_amount = running_subtotal * 0.05
      running_subtotal = running_subtotal - discounted_amount
      #calculating tax on discounted amount
   tax = running_subtotal * 0.10
   total = running_subtotal + tax
   print("==========================================")
   print(f"       The total is ${total:.2f}"         )
   print("==========================================")

   #Calculate the amount payment
   #Intitializing change
   change = 0
   while True:
      try:
         #user enter the the payment amount
         payment_amount = float(input("Enter the cash amount received: "))
         if payment_amount < total:
            print(f"Incomplete payment!Customer still owes ${total - payment_amount:.2f} ")
            continue
         if payment_amount >= total:
           change = payment_amount - total
           print(f"Customer change is ${change:.2f}")
         break
      except ValueError:
         print("Invalid input. Please enter numeric amount")
   generate_receipt(running_subtotal, discounted_amount, tax, total, payment_amount,change)
        
     
def generate_receipt(running_subtotal, discounted_amount, tax, total, payment_amount,change ):
   print("=======================================================")
   print("|                BEST BUY RETAIL STORE                |")
   print("=======================================================")
   print(f"Date:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

   #looping through cart for receipt details using 
   print('------------------------------------------------------' )
   for item in cart:
      #calculating item total
      item_total = item['quantity'] * item['price']
      #printing the total for each item.
      print(f"{item['itemName']:<20} x {item['quantity']} | {item['price']} = ${item_total}")
   print("-----------------------------------------------------")
   #generating the data for the receipt output
   print(f'Subtotal:                   ${running_subtotal:.2f}')
   if running_subtotal > 5000:
         print(f"Discount 5% -              ${discounted_amount:.2f}")
   print(f"Tax (10%)                    ${tax:.2f}")
   print('------------------------------------------------------')
   print(f"Amount Paid:                 ${payment_amount:.2f}")
   print(f"Change:                      ${change:.2f}")
   print("=======================================================")
   print(             "THANK YOU FOR YOUR PURCHASE")
   print("=======================================================")



#clear cart Function
def clear_cart():
    if cart == []:
        print("Cart is already empty!")
        return
    #user inputing value
    confirm = input("Are you sure you want to clear the cart? (Y/N): ").upper()
    if confirm == "Y":
        cart.clear()
        print("Cart is has been successfully cleared")
        display_catalog()
    elif confirm == "N":
        print("Cart was not cleared.")
    else:
        print("Invalid input, cart was not cleared.")




#menu for user selection, so that they can have full control of which function they would like to carry out
def main_menu():
    while True:
        print("\n1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Clear Cart")
        print("6. Exit     ")
        choice = input("Enter choice: ")
        
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
           print("SEE YAH LATER..................")
           break
        else:
         print("Invalid Choice, please enter 1-6")
         



#calling the main_menu function
main_menu()
 
Author: Saraijah Porth

Date Created: April 4, 2026

Course: ITT103

GitHub Public URL to Code:https://github.com/sporthUCC/Point-of-Sale-Program-with-Python
 

The purpose of the program:

This program's goal was to develop an easy-to-use point-of-sale system.

to assist Best Buy retail locations in efficiently processing customer orders while upholding a straightforward yet effective approach to assist Best Buy in digitizing its sales process and increasing productivity.


How the program runs:


1. Initializing: The program begins by displaying a product catalog containing at least 10 items (e.g., Kiss Cake, Foska Oats, and Dettol Soap) with their respective prices and stock levels.

2. Main Menu: The cashier may then effectively navigate the system thanks to a menu option that determines which function the user would like to follow: add, remove, view, checkout, clear, or exit.

3. Adding Items: They will be prompted to provide the appropriate product ID and quantity when they choose the add option (for example, 1). The system checks the stock. Once the system validates the selection, we then return to the main menu.

4. View Cart & remove item: The cashier (user) can view the cart options by selecting (3). The user is able to see the quantity, price, item name, and ID. Once this option is selected, the catalog is automatically displayed. If an item needs to be removed, the user can select the "remove item from cart" option. 2. Once an item is removed, it is added back to the store’s inventory.

5. Checkout & receipt: This checkout option is triggered by selecting the checkout option (4). The final total is inclusive of the tax and discount where applicable; discounts are only applied when the purchase is greater than $5000. Once payment is valid, a receipt will be generated for the customer, which includes the date stamp; the tax; the discount, if applicable; the change; the store name; and the thank you message.

6. Clear Cart – This allows us to reset the cart and handle multiple different customer transactions.

7. Low Stock Check: This feature was added to the add cart feature to determine whether an item was in stock or if there were fewer than five units.


Modification:

- Update the generate receipt as its own function instead of including it in the checkout function

- Add the while loops in the clear cart so that values keep running.

- Adding payment validation to ensure the customer cannot pay less than the total amount due.

- To keep track of the initial total prior to the discount, a variable called origin_subtotal was created.


Assumptions:

- All transactions are processed in Jamaican Dollars (JMD).

- The system can accept either cash or card.

- The 10% tax and 5% discount over 5000 are fixed business rules for this POS.

- The person using the POS system is a trained cashier.


Limitations:

-Static Data: The product catalog is hard-coded information. There is not a separate database like for MySQL or MongoDB, which is disadvantageous, especially from a user perspective.

-Temporary Data: Because there is no external database, all the data is lost when the program restarts.

-User Interface: The code uses the command-line interface and does not have a graphical user interface.


"I CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMENT."
# Uge 7

## System og Design
The system was designed to try and seperate each layer as much as possible and make each class only have the responsibilities that their class would have.

Transactions, categories and item are split up into their own classes that defines the their respective tables and has functions that run on an object of that type, but also runs statically, often using an id of said object.

Besides that there's the database class that connects to the database, making sure its a singleton, the main that has all the database connections that might be needed, the terminalHelper class that got some classes for doing terminal related things and the startUi that contians the terminal ui logic and uses all of the forementioned classes



The files to set up the sql was not included, as i had trouble figuring it out, but a MySQL database called uge7 running on localhost will work, username and password can be whatever as they can be changed in Main.py as they are currently staticly located there (Not ideal for many reasons, but due to time this was how it turned out)

## Missing feature and how they would have been implemented
Log in, would simple use the terminal to check if the username and password would allows access to the database and accepting if it did.

Transaction: Would have been called from the ChangeStockAmount() function in the Item class and would have simple added a transaction object to the database like the item and category currently does.
The printing would simply have used the terminal to dertime the timeframe for which to print and the queried the database for timestamps that fits the given range and returned them, finally printing them to screen.

## Handling removed categories
When removing categories it could create a problem, as the Item table has a foreign key to categories, i thought of 3 solution whic could be implemented to fix this. The first was a suggestion of just having a default "None" categories that would replaces the removed categories of all items. This would simply use the update methods for items to change that after a query on all items on the old id.
The second solution was to prompt user to select another category to switch all items to.
And the third solution was to prompt the user to make a new category for all items to switch to.
I think i would have gone with 1st and 2nd and then allowing them to do either as they see fit. 
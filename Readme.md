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


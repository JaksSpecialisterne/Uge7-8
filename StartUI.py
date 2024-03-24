from TerminalHelper import TerminalHelper as th
from Item import Item
from Category import Category
import os
import Main

#Adds a new item to database by user input
def AddItem():
    os.system('cls')
    name = th.StringInput("the name of the new product")
    price = th.IntInput("the price of the new product")
    amountStored = th.IntInput("the initial stored of the new product")

    categoryId = CreateOrSelectCategory()

    item = Item(_name=name, _categoryId=categoryId, _price=price, _amountStored=amountStored)
    item.AddToDatabase(Main.session)

#Removes item from database by either inputting id or selecting an item from among all items
def RemoveItem():
    os.system('cls')
    print("Choose an option:")
    print("1: Enter id of item to remove")
    print("2: Select item among all items to remove")
    itemId = EnterOrSelectItem("remove")
    if itemId == -1:
        print("No items currently in database")
        return
    Item.RemoveFromDatabase(Main.session, itemId)

#Updates item in database by either inputting id or selecting an item from among all items
def UpdateItem():
    os.system('cls')
    print("Choose an option:")
    print("1: Enter id of item to change")
    print("2: Select item among all items to change")
    itemId = EnterOrSelectItem("change")
    if itemId == -1:
        print("No items currently in database")
        return
    UpdateItemSub(itemId)

#Updates specified part of specified item, it allows you to change multiple things in one session until you manually leave
#Takes as input an interget specifying what item is being changed
def UpdateItemSub(itemId: int):
    while True:
        os.system('cls')
        print("What would you like to update?")
        print("1: Name")
        print("2: category Id")
        print("3: Price")
        print("4: Exit")

        updateType = th.NumberInput(1, 4)

        match updateType:
            case 1:
                val = th.StringInput("new name")
            case 2:
                #Possibly prompt to show all categories?
                print("Show all categories id's?")
                print("1: Yes")
                print("2: No")
                tInput = th.NumberInput(1,2)
                if tInput == 1:
                    PrintCategories(ShowCategories(Main.session))
                val = th.IntInput("new category id")
            case 3:
                val = th.IntInput("new price")
            case 4:
                break
        
        Item.ChangeInDatabase(Main.session, itemId, val, updateType)

#Returns a list of all items in the database
def ShowItems() -> list:
    return Item.GetAllFromDatabase(Main.session)

#A helper function that returns a selected itemId by either input or selection among all items
#Takes as input a string that helps clarify what is being done currently
#Returns an itemId of selected item
def EnterOrSelectItem(string: str) -> int:
    tInput = th.NumberInput(1,2)
    list = ShowItems(Main.session)
    if not list:
        return -1
    if tInput == 1:
        while True:
            tInput2 = th.IntInput(f"the id of the item you wish to {string}")
            if Item.GetFromDatabase(Main.session, tInput2) is not None:
                itemId = tInput2
                break
            print("Id could not be found")
    else:
        i = 1
        for item in list:
            print(f"{i}: {item._name}")
            i += 1
        selectedC = th.NumberInput(1, len(list))
        itemId = list[selectedC]._itemId
    return itemId




#Adds a new item to database by user input
#Returns id of added category
def AddCategory() -> int:
    os.system('cls')
    givenName = GetNewCategoryName()
    category = Category(name=givenName)
    category.AddToDatabase(Main.session)
    return category._categoryId

#Removes category from database by either inputting id or selecting an category from among all categories
def RemoveCategory():
    os.system('cls')
    print("Choose an option:")
    print("1: Enter id of category to remove")
    print("2: Select category among all categories to remove")
    categoryId = EnterOrSelectCategory("remove")
    if categoryId == -1:
        print("No categories currently in database")
        return
    #Prompt wether to create new category for all items contained deleted category, give them an existing category or make an empty category
    Category.RemoveFromDatabase(Main.session, categoryId)

#Updates category from database by either inputting id or selecting an category from among all categories
def UpdateCategory():
    givenName = GetNewCategoryName()
    categoryId = EnterOrSelectCategory("update")
    if categoryId == -1:
        print("No categories currently in database")
        return
    Category.ChangeInDatabase(Main.session, categoryId, givenName)

#Used to get name for a category that is either being created or updated, makes sure the name does not already exist
#Returns the unique chosen name
def GetNewCategoryName() -> str:
    while True:
        givenName = th.StringInput("the name of the new category")
        existingName = Category.GetFromDatabaseByName(Main.session, givenName)
        if existingName is None:
            return givenName
        else:
            print("Category name already exists, enter new name please")

#Returns a list of all categories in the database
def ShowCategories(session) -> list:
    return Category.GetAllFromDatabase(session)

#Prints all categories from given list and displays their id and name
def PrintCategories(list: list):
    for category in list:
        print(f"ID: {category._categoryId}, named {category._name}")

#A helper function used when selection of a category is neccesary, it allows you to choose a category from among all categories
#or create a new one if so. If no categories exist it forces the latter option
#Returns a categoryId of the selected or created category
def CreateOrSelectCategory() -> int:
    list = ShowCategories()
    tInput = 1
    mustCreateNewCategory = True
    if len(list) > 0:
        mustCreateNewCategory = False
        print("Would you like to create a new category for the new product or use an existing one?")
        print("1: Create new")
        print("2: Use existing")
        tInput = th.NumberInput(1,2)
    
    if mustCreateNewCategory:
        print("No categories found, a new one must be made now")
        th.KeyToContinue()

    if tInput == 1:
        categoryId = AddCategory()
    else:
        i = 1
        for category in list:
            print(f"{i}: {category._name}")
            i += 1
        selectedC = th.NumberInput(1, len(list))
        categoryId = list[selectedC]._categoryId
    return categoryId

#A helper function that returns a selected categoryId by either input or selection among all items
#Takes as input a string that helps clarify what is being done currently
#Returns an categoryId of selected item
def EnterOrSelectCategory(string: str) -> int:
    tInput = th.NumberInput(1,2)
    list = ShowCategories(Main.session)
    if not list:
        return -1
    if tInput == 1:
        while True:
            tInput2 = th.IntInput(f"the id of the category you wish to {string}")
            if Category.GetFromDatabase(Main.session, tInput2) is not None:
                itemId = tInput2
                break
            print("Id could not be found")
    else:
        i = 1
        for item in list:
            print(f"{i}: {item._name}")
            i += 1
        selectedC = th.NumberInput(1, len(list))
        itemId = list[selectedC]._itemId
    return itemId




#Shows stock by selected value, calling sub methods depending on what is required
def ShowStock():
    while True:
        os.system('cls')
        print("How would you like your stock shown?")
        print("1: Show all")
        print("2: Show by category")
        print("3: Show of specific item")
        print("4: Return to menu")

        option = th.NumberInput(1, 4)
        if option == 4:
            break
        options = [StockAll, StockByCateogory, StockOfSpecificItem]
        items = options[option-1]()
        PrintStock(items)

#Returns a list of all items
def StockAll() -> list:
    os.system('cls')
    print("List of all stock: ")
    return ShowItems()

#Returns a list of all items by specified category
def StockByCateogory() -> list:
    os.system('cls')
    print("Choose an option: ")
    print("1: List all categories then select")
    print("2: Input category id to show items of")
    print("3: Input category name to show items of")
    print("4: Return to previous menu")

    option = th.NumberInput(1, 4)
    if option == 4:
        return
    options = [StockByCategorySub1, StockByCategorySub2, StockByCategorySub3]
    items = options[option-1]()
    PrintStock(items)

#Helper function that shows all categories then allows you to select one
def StockByCategorySub1():
    categories = ShowCategories(Main.session)
    if not categories:
        print("No categories currently exists")
        return
    print("All categories: ")
    PrintCategories(categories)

    maxInputs = len(categories)
    option = th.NumberInput(1, maxInputs)-1
    selCategory = categories[option]._categoryId

    return Item.GetFromDatabaseByCategory(Main.session, selCategory)

#Helper function that shows specific category by id, keeps prompting until valid id is given or user returns
def StockByCategorySub2():
    #Do a loop that goes until valid id is given
    print("Not implemented")
    th.KeyToContinue()
    pass

#Helper function that shows specific category by name, keeps prompting until valid id is given or user returns
def StockByCategorySub3():
    #Do a loop that goes until valid name is given
    print("Not implemented")
    th.KeyToContinue()
    pass


#Returns a list containing the item if id is given, or a list of all items containing given searchterm as a substring
def StockOfSpecificItem() -> list:
    os.system('cls')
    print("Choose an option: ")
    print("1: Input item id to show")
    print("2: Input item name to show")
    print("3: Return to previous menu")


# Prints the entire given list to screen
def PrintStock(stockList: list):
    i = 1
    for item in stockList:
        print(f"{i}: ID: {item._itemId}, named {item._name} currently has {item._amountStored} stored")




#Generate a print with recent transactions, recent is determined upon use
def GenerateTransactionPrint():
    os.system('cls')
    print("Generating transaction print...")



#Start menu where you got your options
def StartMenu():
    while True:
        print("Would you like to enter as admin or consumer?")
        print("1: Admin menu")
        print("2: Consumer menu")
        print("3: Exit")

        maxInputs = 3
        options = [AdminMenu, ConsumerMenu]
        option = th.NumberInput(1, maxInputs)
        if option == maxInputs:
            break
        options[option-1]()

#Menu for Consumers (Not implemented due to time)
def ConsumerMenu():
    pass

#Menu for Admins that allows changes all kinds of stuff
def AdminMenu():
    while True:
        th.KeyToContinue()
        print("What would you like to do?")
        print("1: Add item to warehouse")
        print("2: Remove item from warehouse")
        print("3: Update item in warehouse")
        print("4: Create new item category")
        print("5: Remove item category")
        print("6: Update item category")
        print("7: Show stock of all items, by category or of specific item")
        print("8: Generate print of recent transactions")
        print("9: Exit")

        maxInputs = 9

        options = [AddItem, RemoveItem, UpdateItem, AddCategory, RemoveCategory, UpdateCategory, ShowStock, GenerateTransactionPrint]
        option = th.NumberInput(1, maxInputs)
        if option == maxInputs:
            break
        options[option-1]()

#Used to log into the database (Not implemted due to time)
def DatabaseLogIn():
    pass


#Main
if __name__ == '__main__':
    DatabaseLogIn()
    StartMenu()
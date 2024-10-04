# Paige LaFave              4/15/2024   
# Assignment #5

# This script allows a user to 
    # create a new list, load a list, or quit and also edit a todo list in the following ways: 
        # add items, move items, delete items, save, and quit

import sys
import pickle

def printTitleMaterial():
    """Prints the title material for the game, including the student's name, class, and section number.
    """
    print("The Ultimate TODO List!")
    print()
    print("By: Paige LaFave")
    print("[COM S 127 Section 2A]")
    print()

def initList():
    """Create a Dictionary of Lists - this is the primary data structure for the script.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []

    return todoList

def checkIfListEmpty(todoList):
    """This function checks if there are any entries in the Dictionary of Lists data structure.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean: If there is at least one item in the data structure, return False - it is not empty. Otherwise return True.
    """
    if (len(todoList["backlog"]) > 0 or 
        len(todoList["todo"]) > 0 or
        len(todoList["in_progress"]) > 0 or
        len(todoList["in_review"]) > 0 or
        len(todoList["done"]) > 0):

        return False
    
    return True

def saveList(todoList):
    """Allows the user to save their data to a binary file.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")

        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)

    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()

def loadList():
    """Allows the user to load their data from a binary file.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")

        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)

    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    
    return todoList

def checkItem(item, todoList):
    """This function iterates through all the keys in the dictionary, and checks each list to see if a key is present.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, String, Integer: This function returns True/ False depending on whether the item was found, the String of the keyName, and the index in the list where the item was found.
    """
    itemFound = False
    keyName = ""
    index = -1

    for key, lst in todoList.items(): #iterate through keys (items) and check each list

        if item in lst: #is item present? if item IS present:
            itemFound = True #itemFound = True (as needed)
            keyName = key   #keyName = key where item was found
            index = lst.index(item) #index = item in list where found

        else: #if item is not present:
            break #nothing happens = "default data"

    return itemFound, keyName, index #returns keyName string, itemFound boolean, and index integer


def addItem(item, toList, todoList):
    """This function allows the user to add an item to a specific list in the todoList data structure.

    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """

    itemFound, keyName, index = checkItem(item, todoList) #call function "checkItem"
    if not itemFound: #if item does not exist in itemFound:

        if toList in todoList: #if toList is in todoList:
            todoList[toList].append(item) #add item

        else:
            todoList[toList] = [item] #else:

    else:
        print("error. '{0}'exists in list {1} at {2}".format(item, keyName, index)) #error message

    return todoList

def deleteItem(item, todoList):
    """This function allows the user to delete an item in the todoList data structure.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, Dictionary of Lists: This function returns True/ False depending on whether the item was found, and the modified Dictionary of Lists data structure.
    """
    
    itemFound, keyName, index = checkItem(item, todoList) #call function "checkItem"
    if itemFound: #if itemFound True
        del todoList[keyName][index] #deletes item from dict. 
    else: #not found
        print("error. '{0}' does not exist.".format(item)) #error message

    return itemFound, todoList

def moveItem(item, toList, todoList):
    """This function allows the user to move an item from one List in the Dictionary of Lists to another.

    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """
 
    itemFound, todoList = deleteItem(item, todoList) #call function "deleteItem"
    if itemFound: #if itemFound = True:
        todoList = addItem(item, toList, todoList) #call function "addItem" and reassign todoList

    return todoList

def printTODOList(todoList):
    """This function prints out the contents of the Dictionary of Lists data structure.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return None: After printing out the contents of the Dictionary of Lists data structure, we are explicitly returning 'None.'
    """

    for key, lst in todoList.items():  #iterate throught keys in dict (with key and lst)
        print("todo: {0}: {1}".format(key, lst)) #print ex: todo: ['laundry', 'dishes']

    return None

def runApplication(todoList):
    """This function provides the primary funcionality for the application. It allows the user to add items to the data structure, move items,
    delete items, save the data structure to a binary file, and return to the main menu.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()

        if choice == "a": #if a is choice:

            add_item = input("Please add your item: ") #input from user as string
            todoList = addItem(add_item, 'backlog', todoList) #call addItem function and reassign todoList

            printTODOList(todoList) #calls print funciton

            pass

        elif choice == "m":
            checking = checkIfListEmpty(todoList)#call checkIfListEmpty to see if lists have data structure

            if checking == False: # if checkIfListEmpty is false:

                new_item = input("Please enter an item: ") #prompt user for new item as string

                while not checkItem(new_item, todoList)[0]: #while item is not in "data structure":
                    print("error. Item does not exist.")  #print error (item doesn't exist)
                    new_item = input("Please enter another item: ") #enter item 

                dictkeymove = input("Please enter a dictionary key that list moves to: ") #prompt user

                while dictkeymove not in todoList: #while key not in list:
                    print("error. Key does not exist. ") #print error (key doesn't exist)
                    dictkeymove = input("Please enter a dictionary key: ") #enter key
                
                todoList = moveItem(new_item, dictkeymove, todoList) #call function moveItem(item, key, todoList)
            
            else: #otherwise: 
                print("error. No items to move!") #print error

            printTODOList(todoList) #calls print function

            pass


        elif choice == "d":


            checking = checkIfListEmpty(todoList) #calls checkIfListEmpty function

            if checking == False: #if checkIfListEmpty is false:
                deleting_item = input("Please enter item: ") #prompt user for item as string
                deleteItem(deleting_item, todoList)#deleteItem function to remove item from data structure if present
            
            else: 
                print("error. No Items to delete!") #error message

            printTODOList(todoList) #call function to print regardless if empty

            pass


        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)


        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break


        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()

    return todoList

def main():
    """This is the main() function for the program. It contains all of the initial choices the user can make. These choices include:
    - Starting a new Dictionary of Lists.
    - Loading a previously saved Dictionary of Lists.
    - Quitting the script altogether.
    """
    taskOver = False

    printTitleMaterial()

    while taskOver == False:

        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()

        if choice == "n": 
            todoList = initList()
            printTODOList(todoList)
            runApplication(todoList)

        elif choice == "l":
            todoList = loadList()
            printTODOList(todoList)
            runApplication(todoList)

        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()

        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()
import easygui

MAX_PRICE = 10
MIN_PRICE = 1

# nested dictionary to store the combos
combo_menu = {
    "Value": {
        "Beef burger": 5.69,
        "Fries": 1.00,
        "Fizzy drink": 1.00
    },
    "Cheezy": {
        "Cheeseburger": 6.69,
        "Fries": 1.00,
        "Fizzy drink": 1.00
    },
    "Super": {
        "Cheeseburger": 6.69,
        "Large fries": 2.00,
        "Smoothie": 2.00
    }
}


#MAIN MENU
def main_menu():

    #list to store the buttons for the different functions to run
    # after the user choice
    options = {
        "All Combos": all_combos,
        "Search Combos": search_combos,
        "Add New Combo": add_combo,
        "Remove Combo": remove_combo
    }

    while True:
        
        # info for printing out within easygui
        msg = "Welcome to Sam's Combos, what would you like to do?"
        title = "WELCOME"
        choices = []

        # adding the different options to a list of choices for 
        # the user.
        for items in options:
            choices.append(items)

        user_choice = easygui.buttonbox(msg, title, choices)

        # if the user tries to exit out the program, it wont break
        if user_choice is None:
            break
        
        #runs the function based on the user choice
        input = options[user_choice]()


#PRINT ALL THE COMBOS
def all_combos():
    # info for the printing
    msg = "Sams Combos - All"
    title = "ALL COMBOS"
    # different choices
    options = ["Edit Combo", "Back"]

    # gathering information for each category, combo and corresponding
    # price of each combo and adds all of it to a variable as a 
    # string to be printed out
    for combo_name, combo_items in combo_menu.items():
        msg += f"\n\n{combo_name}\n--------"
        for item, price in combo_items.items():
            msg += f"\n {item}: ${price}"

    #prints out the whole nested dictionary in a good format
    # gives the option to edit something or return to main menu
    choice = easygui.buttonbox(msg, title, options)

    # if they exit out or choose 'back' it returns to the
    # menu function
    # else: it will run the edit function for the user to edit a combo
    if choice is None or choice == "Back":
        return
    else:
        edit_combo()


#EDIT THE COMBOS IN THE LIST
def edit_combo():
    # info for printing
    msg = "What combo would you like to edit?"
    title = "CHOSE A COMBO TO EDIT"
    # empty string to add items items to
    categories = []

    # goes through the different categories in combo_menu and adds
    # them to a list 'categories' in order to make buttons
    for group in combo_menu:
        categories.append(group)

    # gives the user a choice of categories to find their combo to edit
    category_choice = easygui.buttonbox(msg, title, categories)

    # returns if user doesn't choose anything
    if category_choice is None:
        return
    
    # edits the title based on what category the user chose
    title += f" --> {category_choice.upper()}"
    options = []
    
    # goes through combos in chosen category and adds to list
    for item in combo_menu[category_choice]:
            options.append(item)

    combo_choice = easygui.buttonbox(msg, title, options)

    # returns if user chooses nothing
    if category_choice is None:
        return

    # info for printing
    # includes previous choices 
    msg = f"What do you want to edit about '{combo_choice}'?"
    title += f" --> {combo_choice.upper()}"
    options = ["Name", "Price"]

    # choice between what they want to edit
    choice = easygui.buttonbox(msg, title, options)

    # lets them edit the name of the chosen combo
    if choice == "Name":
        # info for printing
        msg = f"Enter new name for {combo_choice}"
        title = "NEW NAME"

        # box to enter their new info
        new_name = easygui.enterbox(msg, title)

        # makes user confirm that they want to edit w/ this info
        # includes all new info + old info for comparison
        msg = f"Is this info correct?\nOLD --> {combo_choice}: \
${combo_menu[category_choice][combo_choice]}\
\nNEW --> {new_name}: ${combo_menu[category_choice][combo_choice]}"
        title = "CONFIRM EDIT"
        options = ["Confirm", "Cancel"]
        
        # choice between confirming or cancelling the edit
        confirm = easygui.buttonbox(msg, title, options)

        # based on the user choice either sets the new info or 
        # returns to the combo_menu function
        if confirm == "Confirm":
            new_price = combo_menu[category_choice][combo_choice]
            del combo_menu[category_choice][combo_choice]
            combo_menu[category_choice][new_name] = new_price
        else:
            return

    # lets the user edit the price of the chosen combo
    elif choice == "Price":
        msg = f"Enter new price for {combo_choice}"
        title = "NEW PRICE"

        new_price = easygui.integerbox(msg, title,
                upperbound=MAX_PRICE, lowerbound=MIN_PRICE)

        # makes user confirm that they want to edit w/ this info
        # includes all new info + old info for comparison
        msg = f"Is this info correct?\nOLD --> {combo_choice}: \
${combo_menu[category_choice][combo_choice]}\
\nNEW --> {combo_choice}: ${new_price}"
        title = "CONFIRM EDIT PRICE"
        options = ["Confirm", "Cancel"]

        # choice between cancelling or confirming the edit
        confirm = easygui.buttonbox(msg, title, options)

        # depending on choice either sets the new price to chosen
        # combo or returns to main function
        if confirm == "Confirm":
            combo_menu[category_choice][combo_choice] = new_price
        else:
            return
    else:
        return
    

#LETS USER CHOOSE WHAT TO SEARCH WITH
def search_combos():
    # printing info
    msg = "How would you like to search?"
    title = "Search"
    options = ["Category", "Item Search"]

    # choice between item or category search
    search_type = easygui.buttonbox(msg, title, options)

    # based on response, runs chosen function
    if search_type == "Category":
        category_search()
    elif search_type == "Item Search":
        item_search()
    else:
        return
    

# SEARCHES VIA CATEGORY
def category_search():
    
    # info for printing
    msg = "Select a category that you would like to search:"
    title = "CATEGORY SEARCH"
    options = []

    # adding each category to an empty list
    for item in combo_menu:
        options.append(item)
    
    # choice between different categories
    category_choice = easygui.buttonbox(msg, title, options)

    # returns to main menu if no response
    if category_choice is None:
        return

    # printing info
    msg = f"Choose an combo from '{category_choice}'"
    options = []

    # runs through different combos and adds them to an empty list
    for combo in combo_menu[category_choice]:
        options.append(combo)
    
    # choice between different combos within a chosen category
    combo_choice = easygui.buttonbox(msg, title, options)

    # returns if no input
    if combo_choice is None:
        return

    # printing info
    msg = f"Chosen combo was in '{category_choice}'\n---------\n"
    msg += f"{combo_choice}: ${combo_menu[category_choice][combo_choice]}"
    title = "COMBO FOUND"
    options = ["Edit Combo", "Back"]

    # choice between editing the chosen combo or returning to menu
    choice = easygui.buttonbox(msg, title, options)

    # returns to menu if no input or 'Back' input
    # else runs edit function
    if choice == "Back" or choice is None:
        return
    else:
        edit_combo()


# SEARCH VIA ITEM INPUT
def item_search():

    # runs until stated otherwise
    while True:
        
        # printing info
        msg = "What item would you like to search for? :"
        title = "ITEM SEARCH"

        # user enters in what combo they are searching for
        search = easygui.enterbox(msg, title)

        # returns if no input
        if search is None:
            return

        # runs through everything within the nested dictionary and if
        # there is the searched item, adds it to the 'msg' variable
        # to print
        for category, combo in combo_menu.items():
            for combo, price in combo.items():
                if search.lower() == combo.lower():
                    known_category = category
                    msg = f"ITEM FOUND IN '{category}'\n"
                    msg += f"\n{combo}: ${price}"
                    title = "COMBO FOUND"
                    options = ["Edit Combo", "Back"]
                    
                    choice = easygui.buttonbox(msg, title, options)
                    
                    # if no response or chooses back, returns to menu
                    # else runs 'edit_combo' variable
                    if choice == "Back" or choice is None:
                        return
                    else:
                        edit_combo()
                        return
                    
        # if item not found, continue loop until they either exit or
        # correct information is entered
        msg = f"'{search}' not found in Combo Menu"
        title = "COMBO NOT FOUND"
        easygui.msgbox(msg, title)


# ADDING COMBO
def add_combo():
    
    # printing info
    msg = "What is your new combo named?"
    title = "ADD COMBO"

    # textbox to enter answer
    new_combo_name = easygui.enterbox(msg, title)

    # if no response, returns to menu
    if new_combo_name is None:
        return

    # info for printing including previous answer
    msg = f"What is the price of '{new_combo_name}'?"

    # enter new price
    new_combo_price = easygui.integerbox(msg, title, 
                            upperbound=MAX_PRICE, lowerbound=MIN_PRICE)

    # if no response, returns to menu
    if new_combo_price is None:
        return

    # info for printing
    msg = "What category will this combo be placed?"
    options = []

    # going through list and adding all categories to 'options' list
    for item in combo_menu:
        options.append(item)

    # choice between categories
    new_combo_category = easygui.buttonbox(msg, title, options)

    # if no response, goes to menu
    if new_combo_price is None:
        return
    
    # info for the user to confirm adding their new combo
    msg = f"Confirm your new combo in the '{new_combo_category}' category"
    msg += f"\n{new_combo_name}: {new_combo_price}"
    title = "CONFIRM NEW COMBO"
    options = ["Confirm", "Cancel"]
    
    # choice between confirm or cancel
    confirm = easygui.buttonbox(msg, title, options)

    # if no input or choose cancel, return to menu
    if confirm is None or confirm == "Cancel":
        return
    else:
        # edits the item 'new_combo_name', which doesn't exist, 
        # therefore adding a new item equal to the chosen price
        combo_menu[new_combo_category][new_combo_name] = new_combo_price

        # info for printing
        msg = "Your new combo was added!"
        title = "COMBO ADDED"

        # confirmation message
        easygui.msgbox(msg, title)

# REMOVING COMBOS
def remove_combo():
    
    #printing info
    msg = "Where is the combo would you like to remove?"
    title = "REMOVE COMBO"
    options = []

    # adding all categories to 'options' list
    for item in combo_menu:
        options.append(item)

    # choice between categories
    category_choice = easygui.buttonbox(msg, title, options)

    # if no input, returns to menu
    if category_choice is None:
        return

    # info for printing
    msg = "What combo would you like to remove?"
    options = []

    # adds all combo names within chosen category to 'options' list
    for item in combo_menu[category_choice]:
        options.append(item)

    # choice between combos within chosen category
    remove_choice = easygui.buttonbox(msg, title, options)

    # if no input, returns to menu
    if remove_choice is None:
        return

    # info for the user to confirm the removal of the combo
    msg = f"Confirm delete combo '{remove_choice}' from category \
'{category_choice}'"
    title = "CONFIRM DELETE"
    options = ["Confirm", "Cancel"]

    # confirmation choice
    confirm = easygui.buttonbox(msg, title, options)

    # if no input or chose cancel, return to menu
    if confirm is None or confirm == "Cancel":
        return
    else:
        # deletes combo based on info given
        del combo_menu[category_choice][remove_choice]
        
        # confirmation message
        msg = f"'{remove_choice}' successfully removed from \
'{category_choice}'"
        title = "COMBO DELETED"

        easygui.msgbox(msg, title)


# runs main function after defining all other functions
main_menu()
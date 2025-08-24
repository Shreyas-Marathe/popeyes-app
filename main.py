"""\
Popeyes App
-----------
"""

menu_dict = {"Chicken Sandwitch": 6.99, "Loaded Fries": 3.99, "Coke": 1.1}


def menu() -> None:
    """\
    Prints the menu.
    """    
    print("\nMenu")

    for i, (item_name, cost) in enumerate(menu_dict.items()):
        print(f"{i + 1} {item_name} - £{cost:0.2f}")

    print()


def order() -> None:
    user_order = input("What would you like to order? (Please enter a number) : ")
    
    if user_order.isdigit():
         menu_list = list(menu_dict.keys())
         selected_item = menu_list[int(user_order) - 1] 
         item_price = menu_dict[selected_item]
         print(selected_item, item_price)
         

    else:
        print("invalid")

   
    


def main() -> None:
    """\
    Main function.
    """
    print("Welcome to the Popeyes app!")

    menu()
    order()


if __name__ == "__main__":
    main()
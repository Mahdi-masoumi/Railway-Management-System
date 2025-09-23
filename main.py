import admin
from employee import Employee
from purchase_panel import PurchasePanel


def main_menu():
    while True:
        print("---- MAIN MENU ----")
        main_menu_choice = input(
            "enter 1-4:\n 1.Admin Panel\n 2.Employee Panel\n 3.User Panel\n 4.Exit\n")
        if main_menu_choice not in [str(i) for i in range(1, 5)]:
            print("Invalid choice. Please enter a number between 1 and 4.")
            main_menu()
            return
        # admin panel
        if main_menu_choice == "1":
            admin.admin_panel()
        # employee panel
        if main_menu_choice == "2":
            Employee().employee_panel()
        # user panel
        if main_menu_choice == "3":
            # TODO: pass in the trains list and is_user_logged_in to the user panel
            trains = Employee().trains_list
            PurchasePanel(trains, True).print_panel()
        # Exit
        if main_menu_choice == "4":
            print("👋 Goodbye!")
            break


main_menu()

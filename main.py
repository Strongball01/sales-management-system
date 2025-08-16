# main.py - Entry point for Sales Management System

from modules import login, sales, reports

def main():
    print("=== Sales Management System ===")
    print("1. Login")
    print("2. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        user = login.login_user()
        if user:
            print(f"\nWelcome {user['username']}! Role: {user['role']}")
            sales.menu(user)  # Open sales menu
        else:
            print("\nInvalid login, try again.")
    else:
        print("Exiting system...")

if __name__ == "__main__":
    main()

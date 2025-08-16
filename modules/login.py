# modules/login.py
# Handles user authentication

USERS = [
    {"username": "admin", "password": "1234", "role": "Admin"},
    {"username": "vendedor", "password": "abcd", "role": "Vendor"}
]

def login_user():
    print("=== Login ===")
    username = input("Username: ")
    password = input("Password: ")

    # Buscar usuario válido
    for user in USERS:
        if user["username"] == username and user["password"] == password:
            return user

    print("Invalid credentials!")
    return None

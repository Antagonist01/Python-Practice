# Predefined username and password
correct_username = "admin"
correct_password = "1234"

attempts = 3  # Maximum login attempts

while attempts > 0:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username:
        if password == correct_password:
            print("Login successful! Welcome to the system.")
            break
        else:
            print("Incorrect password! Try again.")
    else:
        print("Username not found!")

    attempts -= 1
    if attempts > 0:
        print(f"You have {attempts} attempts left.\n")
    else:
        print("Too many failed attempts! Access denied.")

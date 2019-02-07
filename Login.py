import sqlite3
import random


conn = sqlite3.connect("NotTheUsersDetails.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT UNIQUE, password TEXT, code INTEGER)")




def print_menu():
    print("Welcome to the most secure bank IN THE WORLD!!!")
    print()
    print("1. Setup user account.")
    print("2. Forgot password...")
    print()

def select_choice():
    while True:
        try:
            choice = int(input("Choose an option: "))
        except:
            print("=====!!! ERROR !!!=====")
            print("Invalid input...")
            print()
            continue

        if choice == 1:
            return 1
        elif choice == 2:
            return 2
        else:
            print("=====!!! ERROR !!!=====")
            print("Enter a valid option...")
            print()
            continue



def data_entry(user, pwd, random_code):
    try:
        c.execute("INSERT INTO users(username, password, code) VALUES(?, ?, ?)",
                  (user, pwd, random_code))

        conn.commit()
        print("Data entered successfully!")
        return True
    except:
        print()
        print("=====!!! ERROR: Database entry error! !!!=====")
        print()
        return False







def forgot_password():
    print("===== Forgot Password =====")
    user_name = get_username()
    user_code = get_secret_code()

    c.execute("SELECT * FROM users WHERE username = (?) AND code = (?)",
              (user_name, user_code))

    try:
        print()
        print("Welcome, {}. Your password is: {}".format(user_name, c.fetchone()[1]))
        print("Have a nice day!")
        print()
        
    except:
        print("=====!!! ERROR: Invalid details entered !!!=====")
        print()


def setup_user():
    print("===== Setup User Account =====")
    uid = get_username()
    pwd = get_password()
    code = generate_random_code()
    print()
    
    entered = data_entry(uid, pwd, code)

    if entered:

        print()
        print("=====!!! ALERT !!!=====")
        print(uid + ", your secret code is:", code)
        print("Thank you, come again.")

        





def get_username():
    while True:
        try:
            name = str(input("Enter a username: "))

            if len(name) >= 1:
                return name
            else:
                continue
        except:
            print()
            print("=====!!! ERROR !!!=====")
            print()
            continue
    

def get_password():
    while True:
        try:
            pwd = str(input("Enter a password: "))
            return pwd
        except:
            print()
            print("=====!!! ERROR !!!=====")
            print()
            continue

def generate_random_code():
    digits = int(random.randint(1000, 9999))
    return digits

def get_secret_code():
    while True:
        try:
            secret_code = int(input("Enter your secret code: "))
            
            if len(str(secret_code)) == 4:
                return secret_code
            else:
                print()
                print("=====!!! ERROR: Wrong length !!!=====")
                print()
                continue
            
        except:
            print()
            print("=====!!! ERROR: Invalid character !!!=====")
            print()
            continue
        




if __name__ == "__main__":
    create_table()

    print_menu()
    choice = select_choice()
    print()

    if choice == 1:
        setup_user()
    elif choice == 2:
        forgot_password()
    else:
        print("Error")


    input()
    c.close()
    conn.close()

    
    

from cryptography.fernet import Fernet

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()

"""


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close
    return key


master_pwd = input("What is the master password? ")

key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open("password.txt", "r") as a:
        for line in a.readline():
            line.rstrip()
    print(f"Uname {name}")


def add():
    name = input("Account name: \n")
    pwd = input("Password: \n")

    with open("password.txt", "a") as f:
        f.write("UserName => " + name + ", Password => " +
                str(fer.encrypt(pwd.encode())) + "\n")


while True:
    mode = input("Would like to add a new password or view the existing one?")

    if mode == "q":
        quit()

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue

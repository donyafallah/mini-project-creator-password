import random
import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = "!@#~$%^&*()_+}{|"":><?}"
numbers = "0123456789"
all = lower + upper + symbols + numbers
while True:
    print("Choose options:\n1)Creat a password\n2)Exit")
    choice = input("Your option :")
    if choice == "1":
        length = int(input("Enter the length of your password :"))
        password = "".join((random.sample(all,length)))
        print(password)
    elif choice == "2":
        break 
    else:
        print("Your option is wrong!")
try:
    value = 10/0
    user = int(input("Enter the number : "))
    print(user)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invaild input")
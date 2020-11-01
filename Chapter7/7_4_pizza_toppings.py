flag = True
while flag:
    message = input("Input a topping: ")
    if message == 'quit':
        flag = False
    else:
        print("You will add " + message + " to your pizza.")
        
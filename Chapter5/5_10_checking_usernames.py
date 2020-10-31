current_users = ['admin', 'Mike', 'Tim', 'Peter', 'Martin']
new_users = ['mike', 'Sherlock', 'Tom', 'MARTIN', 'James']

for new_user in new_users:
    in_current_list = False
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            in_current_list = True

    if in_current_list:
        print("You need to enter a new username.")
    else:
        print("The username is avaliable.")

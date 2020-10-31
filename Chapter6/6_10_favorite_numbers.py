favorite_numbers = {
    'Tom': [2, 33],
    'Tim': [6, 66, 666],
    'Mike': [8, 89],
    'Martin': [669, 996],
    'James': [23],
}

for name, nums in favorite_numbers.items():
    if len(nums) <= 1:
        print(name.title() + " likes " + str(nums[0]))
    else:
        print(name.title() + " likes: ")
        print(nums)
        print("\n")

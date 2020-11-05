def addItemsToSandwich(*items):
    print("This sandwich has: ")
    for item in items:
        print("- " + item)

addItemsToSandwich('egg', 'bacon', 'tomato')
addItemsToSandwich('cheese', 'tomato', 'fruit')
addItemsToSandwich('beef', 'egg')

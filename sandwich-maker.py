import pyinputplus as pyip

def makeSandwich():

    sandwichList = []
    totalCost = 0

    #Ask customer for type of bread
    bread = pyip.inputMenu(['wheat', 'white', 'sourdough'])
    sandwichList.append(bread)

    #Ask customer for choice of protein
    meat = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
    sandwichList.append(meat)

    #Ask customer if they want cheese
    cheesePrompt = 'Would you like cheese'
    cheese = pyip.inputYesNo(cheesePrompt)
    if cheese == 'yes':
        typeCheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'])
        sandwichList.append(typeCheese)

    mayoPrompt = 'Would you like mayo'
    mayo = pyip.inputYesNo(mayoPrompt)
    if mayo == 'yes':
        sandwichList.append('mayo')

    mustardPrompt = 'Would you like mustard'
    mustard = pyip.inputYesNo(mustardPrompt)
    if mustard == 'yes':
        sandwichList.append('mustard')

    lettucePrompt = 'Would you like lettuce'
    lettuce = pyip.inputYesNo(lettucePrompt)
    if lettuce == 'yes':
        sandwichList.append('lettuce')

    tomatoPrompt = 'Would you like tomato'
    tomato = pyip.inputYesNo(tomatoPrompt)
    if tomato == 'yes':
        sandwichList.append('tomato')

    #Ask how many sandwiches they want
    numSandwichesPrompt = 'How many sandwiches would you like'
    print(numSandwichesPrompt)
    numSandwiches = pyip.inputInt(min=1)

    for ingredient in sandwichList:
        if ingredient == 'wheat' or ingredient == 'white' or ingredient == 'sourdough':
            totalCost += 1
        elif ingredient == 'chicken' or ingredient == 'turkey' or ingredient == 'ham':
            totalCost += 3
        elif ingredient == 'tofu':
            totalCost += 4
        elif ingredient == 'cheddar' or ingredient == 'swiss' or ingredient == 'mozzarella':
            totalCost += 1

    totalCost = totalCost * int(numSandwiches)
    print(sandwichList)
    return print('Total cost is: $' + str(totalCost))

makeSandwich()
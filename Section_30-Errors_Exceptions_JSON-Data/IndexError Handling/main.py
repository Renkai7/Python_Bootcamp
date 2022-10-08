fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    # If value is higher than list length then return something else
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)

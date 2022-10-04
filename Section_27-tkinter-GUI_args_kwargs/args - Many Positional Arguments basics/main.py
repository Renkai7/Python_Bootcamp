# Arguments with Default Values - you don't have to assign anything to function
# def my_function(a=1, b=2, c=3):
# Do this with a
# Then do this with b
# Finally do this with c
# my_function()

# Unlimited Arguments
# def add(*args):
#     for n in args:
#         print(n)

def add(*numbers):
    num_sum = 0
    for num in numbers:
        num_sum += num
    return num_sum


print(add(2, 4, 6, 8))

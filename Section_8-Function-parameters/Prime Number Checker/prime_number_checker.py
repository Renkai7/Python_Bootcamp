# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
    else:
        is_prime = False

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

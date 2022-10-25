# Simple Python Decorator Functions
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


# say_hello()


# # With the @ syntactic sugar
# @delay_decorator
# def say_bye():
#     print("Bye")
#
#
# # Without the @ syntactic sugar
# def say_greeting():
#     print("How are you?")
#
#
# decorated_function = delay_decorator(say_greeting)
# decorated_function()

# Advanced Python Decorator Functions
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)

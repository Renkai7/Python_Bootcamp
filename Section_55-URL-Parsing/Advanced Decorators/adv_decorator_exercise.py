def logging_decorator(function):
    def wrapper(*args, **kwargs):
        function(args)
        print(f"{function.__name__} {args}")

    return wrapper


@logging_decorator
def nen_type(nen):
    print(f"Your nen type is {nen}")


nen_type("Specialist")

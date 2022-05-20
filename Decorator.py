def my_decorator(func):
    def say_bye(*args, **kwargs):
        print("its working good")
        func(*args, **kwargs)

    return say_bye


@my_decorator
def say_hello(name):
    print(f"hello {name}")

@my_decorator
def say_my_name(name, family):
    print(f"{name} {family}")

# say_hello = my_decorator(say_hello("hany"))

# say_hello

say_my_name('hany', 'seyedy')
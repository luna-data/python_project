def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

example_function(a=1, b=2, c=3)
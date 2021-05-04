def howareyou(fun):
    def inner(n):
        result = fun(n)
        return f"{result} How are you!"
    return inner

@howareyou
def hello(name):
    return "Hello "+name


print(hello("Muzmmil"))
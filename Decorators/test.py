def my_life(func):
    def wapper(**kwargs):
        func(**kwargs)
    return wapper


@my_life
def my_name_age(**kwargs):
    print(kwargs)


my_name_age(Name='Danya', Age=20)

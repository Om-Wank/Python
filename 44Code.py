def create_profile(**kwargs):
    for key ,value in kwargs.items():
        print(key ,"->",value)


create_profile(name = "Om",age =24,city="Washim")        
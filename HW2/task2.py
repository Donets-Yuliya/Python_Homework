def join_strings(*args, sep=' '):
    str = sep.join(args)
    return str
    
str = join_strings("Hello", "world")
print(str)

str = join_strings("red", "green", "blue", sep=", ")
print(str)

str = join_strings("Python", "is", "awesome", sep="-")
print(str)

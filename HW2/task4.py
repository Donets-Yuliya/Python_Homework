def characterPrinter():
    pos = 0
    
    def func(str, n):
        str_print = ""
        nonlocal pos
         
        while len(str_print) != n:
            str_print += str[pos:pos+1]
            if pos == len(str) - 1:
                pos = 0
            else:
                pos += 1

        print(str_print)

    return func

printer = characterPrinter()

printer("Hello world!", 3) # Hel

printer("Hello world!", 4) # lo w

printer("Hello world!", 4) # orld

printer("Hello world!", 2) # !H

printer("Hello world!", 4) # ello

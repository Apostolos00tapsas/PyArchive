def fibo():
    a,b = 1,1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b


    

        

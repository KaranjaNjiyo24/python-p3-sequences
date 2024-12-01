#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
    elif length == 1:
        print ([0])
    elif length == 2:
        print([0,1])
    else:
        fibonacci = [0,1]
        while len(fibonacci) < length:
            next_num = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(next_num)
        
        print(fibonacci)
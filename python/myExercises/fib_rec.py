# coding: utf-8
# fib_recursivo.py

def fibonacci(i):
    if i == 1 or i == 2:
        return 1
    return fibonacci(i - 1) + fibonacci(i - 2)
fibonacci(10)


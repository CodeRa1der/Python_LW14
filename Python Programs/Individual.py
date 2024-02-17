#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def outer_function(type='max'):
    def inner_function(collection):
        if type == 'max':
            return max(collection)
        else:
            return min(collection)
    return inner_function

if __name__ == "__main__":
    input_data = input("Введите значения через пробел: ").split()
    input_numbers = [int(x) for x in input_data]
    max_func = outer_function()
    print("Максимальное значение:", max(input_numbers))
    min_func = outer_function(type='min')
    print("Минимальное значение:", min(input_numbers))
    
#works in concert with main.tex file

import numpy as np
from functools import reduce

max_number = 5

def form_subtraction():
    rng = np.random.default_rng()
    a, b = rng.choice(10, size=2, replace=True, p=None)
    if a >= b:
        top = a
        bottom = b
    else:
        top = b
        bottom = a
    return f'\\subt{{{top}}}{{{bottom}}}'

def form_addition():
    rng = np.random.default_rng()
    a, b = rng.choice(10, size=2, replace=True, p=None)
    len_a = len(str(a))
    len_b = len(str(b))
    if len_a >= len_b:
        top = a
        bottom = b
    else:
        top = b
        bottom = a
    return f'\\addi{{{top}}}{{{bottom}}}'

def form_multiplication():
    rng = np.random.default_rng()
    a, b = rng.choice(max_number, size=2, replace=True, p=None)
    len_a = len(str(a))
    len_b = len(str(b))
    if len_a >= len_b:
        top = a
        bottom = b
    else:
        top = b
        bottom = a
    return f'\\mult{{{top}}}{{{bottom}}}'

def factorize(n: int):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def numbers_and_factors():
    rng = np.random.default_rng()
    num = rng.choice(max_number, size=1, replace=True, p=None)[0]
    # prevent num = 0 or divisor = 1 or divisor = dividend
    factor = 1
    while not num or factor == 1 or factor == num:
        num = rng.choice(max_number, size=1, replace=True, p=None)[0]
    # pick a factor of num; answer will always be an integer
        if num:
            factor = rng.choice(list(factorize(num)), size=1, replace=True, p=None)[0]
    return num, factor

def form_division():
    num, factor = numbers_and_factors()
    return f'\\divi{{{factor}}}{{{num}}}'

def form_factorize():
    rng = np.random.default_rng()
    num = rng.choice(10, size=1, replace=False, p=None)[0]
    return f'\\fact{{{num}}}' 

def form_reduce():
    num, factor = numbers_and_factors()
    return f'\\redu{{{factor}}}{{{num}}}'

def get_row_of_random_problems(size=6):
    probs_ = [f'{form_addition()}',
              f'{form_addition()}',
              f'{form_addition()}',
              f'{form_addition()}',
              f'{form_addition()}',
              f'{form_addition()}',
              f'{form_addition()}',
              f'{form_addition()}',
              f'{form_addition()}',
              f'{form_addition()}',
              f'{form_addition()}',
              f'{form_addition()}',
              f'{form_addition()}',
              f'{form_addition()}',]
               #f'{form_multiplication()}',
               #f'{form_division()}',
               #f'{form_subtraction()}',
               #f'{form_factorize()}',
               #f'{form_reduce()}',
    rng = np.random.default_rng()
    ind_ = rng.choice(len(probs_), size=size, replace=False, p=None)
    a, b, c, d, e, f = [probs_[i] for i in ind_]
    return f'\\sixprobs{{{a}}}{{{b}}}{{{c}}}{{{d}}}{{{e}}}{{{f}}}'

def get_rows_of_random_problems(n):
    rows = ""
    for x in range(n):
        rows = rows +  '\n\n\\vspace{1.2cm}\n\n' + get_row_of_random_problems()
    return rows

problems = get_rows_of_random_problems(5) 

print(problems)
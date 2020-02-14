#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-07 17:21:33
# @Author  : Dahir Muhammad Dahir

import numpy as np
from numpy import pi



# in numpy dimensions are called axes

a: np.ndarray = np.arange(15)
print(f"a single dimension array: {a}")

a = a.reshape(3,5)
print(a)

# dimension of the array
print(f"dimension: {a.ndim}")

# print size of the array
print(f"size of the array: {a.size}")

print(f"size of array items: {a.itemsize}")

print(a.data)

b = np.array([2,3,4])
print(b)

print(a.dtype)

b = np.array([1.2, 3.5, 5.1])
print(b.dtype)

b = np.array([(1,2,3), (4,5,6)])
print(b)

# complex array
d = np.array([[1,2], [3,4]], dtype=complex)
print(d)

# zeroed out
zeroes = np.zeros((3,4))
print(zeroes)

# oned out
ones = np.ones((3,2,4))
print(ones)

# emptied
empties = np.empty((2,3))
print(empties)

# numpy range
x = np.arange(10, 100, 5)
print(x)

# 
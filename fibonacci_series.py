# -*- coding: utf-8 -*-
"""fibonacci series

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nL55QM5v120RDnywLGv4Q7P9JhOIe5Re
"""

n = int(input("enter number of terms"))
a = 0
b = 1
s= 0

for x in range(n):
  print(s,end=" ")
  s = a+b
  b = a
  a= s
import sys
import os
import wordf

a = ['1','2','3','dashjdashkjda  123']

for i in range(10):
    a = a[-1].replace(str(i),' ')
    print(a)
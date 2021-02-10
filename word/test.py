import random

def f(list):
    return list[0]

list1=[]    
word=['a','b','c','d','e','f','g','h','i']
for i in range(100,120):
    l=random.choice(word)+str(i)
    list1.append(l)
list1.sort(key=f)
print(list1)
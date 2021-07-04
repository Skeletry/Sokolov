import random

Numb = random.sample(range(-100,100),30)
print(Numb)
print("\nMax:",max(Numb))
print("Index number:",Numb.index(max(Numb)))
new_Numb = [i for i in Numb if i % 2 != 0]

A = new_Numb
A = sorted(new_Numb,reverse = True)
print("Odd_Reversed:",A)
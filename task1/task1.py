st = input("Enter string: ")
print('_'*50)

print("Your string: ",st)
print('_'*50)

# Remove numbers start
import re
words = re.sub("[0-9]", "", st)
print ("Words: ",words)
# Remove numbers end

# Remove words start
num_list=[]
num=''
for char in st: 
    if char.isdigit():
        num = num + char
    else:
        if num != '':
            num_list.append(int(num))
            num = ''
if num != '':
    num_list.append(int(num))
print('_'*30)
print("Numbers: ",num_list)
print('_'*30)
# Remove words end

# Max number start
max_num = 0
for i in num_list:
    if i > max_num:
        max_num = i
print("Max number: ",max_num)
print('_'*30)
# Max number end

print(words.title())

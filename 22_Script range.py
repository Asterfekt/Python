#1
print("----------------1----------------")
string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for number in range(1,11):
    print(string_A)
    
#2
print("----------------2----------------")
for i in range(9):
    if i % 2 == 0:
        print(string_A)
    else:
        print(string_B)
  
#3
print("----------------3----------------")        
for i in range(1,10):
    print("x"*i)
#4  
print("----------------4----------------")   
for i in range(1,10):
    if i % 2 == 0:
        print("x"*i)
    else:
        print("o"*i)

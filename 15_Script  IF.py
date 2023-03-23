#INSTRUKCJA WARUNKOWA

'''
age=tu wpisz liczbe
if age >=18:
 tabmusi byc   print("You are adult and you can buy alcohol")
 else:
 tab również musi być ("you are too young to buy alcohol")
'''
#1
MIN_LIKES = 500
MIN_SHARES = 100

num_likes =60
num_shares = 10

if num_likes>=MIN_LIKES and num_shares>=MIN_SHARES:
    print("discount value less 10 %")
else:
    print("condition is not enough to get discount")
#2
isPizzaOrdered=True
isBigDrinkOrdered=True
isWeekend=True
if isPizzaOrdered==True and isBigDrinkOrdered==True and isWeekend==False:
    print("You get burger voucher ")
else:
    print("I invite you again")

#3
diskSize = 140
diskSizeUsed = 116
fileSize = 10

if diskSize - diskSizeUsed >= fileSize :
    print('The file can be downloaded')
else:
    print('There isn\'t enough free disk space to download the file. Sorry :(')

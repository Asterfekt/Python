#1
##numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
##
##i=0
##max=len(numbers)-1
##
##while i<max:
##    print(i,numbers[i],numbers[i+1])
##    if numbers[i+1]==(numbers[i]*numbers[i]):
##        print("found",numbers[i],numbers[i+1])
##    i+=1


###2
##numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
##
##k=0
##max=len(numbers)-2
##
##while k<max:
##    print(k,numbers[k],numbers[k+1],numbers[k+2])
##    if numbers[k+1]==(numbers[k]*numbers[k]) and numbers[k+2]==(numbers[k+1]*numbers[k+1]):
##        print("found",numbers[k],numbers[k+1],numbers[k+2])
##    k+=1
## 

#3
texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

j=0
max=len(texts)-1

while j<max:
    print(j, texts[j],texts[j+1])

    if len(texts[j]) == len(texts[j+1]):

        print("\tFOUND!")


    j+=1
    

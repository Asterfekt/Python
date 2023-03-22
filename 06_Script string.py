'''
https://en.wikipedia.org/wiki/Monty_Python
'''
article = "Monty Python (also collectively known as the Pythons)[2][3] were a British surreal comedy group "
print(article.upper())
print(article.lower().replace('monty','flying'))
print(article.split(' '))
print('word python appears',article.lower().count('python'),'times')
 
print('to print the \\ you need to put \\ twice in your text like this: \\\\')
print('The best hits of \'80s!!!')
print("The best hits of '80s!!!")
print('\n')

amountPLN=234
print('cur','\texchange','amount')
print('USD',"\t",3.65,"\t",amountPLN/3.65)
print('EUR','\t',4.23,"\t",amountPLN/4.23)
valueAsText = '123.45'
factor =1.23
print('value is ', valueAsText,'factor is',factor,'value*factor=',float(valueAsText)*factor)

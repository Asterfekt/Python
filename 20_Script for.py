#1
data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
for error in data:
    print(error.upper())

#2
print('----------------')
for s in data:
 
    elements = s.split(':')
    print(elements[0].upper())
    print(elements[1])
print('----------------')

for d in data:
 
    elements = d.split(':')
    if elements[0] == 'Error':
        print(elements[1].upper())
    else:
        print(elements[1])

import math
'''
1° = (π * rad)/180   
1 rad = 180°/π
'''

degree = 360
radian = degree * math.pi /180
print(radian)
print('---------------')
degree = 45
radian = degree * math.pi /180
print(radian)
print('---------------')
print(math.radians(360))
print(math.radians(45))

small_pizza_r=0.22
big_pizza_r=0.27
family_pizza_r=0.38

small_pizza_price=11.5
big_pizza_price=15.6
family_pizza_price=22

#pirr
print('-------Powierzchnia Pizzy--------')
print('mała pizza',math.pi*pow(small_pizza_r,2),"m^2")
print('duza pizza',math.pi*pow(big_pizza_r,2),"m^2")
print('rodzinna pizza',math.pi*pow(family_pizza_r,2),"m^2")
    
print('')
print('small', small_pizza_price/math.pi*pow(small_pizza_r,2))
print('big', big_pizza_price/math.pi*pow(big_pizza_r,2))
print('family', family_pizza_price/math.pi*pow(family_pizza_r,2))
print('')
      
math_ls = dir(math) 
print(math_ls)

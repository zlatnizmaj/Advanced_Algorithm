n = 0
while n < 5:
    print(n)
    n+= 1

# for loops
for n in range (5): # 0,1,2,3,4
    print(n)
# break
mysum = 0
for i in range(5,11,2):
    mysum += i
    if i % 5 == 0:
        break
print(mysum)

#
# if type(varA) == str or type(varB) == str:
#     print('string involved')
# elif varA > varB:
#     print('bigger')
# elif varA == varB:
#     print('equal')
# else:
#     print('smaller')

# num = 0
# while num <= 5:
#     print(num)
#     num += 1
#
# print("Outside of loop")
# print(num)
#
# num = 10
# while num > 3:
#     num -= 1
#     print(num)
print('Range')
for i in range(10,1,-2):
    print(i)
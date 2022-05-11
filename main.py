# lst = [11,5,8,32,15,3,20,132,21,4,555,9,20]
# b=[]
# c=0
# for i in lst:
#     a = i%3
#     if a==0 and  i<30:
#         print(i)
#     else:
#         b.append(i)
# for i in b:
#     c = c + i
# print(c)

# lst = [11,5,8,32,15,3,20,139,21,4,555,9,20]
# for i in lst:
#     a = i%2
#     if i == 139:
#         break
#     elif a != 0:
#         print(i)


# def calc(a,b,c):
#     if c == '+':
#         print(a + b)
#     elif c == '-':
#         print (a - b)
#     elif c == '*':
#         print(a * b)
#     elif c == '/':
#         print(a/b)
#     else:
#         print('operaction isnt supposed')
#
# a = float(input('first number:',))
# b = float(input('second number:',))
# c = input('action:',)
# calc(a,b,c)

# def month_to_season(a):
#     if a == 1 or a == 2 or a == 12:
#         print('Winter')
#     elif a == 3 or a == 4 or a == 5:
#         print ('Spring')
#     elif a == 6 or a == 7 or a == 8:
#         print ('Summer')
#     elif a == 9 or a == 10 or a == 11:
#         print('Autumn')
#     else:
#         print('in year exist 12 months')
#
# month_to_season(int(input('number of month in year:')))
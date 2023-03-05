First = input("Weight: ")
Second = input("(K)g or (L)bs: ")
if Second == 'k':
    total = float(First) * 2.204
    print("Weight in Lbs:"+ str(total))
elif Second == 'l':
    total = float(First) / 2.204
    print("Weight in Kg:" + str(total))
else:
    print('Try Again!')
# how to find average of data set

count = 0
total = 0
print('before:', count, total)
for value in [0, 1, 2, 8, 22]:
    count = count + 1
    total = total + value
    print('during:', count, total)
print("Entries:", count)
print("Sum", total)
print("Average", total/count)

# how to find the smallest number in a data set
print(">")
print(">")
print(">")
# ::::what we are saying::::
# 'o' = nothing
# start loop
# if o = nothing, assign first variable from data set
# then, if o is something, compare to next variable
# if next variable is greater than o, make o that variable
# loop ends here
# print the final variable, after program runs through the loop
# BOOM ya just found the largest number
o = None
print("Value:", o)
for d in [3, 2, 9, 10, 88, 31, 3]:
    if o is None:
        o = d
    elif o < d:
        o = d
    print("Running:", o, d)
print("New Value:", o)





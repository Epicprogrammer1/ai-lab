"""
Implement a python program to implement List operations (Nested List, Length, Concatenation, Membership, Iteration, Indexing and Slicing),
"""

#nested List 
nestedList=[1,2,3,4,[5,6,7,8]]
print("Length of nested List is : ", len(nestedList))

#concatination example 
a=[1,2,3]
b=[4,5,6]
print("a+b is ", a+b)

#Membership Operator

print("1 is present in list a", 1 in a)

print("9 is present in list a", 9 in a)

print("10 is not present in a ",10 not in a)

#iteration 
print("Elements of list a are: ")
for i in a:
    print(a)

#Indexing
print("Element at 0 and -1 index of 'a' are: ",a[0],a[-1])

#slicing 
c=a+b
print("Slicing:",c[0:len(c):2])

"""
Output:
Length of nested List is :  5
a+b is  [1, 2, 3, 4, 5, 6]
1 is present in list a True
9 is present in list a False
10 is not present in a  True
Elements of list a are: 
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
Element at 0 and -1 index of 'a' are:  1 3
Slicing: [1, 3, 5]

"""

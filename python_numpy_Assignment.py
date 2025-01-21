#Assignment:
#1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.
import numpy as np

#10 zeros
s1 = np.zeros(10)
print("An array of 10 zeros : ", s1)

#10 ones
s2 = np.ones(10)
print("An array of 10 ones :", s2)

#10 fives
s3 = np.array([5.]*10)
print("An array of 10 fives : ", s3)


#2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
a1 = np.arange(2,11).reshape(3,3)
print(a1)

#3. Write a NumPy program to create an array with values ranging from 12 to 38.
a2 = np.arange(12,39)
print(a2)

#4. Write a NumPy program to convert a list and tuple into arrays.
l = [1,2,3,4,5,6,7,8]
t = ([8,4,6],[1,2,3])
#conterting
l1= np.array(l)
t1 = np.array(t)

print("Array from list : ", l1)
print("\nArray from tuple :", t1)

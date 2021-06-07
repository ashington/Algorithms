#!/usr/bin/env python
# coding: utf-8

# In[3]:


#armstrong number
# 153 = cube(1)+cube(5)+cube(3)

# Defining a variable with the number to check if it is pallindrome or not
n = 11

# To store the sum of the cube of all the digits extracted
s1 = 0

# defining a temporary variable to save the original number
temp = n

# Starting with the logic
while n!=0:                    # While loop will only break when the number will become Zero
    d = int(n%10)              # Extracting the last digit present in "n"
    s1=s1+(d**3)               # taking cube of the digit extracted and adding it to the variable 's1'
    n = int(n/10)              # removing the last digit extracted from the original number

if s1==temp:
    print(temp,"is armstrong number")
else:
    print(temp,"is not armstrong snumber")


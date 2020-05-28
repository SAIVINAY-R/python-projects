#!/usr/bin/env python
# coding: utf-8

# # Random Password Generator

#                                                                                            -by 18N31A05J3(RAYALA SAI VINAY)

# In[1]:


import string
import random

# string.ascii_letters 
# string.punctuation
# string.digits

characters = string.ascii_letters + string.punctuation  + string.digits
while True :
    while True :
        try :
            length = int(input('Enter the length of the password : '))
            break
        except ValueError :
            print("Oops! Enter only an integer number.  Try Again....")

    password = ""
    if length >= 4 and length <= 18 :
        while True:
            password = ""
            for i in range(0, length):
                password = password + random.choice(characters)
            if any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char.islower() for char in password):
                break

        print('Password :', password)
        break
    else : 
        print('The password length must be greater than or equal to 4 and less than or equal to 18.  Try Again....')


# In[ ]:





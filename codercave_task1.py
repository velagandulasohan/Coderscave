# -*- coding: utf-8 -*-
"""codercave task1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f9JCWlLc4KuB4k53Hwo9ZtvkpPQSYmqy
"""

#PHASE 1
#TASK 1

import math
def addition(num1,num2):
  return num1+num2
def subtraction(num1,num2):
  return num1-num2
def mul(num1,num2):
  return num1*num2
def division(num1,num2):
  return num1/num2
def mod(num1,num2):
  return num1%num2

print("operations to select \n"
       "1.addition"
       "2.subtraction"
       "3.multiplication"
       "4.division"
       "5.mod")
select=int(input("select operation 1,2,3,4,5"))
num1=int(input("enter the number1"))
num2=int(input("enter the number2"))
if select==1:
  print(addition(num1,num2))
elif select==2:
  print(subtraction(num1,num2))
elif select==3:
  print(mul(num1,num2))
elif select==4:
  print(division(num1,num2))
elif select==5:
  print(mod(num1,num2))
else:
  print("invalid option")


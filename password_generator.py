# import the string lib for the characters
import string
# import the random lib
import random
lower_case=string.ascii_lowercase
upper_case=string.ascii_uppercase
digits=string.digits
symbols=string.punctuation

upper,lower,nums,syms=True,True,True,False 
# create an empty string to store the password characters
pswd=""

if upper:
    pswd+=upper_case
if lower:
    pswd+=lower_case
if nums:
    pswd+=digits
if syms:
    pswd+=symbols



# set the length of the password and the amount of passwords you want to be generated
length=10
amount=10
# loop through the the range of the amount

for i in range(amount):
    password="".join(random.sample(pswd,length))
    print(password) 
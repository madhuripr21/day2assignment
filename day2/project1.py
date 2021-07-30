import random as t
import string
length = 8
OTP = ''
char = string.ascii_letters + string.digits
print (char)

for i in range(length):
    OTP = OTP + t.choice(char)
print (OTP)
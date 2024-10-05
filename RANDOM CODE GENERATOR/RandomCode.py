import random
import string

len=int(input("enter the length of code : "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols
temp = random.sample(all,len)

password="".join(temp)
print(password)
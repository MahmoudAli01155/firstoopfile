import os
import re
from myexperiance.fileoperation import *
pwd=os.getcwd()
#'asd@yahoo.com'
try:
    email = input('enter your email')
    pattern = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    print(re.match(pattern, email))
except:#generl case
    print("error")
finally:
    print('thank you for using my app')


read(path)


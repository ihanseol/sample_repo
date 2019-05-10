import math
import sys
from os import rename

import requests

# name = input("input your name : ")
# print("Hello, ", name)

for i in range(10):
    print("num : {}".format(i))

r = requests.get("https://coreyms.com")
print(r.status_code)
print(r.ok)


#coding:utf-8

import  requests
import os
import time
#currentDir=os.path.dirname(os.path.realpath(__file__))
currentDir=os.path.dirname(__file__)
print(currentDir)
parent_path = os.path.dirname(currentDir)
#parent_path = os.path.dirname(parent_path)
#print(parent_path+"/")



urlhtpps = "https://www.baidu.com"
req = requests.get(urlhtpps,verify=False)
print(req.text)

a = [1, 2, 3, "sdf", 5]
b = [3, "sdf", 5]
#print(type(b))
d = [False for c in b if c not in a]
#print(d)
if d:
    print("a不包含b的所有元素")
else:
    print("a包含b的所有元素")

ecl_data="asdfds"
sss=ecl_data.split(":")
print(len(sss))

for i in range(10):
    time.sleep(1)
    print(i)






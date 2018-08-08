#coding:utf-8
import  requests
import  json
from utils.operation_json import OperationJson

class RunQuest:
    def __init__(self,url,method,data,headers,cookies=None):
        self.res=self.Run_Main(url,method,data,headers,cookies)

    def Post_Main(self,url,data=None,headers=None,cookies=None):
        res=None
        self.operjson = OperationJson()
        if headers!=None:
            res=requests.post(url=url,data=data,headers=headers,cookies=cookies,verify=False) #,verify=False 忽略https
            print(res.status_code)
            if self.operjson.is_json(res.text):
                res = res.json()
            else:
                res = str(res.status_code) + ";" + res.text
            # if res.status_code != 200:
            #     res=str(res.status_code)+";"+res.text
            # else:
            #     res=res.json()
        else:
            res=requests.post(url=url, data=data,cookies=cookies,verify=False)
            print(res.status_code)
            if self.operjson.is_json(res.text):
                res = res.json()
            else:
                res = str(res.status_code) + ";" + res.text
        return res

    def Get_Main(self,url,data=None,headers=None,cookies=None):
        res = None
        self.operjson = OperationJson()
        if headers != None:
            res=requests.post(url=url, data=data, headers=headers,cookies=cookies,verify=False)
            print(res.status_code)
            if self.operjson.is_json(res.text):
                res = res.json()
            else:
                res = str(res.status_code) + ";" + res.text
        else:
            res=requests.post(url=url, data=data,cookies=cookies,verify=False)
            print(res.status_code)
            if self.operjson.is_json(res.text):
                res = res.json()
            else:
                res = str(res.status_code) + ";" + res.text
        return res

    def Run_Main(self,url,method,data,headers,cookies):
        res=None
        if method=="POST":
            res=self.Post_Main(url,data,headers,cookies)
        else:
            res=self.Get_Main(url,data,headers,cookies)
        return  res



if __name__=="__main__":
    url="http://127.0.0.1:8000/plogin"
    data={'usename': 'afsdaf', 'password': '123456'}
    headers={'Content-Type':'application/x-www-form-urlencoded'}
    #print(requests.post(url=url, data=data, headers=headers).text)
    #runmian=RunQuest.Post_Main(url,data,headers)
    #print(type(data))
    #print(type(headers))
    #runmian=RunQuest.Run_Main(url,"POST",data,headers)
    runmian=RunQuest(url,"POST",data,headers)
    if isinstance(runmian.res,str):
        runlists=runmian.res.split(";")
        print(len(runlists))
    print(runmian.res)












#coding:utf-8
import  requests
import json

class GetCookie:
    def __init__(self,data=None):
        if data ==None:
            self.data=self.read_data()
        else:
            self.write_data(data)

    #写入cookie
    def write_data(self,data):
        with open("../dataconfig/cookie.json","w") as fp:
            #print(data)
            fp.write(json.dumps(data))

    #读取cookie
    def read_data(self):
        with open("../dataconfig/cookie.json","r") as fp:
            try:
                data = json.load(fp)
            except:
                print("不是json格式!")
            else:
                return  data

    def get_data(self,name):
        return  self.data[name]



if __name__=="__main__":
    #jenkins cookie
    url="http://127.0.0.1.:8080/j_acegi_security_check"
    jsons='{"j_username": "kllay", "j_password": "123456", "remember_me": false, "from": "/", "Jenkins-Crumb": "45760950c26842b77c55adfe29f0d10a"}'
    #jsons=json.dumps([{"j_username": "kllay", "j_password": "123456", "remember_me": False, "from": "/", "Jenkins-Crumb": "45760950c26842b77c55adfe29f0d10a"}])
    data={
        "j_username":"127.0.0.1",
        "j_password":"123456",
        "from":"/",
        "Jenkins-Crumb":"45760950c26842b77c55adfe29f0d10a",
        "json":jsons,
        "Submit":"登录"
    }
    request=requests.post(url,data, allow_redirects=False)
   # print(request.status_code)
   # print(request.headers)
    #print(request.cookies)
    #获取到cookie
    cookie=requests.utils.dict_from_cookiejar(request.cookies)
    GetCookie(cookie)
    #print(requests.utils.dict_from_cookiejar(request.cookies))
    #print(request.text)
    #print(request.history)

    urls="http://127.0.0.1.:8080/job/projectInterface/changes"
    requestget=requests.get(urls,cookies=cookie)
    #print(requestget.text)
    getcookie=GetCookie().read_data()
    print(getcookie)













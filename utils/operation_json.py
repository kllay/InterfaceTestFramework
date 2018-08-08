#coding:utf-8
import  json

'''
fp=open("login.json","r")
data=json.load(fp)

print(data)
print(type(data))
fp.close()
'''

class OperationJson:
    def __init__(self,filename=None):
        if filename:
            #self.fp = open(filename, "r")
            self.data=self.read_data(filename)
        else:
            filename="../dataconfig/login.json"
            #self.fp=open("../dataconfig/login.json","r")
            self.data=self.read_data(filename)

    '''
    def  get_json(self):
        data = json.load(self.fp)
        self.fp.close()
        return  data
    '''
    #读取文件
    def read_data(self,filename):
        with open(filename,"r") as fp:
            try:
                data = json.load(fp)
            except:
                print("不是json格式!")
            else:
                return  data
    def get_data(self,name):
        try:
            return  self.data[name]
        except:
            print("请检查login.json文件是否存在:"+name+"或者格式错误!!")

    #判断json是否符合格式
    def is_json(self,myjson):
        try:
            json.loads(myjson)
        except ValueError:
            return False
        return True


if __name__=="__main__":
    ex_data=OperationJson()
    #print(ex_data.get_json())
    print(ex_data.get_data("login"))










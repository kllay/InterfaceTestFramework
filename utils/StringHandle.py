#conding:utf-8
import  json
import operator
import string
import ast

class StringHandle:
    #判断json字符串是否包含
    def is_content(self,lookup_strs,be_lookup_strs):
        flag=None
        #be_lookup_strs = json.dumps(be_lookup_strs)
        be_lookup_strs = str(be_lookup_strs).replace("\"","'").replace(" ","")
        lookup_strs=str(lookup_strs).replace("\"","'").replace(" ","")
        if isinstance(lookup_strs,str):
            lookup_strs=lookup_strs.encode("unicode_escape").decode("utf-8")
        if isinstance(be_lookup_strs,str):
            be_lookup_strs=be_lookup_strs.encode("unicode_escape").decode("utf-8")

        # print(lookup_strs)
        # print(be_lookup_strs)
        # print(type(lookup_strs))
        # print(type(be_lookup_strs))
        if lookup_strs in be_lookup_strs:
            flag=True
        else:
            flag=False
        return  flag


    #比较两个字典，相同为True
    def is_equ_dict(self,dict_one,dict_two):
        return self.get_cmp_dict(dict_one,dict_two)

    #比较字典函数是否相等
    def get_cmp_dict(self,src_data,dst_data):
        if isinstance(src_data,str):
            src_data=json.dumps(src_data)
        if isinstance(dst_data,str):
            dst_data=json.dumps(dst_data)
        if len(src_data) != len(dst_data):
            return False
        else:
            src_key=list(src_data.keys())
            dst_key=list(dst_data.keys())
            if operator.eq(src_key,dst_key):
                src_val=list(src_data.values())
                dst_val=list(dst_data.values())
                if operator.eq(src_val,dst_val):
                    for key in src_data.keys():
                        if src_data[key] != dst_data[key]:
                            # print(src_data1[key])
                            return False
                    return True
                else:
                    return False
            else:
                return False

    #比较字典函数是否包含
    def get_contain_dict(self,src_data,dst_data):
        src_data1=src_data
        dst_data1=dst_data
        # src_data = str(src_data).replace("\"", "'").replace(" ", "")
        # dst_data = str(dst_data).replace("\"", "'").replace(" ", "")
        # if isinstance(src_data,str):
        #     src_data1=json.dumps(src_data)
        # if isinstance(dst_data,str):
        #     dst_data1=json.dumps(dst_data)
        if isinstance(src_data1,str): #再次判断是否为str
            src_data1 =self.is_loads(src_data1)
            if isinstance(src_data1,str):  #在判断是否为str
                return  self.is_content(src_data,dst_data)
            else:
                if isinstance(src_data1,bool):
                    return self.is_content(src_data, dst_data)

        src_key=list(src_data1.keys())
        dst_key=list(dst_data1.keys())
        # print(str(src_key))
        # print(str(dst_key))
        pd=[False for c in src_key if c not in dst_key]
        if pd:
            return False
        else:
            src_val = list(src_data1.values())
            dst_val = list(dst_data1.values())
            pds = [False for c in src_val if c not in dst_val]
            if pds:
                return False
            else:
                for key in src_data1.keys():
                    if src_data1[key]!=dst_data1[key]:
                        #print(src_data1[key])
                        return False
                return  True

    #str转为dict
    def is_loads(self,strs):
        try:
            strs=ast.literal_eval(strs)
            return strs
        except:
            return True



if __name__=="__main__":
    # lookup_strs='uanme":'
    # be_lookup_strs={"addrs": "123456", "uanme": "afsdaf"}
    # flag=StringHandle().is_content(lookup_strs,be_lookup_strs)
    # print(flag)
    dict1 = {'Name': 'Zara', 'Age': 7}
    dict2 = {'Name': 'Mahnaz', 'Age': 27, "sdaf": 23}
    dict3 = {'Name': 'Abid', 'Age': 27}
    dict4 = {'Name': 'Zara', 'Age': 7}
    dict5 = {'Name': 'Zara','sadf':23}
    dict6 = {'Name': 'Zara','password':'123123'}
    dict8 = {'Name': '123123', 'password': 'Zara'}
    dict9 = {'Name': 'Zara', 'password': '123123'}
    dict7={}

    print(StringHandle().get_contain_dict(dict6, dict9))
    print(StringHandle().get_cmp_dict(dict6,dict9))

    # strs1="{'message': '手机格式错误,请检查后重新输入', 'code': 403}"
    # strs2="'message':'手机格式错误,请检查后重新输入'"
    # flag = StringHandle().is_content(strs2, strs1)
    # print(flag)

    # strs='{"sdaf":32,"aa":"rwer"}'

    #mmm=json.dumps(strs)
    # print(strs)
    # print(type(strs))
    # print(mmm)
    # print(type(mmm))

    # def is_loads(strs):
    #     try:
    #         strs=json.loads(strs)
    #         return True
    #     except:
    #         return False

    #strs='该用户不存在'
    #strs = '"该用户不存在"'
    #strs='"\\u8be5\\u7528\\u6237\\u4e0d\\u5b58\\u5728"'
    #strs='{"sdaf":32,"aa":"rwer"}'
    #sss=StringHandle().is_loads(strs)

    #strs='"{\\"code\\":403,\\"message\\":\\"\\u624b\\u673a\\u683c\\u5f0f\\u9519\\u8bef,\\u8bf7\\u68c0\\u67e5\\u540e\\u91cd\\u65b0\\u8f93\\u5165\\"}"'
    #strs = '"{\\"sdaf\\":32,\\"aa\\":\\"rwer\\"}"'
    #strs='{"code":403,"message":"手机格式错误,请检查后重新输入"}'
   # sss = ast.literal_eval(strs)
    #sss=eval(strs)
    #sss=json.loads(strs)
    #sss=eval(strs)
    #strs = '"{"sdaf":32,"aa":"rwer"}"'

    def is_loads(strs):
        try:
            strs=ast.literal_eval(strs)
            return strs
        except:
            return True


    #sss = is_loads(strs)
    # sss = eval(strs)
    # print(sss)
    # print(type(sss))
    # print(isinstance(sss, str))














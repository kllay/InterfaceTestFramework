#coding:utf-8
import  sys
import os
import time
currentDir=os.path.dirname(__file__)
parent_path = os.path.dirname(currentDir)
#print(parent_path+"/")
sys.path.append(parent_path+"/")  #把上级目录加入到环境变量中

from utils.RunQuest import  RunQuest
from data.get_data import GetData
from utils.StringHandle import StringHandle
from data.DependentData import DependentData
from utils.SendMail import SendMail
from utils.GetTime import GetTime
from utils.GetCookie import GetCookie

class RunTest:
    def __init__(self):
        self.datas=GetData()
        self.sendmail=SendMail()
        self.gettime=GetTime()
        self.strhandle=StringHandle()

    def go_on_main(self):
        #res=None
        # cookie=None
        pass_count=[]
        fail_count=[]
        lines=self.datas.get_case_lines() #获取总行数
        for i in range(1,lines):
            res = None
            cookie = None
            start_time = time.time() #耗时开始
            #print(excepts)
            isrun=self.datas.get_is_run(i) #判断是否运行
            if isrun: #判断是否运行
                url = self.datas.get_request_url(i)
                # print(url)
                method = self.datas.get_request_method(i)
                # print(method)
                headers = self.datas.get_header_for_json(i)
                # print(headers)
                # print(type(headers))
                data = self.datas.get_data_for_json(i)
                # print(data)
                # 获取预期结果值
                excepts = self.datas.get_except_val(i)

                #获取请求的依赖key
                depend_case=self.datas.is_depend(i)
                if depend_case != None:  #判断是否依赖case
                    depend_rep=self.datas.get_depend_key(i)
                    if depend_rep!=None: #判断依赖响应的key是否有
                        self.denpedata=DependentData(depend_case)
                        depend_request_data=self.denpedata.get_data_for_key(i) #获取响应依赖的值
                        cookie=depend_request_data #把返回值赋值给cookie
                        #print("depend_request_data:%s" %depend_request_data)
                        if depend_request_data !=None:
                            depend_key=self.datas.get_depend(i) #获取依赖key
                            if depend_key !=None:
                                data[depend_key]=depend_request_data
                                if depend_header_key != None:
                                    headers[depend_header_key]=depend_request_data
                            else:
                                depend_header_key = self.datas.get_header_depend(i)  # 获取依赖key
                                if depend_header_key != None:
                                    depend_request_data="Basic "+depend_request_data
                                    headers[depend_header_key]=depend_request_data
                    else:
                        self.denpedata = DependentData(depend_case)
                        self.denpedata.get_is_req_sucess()

                #延迟发送
                times=self.datas.get_delaytime_mm(i)
                self.gettime.delaytime(times)

                #获取短信验证码
                cellphone=data["phone"]
                smscode=self.datas.get_sms_value(cellphone)
                data["smscode"]=smscode

                #获取cookies
                cookies=self.datas.get_is_cookie(i)
                if cookies != None:
                    if cookies !="write":
                        # 发送请求
                        # print(headers)
                        try:
                            res = RunQuest(url, method, data, headers,cookies).res
                        except:
                            print("cookie json格式不对!")
                    else:
                        cookie={"Authorization":"Basic "+cookie}
                        GetCookie(cookie) #写入cookie

                # 发送请求
                # print(headers)
                if res==None: #判断res是否为空
                    res = RunQuest(url, method, data, headers).res
                if isinstance(res, dict): #判断是否请求成功
                    if excepts: #判断预期值是否为空
                        if self.strhandle.get_contain_dict(excepts,res): #判断是否和预期值一样 is_content
                            self.datas.write_result(i,"pass")
                            self.datas.write_update_time(i,self.gettime.get_current_time()) #写入当前时间
                            pass_count.append(i)
                            elapse_time = str(time.time() - start_time)
                            print("第"+str(i)+"条用例测试通过! 耗时："+elapse_time)
                        else:
                            #self.datas.write_result(i, "fail")
                            self.datas.write_result(i, str(res))
                            self.datas.write_update_time(i, self.gettime.get_current_time())  # 写入当前时间
                            fail_count.append(i)
                            elapse_time = str(time.time() - start_time)
                            print("第"+str(i)+"条用例测试失败! 耗时："+elapse_time)
                    else:
                        self.datas.write_result(i, "没有预期值:"+str(res))
                        self.datas.write_update_time(i, self.gettime.get_current_time())  # 写入当前时间
                        pass_count.append(i)
                        elapse_time =str(time.time() - start_time)
                        print("第"+str(i)+"条用例测试通过! 耗时："+elapse_time)
                else:
                    self.datas.write_result(i, str(res))
                    self.datas.write_update_time(i, self.gettime.get_current_time())  # 写入当前时间
                    elapse_time =str(time.time() - start_time)
                    print("第"+str(i)+"条用例请求失败! 耗时："+elapse_time)
        # return  res
        print("通过总数:%s"%len(pass_count))
        print("失败总数:%s" % len(fail_count))
        #self.sendmail.send_main(pass_count,fail_count)












if __name__=="__main__":
    runtest=RunTest()
    #res=runtest.go_on_main()
    runtest.go_on_main()
    #print(res)




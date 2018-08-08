#coding:utf-8

from utils.operation_excel import OperationExcel
from utils.RunQuest import  RunQuest
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse
from utils.GetTime import GetTime
import  json
import time

#处理依赖数据
class DependentData:
    def __init__(self,case_id):
        self.case_id=case_id
        self.opera_excel=OperationExcel()
        self.datas=GetData()
        self.gettime=GetTime()

    def get_case_line_data(self):
        rows_data=self.opera_excel.get_rows_data(self.case_id)   #根据caseid获取excel整行数据

    def run_dependent(self):
        row_num=self.opera_excel.get_rows_num(self.case_id)
        url = self.datas.get_request_url(row_num)
        # print(url)
        method = self.datas.get_request_method(row_num)
        # print(method)
        headers = self.datas.get_header_for_json(row_num)
        # print(headers)
        # print(type(headers))
        data = self.datas.get_data_for_json(row_num)
        # print(data)
        # 获取预期结果值
        #excepts = self.datas.get_except_val(row_num)
        # 延迟发送
        times = self.datas.get_delaytime_mm(row_num)
        self.gettime.delaytime(times)
        # 获取cookies
        cookies = self.datas.get_is_cookie(row_num)
        if cookies != None:
            if cookies != "write":
                # 发送请求
                # print(headers)
                res = RunQuest(url, method, data, headers, cookies).res
                return  res
        res = RunQuest(url, method, data, headers).res
        #res=json.loads(res)
        return res

    #只根据依赖请求
    def get_is_req_sucess(self):
        res=self.run_dependent()
        time.sleep(1)
        print(self.case_id+"依赖请求:"+str(res))


    #根据依赖的key 获取依赖的case的响应中的值
    def get_data_for_key(self,row):
        depend_data=self.datas.get_depend_key(row) #获取响应依赖的数据
        depend_data=depend_data.split(":")
        res_data=self.run_dependent()   #获取响应的值
        if isinstance(res_data, dict):  # 判断是否请求成功
            # json_exe=parse(depend_data)
            # madle=json_exe.find(res_data)
            # return [math.value for math in madle][0]
            for_key_value=self.get_for_key(res_data,depend_data)
            if for_key_value !=None:
                return  for_key_value
            else:
                return  None

        else:
            return None


    def get_for_key(self,res_data, *keys):
        res_datas = res_data
        for ks in keys:
            for k in ks:
                #print(k)
                res_datas = self.get_for_key_value(res_datas, k)
                # print(res_datas)
        # print(res_datas)
        return  res_datas

    #判断是否存在
    def get_for_key_value(self,res_data, depend_data):
        try:
                json_exe = parse(depend_data)
                # print(json_exe)
                madle = json_exe.find(res_data)
                # print(madle)
                # print(type(madle))
                datas = [math.value for math in madle][0]
                #print(datas)
                # print(type(datas))
                return datas
        except:
                return None




if __name__=="__main__":
    res_data={'data': {'status': 1000, 'token': 'wefwf43543erwerwerwe'}, 'message': 'success', 'code': 200}
    #res_data={'status': 1000, 'token': 'sdfsdaff3'}
    depend_data="data"
    # if isinstance(res_data, dict):  # 判断是否请求成功
    #     json_exe = parse(depend_data)
    #     print(json_exe)
    #     madle = json_exe.find(res_data)
    #     print(madle)
    #     print(type(madle))
    #     datas=[math.value for math in madle][0]
    #     print(datas)
    #     print(type(datas))


    def get_for_key(res_data,*keys):
        res_datas=res_data
        for ks in keys:
            for k in ks:
                print(k)
                res_datas=get_for_key_value(res_datas,k)
                #print(res_datas)
        print(res_datas)



    def get_for_key_value(res_data,depend_data):
        try:
            if isinstance(res_data, dict):  # 判断是否请求成功
                json_exe = parse(depend_data)
                # print(json_exe)
                madle = json_exe.find(res_data)
                # print(madle)
                # print(type(madle))
                datas = [math.value for math in madle][0]
                #print(datas)
                # print(type(datas))
                return datas
        except:
                return None


    strs={'data','token1'}
    get_for_key(res_data,strs)

    # def calc(*numbers):
    #     sum = 0
    #     for n in numbers:
    #         print(n)
    #         sum = sum + n * n
    #     return sum
    #
    #
    # print(calc(1, 2))
    # def strs(*sss):
    #     for s in sss:
    #         for p in s:
    #             print(p)
    #
    # ss=("sdf","sdfaa")
    # strs(ss)










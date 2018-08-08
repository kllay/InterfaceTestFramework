#coding:utf-8
from utils.operation_excel import OperationExcel
from utils.operation_json import OperationJson
from data.data_config  import  GlobalVar
from utils.GetCookie import GetCookie
from utils.Connect_db import ConnectDb

class GetData:
    def __init__(self):
        self.data=OperationExcel()
        self.dataconfig=GlobalVar()

    #获取总行数
    def get_case_lines(self):
        return  self.data.get_rows()

    #获取是否执行case
    def get_is_run(self,row):
        flag=None
        col=self.dataconfig.get_run()
        runvalue=self.data.get_value(row,int(col))
        if runvalue =="yes":
            flag=True
        else:
            flag=False
        return  flag

    # 获取获取header关键词
    def get_req_header(self,row):
        col = self.dataconfig.get_header()
        headervalue = self.data.get_value(row, int(col))
        if headervalue == "":
            return None
        return headervalue
        # if headervalue == "yes":
        #     return self.dataconfig.get_header_value()
        # else:
        #     return None

    # 根据关键词获取请求header的json内容
    def get_header_for_json(self, row):
        if self.get_req_header(row)!=None:
            for_json = OperationJson(filename="../dataconfig/header.json")
            req_header = for_json.get_data(self.get_req_header(row))
            return req_header
        else:
            return None


    #获取是否获取cookie
    def get_is_cookie(self,row):
        col = self.dataconfig.get_cookies()
        cookievalue = self.data.get_value(row, int(col))
        if cookievalue=="write":
            return  cookievalue
        elif cookievalue == "yes":
            self.getcookie = GetCookie()
            return self.getcookie.read_data()  #读取cookie
        else:
            return None

    #获取请求方式
    def get_request_method(self,row):
        col=self.dataconfig.get_method()
        req_methods=self.data.get_value(row,int(col))
        return req_methods

    #获取请求url
    def get_request_url(self,row):
        col = self.dataconfig.get_url()
        req_url = self.data.get_value(row, int(col))
        return req_url

    #获取请求数据的josn关键词
    def get_request_data(self,row):
        col = self.dataconfig.get_data()
        req_data = self.data.get_value(row, int(col))
        if req_data=="":
            return None
        return req_data

    #根据关键词获取请求数据的json内容
    def get_data_for_json(self,row):
        ecl_data=self.get_request_data(row)
        if self.get_request_data(row)!=None:
            datas=ecl_data.split(":")
            if len(datas)>1:
                for_json=OperationJson("../dataconfig/"+datas[0]+".json")
                req_data=for_json.get_data(datas[1])
                return req_data
            else:
                print("请求数据格式不对!格式必须为 filename:jsonname")
                return None
        else:
            return None


    #获取预期结果
    def get_except_val(self,row):
        col = self.dataconfig.get_except()
        req_except = self.data.get_value(row, int(col))
        if req_except=="":
            return  None
        return req_except

    #获取返回响应的依赖数据的key
    def get_depend_key(self,row):
        col=int(self.dataconfig.get_data_depend()) #获取列
        depend_key=self.data.get_value(row,col)
        if depend_key == "":
            return  None
        else:
            return depend_key

    #判断是否有case依赖 获取依赖的case
    def is_depend(self,row):
        col = int(self.dataconfig.get_case_depend())  # 获取列
        depend_case_id = self.data.get_value(row, col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    #  获取请求数据的依赖key
    def get_depend(self, row):
        col = int(self.dataconfig.get_field_depend())  # 获取列
        data = self.data.get_value(row, col)
        if data == "":
            return None
        else:
            return data

    #  获取请求数据的依赖key
    def get_header_depend(self, row):
        col = int(self.dataconfig.get_header_depend())  # 获取列
        headers = self.data.get_value(row, col)
        if headers == "":
            return None
        else:
            return headers


    #写入实际结果
    def write_result(self,row,value):
        col=int(self.dataconfig.get_result())
        self.data.write_value(row,col,value)

    # 写入更新时间
    def write_update_time(self, row, value):
        col = int(self.dataconfig.get_update_time())
        self.data.write_value(row, col, value)

    #获取请求延迟时间 毫秒
    def get_delaytime_mm(self,row):
        col=int(self.dataconfig.get_delaytime())
        delayvalue = self.data.get_value(row, int(col))
        if delayvalue == "":
            return None
        else:
            return  delayvalue

    #获取短信验证码
    def get_sms_value(self,cellphone):
        sql="select code from driver_oauth where cellphone="+cellphone
        self.dbs=ConnectDb()
        self.dbs.get_sms_db()
        sms=self.dbs.get_data_one(sql)
        print(sms)
        return  sms







if __name__=="__main__":
    data=GetData()
    print(data.get_case_lines())
    print(data.get_is_run(1))
    print(data.get_is_header(1))
    print(data.get_request_method(1))
    print(data.get_data_for_json(1))



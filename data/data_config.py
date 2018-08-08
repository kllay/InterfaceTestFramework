#coding:utf-8
class GlobalVar:
    Id='0'
    LoginName='1' #模块
    Prerequisite='2' #前提条件
    Url='3'
    Method='4' #请求方法
    Run='5'  #是否运行
    Header='6'
    Cookies='7'
    Case_depend='8' #依赖case
    Data_depend='9' #依赖请求返回字段
    Field_depend='10' #请求依赖数据字段
    Header_depend='11'#请求依赖header字段
    Data='12' #请求数据
    DelayTime='13' #延迟时间
    Except='14' #预期结果
    Result='15' #实际结果
    Updatetime='16' #执行时间
    Remarks='17' #备注

    def get_id(self):
        return  GlobalVar.Id
    def get_loginname(self):
        return GlobalVar.LoginName
    def get_prerequisite(self):
        return  GlobalVar.Prerequisite
    def get_url(self):
        return  GlobalVar.Url
    def get_method(self):
        return  GlobalVar.Method
    def get_run(self):
        return  GlobalVar.Run
    def get_header(self):
        return GlobalVar.Header
    def get_cookies(self):
        return  GlobalVar.Cookies
    def get_case_depend(self):
        return  GlobalVar.Case_depend
    def get_data_depend(self):
        return  GlobalVar.Data_depend
    def get_field_depend(self):
        return  GlobalVar.Field_depend
    def get_header_depend(self):
        return  GlobalVar.Header_depend
    def get_data(self):
        return  GlobalVar.Data
    def get_delaytime(self):
        return  GlobalVar.DelayTime
    def get_except(self):
        return GlobalVar.Except
    def get_result(self):
        return  GlobalVar.Result
    def get_update_time(self):
        return  GlobalVar.Updatetime

    def get_remarks(self):
        return  GlobalVar.Remarks

    #header模拟的内容
    # def get_header_value(self):
    #     data={'Content-Type':'application/x-www-form-urlencoded'}
    #     return  data











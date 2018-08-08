#coding:utf-8
import datetime
import time

class GetTime:
    #获取当前时间
    def get_current_time(self):
        cur_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #print(cur_time)
        return cur_time

    #秒转为毫秒
    def delaytime(self,times):
        if times==None:
            return
        if isinstance(times,int):
            time.sleep(times/1000)
        else:
            times=int(times)
            time.sleep(times / 1000)




if __name__=="__main__":
    time=GetTime().get_current_time()
    print(time)

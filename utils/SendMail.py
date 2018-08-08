#coding:utf-8
import  smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendMail:
    global mail_host
    global mail_user
    global mail_pass
    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "*****@163.com"  # 用户名
    mail_pass = "****"  # 口令
    #发送普通邮件
    def send_mail(self,userlist, subject,content):
         user="Test"+"<"+mail_user+">"
         message=MIMEText(content,_subtype='plain',_charset='utf-8')
         message['Subject']=subject #主题
         message['From']=user
         message['To']=";".join(userlist)
         try:
             smtpObj = smtplib.SMTP()
             smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
             smtpObj.login(mail_user, mail_pass)
             smtpObj.sendmail(user, userlist, message.as_string())
             smtpObj.close()
             print("!邮件发送成功")
         except smtplib.SMTPException:
             print("Error: 无法发送邮件!")

    #发送html 邮件
    def send_html_mail(self,userlist, subject,content):
         user="Test"+"<"+mail_user+">"
         message=MIMEText(content,_subtype='html',_charset='utf-8')
         message['Subject']=subject #主题
         message['From']=user
         message['To']=";".join(userlist)
         try:
             smtpObj = smtplib.SMTP()
             smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
             smtpObj.login(mail_user, mail_pass)
             smtpObj.sendmail(user, userlist, message.as_string())
             smtpObj.close()
             print("!邮件发送成功")
         except smtplib.SMTPException:
             print("Error: 无法发送邮件!")

    #发送附件邮件
    def send_attach_mail(self, userlist, subject, content):
        # 创建一个带附件的实例
        message = MIMEMultipart()
        user = "Test" + "<" + mail_user + ">"
        message['Subject'] = subject  # 主题
        message['From'] = user
        message['To'] = ";".join(userlist)
        # 邮件正文内容
        message.attach(MIMEText(content, _subtype='html', _charset='utf-8'))
        '''
        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open('../dataconfig/jiekou.xls', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="jiekou.xls"'
        message.attach(att1)
        '''
        #添加附件
        filename='../dataconfig/jiekou.xls'
        message=self.add_attach(message,filename=filename,viewfilename="jiekou.xls")
        #filename = '../dataconfig/login.json'
        #message = self.add_attach(message, filename=filename, viewfilename="login.txt")

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(user, userlist, message.as_string())
            smtpObj.close()
            print("!邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件!")

    #添加附件函数
    def add_attach(self,message,filename,viewfilename):
        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename='+viewfilename
        message.attach(att1)
        return  message



    def send_main(self,pass_list,fail_list):
        pass_num=float(len(pass_list))
        fail_num=float(len(fail_list))
        count_num=pass_num+fail_num
        if count_num!=0:
            pass_result= "%.2f%%" % (pass_num/count_num*100)
            fail_result = "%.2f%%" % (fail_num / count_num * 100)
        else:
            pass_result = "0%"
            fail_result = "0%"

        userlist = ["****@qq.com"]
        sub = "这是一个测试邮件主题"
        #content = "总数%s个，通过个数为%s,失败个数%s,通过率%s,失败率%s" % (count_num,pass_num,fail_num,pass_result,fail_result)
        #self.send_mail(userlist,sub,content)

        #测试html
        #content = "<p>总数%s个，通过个数为%s,失败个数%s,通过率%s,<p3 style='color:red''>失败率%s</p3></p> <p><a href='#'>这是一个测试链接</a></p>" % (count_num, pass_num, fail_num, pass_result, fail_result)
        #self.send_html_mail(userlist,sub,content)

        #测试附件
        content = "<p>总数%s个，通过个数为%s,失败个数%s,<p3 style='color:green''>通过率%s</p3>,<p3 style='color:red''>失败率%s</p3></p><p1>详情请见附件!<p1>" % (count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_attach_mail(userlist,sub,content)







if __name__=="__main__":
    sen=SendMail()
    sen.send_main([1,2,2],[1,23])
    '''
    userlist=["1612886649@qq.com"]
    sub="这是一个测试邮件主题"
    content="这是邮件内容"
    sen.send_mail(userlist,sub,content)
    '''







#coding:utf-8

class FileUtils:

    def get_file_value(self,filepath):
        lines=[]
        files = open(filepath)
        for line in files:
            lists=line.split(":")
            for i in lists:
                lines.append(i)
            #print(line)
        files.close()
        return lines




if __name__=="__main__":
    filepath="../../zhanghao/sqldb.txt"
    # files = open(filepath)
    # for line in files:
    #     print(line)
    # files.close()
    file=FileUtils()
    print(file.get_file_value(filepath))














import os,sys,codecs
from configparser import ConfigParser
sys.path.append(os.path.join(os.getcwd()))
# [MYSQL]
# host = 1.1.1.1
# username = root
# password = 123456
# port = 3306
# database = test
def get_ini(dbname="MYSQL",keyword="host"):
    files = sys.path[-1]+"\\config.ini"
    with open(files)as sourcefile:
        data = sourcefile.read()
        # print(data)
        # remove BOM
        if data[:3] == codecs.BOM_UTF8:  # 判断是否为带BOM文件
            data = data[3:]
            with codecs.open(files) as dest_file:
                dest_file.write(data)
    s = ConfigParser()
    s.read(files)
    return s.get(dbname,keyword)

if __name__ == "__main__":
    test = get_ini("AUTOINFO","url")
    print(test)


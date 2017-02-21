#coding:utf-8

import ConfigParser

import MySQLdb

class MyParse(object):
    """
    a) 获取话题的链接 topic_url
    b) 获取表(link_id)的名称 link_id
    c) 获取赞阈值 zan_th
    d) 获取赞页数 pages
    e) 名称 topic
    f) 表名称 table
    
    g) 多少天之内才会被获取 day
    h) 多少赞才会被获取 zan
    """
    def __init__(self):
        cf = ConfigParser.ConfigParser()
        #参考http://blog.csdn.net/gexiaobaohelloworld/article/details/7976944
        #读写配置文件，这个配置文件的路径使用\\来确定
        cf.read("D:\\soft\\python\\zhihu_self\\hello-world\\zhihuSingleTopic\\config.ini")
        sections = cf.sections()  
        self.topic = cf.get("setting", "topic")
        self.pages = cf.getint("setting", "pages")
        self.zan_th = cf.getint("setting", "zan_th")
        self.queid = cf.getint("question", "queid")
        self.url_link = []
        tmp_url_link = "https://www.zhihu.com/question/"+str(self.queid)+"?sort=created"
        print tmp_url_link
        self.url_link.append(tmp_url_link)

        #链接zhihu这个数据库
        conn = MySQLdb.connect(
            host='localhost',
            user = 'root',
            passwd = 'root',
            port = 3306,
            charset='utf8')
        cur = conn.cursor()
        conn.select_db('zhihu')

        #根据config.ini文件提供的question id创建表
        table_name = 'q%s'%self.queid
        try:
            sql_exe = 'create table if not exists '+ table_name+'(qid int not null, aid int not null, zan_num int, people varchar(128), people_url varchar(128), content text,img_link varchar(4096), pb1 int, pb2 varchar(512), PRIMARY KEY (aid))'
            print sql_exe
            cur.execute(sql_exe) # 主键
            print 'Create table success'
        except MySQLdb.Error, e:
            print 'Mysql error %d: %s' % (e.args[0], e.args[1])

        cur.close()
        conn.close()
        
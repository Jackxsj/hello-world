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
        cf.read("D:\\soft\\python\\zhihu_self\\hello-world\\zhihu_detail\\config.ini")
        sections = cf.sections()  
        print 'sections:', sections
        self.topic = cf.get("setting", "topic")
        self.pages = cf.getint("setting", "pages")
        self.zan_th = cf.getint("setting", "zan_th")

        #链接zhihu这个数据库
        conn = MySQLdb.connect(
            host='localhost',
            user = 'root',
            passwd = 'root',
            port = 3306)
        cur = conn.cursor()
        conn.select_db('zhihu')

        #这里的第二个参数需要用[]包围，因为这个传入的要求必须是数组，多个参数的话用,分割
        #http://stackoverflow.com/questions/21740359/python-mysqldb-typeerror-not-all-arguments-converted-during-string-formatting
        #获取这个topic对应的id值
        cur.execute('select * from topic where topic = %s', [self.topic])
        result = cur.fetchall()
        print self.topic.decode('utf-8')
        
        self.link_id = result[0][0]

        if cmp(self.topic, '电影') == 0:
            self.table = 'movie'
        elif cmp(self.topic, '编程') == 0:
            self.table = 'coding'
        else:
            self.table = 'table%s' % self.link_id
            print self.table.decode('utf-8')


        #获取对应table里面的starturl,获取多条数据，下面的这个链接里面给出了多条数据的方法
        #http://www.cnblogs.com/fnng/p/3565912.html
        sql_cmd = 'select * from '+self.table
        cur.execute(sql_cmd)
        res_all = cur.fetchall()
        self.url_link = []
        for ii in res_all:
            self.url_link.append(ii[4])
        print self.url_link

        #后面还要在这里创建那个供返回数据写入的表
        
        cur.close()
        conn.close()
        
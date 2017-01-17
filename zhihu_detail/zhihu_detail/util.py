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
        #记录aid
        self.aid=[]
        for ii in res_all:
            self.url_link.append(ii[4])
            self.aid.append(ii[0])
        print self.url_link
        print self.aid

        #后面还要在这里创建那个供返回数据写入的表
        for ij in self.aid:
            table_name = 'q%s'%ij
            try:
                sql_exe = 'create table if not exists '+ table_name+'(qid int not null, aid int not null, zan_num int, people varchar(128), people_url varchar(128), content varchar(16384),img_link varchar(512), pb1 int, pb2 varchar(512), PRIMARY KEY (aid))'
                print sql_exe
                cur.execute(sql_exe) # 主键
                print 'Create table success'
            except MySQLdb.Error, e:
                print 'Mysql error %d: %s' % (e.args[0], e.args[1])

        cur.close()
        conn.close()
        
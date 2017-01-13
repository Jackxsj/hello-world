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
        cf.read("D:\\soft\\python\\zhihu_self\\hello-world\\zhihu\\zhihu\\config.ini")
        sections = cf.sections()  
        print 'sections:', sections
        
        self.topic = cf.get("setting", "topic")
        self.pages = cf.getint("setting", "pages")
        self.zan_th = cf.getint("setting", "zan_th")
        
        self.day = cf.getint('getinterest', 'day')
        self.zan = cf.getint('getinterest', 'zan')
        self.receiver = cf.get('getinterest', 'receiver')
        
        conn = MySQLdb.connect(
            host='localhost',
            user = 'root',
            passwd = 'root',
            port = 3306)
        cur = conn.cursor()
        conn.select_db('zhihu')

        #这里的第二个参数需要用[]包围，因为这个传入的要求必须是数组，多个参数的话用,分割
        #http://stackoverflow.com/questions/21740359/python-mysqldb-typeerror-not-all-arguments-converted-during-string-formatting
        cur.execute('select * from topic where topic = %s', [self.topic])
        result = cur.fetchall()
        print self.topic.decode('utf-8')
        
        self.link_id = result[0][0]
        self.topic_url = 'http://www.zhihu.com/topic/%s/top-answers' % self.link_id
        #打印结果为 http://www.zhihu.com/topic/19556758/top-answers/
        #上面的那个结果为待回答问题，如果选择top或者hot结尾分别为精华或者热门
        print self.topic_url.decode('utf-8')

        if cmp(self.topic, '电影') == 0:
            self.table = 'movie'
        elif cmp(self.topic, '编程') == 0:
            self.table = 'coding'
        else:
            self.table = 'table%s' % self.link_id
            print self.table.decode('utf-8')
        
        cur.close()
        conn.close()
        
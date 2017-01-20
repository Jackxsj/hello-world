# -*- coding: utf-8 -*-


import jieba
import jieba.analyse


import sys
reload(sys)
sys.setdefaultencoding('utf8')

class readAnswer:
#    def __init__(self):
#        self.conn = MySQLdb.connect(
#			host='localhost',
#			user = 'root',
#			passwd = 'root',
#			port = 3306,
#            charset='utf8')
#		self.cur = self.conn.cursor()
#		self.conn.select_db('zhihu')

		
	def read_answer(self, lst):
		order = 1
		l = len(lst)
		file_name = '%s.txt' % ZhihuSpider.my_parse.topic
		f = codecs.open(file_name, 'w')
		msg = MIMEMultipart("related")
		
		body = ''
		for answer in lst:
			f.write('%s个赞\n' % answer[1])
			f.write('时间%s\n' % time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(answer[2])))
			f.write('%s%s' % (answer[3], answer[4]))
			f.write('%s/%s\n' % (order, l))
			f.write('*' * 50)
			f.write('\n')
			'''body += "<h1>%s</h1>" % answer[3] # 问题
			body += "<p>%s个赞</p>" % answer[1]
			body += '<p>时间:%s</p>' % time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(answer[2]))
			body += '<p>%s</p>' % answer[4]
			body += '<p>%s/%s</p>' % (order, l)
			body += '<p>*********************************************************************</p>' '''
			body += "%s\n" % answer[3] # 问题
			body += "%s个赞\n" % answer[1]
			body += '时间:%s\n' % time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(answer[2]))
			body += '%s\n' % answer[4]
			body += '%s/%s\n' % (order, l)
			body += '*********************************************************************\n'
			order += 1
		f.close()
		'''if self.containsnonasciicharacters(body):
			msg_html = MIMEText(body.decode('utf-8','ignore').encode('utf-8'), 'html','utf-8')
		else:
			msg_html = MIMEText(body, 'html')  '''
		# msg_html = MIMEText(body, 'html')
		header = '<h1>抓抓小能手</h1>'
		msg_html = MIMEText(header, 'html')
		msg.attach(msg_html)
		
		part = MIMEApplication(body.decode('utf-8','ignore').encode('utf-8'))  
		part.add_header('Content-Disposition', 'attachment', filename=file_name.decode('utf-8').encode('gb2312'))  
		msg.attach(part) 
		##msg.attach(msg_html)
		self.send_email(self.receiver, msg)
		
	def containsnonasciicharacters(self, s):
		return not all(ord(c) < 128 for c in s) 
		
	def send_email(self, receiver, msg):
		"""
		1、receiver
		2、msg
		"""
		host = "smtp.qq.com"
		port = 465
		user = "714586001@qq.com"
		pwd = "wxq770260108"
		s = smtplib.SMTP_SSL(host, port)
		s.set_debuglevel(1)
		s.login(user, pwd)
		msg["subject"] = "topic:%s;zan>%s;time:%s天内" % (ZhihuSpider.my_parse.topic, ZhihuSpider.my_parse.zan, ZhihuSpider.my_parse.day)
		msg["from"] = '卖报小行家'
		msg["to"] = receiver
		# msg['Content-Type'] = "text/html; charset=utf-8"
		s.sendmail(user, receiver, msg.as_string())  # 给对方发邮件
		s.sendmail(user, user, msg.as_string()) # 给自己也发一份
		
#jieba.cut 方法接受三个输入参数: 需要分词的字符串；cut_all 参数用来控制是否采用全模式；HMM 参数用来控制是否使用 HMM 模型
	def start(self):
		lines = '''当我们有一项工作要做时，只需要指出一个大概方向，有的伙伴就可以欢快的向前冲，自己找到各种可能性，自己探路，而不是等待下一个「指示」。他们手里总是有事情做。'''
		lst = jieba.cut_for_search(lines)
		for i in lst:
			print i
		tags = jieba.analyse.extract_tags(lines)
		tagsw = ",".join(tags)
		print tagsw

    
		
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 14:05:43 2018

@author: Administrator
"""

import mysql.connector
import numpy as np
import time
from decimal import *



def insertOrder2():
    conn = mysql.connector.connect(user="jfwxmm", password="jfwx6o8", 
                                   host="192.168.1.44", database="db_user")
    cur = conn.cursor()
    
    #目前还没有做商户的隔离，所以business_id 一直是1
    business_id = 1
    
    merchant_info = {}
    
    chaxunshangjia = """select id,business_id,merchant_name from business_merchant 
    where business_id =%s """ %(business_id)
    cur.execute(chaxunshangjia)
    print("id, business_id, merchant_name")
    for i in cur:
        merchant_info[i[0]]=[i[0],i[2]]
        print(i)
    
    
    conn2 = mysql.connector.connect(user="jfwxmm", password="jfwx6o8", 
                                   host="192.168.1.44", database="db_hotel")
    cur2 = conn2.cursor()
    chaxunfangjian = """select id,business_id,merchant_id,store_id,floor,room_number 
    from hotel_room"""
    cur2.execute(chaxunfangjian)
    room_info = {}
    print("id,business_id,merchant_id,store_id,floor,room_number")
    for i in cur2:
        room_info[i[0]]=[i[0],i[1],i[2],i[3],i[4],i[5]]
        print(i)
    
    room_tmp_no = input("请输入想生成订单的房间的ID（第一个列为ID）：");
    print("输入的房间号为"+room_tmp_no)
    
    merchant_id = room_info[int(room_tmp_no)][2] #临时设置，可以从那个merchant_info中去取  
    store_id = room_info[int(room_tmp_no)][3]
    
    
    conn3 = mysql.connector.connect(user="jfwxmm", password="jfwx6o8", 
                                   host="192.168.1.44", database="db_wechat")
    cur3 = conn3.cursor()
    chaxunShouQuan = """select id,appid,business_id,merchant_id,nick_name,authorizer_type 
    from wx_authorizer where merchant_id = %s""" %merchant_id
    
    cur3.execute(chaxunShouQuan)
    authorizer_info = []
    print("当前房间对应的授权信息如下")
    print("id,appid,business_id,merchant_id,nick_name,authorizer_type")
    for i in cur3:
        if i[5] == 'MINI':
            authorizer_info.append([i[0],i[1],i[2],i[3],i[4],i[5]])
            print(i)
    #因为查询的时候固定了merchant_id 所以这个授权的微信号固定
    if not authorizer_info:
        print("该merchant id未授权")
        return
    authorizer_id = authorizer_info[0][0]
    authorizer_appid = authorizer_info[0][1]
    
    #查看该商户下的所有的会员（在一个门店注册为会员后，在商户下所有门店均为会员）
    conn4 = mysql.connector.connect(user="jfwxmm", password="jfwx6o8", 
                                   host="192.168.1.44", database="db_member")
    chaxunYongHu = """select id,nick_name,card_code,business_id,user_name from member 
    where business_id = %s """ %business_id
    cur4 = conn4.cursor()
    cur4.execute(chaxunYongHu)
    user_info = {}
    print("---------------------------------------")
    print("该business_id(%s) 下的用户有："%business_id)
    print("id,nick_name,card_code,user_name")
    for i in cur4:
        user_info[i[0]]=[i[0],i[1],i[2],i[3],i[4]]
        print(i)
    
    
    print("---------------------------------------")
    user_tmp_id = input("请输入用户的ID（第一个列为ID）：")
    user_id = user_info[int(user_tmp_id)][0]
    user_name = user_info[int(user_tmp_id)][1]
    
    order_construct = "1"+str(int(time.time()))[-8:]+"%04d"%int(str(user_id)[-4:])+str(np.random.randint(0,999))
    order_no = int(order_construct)
    order_status = 1 #已下单
    order_channel = 2 # 2为小程序
    order_type = 1 #配送到房
    
    chaxunFangJianShangPin = """SELECT id,store_id,product_no,product_name,product_second_name,
    product_number,price,origin_price FROM hotel_product
    WHERE product_status = 2 and store_id = %s
    """%store_id
    cur2.execute(chaxunFangJianShangPin)
    product_info = {}
    product_choose = {}
    print("在这个门店可以选择的商品有这些：")
    print("id,store_id,product_no,product_name,product_second_name,product_number,price,origin_price")
    for i in cur2:
        product_info[i[0]]=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
        print(i)
    print("请输入需要购买的商品（第一列为id值）和数量。输入xx结束(最多10件)")
    while(True):
        tmpInput = input("商品ID,数量（例如 43,10）：")
        if "xx" == tmpInput:
            if not product_choose:
                print("至少需要一件商品！")
                continue
            else:
                break
        [tmpID,tmpNum]=tmpInput.split(',');
        product_choose[tmpID] = tmpNum;
    
    allorderProduct = []
    for j in product_choose:
        i = int(j)
        orderProduct = {}
        orderProduct["id"] = "DEFAULT";
        orderProduct["order_id"] = int(order_construct); #!!!!需要使用数据库的id值
        orderProduct["product_id"] = product_info[i][0];
        orderProduct["product_no"] = product_info[i][2];
        orderProduct["category_id"] = 1;
        orderProduct["product_name"] = product_info[i][3];
        orderProduct["origin_price"] = product_info[i][7];
        orderProduct["price"] = product_info[i][6];
        orderProduct["number"] = int(product_choose[j]);
        orderProduct["product_second_name"] = product_info[i][4];
        orderProduct["product_number"] = product_info[i][5];
        orderProduct["discount_amount"] = float(product_info[i][7])-float(product_info[i][6]);
        orderProduct["discount_amount_total"] = orderProduct["discount_amount"]*int(product_choose[j]);
        orderProduct["sub_amount"] = float(product_info[i][6])*int(product_choose[j]);
        orderProduct["create_time"] = "CURRENT_TIMESTAMP";
        orderProduct["create_user_id"] = user_id;
        
        allorderProduct.append(orderProduct)
        
        
    room_id = int(room_tmp_no)  #由用户输入显示
    room_number = room_info[room_id][5]
    product_count_total =  len(allorderProduct) #随机生成数量
    
    tmp_origin_amount_total = 0.0
    tmp_amount_total = 0.0
    tmp_discount_amount_total = 0.0
    tmp_order_amount_total = 0.0
    
    for i in allorderProduct:
        tmp_origin_amount_total = tmp_origin_amount_total+i["sub_amount"]+i["discount_amount_total"]
        tmp_amount_total = tmp_amount_total+i["sub_amount"]
        tmp_discount_amount_total = tmp_discount_amount_total+i["discount_amount_total"]
        tmp_order_amount_total = tmp_amount_total
        
    product_origin_amount_total = tmp_origin_amount_total
    product_amount_total=tmp_amount_total
    discount_amount_total=tmp_discount_amount_total
    order_amount_total =tmp_order_amount_total
    
    pay_type = [11,12,21,22,31][np.random.randint(0,5)] #11为记房账，12为现金，21为微信支付，22为微信支付，31为协议团客
    pay_order_no =  order_no #采用order_no做随机值
    pay_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    pay_amount_total = order_amount_total #和上面的值一样
    delivery_time = "NULL"
    user_remark = np.random.randint(1,5) #随机生成
    complete_time = "NULL"
    complete_user_id = 0
    complete_user_name = ''
    handle_remark = ''
    create_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    
    valueCon= {}
    valueCon["order_id"] = "Default";
    valueCon["business_id"] = business_id;
    valueCon["merchant_id"] = merchant_id;
    valueCon["store_id"] = store_id;
    valueCon["authorizer_id"] = authorizer_id;
    valueCon["authorizer_appid"] = authorizer_appid;
    valueCon["order_no"] = order_no;
    valueCon["order_status"] = order_status;
    valueCon["order_channel"] = order_channel;
    valueCon["order_type"] = order_type;
    valueCon["user_id"] = user_id;
    valueCon["user_name"] = user_name;
    valueCon["room_id"] = room_id;
    valueCon["room_number"] = room_number;
    valueCon["product_count_total"] = product_count_total;
    valueCon["product_origin_amount_total"] = product_origin_amount_total;
    valueCon["product_amount_total"] = product_amount_total;
    valueCon["discount_amount_total"] = discount_amount_total;
    valueCon["order_amount_total"] = order_amount_total;
    valueCon["pay_type"] = pay_type;
    valueCon["pay_order_no"] = pay_order_no;
    valueCon["pay_time"] = pay_time;
    valueCon["pay_amount_total"] = pay_amount_total;
    valueCon["delivery_time"] = delivery_time;
    valueCon["user_remark"] = user_remark;
    valueCon["complete_time"] = complete_time;
    valueCon["complete_user_id"] = complete_user_id;
    valueCon["complete_user_name"] = complete_user_name;
    valueCon["handle_remark"] = handle_remark;
    valueCon["create_time"] = create_time;
	
    
    zengjiaDingdan = """insert into hotel_order values (
    %(order_id)s,
    %(business_id)d,
    %(merchant_id)d,
    %(store_id)d,
    %(authorizer_id)d,
    \"%(authorizer_appid)s\",
    \"%(order_no)s\",
    %(order_status)d,
    %(order_channel)d,
    %(order_type)d,
    %(user_id)d,
    \"%(user_name)s\",
    %(room_id)d,
    \"%(room_number)s\",
    %(product_count_total)d,
    %(product_origin_amount_total)d,
    %(product_amount_total)d,
    %(discount_amount_total)d,
    %(order_amount_total)d,
    %(pay_type)d,
    \"%(pay_order_no)s\",
    \"%(pay_time)s\",
    %(pay_amount_total)d,
    %(delivery_time)s,
    \"%(user_remark)s\",
    %(complete_time)s,
    %(complete_user_id)d,
    \"%(complete_user_name)s\",
    \"%(handle_remark)s\",
    \"%(create_time)s\"
    )""" % valueCon
    print(zengjiaDingdan)
    cur2.execute(zengjiaDingdan)
    cur2.execute("Commit;")
    conn2.commit()

    
    sqlOrderId = "select id from hotel_order where order_no = %d" %order_no
    
    print(sqlOrderId)
    cur2.execute(sqlOrderId)
    for i in cur2:
        tmpOrderId = i[0]
    print(tmpOrderId)
    for i in allorderProduct:
        i["order_id"] = tmpOrderId
        charuShangPing = """insert into hotel_order_product values (
        %(id)s,
        %(order_id)d,
        %(product_id)d,
        \"%(product_no)s\",
        %(category_id)s,
        \"%(product_name)s\",
        %(origin_price)d,
        %(price)d,
        %(number)d,
        \"%(product_second_name)s\",
        \"%(product_number)s\",
        %(discount_amount)d,
        %(discount_amount_total)d,
        %(sub_amount)d,
        %(create_time)s,
        %(create_user_id)d
        )""" % i
        cur2.execute(charuShangPing)
        
    conn2.commit()
    cur.close()
    cur2.close()
    cur3.close()
    conn2.close()
    conn3.close()
    conn.close()
insertOrder2()





#coding=utf-8
#TCP服务器端程序
import socket
import time
from ctypes import c_uint32
import hashlib
import socketserver

#仅在生成的时候用，生成的data.txt需要提供给jemeter使用

def readFromFile():
    file_path="data2.txt"
    f=open(file_path, "r")
    arpTable = {}
    for i in f.readlines():
        tmp = i.split(',')
        
        tmp_req_id = [int(int(tmp[2])/256),int(tmp[2])%256]
        
        tmp_challenge = tmp[3].split(".")
        arpTable[tmp[1]]=[tmp[0],tmp_req_id,[int(xval) for xval in tmp_challenge],tmp[4]]
    print("read all data in, and ready")
    return arpTable

def udplink(sock):
    while True:
        data,addr=sock.recvfrom(1024)
        print("accept new connection from %s:%s..." %addr)
        print(data)
        tmp_data = data
        print(tmp_data[4])
        #tmp_ip = 
        #tmp_resid = "\x01\x02"
        #tmp_respone = "\x01\x02\x00\x00"+tmp_data[4]+tmp_resid
        
        #s.sendto('this is the UDP server',address)
    sock.close()
    print("Connection from %s:%s closed." % addr)

def getVal(tmp_k):
    return {
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            'a':10,
            'b':11,
            'c':12,
            'd':13,
            'e':14,
            'f':15
            }.get(tmp_k)
def get2CharacterHex(tmp_s):
    return getVal(tmp_s[0])*16+getVal(tmp_s[1])

def radiusAuth(tmp_b,tmp_acct):
    r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    r.sendto(tmp_b,("192.168.1.5",1812))

    data,addr=r.recvfrom(1024)   
    if data[0] == 2:
        r.sendto(tmp_acct,("192.168.1.5",1813))
        data1,addr1=r.recvfrom(1024)
        r.close()
        return 0
    if data[0] == 3:
        
        r.close()
        return 1

def constructAckChallenge(tmp_data,req_id,challenge_val_int): 
    ack_challenge = bytearray()

    ack_challenge.append(tmp_data[0])
    ack_challenge.append(2)
    #这里固定的是chap
    ack_challenge.append(0)
    #rsvID为带过来的值
    ack_challenge.append(tmp_data[3])
    #直接把serial no 拷贝过来
    ack_challenge.extend(tmp_data[4:6])
    
    #这里的这个req_id值后面需要变化,2个字节，现在设置为全局值
    #req_id值这里采用的规则为 ip地址后两位，即tmp_data的内容
    ack_challenge.extend(req_id)
    
    #ip地址
    for i in tmp_data[8:12]:
        ack_challenge.append(i)
    #userport 2个字节
    ack_challenge.append(tmp_data[12])
    ack_challenge.append(tmp_data[13])
    #errorcode 一直为0
    ack_challenge.append(0)
    #attrnum 为1
    ack_challenge.append(1)
    #tlv challenge ack挑战值在外部被随机生成好，后面access_request需要使用
    #这个challenge val的计算规则
    
    ack_challenge.append(3)
    ack_challenge.append(18)
    ack_challenge.extend(challenge_val_int)
    
    return ack_challenge

def constructRadius(tmp_data,mac_val,packet_id,challenge_val_int,req_id,frame_ip,accounting_id):
    service_type = [0,0,0,2]
    frame_protocal = [0,0,0,1]
    nas_type_val = [0,0,0,19]
    nas_ip = [192,168,1,8]
    called_station_val = (mac_val+":200").encode("utf-8")   
    nas_port_val = b"slot=0;subslot=0;port=0;vlanid=200"
 
    
    tmp_dict = {}
    #计算req_auth的属性长度并放置在dictionary中
    len1=tmp_data[17]
    len2=tmp_data[16+len1+1]
    tmp_dict[tmp_data[16]]=tmp_data[18:16+len1]
    tmp_dict[tmp_data[16+len1]]=tmp_data[16+len1+2:16+len1+len2]
    
    access_req =  bytearray()
    acct_req = bytearray()
    #req_auth
    access_req.append(1)
    acct_req.append(4)
    
    #packet id
    access_req.append(packet_id)
    acct_req.append(packet_id)
    #这个整个的长度len需要后面再重新定值
    access_req.append(0)
    access_req.append(0)
    
    acct_req.append(0)
    acct_req.append(0)
    
    #authenticator取值从req_auth中的ChapPassWord去取
    #access_req[4:19]=tmp_dict[4]
    access_req.extend(challenge_val_int)
    #authenticator 后面需要进行生成
    acct_req.extend([0 for i in range(16)])
    
    
    #access_req添加用户名
    tmpName = bytearray()
    tmpName.append(1)
    tmpName.append(0)
    tmpName.extend(tmp_dict[1])
    tmpName[1]=len(tmpName)

    access_req.extend(tmpName)
    acct_req.extend(tmpName)
    
    #添加chap_password
    access_req.append(3)
    access_req.append(19)
    access_req.append(req_id[1])
    access_req.extend(tmp_dict[4])
    
    #添加challenge值
    access_req.append(60)
    access_req.append(18)
    access_req.extend(challenge_val_int)
    
    #添加service-type值
    access_req.append(6)
    access_req.append(6)
    access_req.extend(service_type)
    
    acct_req.append(6)
    acct_req.append(6)
    acct_req.extend(service_type)
    
    #添加frame-protocal值
    access_req.append(7)
    access_req.append(6)
    access_req.extend(frame_protocal)
    
    acct_req.append(7)
    acct_req.append(6)
    acct_req.extend(frame_protocal)
            
    #添加frame-ip值
    access_req.append(8)
    access_req.append(6)
    access_req.extend(frame_ip)
    
    acct_req.append(8)
    acct_req.append(6)
    acct_req.extend(frame_ip)
    
    #添加calling-station-id,后面需要扩展
    access_req.append(31)
    access_req.append(len(mac_val)+2)    
    access_req.extend(mac_val.encode("utf-8"))
    
    acct_req.append(31)
    acct_req.append(len(mac_val)+2)    
    acct_req.extend(mac_val.encode("utf-8"))
    
    #添加nas-port-type,后面需要扩展
    access_req.append(61)
    access_req.append(6)    
    access_req.extend(nas_type_val)
    
    acct_req.append(61)
    acct_req.append(6)    
    acct_req.extend(nas_type_val)
    
    #添加nas-port,后面需要扩展
    access_req.append(87)
    access_req.append(len(nas_port_val)+2)    
    access_req.extend(nas_port_val)
    
    acct_req.append(87)
    acct_req.append(len(nas_port_val)+2)    
    acct_req.extend(nas_port_val)
    
    #添加called-station-id
    access_req.append(30)
    access_req.append(len(called_station_val)+2)    
    access_req.extend(called_station_val)
    
    acct_req.append(30)
    acct_req.append(len(called_station_val)+2)    
    acct_req.extend(called_station_val)
            
    #添加nas-ip
    access_req.append(4)
    access_req.append(6)    
    access_req.extend(nas_ip)
    
    acct_req.append(4)
    acct_req.append(6)    
    acct_req.extend(nas_ip)
    
    #添加acccounting-id
    access_req.append(44)
    access_req.append(len(accounting_id)+2)    
    access_req.extend(accounting_id)
    
    acct_req.append(44)
    acct_req.append(len(accounting_id)+2)    
    acct_req.extend(accounting_id)
    
    tmp_len = len(access_req)
    access_req[2] = int(tmp_len/256)
    access_req[3] = tmp_len%256
    
    #accounting extra
    acct_req.append(40)
    acct_req.append(6)
    acct_status = [0,0,0,1]
    acct_req.extend(acct_status)
    #
    acct_req.append(41)
    acct_req.append(6)
    acct_req.extend([0,0,0,0])
    
    acct_req.append(45)
    acct_req.append(6)
    acct_req.extend([0,0,0,1])
    
    #加了这个时间戳后不正常，舍掉这个时间戳
    #acct_req.append(55)
    #acct_req.append(6)
    #acct_req.extend(bytes(c_uint32(int(time.time()))))
    
    tmp_len2 = len(acct_req)
    acct_req[2] = int(tmp_len2/256)
    acct_req[3] = tmp_len2%256
    #accounting 计算authenticator
    tmp_acct_req = acct_req
    tmp_acct_req.extend(b"testing123")
    m = hashlib.md5()
    m.update(tmp_acct_req)
    acct_req[4:20] = m.digest()
    
    return [access_req,acct_req]

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request[0]
        socket = self.request[1]
        tmp_address = self.client_address
        if self.data=='exit' or not self.data:
            return -1
        tmp_data = self.data
         
        frame_ip = tmp_data[8:12]
        
        tmp_ip = ""
        for i in frame_ip :
            tmp_ip = tmp_ip+str(i)+"."
        tmp_ip = tmp_ip[:-1]
    
        req_id = arpTable[tmp_ip][1] #采用在数据库存储的id值


        packet_id = req_id[1]  #采用数据库存储的id值得低8位
        challenge_val_int = arpTable[tmp_ip][2]
    
        mac_val = arpTable[tmp_ip][0]
        accounting_id = arpTable[tmp_ip][3].encode("utf-8")
        
        if tmp_data[1] == 1:
            ack_challenge = constructAckChallenge(tmp_data,req_id,challenge_val_int)
            socket.sendto(ack_challenge,tmp_address)
            
        if tmp_data[1] == 3:
            access_req,acct_req=constructRadius(tmp_data,mac_val,packet_id,challenge_val_int,req_id,frame_ip,accounting_id)       
            if 0 == radiusAuth(access_req,acct_req):
                ack_auth = bytearray()
                ack_auth.extend(tmp_data[0:16])
                ##################增加错误处理流程#################################
                ack_auth[1] = 4
                ack_auth[15] = 0
                socket.sendto(ack_auth,tmp_address)
            else:
                ack_auth = bytearray()
                ack_auth.extend(tmp_data[0:16])
                ##################增加错误处理流程#################################
                ack_auth[1] = 4
                ack_auth[15] = 1
                socket.sendto(ack_auth,tmp_address)


arpTable = readFromFile()

HOST = '192.168.1.8'
PORT = 2000

server = socketserver.ThreadingUDPServer((HOST,PORT),MyUDPHandler)
server.serve_forever()



# coding:utf8  
'''''创建客户端程序，向服务器传递数据'''  
  
from socket import *             #引入socket模块内的函数，创建一个套接口
from time import ctime        #引入time模块内的ctime()函数，ctime()函数会显示当前日期与时间
  
def client():                  #定义client端函数
    HOST = '127.0.0.1'         #指定ip为本机ip地址
    PORT = 65533               #指定监听端口为65533
  
    clientsocket = socket(AF_INET,SOCK_STREAM)     #建立服务器之间的网络通信，建立基于TCP的流式套接口（SOCK_STREAM 类型是基于TCP的，有保障的面向连接的socket）
    clientsocket.connect((HOST,PORT))          #调用客户端的connect()函数，连接到address(host,port)处的套接字，如果连接出错，返回socket.error错误。
    while True:  
        data = raw_input('Client>>')       #调用raw_input()函数，读取在客户端输入的内容，将数据以字符型式输出
        if not data:                        #如果没有数据输入则跳出循环
            break  
        clientsocket.send('[%s]%s'%(ctime(),data))  #发送TCP数据，将字符型数据发送到连接的服务器，客户端在收到数据同时也会收到接收数据的时间。
        data = clientsocket.recv(1024)            #客户端接收来自服务器的数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。
        if not data:           #如果没有收到数据则跳出循环
            break  
        print data    #显示接收到的数据
  
client()  

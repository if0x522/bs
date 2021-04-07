import socket
import os
import urllib.parse


def WebInit():
    cok = socket.socket()
    cok.settimeout(60)
    s = cok.bind(('127.0.0.1',8000))
    cok.listen(1)
    return s,cok

def send_data(date,conn):
    bt = bytes(date,encoding='UTF-8')
    conn.send(b'HTTP/1.0 200 OK\r\n\r\n')
    conn.send(bt)
    conn.close()

def fileRead(filename):
    fe = open(filename)
    date = fe.read()
    fe.close()
    return date

def home():
    namelist = os.listdir('date/')
    htmlDate = fileRead('index.html')
    print(htmlDate)
    add_date = ''
    for name in namelist:
        deleurl = '/delete.zhen?name='+name
        viewUrl = '/view.zhen?name='+name
        nameline = '<tr><td>'+name+'</td><td><a href='+deleurl+'>删除</td><td><a href='+viewUrl+'>修改</td></tr>'
        add_date = add_date+nameline
    return(htmlDate.replace('@@namelist@@',add_date))

def dele(cs):
    nam = cs.split('=')
    namedir = 'date/'+urllib.parse.unquote(nam[1])
    imglis = os.listdir(namedir)
    if len(imglis) != 0:
        for img in imglis:
            path = namedir+'/'+img
            os.remove(path)
    os.rmdir(namedir)
    return(fileRead('delete.html'))

def adduser(method,body):
    if method=='GET':
        return(fileRead('adduserind.html'))
    elif method=='POST':
        name = body.split('=')
        path = 'date/'+urllib.parse.unquote(name[1])
        os.mkdir(path)
        return(fileRead('addusered.html'))

def viewuser(method,cs,body):
    return(0)

def Urls(cok):
    conn,addr = cok.accept()
    date = conn.recv(50000)
    date = str(date,encoding='UTF-8')
    header,body = date.split('\r\n\r\n')
    header_line = header.split('\r\n')
    method,url,protocal = header_line[0].split(' ')
    a = url.find('?')
    if a==-1:
        url_t = url
    else:
        url_t,cs = url.split('?')
    if url_t == '/':
        htmlDate=home()
        send_data(htmlDate,conn)
    elif url_t == '/delete.zhen':
        htmlDate=dele(cs)
        send_data(htmlDate,conn)
    elif url_t == '/adduser.zhen':
        htmlDate = adduser(method,body)
        send_data(htmlDate,conn)
    elif url_t == '/viewuser.zhen':
        htmlDate = viewuser(method,cs,body)


s,cok=WebInit()
if s==None:
    while(True):
        Urls(cok)
else:
    print(s)

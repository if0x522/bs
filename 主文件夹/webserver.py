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

def send_remo(nn,conn):
    html = 'HTTP/1.0 302 Temporary Redirect\r\nLocation: /upload.zhen?name=' + nn + '\r\n\r\n'
    conn.send(bytes(html,encoding='UTF-8'))
    conn.close()

def fileRead(filename):
    fe = open('html/'+filename)
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
    htmlfile = fileRead('tishi.html')
    htmlfile = htmlfile.replace('@@def@@','删除')
    htmlfile = htmlfile.replace('@@value@@','删除成功')
    return(htmlfile)

def adduser(method,body):
    if method=='GET':
        return(fileRead('adduserind.html'))
    elif method=='POST':
        body = str(body,encoding='UTF-8')
        name = body.split('=')
        path = 'date/'+urllib.parse.unquote(name[1])
        os.mkdir(path)
        htmlfile = fileRead('tishi.html')
        htmlfile = htmlfile.replace('@@def@@','添加用户')
        htmlfile = htmlfile.replace('@@value@@','添加成功')
        return(htmlfile)

def viewuser(method,cs):
    nam = cs.split('=')
    html_file = fileRead('view.html')
    name = urllib.parse.unquote(nam[1])
    namedir = 'date/'+ name
    imglist = os.listdir(namedir)
    if imglist!=0:
        add_html = ''
        for img in imglist:
            adddate = '<img src="/' + namedir +'/' + img + '"alt="/' + img + '" height="300" width="300">'
            add_html = add_html + adddate
        html_file = html_file.replace('@@img@@',add_html)
    else:
        html_file = html_file.replace('@@img@@','目录为空')
    html_file = html_file.replace('@@name@@',name)
    return(html_file)

def upload(method,cs,body):
    if method == 'GET':
        nam = cs.split('=')
        htmlfile = fileRead('uploading.html')
        return(1,htmlfile.replace('@@name@@',urllib.parse.unquote(nam[1])))
    elif method == 'POST':
        nam = cs.split('=')
        if len(body)>100:
            name,byt = body.split(b'\r\n\r\n',1)
            name = str(name,encoding='UTF-8')
            print(name)
            li = name.split('\r\n')
            imgName = li[1]
            i = imgName.find('filename')
            Img = imgName[i+10:-1]
            Img = 'date/'+ urllib.parse.unquote(nam[1]) + '/' +Img
            ww = open(Img,mode='wb')
            ww.write(byt)
            ww.close()
            htmlfile = fileRead('tishi.html')
            htmlfile = htmlfile.replace('@@def@@','上传')
            htmlfile = htmlfile.replace('@@value@@','上传成功')
            return(1,htmlfile)
        else:
            return(0,urllib.parse.unquote(nam[1]))


def Urls(cok):
    conn,addr = cok.accept()
    print(addr)
    date = conn.recv(50000000)
    header,body = date.split(b'\r\n\r\n',1)
    header = str(header,encoding='UTF-8')
    header_line = header.split('\r\n')
    method,url,protocal = header_line[0].split(' ')
    print(protocal)
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
    elif url_t == '/view.zhen':
        htmlDate = viewuser(method,cs)
        send_data(htmlDate,conn)
    elif url_t == '/upload.zhen':
        nn,htmlDate = upload(method,cs,body)
        if nn != 0:
            send_data(htmlDate,conn)
        else:
            send_remo(htmlDate,conn)



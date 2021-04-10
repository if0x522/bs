import socket


sok = socket.socket()
sok.settimeout(20)
s = sok.bind(('127.0.0.1',8000))
print(s)
sok.listen(5)

def send_html(feliname):
    html = open(feliname,'rb')
    byte = html.read()
    #byte = bytes(byte,encoding='UTF-8')
    #print(byte)
    conn.send(b'HTTP/1.0 200 OK\r\n\r\n')
    conn.send(byte)
    html.close()

def index():
    send_html('index.html')

def post(method,body):
    if method == 'GET':
        print('GET')
        send_html('upload.html')
    elif method == 'POST':
        #print(body)
        if len(body) > 10:
            print('abc')
            name,byt = body.split(b'\r\n\r\n',1)
            name = str(name,encoding='UTF-8')
            li = name.split('\r\n')
            imgName = li[1]
            print(imgName)
            i = imgName.find('filename')
            Img = imgName[i+10:-1]
            print(Img)
            ww = open(Img,mode='wb')
            ww.write(byt)
            ww.close()
            send_html('index.html')
        else:
            print('noe')
            send_html('posts.html')

def resend():
    u = '/'
    conn.send(b'HTTP/1.0 302 Temporary Redirect\r\nLocation: https://www.baidu.com\r\n\r\n')

if s==None:
    while(True):
        conn,addr = sok.accept()
        date = conn.recv(50000000)
        ww=open('send.txt','ab')
        ww.write(date)
        ww.close()
        a = date.find(b'\r\n\r\n',0,900)
#        if a==-1:
#            print('二进制')
#            print(date)
#            headers,body = date.split(b'\n\n',1)
#            headers = str(headers,encoding='UTF-8')
#            header_list = headers.split('\n')
#        else:
        #print('字节')
        print(a)
        headers,body = date.split(b'\r\n\r\n',1)
        #print(body)
        headers = str(headers,encoding='UTF-8')
        header_list = headers.split('\r\n')
        method,url,protocal = header_list[0].split(' ')
        if url == '/':
            index()
        elif url == '/post':
            post(method,body)
        elif url == '/re':
            resend()
        else:
            msg = b'HTTP/1.1 200 OK\r\n\r\n404 not found'
    
    #conn.send(msg)
    #print('hello')
        conn.close()
else:
    print(s)

#! C:\Users\91766\AppData\Local\Programs\Python\Python311\python.exe
print('content-Type:text/html\r\n\r\n')
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="rays_desk",passwd="rays_desk",database="rays_desk")
t=con.cursor()
f=cgi.FieldStorage()
try:
    d=f.getvalue('t')
    if d=='sign':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        t.execute('select u_id from signup where u_id="'+str(d2)+'"')
        r=t.fetchall()
        if r==[]:
            url='insert into signup (uname,u_id,sec_qus,sec_ans,pas) value(%s,%s,%s,%s,%s)'
            t.execute(url,(d1,d2,d3,d4,d5))
            con.commit()
            print('SIGN UP SUCCESSFULLY , NOW YOU CAN LOGIN  !')
        else:
            print(0)
    elif d=='log':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        t.execute('select uname from signup where u_id="'+str(d1)+'" and pas="'+str(d2)+'"')
        r=t.fetchall()
        if r==[]:
            print(0)
        else:
            nam=r[0][0].split(' ')[0]
            print(d1,nam,sep=',,')
    elif d=='forgot':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        # d4=f.getvalue('t4')
        t.execute('select stat from signup where u_id="'+str(d1)+'"and sec_qus="'+str(d2)+'"and sec_ans="'+str(d3)+'"')
        r=t.fetchall()
        if r==[]:
            print(0)
        elif int(r[0][0])==0:
            print(1)
        else:
            print(r[0][0])
    elif d=='fgt':
        d1=f.getvalue('t1')
        t.execute("update signup set stat='0' where u_id='"+d1+"'")
        con.commit()
    elif d=='fgt2':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        url=('update signup set pas="'+str(d4)+'" where u_id="'+str(d1)+'"and sec_qus="'+str(d2)+'"and sec_ans="'+str(d3)+'"')
        t.execute(url)
        con.commit()
        print('your password is updated!')
    elif d=='change':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        url=('update signup set pas="'+str(d2)+'" where pas="'+str(d1)+'"')
        t.execute(url)
        con.commit()
        print('your password is updated!')
except Exception as e:
    print('unsuccess',e)
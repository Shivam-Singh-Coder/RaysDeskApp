#! C:\Users\HP\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector
con=mysql.connector.connect(host='localhost', user='webrays', passwd='rayssoft',database='webrays')
t=con.cursor() #ready and create explicit cursor that hold query
def autogen(cert,ch,yy):
    cert=cert+1
    if(cert!=10000):
        if(cert<10):
            b="REPL/CERT"+"/"+yy+"/"+ch+"000"+str(cert)
        elif(cert<100):
            b="REPL/CERT"+"/"+yy+"/"+ch+"00"+str(cert)
        elif(cert<1000):
            b="REPL/CERT"+"/"+yy+"/"+ch+"0"+str(cert)
        elif(cert<10000):
            b="REPL/CERT"+"/"+yy+"/"+ch+str(cert)
        print(b,ch,yy,cert,sep=",,,")
    else:
        ch=chr(ord(ch)+1)
        cert=0
        autogen(cert,ch,yy)
try:
    f=cgi.FieldStorage()
    d=f.getvalue('cond')
    if(d=='ins'):
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6')
        d7=f.getvalue('t7')
        d8=f.getvalue('t8')
        d9=f.getvalue('t9')
        d10=f.getvalue('t10')
        d11=f.getvalue('t11')
        ch=f.getvalue('t12')
        yy=f.getvalue('t13')
        cert=f.getvalue('t14')
        url="insert into certificate values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        t.execute(url,(d1,d2,d3,d4,d5,d6,d8,d7,d9,d11,d10))
        url="update automatic set ch='"+ch+"', cert="+cert+", yy='"+yy+"'"
        t.execute(url)
        con.commit()
        print("Successfully Inserted"+",,,10")
    elif(d=='search'):
        opt=f.getvalue('t2')
        val=f.getvalue('t3')
        if(opt=='Registration No'):
            url="select * from certificate where regno='%s'"%(val)
        elif(opt=='Certification No'):
            url="select * from certificate where cert_no='%s'"%(val)
        elif(opt=='Institution Code'):
            url="select * from certificate where inst_code='%s'"%(val)
        elif(opt=='Student Name'):
            url="select * from certificate where sname='%s'"%(val)
        t.execute(url)
        rs=t.fetchall()
        if(rs!=[]):
            for a in rs:
                if(a[9]==None):
                    b=''
                else:
                    b=a[9].decode()
                print("<tr class='tab_r'><td class='tab_c'>"+a[0]+"  "+"</td><td class='tab_c'>"+a[1]+"  "+"</td><td class='tab_c'>"+a[2]+"  "+"</td><td class='tab_c z' contenteditable='true'>"+str(a[3])+"  "+"</td><td class='tab_c z' contenteditable='true'>"+str(a[4])+"  "+"</td><td class='tab_c' contenteditable='true'><input class='dt' type='date' value="+a[5]+"></td><td class='tab_c z' contenteditable='true'>"+str(a[6])+"  "+"</td><td class='tab_c z' contenteditable='true'>"+str(a[7])+"  "+"</td><td class='tab_c z' contenteditable='true'>"+str(a[8])+"  "+"</td><td class='tab_c' contenteditable='true'><input class='dtt' type='date' value="+a[10]+"></td><td class='tab_c v'><img class='img' alt='No Pic Available' style='width:4rem;height:2rem;' id='img1' src="+b+"  "+"></td><td class='tab_c'><input class='upld' id='upld' accept='image/png, image/jpeg' type='file' value=''></td><td class='tab_c'><input class='rad' type='radio' name='rad'></td></tr>""")
        else:
            a=0
            print(a)
    elif(d=='update'):
        q=f.getvalue('t1')
        w=f.getvalue('t2')
        e=f.getvalue('t3')
        r=f.getvalue('t4')
        a=f.getvalue('t5')
        y=f.getvalue('t6')
        u=f.getvalue('t7')
        i=f.getvalue('t8')
        k=f.getvalue('t9') 
        kl=str(f.getvalue('t10'))
        url="update certificate set sname='"+e+"',fname='"+r+"',dob='"+a+"',duration='"+y+"',course='"+u+"',marks='"+i+"',issue_date='"+k+"',sphoto='"+kl+"' where cert_no='"+q+"' and regno='"+w+"'"
        t.execute(url)
        con.commit()
        print("Successfully Updated!")
    elif(d=='delete'):
        dp=f.getvalue('t1')
        rg=f.getvalue('t2')
        url="delete from certificate where cert_no='"+dp+"' and regno='"+rg+"'"
        t.execute(url)
        con.commit()
        print("Successfully Deleted!")
    elif(d=='searchall'):
        val=f.getvalue('t2')
        url="select * from certificate where cert_no='%s'"%(val)
        t.execute(url)
        rs=t.fetchall()
        if(rs!=[]):
            for i in rs[0]:
                print(i,',,,')
        else:
            a=0
            print(a)
    else:
        yy=f.getvalue('t1')
        t.execute("select * from automatic")
        rs=t.fetchall()
        if(rs!=[]):
            for a in rs:
                cert=a[1]
                ch=a[0]
                if(int(a[2])!=int(yy)):
                    cert=0
                    ch='A'
            autogen(cert,ch,yy)
except Exception as e:
    print("Unsuccesss",e)
finally:
    if con.is_connected:
        con.close()
        t.close()
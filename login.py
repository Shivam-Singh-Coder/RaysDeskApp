#! C:\Users\HP\AppData\Local\Programs\Python\Python311\python.exe
print('contact-type:text/html\r\n\r\n')
import cgi
import mysql.connector
con=mysql.connector.connect(host='localhost', user='webrays', passwd='rayssoft',database='webrays')
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
        d6=f.getvalue('t6')
        d7=f.getvalue('t7')
        t.execute('select u_id from signup where u_id="'+str(d2)+'"')
        r=t.fetchall()
        if r==[]:
            url='insert into signup (uname,u_id,sec_qus,sec_ans,pas,role,stat,cancel) value(%s,%s,%s,%s,%s,%s,%s,%s)'
            t.execute(url,(d1,d2,d3,d4,d5,d6,d7,0))
            con.commit()
            print('SIGN UP SUCCESSFULLY,NOW YOU CAN LOGIN !')
        else:
            print(0)
    elif d=='log':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        t.execute('select * from signup where u_id="'+str(d1)+'" and pas="'+str(d2)+'"')
        r=t.fetchall()
        if r!=[]:
            if(r[0][7].strip()=='Inactive'):
                print(10)
            else:
                print(r[0][2],r[0][8],r[0][1],sep=',,')
            # t.execute('select uname,bcode from signup where u_id="'+str(d1)+'" and pas="'+str(d2)+'"')
            # r1=t.fetchall()
            # if(r1!=[]):
            #     print(10)
            # else:
            #     print(0)
        else:
            print(0)
    # elif d=='log':
    #     d1=f.getvalue('t1')
    #     d2=f.getvalue('t2')
    #     t.execute('select uname,bcode from signup where u_id="'+str(d1)+'" and pas="'+str(d2)+'" and stat=Active')
    #     r=t.fetchall()
    #     if r==[]:
    #         t.execute('select uname,bcode from signup where u_id="'+str(d1)+'" and pas="'+str(d2)+'"')
    #         r1=t.fetchall()
    #         if(r1!=[]):
    #             print(10)
    #         else:
    #             print(0)
    #     else:
    #         print(r[0][0],r[0][1],sep=",,")
    elif d=='forgot':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        # d4=f.getvalue('t4')
        t.execute('select stat from signup where u_id="'+str(d1)+'"and sec_qus="'+str(d2)+'"and sec_ans="'+str(d3)+'"')
        r=t.fetchall()
        if r==[]:
            print(0)
        elif r[0][0]=='Inactive':
            print(1)
        else:
            print(r[0][0])
    elif d=='fgt':
        d1=f.getvalue('t1')
        t.execute("update signup set stat=Inactive where u_id='"+d1+"'")
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
        url1='select u_id from signup where pas="'+str(d1)+'"'
        t.execute(url1)
        r=t.fetchall()
        if r==[]:
            print("No ANy User!")
        else:
            url=('update signup set pas="'+str(d2)+'" where u_id="'+str(r[0][0])+'"')
            t.execute(url)
            con.commit()
            print('your password is updated!')
    elif d=='admin':
        url=('select count(sn) from signup')
        t.execute(url)
        r=t.fetchall()
        print(r[0][0])
except Exception as e:
    print('unsuccess',e)
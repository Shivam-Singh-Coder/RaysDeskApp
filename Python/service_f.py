#! C:\Users\sudhanshu\AppData\Local\Programs\Python\Python311\python.exe
print("content-Type:text/html\r\n\r\n")
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="pl",passwd="rays@1324",database="patna")
t=con.cursor()
f=cgi.FieldStorage()
try:
    a=f.getvalue('x')
    if(a=='inst'):
        q2=f.getvalue('b1')
        q3=f.getvalue('b2')
        q4=f.getvalue('b3')
        q5=f.getvalue('b4')
        q6=f.getvalue('b5')
        q7=f.getvalue('b6')
        q8=f.getvalue('b7')
        q9=f.getvalue('b8')
        url="insert into internship(position,category,location,s_date,duration,stipend,skill_req,end_date) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        t.execute(url,(q2,q3,q4,q5,q6,q7,q8,q9))
        con.commit()
        print("Suceessfully Inserted!")
    elif(a=='optsel'):
        opt=f.getvalue('t2')
        if(opt=='Position'):
            url="select position from internship"
        elif(opt=='Category'):
            url="select category from internship"
        else:
            url="select location from internship"
        t.execute(url)
        rs=t.fetchall()
        for a in rs:
            print("<option>"+a[0]+"</option>")
    elif(a=='search'):
        opt=f.getvalue('t2')
        val=f.getvalue('t3')
        if(opt=='Position'):
            url="select * from internship where position='%s'"%(val)
        elif(opt=='Category'):
            url="select * from internship where category='%s'"%(val)
        elif(opt=='Location'):
            url="select * from internship where location='%s'"%(val)
        t.execute(url)
        rs=t.fetchall()
        if(rs!=[]):
            for a in rs:
                print("<tr class='tab_r'><td class='tab_c'>"+a[1]+"  "+"</td><td class='tab_c z' contenteditable='true'>"+str(a[2])+"  "+"</td><td class='tab_c z' contenteditable='true'>"+str(a[3])+"  "+"</td><td class='tab_c z' contenteditable='true'>"+str(a[4])+"  "+"</td><td class='tab_c z' contenteditable='true'>"+str(a[5])+"  "+"</td><td class='tab_c z' contenteditable='true'>"+str(a[6])+"  "+"</td><td class='tab_c z' contenteditable='true'>"+str(a[7])+"  "+"</td><td class='tab_c z' contenteditable='true'>"+str(a[8])+"  "+"</td><td class='tab_c'><input class='rad' type='radio' name='rad'></td></tr>""")
        else:
            a=0
            print(a)
    elif(a=='update'):
        q=f.getvalue('t1')
        w=f.getvalue('t2')
        e=f.getvalue('t3')
        r=f.getvalue('t4')
        t=f.getvalue('t5')
        y=f.getvalue('t6')
        u=f.getvalue('t7')
        i=f.getvalue('t8')
        if(q==None):
            print("Please Select Any Row!")
        else:       
            url="update internship set category='"+w+"',location='"+e+"',S_date='"+r+"',duration='"+t+"',stipend='"+y+"',skill_req='"+u+"',end_date='"+i+"' where position='"+q+"'"
            t.execute(url)
            con.commit()
            print("Successfully Updated!")
    elif(a=='delete'):
        dp=f.getvalue('t1')
        if(dp==None):
            print("Please Select Any Row!")
        else:
            url="delete from internship where position='"+dp+"'"
            t.execute(url)
            con.commit()
            print("Successfully Deleted!")
except Exception as e:
    print("Unsuccesss",e)
finally:
    if con.is_connected:
        con.close()
        t.close()
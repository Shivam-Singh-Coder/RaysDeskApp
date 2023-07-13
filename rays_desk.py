#! C:\Users\HP\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\r\n\r\n")
import cgi
from datetime import date
import mysql.connector
con=mysql.connector.connect(host='localhost', user='rays_desk', passwd='rays_desk',database='rays_desk')
t=con.cursor() #ready and create explicit cursor that hold query
try:
    f=cgi.FieldStorage()
    d=f.getvalue('cond')
    ######################REGISTRATION DETAILS##############
    if(d=='auto_reg'):
        t.execute("select reg_no from automatic")
        rs=t.fetchall()
        reg_no=rs[0][0]+1
        year=date.today().year%100
        t.execute('select max(reg_no) from registration')
        rs=t.fetchall()
        yr=rs[0][0][10:12]
        if(year>int(yr)):
            reg_no=1
        if(reg_no<10):
            strr="REPL/"+"BR01/"+str(year)+"/R000"+str(reg_no)
        elif(reg_no<100):
            strr="REPL/"+"BR01/"+str(year)+"/R00"+str(reg_no)
        elif(reg_no<1000):
           strr="REPL/"+"BR01/"+str(year)+"/R0"+str(reg_no)
        elif(reg_no<10000):
           strr="REPL/"+"BR01/"+str(year)+"/R"+str(reg_no)
        print(strr,reg_no,sep=',,,')
    elif(d=='cmb_reg'):
        print('hii')
    #############Course Details###################
    elif(d=='ins_course'):
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6')
        d7=f.getvalue('t7')
        url="insert into course values(%s,%s,%s,%s,%s,%s)"
        t.execute(url,(d1,d2,d3,d4,d5,d6))
        t.execute("update automatic set cid="+d7+"")
        con.commit()
        print("Course Created Successfully!,,,10")
    elif(d=='cmb_course'):
        d1=f.getvalue('t1')
        t.execute("select distinct "+d1+" from course")
        rs=t.fetchall()
        if(d1=='cid'):
            print("<option selected disabled>----- Select Course ID -----</option>")
        elif(d1=='cname'):
            print("<option selected disabled>----- Select Course Name -----</option>")
        for a in rs:
            print("<option>"+a[0]+"</option>")
    elif d=='ser_course':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        if(d1=='cname'):
            url="select * from course where cname='"+d2+"'"
        elif(d1=='cid'):
            url="select * from course where cid='"+d2+"'"
        else:
            url="select * from course"
        t.execute(url)
        rs=t.fetchall()
        if rs==[]:
            print(0)
        else:
            i=0
            print('<div id="d5"><table id="table3"><tr><th id="sn">Sn</th><th>Course ID</th><th>Course Name</th><th>Course Dur.</th><th>Course Fee</th><th>One Time Payment(OTP)</th><th colspan="2" style="color:blue;" id="act">Action Here</th></tr>')
            for a in rs:
                i=i+1
                print('<tr class="tr1"><td id="sn" data-label="SN">'+str(i)+'   '+'</td><td data-label="Course ID">'+str(a[0])+'   '+'</td><td data-label="Course Name" contenteditable="true" id="e">'+str(a[1])+'   '+'</td><td data-label="Course Dur." contenteditable="true" id="e">'+str(a[2])+'   '+'</td><td data-label="Course Fee" contenteditable="true" id="e">'+str(a[3])+'   '+'</td><td data-label="One Time Payment(OTP)" contenteditable="true" id="e">'+str(a[4])+'   '+'</td><td data-label="Update"><i class="fa" id="upd" data-toggle="tooltip" title="Update">&#xf044;</i></td><td data-label="Delete"><i class="fa" id="del" data-toggle="tooltip" title="Delete">&#xf014;</i></td></tr>')
            print('</table></div>')
    elif d=='upd_course':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        t.execute('update course set cname="'+d2+'",cdur="'+d3+'",cfee="'+d4+'",otp="'+d5+'" where cid="'+d1+'" ')
        con.commit()
        print('Successfully Updated!')
    elif d=='del_course':
        d1=f.getvalue('t1')
        t.execute('delete from course where cid="'+d1+'"')
        con.commit()
        print('Successfully Deleted!,,,10')
    else:
        # d1=f.getvalue('t1')
        t.execute("select cid from automatic")
        rs=t.fetchall()
        cid=rs[0][0]+1
        if(cid<10):
           str="REPLC00"+str(cid)
        elif(cid<100):
           str="REPLC0"+str(cid)
        elif(cid<1000):
           str="REPLC"+str(cid)
        else:
            str="End Course!"
        print(cid,str,sep=",,,")
except Exception as e:
    print("Unsuccesss",e)
finally:
    if con.is_connected:
        con.close()
        t.close()
#! C:\Users\HP\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\r\n\r\n")
import cgi
from datetime import date
from datetime import datetime
import mysql.connector
con=mysql.connector.connect(host='localhost', user='rays_desk', passwd='rays_desk',database='rays_desk')
t=con.cursor() #ready and create explicit cursor that hold query
try:
    f=cgi.FieldStorage()
    d=f.getvalue('cond')
    ######################REGISTRATION DETAILS##############
    if(d=='auto_reg'):
        t1=f.getvalue('t1')
        t.execute("select reg_no from branch_details where bcode='"+t1+"'")
        rs=t.fetchall()
        reg_no=rs[0][0]+1
        year=date.today().year%100
        t.execute('select max(reg_no) from registration')
        rs=t.fetchall()
        if(rs[0][0]!=None):
            yr=rs[0][0][10:12]
            if(year>int(yr)):
                reg_no=1
        if(reg_no<10):
            strr="REPL/"+t1.upper()+"/"+str(year)+"/R000"+str(reg_no)
        elif(reg_no<100):
            strr="REPL/"+t1.upper()+"/"+str(year)+"/R00"+str(reg_no)
        elif(reg_no<1000):
           strr="REPL/"+t1.upper()+"/"+str(year)+"/R0"+str(reg_no)
        elif(reg_no<10000):
           strr="REPL/"+t1.upper()+"/"+str(year)+"/R"+str(reg_no)
        print(strr,reg_no,sep=',,,')
    elif(d=='reg_district'):
        t1=f.getvalue('t1')
        t.execute("select distr from state1 where stat='"+t1+"'")    
        rs=t.fetchall()
        if(rs!=[]):
            print('<option value="" selected disabled>----------------Select Any District-----------------</option>')
            for a in rs:
                for i in a:
                    for b in i.split(','):
                        print('<option>'+b+'</option>')
        else:
            print("Invalid Choice!")
    elif(d=='reg_insert'):
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
        d12=f.getvalue('t12')
        d13=f.getvalue('t13')
        d14=f.getvalue('t14')
        d15=f.getvalue('t15')
        d16=f.getvalue('t16')
        d17=f.getvalue('t17')
        d18=f.getvalue('t18')
        d19=f.getvalue('t19')
        d20=f.getvalue('t20')
        d21=f.getvalue('t21')
        t.execute("select * from registration where reg_no='"+d1+"'")
        if(t.fetchall()==[]):
            url="insert into registration values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            t.execute(url,(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20))
            t.execute("update branch_details set reg_no="+d21+" where bcode='"+d19+"'")
            con.commit()
            print("Successfully Inserted Record!,,,10")
        else:
            print("Already Inserted Record for this Registration ID!")
    elif d=='ser_reg':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t2')
        d4=f.getvalue('t2')
        if(d3!=None and d4!=None and d1==None and d2==None):
            url="select * from registration where reg_date between '"+d3+"' and '"+d4+"'"
        if(d1=='Registration' and d3==None and d4==None):
            url="select * from registration where reg_no='"+d2+"'"
        if(d1=='Registration' or d1=='Contact' or d1=='College' or d1=='Name' or d1=='Blood Grp' or d1=='Prog' or d1=='College' and d3!=None and d4!=None):
            url=url+"and reg_date between '"+d3+"' and '"+d4+"'"
        if(d1=='Contact' and d3==None and d4==None):
            url="select * from registration where cont_no='"+d2+"'"
        # if(d1=='Contact' and d3!=None and d4!=None):
        #     url=url+"and reg_date between '"+d3+"' and '"+d4+"'"
        if(d1=='Name' and d3==None and d4==None):
            url="select * from registration where sname='"+d2+"'"
        # if(d1=='Name' and d3!=None and d4!=None):
        #     url=url+"and reg_date between '"+d3+"' and '"+d4+"'"
        if(d1=='Blood Grp' and d3==None and d4==None):
            url="select * from registration where blood_grp='"+d2+"'"
        # if(d1=='Blood Grp' and d3!=None and d4!=None):
        #     url=url+"and reg_date between '"+d3+"' and '"+d4+"'"
        if(d1=='Prog' and d3==None and d4==None):
            url="select * from registration where prog='"+d2+"'"
        # if(d1=='Prog' and d3!=None and d4!=None):
        #     url=url+"and reg_date between '"+d3+"' and '"+d4+"'"
        if(d1=='College' and d3==None and d4==None):
            url="select * from registration where clg_name='"+d2+"'"
        # if(d1=='College' and d3!=None and d4!=None):
        #     url=url+"and reg_date between '"+d3+"' and '"+d4+"'"
        else:
            url="select * from registration"
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
    elif d=='upd_reg':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d5=f.getvalue('t6')
        d5=f.getvalue('t7')
        d5=f.getvalue('t8')
        d5=f.getvalue('t9')
        d5=f.getvalue('t10')
        d5=f.getvalue('t11')
        d5=f.getvalue('t12')
        d5=f.getvalue('t13')
        d5=f.getvalue('t14')
        d5=f.getvalue('t15')
        d5=f.getvalue('t16')
        d5=f.getvalue('t17')
        d5=f.getvalue('t18')
        t.execute('update registration set reg_date="'+d2+'",sname="'+d3+'",fname="'+d4+'",mname="'+d5+'",sdob="'+d6+'",email="'+d7+'",cont_no="'+d8+'",prog="'+d9+'",blood_grp="'+d10+'",clg_name="'+d11+'",gender="'+d12+'",prmt_add="'+d13+'",dis="'+d14+'",stt="'+d15+'",sphoto="'+d16+'",aadhaar="'+d17+'",cor_add="'+d18+'" where reg_no="'+d1+'" ')
        con.commit()
        print('Successfully Updated This Record!')
    elif d=='del_reg':
        d1=f.getvalue('t1')
        t.execute('delete from registration where reg_no="'+d1+'"')
        con.commit()
        print('Successfully Deleted This Record!,,,10')
    ##################Admission###########################
    elif(d=='auto_adm'):
        t1=f.getvalue('t1')
        t.execute("select adm_no,adm_ch from branch_details where bcode='"+t1+"'")
        rs=t.fetchall()
        adm_no=rs[0][0]+1
        adm_ch=rs[0][1].strip()
        year=date.today().year%100
        t.execute('select max(adm_no) from admission')
        rs1=t.fetchall()[0][0]
        if(rs1!=None):
            yr=rs1[0:2]
            if(year>int(yr) or year<int(yr)):
                adm_no=1
                adm_ch='A'
        if(adm_no==1000):
            adm_ch=chr(ord(adm_ch)+1)
            adm_no=1
        if(adm_no<10):
            strr=str(year)+str(adm_ch)+"000"+str(adm_no)
        elif(adm_no<100):
            strr=str(year)+str(adm_ch)+"00"+str(adm_no)
        elif(adm_no<1000):
           strr=str(year)+str(adm_ch)+"0"+str(adm_no)
        elif(adm_no<10000):
           strr=str(year)+str(adm_ch)+str(adm_no)
        print(strr,adm_no,adm_ch,sep=',,,')
    elif(d=='adm_insert'):
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
        t.execute("select * from admission where adm_no='"+d1+"'")
        if(t.fetchall()==[]):
            url="insert into admission values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            t.execute(url,(d1,d2,d3,d4,d5,d6,d7,d8,d9,0))
            t.execute("update branch_details set adm_no="+d10+",adm_ch='"+d11+"' where bcode='"+d8+"'")
            con.commit()
            print("Successfully Inserted Record!,,,10")
        else:
            print("Already Inserted Record for this Registration ID!")
    elif d=='ser_adm':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        url=''
        if(d1==None and d2==None and d4!=None and d3!=None and d5!=None):
            url='select * from admission where bcode="'+d5+'" and adm_date between "'+d3+'" and "'+d4+'" order by adm_no desc'
        if(d1=='adm' and d5!=None):
            url='select * from admission where adm_no="'+d2+'" and bcode="'+d5+'" order by adm_no desc'
        if(d1=='adm' and d4!=None and d5!=None):
            url=url[0:url.find('order')]+' and adm_date between "'+d3+'" and "'+d4+'" order by adm_no desc'
        if(d1=='reg' and d5!=None):
            url='select * from admission where reg_no="'+d2+'" and bcode="'+d5+'" order by adm_no desc'
        if(d1=='reg' and d4!=None and d5!=None):
            url=url[0:url.find('order')]+'and adm_date between "'+d3+'" and "'+d4+'" order by adm_no desc'
        if(d1=='sname' and d5!=None):
            url='select * from admission where reg_no in(select reg_no from registration where sname="'+d2+'" and bcode="'+d5+'") and bcode="'+d5+'" order by adm_no desc'
        if(d1=='sname' and d4!=None and d3!=None and d5!=None):
            url=url[0:url.find('order')]+' and adm_date between "'+d3+'" and "'+d4+'" order by adm_no desc'
        t.execute(url)
        rs=t.fetchall()
        if rs==[]:
            print(0)
        else:
            i=0
            print('<div id="d5"><table id="table3"><tr><th id="sn">Sn</th><th>Admission No</th><th>Admission Date</th><th>Registration No</th><th>Course Applied</th><th>Course Fee</th><th>Disc. Type</th><th>Discount</th><th colspan="3" id="chk">Action Here</th></tr>')
            for a in rs:
                i=i+1
                if(a[9]==1):
                    print('<tr class="tr1" style="background-color:red;color:white;"><td id="sn" data-label="SN">'+str(i)+'   '+'</td><td data-label="Admission No">'+str(a[0])+'   '+'</td><td data-label="Admission Date">'+str(a[1])+'   '+'</td><td data-label="Registration No">'+str(a[2]).upper()+'   '+'</td><td data-label="Course Applied">'+str(a[3])+'   '+'</td><td data-label="Course Fee">'+str(a[4])+'   '+'</td><td data-label="Discount Type">'+str(a[5])+'   '+'</td><td data-label="Discount">'+str(a[6])+'   '+'</td><td data-label="Update"><i class="fa" id="upd" data-toggle="tooltip" title="Update" style="color:white;">&#xf044;</i></td><td data-label="Cancel"><i class="fa" id="del" data-toggle="tooltip" title="Cancel" style="color:white;">&#10006;</i></td><td data-label="Print"><i class="fa" id="prt" data-toggle="tooltip" title="Print" style="color:white;">&#xf02f;</i></td></tr>')
                else:
                    print('<tr class="tr1"><td id="sn" data-label="SN">'+str(i)+'   '+'</td><td data-label="Admission No">'+str(a[0])+'   '+'</td><td data-label="Admission Date">'+str(a[1])+'   '+'</td><td data-label="Registration No">'+str(a[2]).upper()+'   '+'</td><td data-label="Course Applied" contenteditable="true" id="e">'+str(a[3])+'   '+'</td><td data-label="Course Fee">'+str(a[4])+'   '+'</td><td data-label="Discount Type" contenteditable="true" id="e">'+str(a[5])+'   '+'</td><td data-label="Discount" contenteditable="true" id="e">'+str(a[6])+'   '+'</td><td data-label="Update"><i class="fa" id="upd" data-toggle="tooltip" title="Update">&#xf044;</i></td><td data-label="Cancel"><i class="fa" id="del" data-toggle="tooltip" title="Cancel">&#10006;</i></td><td data-label="Print"><i class="fa" id="prt" data-toggle="tooltip" title="Print">&#xf02f;</i></td></tr>')
            print('</table></div>')
    elif d=='upd_adm':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6')
        d7=f.getvalue('t7')
        t.execute('update admission set adm_date="'+d2+'",reg_no="'+d3+'",cou_apply="'+d4+'",fee="'+d5+'",dis="'+d6+'" where adm_no="'+d1+'" and bcode="'+d7+'"')
        con.commit()
        print('Successfully Updated This Record!')
    elif d=='del_adm':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        t.execute('update admission set cancel=1 where adm_no="'+d1+'" and bcode="'+d2+'"')
        con.commit()
        print('Successfully Cancelled This Record!,,,10')
    elif d=='cname_adm':
        d1=f.getvalue('t1')
        t.execute('select cname from course where bcode="'+d1+'"')
        rs=t.fetchall()
        if(rs!=[] or rs!=None):
            for a in rs:
                print('<option>'+a[0]+'</option>')
        else:
            print('0')
    elif d=='adm_cfee':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        t.execute('select cfee from course where cname="'+d1+'" and bcode="'+d2+'"')
        rs=t.fetchall()
        if(rs!=[] or rs!=None):
            print(rs[0][0])
        else:
            print('0')
    elif d=='adm_otp':
        d1=f.getvalue('t1').split(',')
        d2=f.getvalue('t2')
        num=0
        for a in range(len(d1)):
            t.execute('select otp from course where cname="'+d1[a]+'" and bcode="'+d2+'"')
            rs=t.fetchall()
            if(rs!=[] or rs!=None):
                num=num+int(rs[0][0])
            else:
                num=num+0
        print(num)
    elif d=='adm_reg':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        t.execute('select sname from registration where reg_no="'+d1+'" and bcode="'+d2+'"')
        rs=t.fetchall()
        if(rs!=[]):
            t.execute('select cou_apply from admission where reg_no="'+d1+'" and bcode="'+d2+'"')
            rs1=t.fetchall()
            if(rs1==[]):
                rs1=None
            else:
                rs1=rs1[0][0]
            print(rs[0][0],rs1,sep=',,,')
        else:
            print('0')
    elif d=='adm_inv':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        t.execute('select * from admission where adm_no="'+d1+'" and bcode="'+d2+'"')
        rs=t.fetchall()
        if(rs!=[]):
            for a in rs:
                for i in a:
                    print(str(i)+"&&")
                t.execute('select sname from registration where reg_no="'+a[2]+'" and bcode="'+d2+'"')
                print(t.fetchall()[0][0])
                t.execute('select distinct cou_apply from admission where reg_no="'+a[2]+'" and bcode="'+d2+'" and adm_date<"'+str(a[1])+'"')
                rs1=t.fetchall()
                print('&&')
                for b in rs1:
                    if(b[0]!=a[3]):
                        print(b[0]+",")
        else:
            print('0')
    ######################################Internship##############
    elif(d=='int_auto'):
        t.execute('select int_no,int_ch from automatic')
        rs=t.fetchall()
        int_no=rs[0][0]+1
        ch=rs[0][1]
        year=date.today().year%100
        t.execute('select max(intern_no) from internship')
        rs1=t.fetchall()
        if(rs1[0][0]!=None):
            yr=rs1[0][0][12:14]
            if(year>int(yr) or year<int(yr)):
                int_no=1
                ch='A'
        if(int_no==1000):
            ch=chr(ord(ch)+1)
            int_no=1
        if(int_no<10):
            strr="REPL/"+"INTERN/"+str(year)+"/"+ch+"00"+str(int_no)
        elif(int_no<100):
            strr="REPL/"+"INTERN/"+str(year)+"/"+ch+"0"+str(int_no)
        elif(int_no<1000):
           strr="REPL/"+"INTERN/"+str(year)+"/"+ch+str(int_no)
        print(strr,int_no,ch,sep=',,,')
    elif(d=='int_insert'):
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
        d12=f.getvalue('t12')
        d13=f.getvalue('t13')
        d14=f.getvalue('t14')
        d15=f.getvalue('t15')
        d16=f.getvalue('t16')
        d17=f.getvalue('t17')
        d18=f.getvalue('t18')
        d19=f.getvalue('t19')
        d20=f.getvalue('t20')
        d21=f.getvalue('t21')
        t.execute("select * from internship where intern_no='"+d1+"'")
        if(t.fetchall()==[]):
            url="insert into internship values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            t.execute(url,(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d20,d21,0))
            t.execute("update automatic set int_no="+d19+",int_ch='"+d18+"'")
            con.commit()
            print("Successfully Inserted Record!,,,10")
        else:
            print("Already Inserted Record for this Intern ID!")
    elif d=='int_branch':
        d1=f.getvalue('t1')
        t.execute('select bname,addr from branch_details where bcode="'+d1+'"')
        rs=t.fetchall()
        if(rs!=[]):
            for a in rs:
                for i in a:
                    print(i+"&&&&")
        else:
            print('0')
    elif d=='ser_int':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        url=''
        if(d1=='cert' and d5!=None):
            url='select * from internship where intern_no="'+d2+'" order by intern_no desc'
        if(d1=='cert' and d3!=None and d4!=None and d5!=None):
            url=url[0:url.find('order')]+' and int_date between "'+d3+'" and "'+d4+'" order by intern_no desc'
        if(d1=='cont' and d5!=None):
            url='select * from internship where cont_no="'+d2+'" order by intern_no desc'
        if(d1=='cont' and d3!=None and d4!=None and d5!=None):
            url=url[0:url.find('order')]+' and int_date between "'+d3+'" and "'+d4+'" order by intern_no desc'
        if(d1=='sname' and d5!=None):
            url='select * from internship where sname="'+d2+'" order by intern_no desc'
        if(d1=='sname' and d3!=None and d4!=None and d5!=None):
            url=url[0:url.find('order')]+' and int_date between "'+d3+'" and "'+d4+'" order by intern_no desc'
        if(d1=='clg' and d5!=None):
            url='select * from internship where coll_name="'+d2+'" order by intern_no desc'
        if(d1=='clg' and d3!=None and d4!=None and d5!=None):
            url=url[0:url.find('order')]+' and int_date between "'+d3+'" and "'+d4+'" order by intern_no desc'
        t.execute(url)
        rs=t.fetchall()
        if rs==[]:
            print(0)
        else:
            i=0
            print("<div id='d5'><table id='table3'><tr><th id='sn'>Sn</th><th>Internship No</th><th>Internship Date</th><th>Student Name</th><th>Father's Name</th><th>Gender</th><th>Date Of Birth</th><th>Email ID</th><th>Contact No.</th><th>College Name</th><th>Project Title</th><th>Duration</th><th>Technologies</th><th>Guidance Name</th><th>Stipend Amt.</th><th>Study Centre</th><th>Student Pic</th><th>Choose File</th><th colspan='4' style='color: blue;' id='chk'>Action</th><th id='sn1'></th></tr>")
            for a in rs:
                i=i+1
                if(a[16]==None):
                    b='#'
                else:
                    b=a[16].decode()
                if(a[19]==1):
                    print("<tr class='tr1' style='background-color:red;color:white;'><td id='sn' data-label='SN'>"+str(i)+"   "+"</td><td data-label='Internship No'>"+str(a[0])+"   "+"</td><td data-label='Internship Date'>"+str(a[1])+"   "+"</td><td data-label='Student Name' contenteditable='true' id='e'>"+str(a[2])+"   "+"</td><td data-label='Father's Name' contenteditable='true' id='e'>"+str(a[3])+"   "+"</td><td data-label='Gender' contenteditable='true' id='e'>"+str(a[4])+"   "+"</td><td data-label='Date Of Birth' contenteditable='true' id='e'>"+str(a[5])+"   "+"</td><td data-label='Email ID' contenteditable='true' id='e'>"+str(a[7])+"   "+"</td><td data-label='Contact No.' contenteditable='true' id='e'>"+str(a[6])+"   "+"</td><td data-label='College Name' contenteditable='true' id='e'>"+str(a[8])+"   "+"</td><td data-label='Project Title' contenteditable='true' id='e'>"+str(a[9])+"   "+"</td><td data-label='Duration' contenteditable='true' id='e'>"+str(a[10])+"   "+"</td><td data-label='Technologies' contenteditable='true' id='e'>"+str(a[11])+"   "+"</td><td data-label='Guidance Name' contenteditable='true' id='e'>"+str(a[12])+"   "+"</td><td data-label='Stipend Amt.' contenteditable='true' id='e'>"+str(a[13])+"   "+"</td><td data-label='Study Centre'>"+str(a[14])+"   "+"</td><td data-label='Student Pic'><img src="+b+" alt='Student Pic' id='imgd' style='height: 5rem;width: 5rem;'>"+   +"</td><td data-label='Choose File'><input type='file' id='imgi'>"+   +"</td><td data-label='Update'><i class='fa' id='upd' data-toggle='tooltip' title='Update' style='color:white;'>&#xf044;</i></td><td data-label='Cancel'><i class='fa' id='del' data-toggle='tooltip' title='Cancel' style='color:white;'>&#10006;</i></td><td data-label='Certificate'><i class='fa' id='cert' data-toggle='tooltip' title='Certificate' style='color:white;'>&#xf15c;</i></td><td data-label='Marksheet'><i class='fa' id='mark' data-toggle='tooltip' title='Marksheet' style='color:white;'>&#xf15b;</i></td><td class='sn'></td></tr>")
                else:
                    print("<tr class='tr1'><td id='sn' data-label='SN'>"+str(i)+"   "+"</td><td data-label='Internship No'>"+str(a[0])+"   "+"</td><td data-label='Internship Date'>"+str(a[1])+"   "+"</td><td data-label='Student Name' contenteditable='true' id='e'>"+str(a[2])+"   "+"</td><td data-label='Father's Name' contenteditable='true' id='e'>"+str(a[3])+"   "+"</td><td data-label='Gender' contenteditable='true' id='e'>"+str(a[4])+"   "+"</td><td data-label='Date Of Birth' contenteditable='true' id='e'>"+str(a[5])+"   "+"</td><td data-label='Email ID' contenteditable='true' id='e'>"+str(a[7])+"   "+"</td><td data-label='Contact No.' contenteditable='true' id='e'>"+str(a[6])+"   "+"</td><td data-label='College Name' contenteditable='true' id='e'>"+str(a[8])+"   "+"</td><td data-label='Project Title' contenteditable='true' id='e'>"+str(a[9])+"   "+"</td><td data-label='Duration' contenteditable='true' id='e'>"+str(a[10])+"   "+"</td><td data-label='Technologies' contenteditable='true' id='e'>"+str(a[11])+"   "+"</td><td data-label='Guidance Name' contenteditable='true' id='e'>"+str(a[12])+"   "+"</td><td data-label='Stipend Amt.' contenteditable='true' id='e'>"+str(a[13])+"   "+"</td><td data-label='Study Centre'>"+str(a[14])+"   "+"</td><td data-label='Student Pic'><img src="+b+" alt='Student Pic' id='imgd' style='height: 5rem;width: 5rem;'>"+   +"</td><td data-label='Choose File'><input type='file' id='imgi'>"+   +"</td><td data-label='Update'><i class='fa' id='upd' data-toggle='tooltip' title='Update'>&#xf044;</i></td><td data-label='Cancel'><i class='fa' id='del' data-toggle='tooltip' title='Cancel'>&#10006;</i></td><td data-label='Certificate'><i class='fa' id='cert' data-toggle='tooltip' title='Certificate'>&#xf15c;</i></td><td data-label='Marksheet'><i class='fa' id='mark' data-toggle='tooltip' title='Marksheet'>&#xf15b;</i></td><td class='sn'></td></tr>")
            print('</table></div>')
    elif d=='upd_int':
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
        d12=f.getvalue('t12')
        d13=f.getvalue('t13')
        d14=f.getvalue('t14')
        d15=f.getvalue('t15')
        d16=f.getvalue('t16')
        t.execute('update internship set int_date="'+d2+'",sname="'+d3+'",fname="'+d4+'",gender="'+d5+'",dob="'+d6+'",cont_no="'+d8+'",email_id="'+d7+'",coll_name="'+d9+'",pro_tit="'+d10+'",dur="'+d11+'",techno="'+d12+'",guide_name="'+d13+'",stip_amt="'+d14+'",stu_pic="'+d15+'" where intern_no="'+d1+'" and bcode="'+d16+'"')
        con.commit()
        print('Successfully Updated This Record!')
    elif d=='del_int':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        t.execute('update internship set cancel=1 where intern_no="'+d1+'" and bcode="'+d2+'"')
        con.commit()
        print('Successfully Cancelled This Record!,,,10')
    #######################Certificate###############
    elif d=='cert_auto':
        t.execute('select cert_no,cert_ch from automatic')
        rs=t.fetchall()
        cert_no=rs[0][0]+1
        cert_ch=rs[0][1]
        year=date.today().year%100
        t.execute('select max(cref_no) from certificate')
        rs1=t.fetchall()
        if(rs1[0][0]!=None):
            yr=rs1[0][0][10:12]
            if(year>int(yr) or year<int(yr)):
                cert_no=1
                cert_ch='A'
        if(cert_no==10000):
            cert_ch=chr(ord(cert_ch)+1)
            cert_no=1
        if(cert_no<10):
            strr="REPL/"+"CERT/"+str(year)+"/"+cert_ch+"000"+str(cert_no)
        elif(cert_no<100):
            strr="REPL/"+"CERT/"+str(year)+"/"+cert_ch+"00"+str(cert_no)
        elif(cert_no<1000):
           strr="REPL/"+"CERT/"+str(year)+"/"+cert_ch+"0"+str(cert_no)
        elif(cert_no<10000):
           strr="REPL/"+"CERT/"+str(year)+"/"+cert_ch+str(cert_no)
        print(strr,cert_no,cert_ch,sep=',,,')
    elif d=='cert_branch':
        d1=f.getvalue('t1')
        t.execute('select bname from branch_details where bcode="'+d1+'"')
        rs=t.fetchall()
        if(rs!=[]):
            print(rs[0][0])
        else:
            print('0')
    elif d=='cert_reg':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        t.execute('select sname,fname,sphoto from registration where reg_no="'+d1+'" and bcode="'+d2+'"')
        rs=t.fetchall()
        if(rs!=[]):
            t.execute('select distinct cou_apply from admission where reg_no="'+d1+'" and bcode="'+d2+'"')
            rs1=t.fetchall()
            if(rs1==[]):
                print('50050')
            else:
                for a in rs1:
                    t.execute('select * from certificate where reg_no="'+d1+'" and course="'+a[0]+'"')
                    if(t.fetchall()==[]):
                        print('<option>'+a[0]+'</option>')
            if(rs[0][2]==None):
                bk='#'
            else:
                bk=rs[0][2].decode()
            print('&&&&'+rs[0][0]+'&&&&'+rs[0][1]+'&&&&'+bk)
        else:
            print('0')
    elif(d=='cert_insert'):
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
        d12=f.getvalue('t12')
        d13=f.getvalue('t13')
        d14=f.getvalue('t14')
        t.execute("select * from certificate where cref_no='"+d1+"'")
        if(t.fetchall()==[]):
            url="insert into certificate values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            t.execute(url,(d1,d2,d3,d4,d5,d6,d7,d8,d9,d14,d13,d10,0))
            t.execute("update automatic set cert_no="+d12+",cert_ch='"+d11+"'")
            con.commit()
            print("Successfully Inserted Record!,,,10")
        else:
            print("Already Inserted Record for this Certificate ID!")
    elif d=='ser_cert':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        url=''
        if(d1==None and d2==None and d4!=None and d3!=None and d5!=None):
            url='select * from certificate where bcode="'+d5+'" and cer_date between "'+d3+'" and "'+d4+'" order by cref_no desc'
        if(d1=='cert' and d5!=None):
            url='select * from certificate where cref_no="'+d2+' and bcode="'+d5+'" order by cref_no desc'
        if(d1=='cert' and d4!=None and d3!=None):
            url=url[0:url.find('order')]+' and cer_date between "'+d3+'" and "'+d4+'" order by cref_no desc'
        if(d1=='reg' and d5!=None):
            url='select * from certificate where reg_no="'+d2+'" and bcode="'+d5+'" order by cref_no desc'
        if(d1=='reg' and d4!=None and d3!=None):
            url=url[0:url.find('order')]+' and cer_date between "'+d3+'" and "'+d4+'" order by cref_no desc'
        if(d1=='sname' and d5!=None):
            url='select * from certificate where sname="'+d2+'" and bcode="'+d5+'" order by cref_no desc'
        if(d1=='sname' and d4!=None and d3!=None):
            url=url[0:url.find('order')]+' and cer_date between "'+d3+'" and "'+d4+'" order by cref_no desc'
        t.execute(url)
        rs=t.fetchall()
        if rs==[]:
            print(0)
        else:
            i=0
            print("<div id='d5'><table id='table3'><tr><th id='sn'>Sn</th><th>Certificate No</th><th>Registration No</th><th>Date Of Issue</th><th>Student Name</th><th>Father's Name</th><th>Course</th><th>Starting Date</th><th>Ending Date</th><th>Study Centre</th><th>Student Pic</th><th colspan='4' style='color: blue;' id='chk'>Action Here</th></tr>")
            for a in rs:
                i=i+1
                if(a[9]==b'#'):
                    b='#'
                else:
                    b=a[9].decode()
                if(a[12]==1):
                    print("<tr class='tr1' style='background-color:red;color:white;'><td id='sn' data-label='SN'>"+str(i)+"   "+"</td><td data-label='Certificate No'>"+str(a[0])+"   "+"</td><td data-label='Registration No'>"+str(a[2])+"   "+"</td><td data-label='Date Of Issue'>"+str(a[1])+"   "+"</td><td data-label='Student Name'>"+str(a[4])+"   "+"</td><td data-label='Father's Name'>"+str(a[5])+"   "+"</td><td data-label='Course' contenteditable='true' id='e'>"+str(a[3])+"   "+"</td><td data-label='Starting Date' contenteditable='true' id='e'>"+str(a[6])+"   "+"</td><td data-label='Ending Date' contenteditable='true' id='e'>"+str(a[7])+"   "+"</td><td data-label='Study Centre'>"+str(a[8])+"   "+"</td><td data-label='Student Pic'><img src='"+b+"' alt='Student Pic' style='height: 5rem;width: 5rem;'></td><td data-label='Update'><i class='fa' id='upd' data-toggle='tooltip' title='Update' style='color:white;'>&#xf044;</i></td><td data-label='Cancel'><i class='fa' id='del' data-toggle='tooltip' title='Cancel' style='color:white;'>&#10006;</i></td><td data-label='Certificate'><i class='fa' id='cert' data-toggle='tooltip' title='Certificate' style='color:white;'>&#xf15c;</i></td><td data-label='Marksheet'><i class='fa' id='mark' data-toggle='tooltip' title='Marksheet' style='color:white;'>&#xf15b;</i></td></tr>")
                else:
                    print("<tr class='tr1'><td id='sn' data-label='SN'>"+str(i)+"   "+"</td><td data-label='Certificate No'>"+str(a[0])+"   "+"</td><td data-label='Registration No'>"+str(a[2])+"   "+"</td><td data-label='Date Of Issue'>"+str(a[1])+"   "+"</td><td data-label='Student Name'>"+str(a[4])+"   "+"</td><td data-label='Father's Name'>"+str(a[5])+"   "+"</td><td data-label='Course' contenteditable='true' id='e'>"+str(a[3])+"   "+"</td><td data-label='Starting Date' contenteditable='true' id='e'>"+str(a[6])+"   "+"</td><td data-label='Ending Date' contenteditable='true' id='e'>"+str(a[7])+"   "+"</td><td data-label='Study Centre'>"+str(a[8])+"   "+"</td><td data-label='Student Pic'><img src='"+b+"' alt='Student Pic' style='height: 5rem;width: 5rem;'></td><td data-label='Update'><i class='fa' id='upd' data-toggle='tooltip' title='Update'>&#xf044;</i></td><td data-label='Cancel'><i class='fa' id='del' data-toggle='tooltip' title='Cancel'>&#10006;</i></td><td data-label='Certificate'><i class='fa' id='cert' data-toggle='tooltip' title='Certificate'>&#xf15c;</i></td><td data-label='Marksheet'><i class='fa' id='mark' data-toggle='tooltip' title='Marksheet'>&#xf15b;</i></td></tr>")
            print('</table></div>')
    elif d=='upd_cert':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6')
        t.execute('update certificate set cer_date="'+d2+'",course="'+d3+'",cstart="'+d4+'",cend="'+d5+'" where cref_no="'+d1+'" and bcode="'+d6+'"')
        con.commit()
        print('Successfully Updated This Record!')
    elif d=='del_cert':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        t.execute('update certificate set cancel=1 where cref_no="'+d1+'" and bcode="'+d2+'"')
        con.commit()
        print('Successfully Cancelled This Record!,,,10')
    ###################Marksheet##############
    elif d=='mark_reg':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        t.execute('select reg_no,sname,fname,course,cstart,cend,study_c from certificate where cref_no="'+d1+'"')
        rs=t.fetchall()
        if(rs!=[]):
            for a in rs:
                aa=0
                for i in a:
                    aa=aa+1
                    if(aa==5 or aa==6):
                        k=datetime.strptime(str(i), '%Y-%m-%d').strftime('%d %b %Y')
                    else:
                        k=str(i)
                    print(k+"&&&&")
            t.execute('select mod_name,mod_desc from course where cname="'+rs[0][3]+'" and bcode="'+d2+'"')
            rs=t.fetchall()
            print(rs[0])
        else:
            print('0')
            
# print(datetime.strptime('2023-07-22', '%Y-%m-%d').strftime('%d %b %Y'))
    #############Course Details###################
    elif(d=='ins_course'):
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
        t.execute("select * from course where cid='"+d1+"'")
        if(t.fetchall()==[]):
            url="insert into course values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            t.execute(url,(d1,d2,d3,d4,d5,d6,d7,d8,d9))
            t.execute("update branch_details set cid="+d10+" where bcode='"+d8+"'")
            con.commit()
            print("Course Created Successfully!,,,10")
        else:
            print("Already Record Inserted!")
    elif(d=='cmb_course'):
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        t.execute("select distinct "+d1+" from course  where bcode='"+d2+"'")
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
        d3=f.getvalue('t3')
        if(d1=='cname'):
            url="select * from course where cname='"+d2+"' and bcode='"+d3+"'"
        elif(d1=='cid'):
            url="select * from course where cid='"+d2+"' and bcode='"+d3+"'"
        else:
            url="select * from course where bcode='"+d3+"'"
        t.execute(url)
        rs=t.fetchall()
        if rs==[]:
            print(0)
        else:
            i=0
            print('<div id="d5"><table id="table3"><tr><th id="sn">Sn</th><th>Course ID</th><th>Course Name</th><th>Module Name</th><th>Module Disc.</th><th>Course Dur.</th><th>Course Fee</th><th>One Time Payment(OTP)</th><th colspan="2" style="color:blue;" id="act">Action Here</th></tr>')
            for a in rs:
                i=i+1
                print('<tr class="tr1"><td id="sn" data-label="SN">'+str(i)+'   '+'</td><td data-label="Course ID">'+str(a[0])+'   '+'</td><td data-label="Course Name" contenteditable="true" id="e">'+str(a[1])+'   '+'</td><td data-label="Module Name">'+str(a[2])+'   '+'</td><td data-label="Module Disc.">'+str(a[3])+'   '+'</td><td data-label="Course Dur." contenteditable="true" id="e">'+str(a[5])+'   '+'</td><td data-label="Course Fee" contenteditable="true" id="e">'+str(a[4])+'   '+'</td><td data-label="One Time Payment(OTP)" contenteditable="true" id="e">'+str(a[6])+'   '+'</td><td data-label="Update"><i class="fa" id="upd" data-toggle="tooltip" title="Update">&#xf044;</i></td><td data-label="Delete"><i class="fa" id="del" data-toggle="tooltip" title="Delete">&#xf014;</i></td></tr>')
            print('</table></div>')
    elif d=='upd_course':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6')
        d7=f.getvalue('t7')
        d8=f.getvalue('t8')
        t.execute('update course set cname="'+d2+'",mod_name="'+d3+'",mod_desc="'+d4+'",cdur="'+d5+'",cfee="'+d6+'",otp="'+d7+'" where cid="'+d1+'" and bcode="'+d8+'"')
        con.commit()
        print('Successfully Updated!')
    elif d=='del_course':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        t.execute('delete from course where cid="'+d1+'" and bcode="'+d2+'"')
        con.commit()
        print('Successfully Deleted!,,,10')
    elif d=='certgen':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        t.execute('select gender from registration where reg_no="'+d1+'"')
        print(t.fetchall()[0][0]+"&&&")
        print(datetime.strptime(d2, '%Y-%m-%d').strftime('%d %b, %Y')+"&&&")
        print(datetime.strptime(d3, '%Y-%m-%d').strftime('%d %b, %Y'))
    else:
        d1=f.getvalue('t1')
        t.execute("select cid from branch_details where bcode='"+d1+"'")
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
        print(str,cid,sep=",,,")
except Exception as e:
    print("Unsuccesss",e)
finally:
    if con.is_connected:
        con.close()
        t.close()
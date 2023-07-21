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
        adm_ch=rs[0][1]
        year=date.today().year%100
        t.execute('select max(adm_no) from admission')
        # rs=t.fetchall()
        if(t.fetchall()[0][0]!=None):
            yr=t.fetchall()[0][0][0:2]
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
        t.execute("select * from admission where adm_no='"+d1+"'")
        if(t.fetchall()==[]):
            url="insert into admission values(%s,%s,%s,%s,%s,%s,%s,%s)"
            t.execute(url,(d1,d2,d3,d4,d5,d6,d7,d8))
            t.execute("update branch_details set adm_no="+d9+",adm_ch='"+d10+"' where bcode='"+d7+"'")
            con.commit()
            print("Successfully Inserted Record!,,,10")
        else:
            print("Already Inserted Record for this Registration ID!")
    elif d=='ser_adm':
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
        t.execute('update admission set reg_date="'+d2+'",sname="'+d3+'",fname="'+d4+'",mname="'+d5+'",sdob="'+d6+'",email="'+d7+'",cont_no="'+d8+'",prog="'+d9+'",blood_grp="'+d10+'",clg_name="'+d11+'",gender="'+d12+'",prmt_add="'+d13+'",dis="'+d14+'",stt="'+d15+'",sphoto="'+d16+'",aadhaar="'+d17+'",cor_add="'+d18+'" where reg_no="'+d1+'" ')
        con.commit()
        print('Successfully Updated This Record!')
    elif d=='del_adm':
        d1=f.getvalue('t1')
        t.execute('delete from admission where adm_no="'+d1+'"')
        con.commit()
        print('Successfully Deleted This Record!,,,10')
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
            url="insert into internship values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            t.execute(url,(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d20,d21))
            t.execute("update automatic set int_no="+d19+",int_ch='"+d18+"'")
            con.commit()
            print("Successfully Inserted Record!,,,10")
        else:
            print("Already Inserted Record for this Intern ID!")
    #############Course Details###################
    elif(d=='ins_course'):
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6')
        d7=f.getvalue('t7')
        t.execute("select * from course where cid='"+d1+"'")
        if(t.fetchall()==[]):
            url="insert into course values(%s,%s,%s,%s,%s,%s)"
            t.execute(url,(d1,d2,d3,d4,d5,d6))
            t.execute("update automatic set cid="+d7+"")
            con.commit()
            print("Course Created Successfully!,,,10")
        else:
            print("Something Wrong,Try Again!")
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
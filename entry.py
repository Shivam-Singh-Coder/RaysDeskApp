#! C:\Users\HP\AppData\Local\Programs\Python\Python311\python.exe
print('contact-type:text/html\r\n\r\n')
import cgi
import datetime
import mysql.connector
con=mysql.connector.connect(host='localhost', user='webrays', passwd='rayssoft',database='webrays')
t=con.cursor()
f=cgi.FieldStorage()
try:
    d=f.getvalue('cond')
    if d=='ent':
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
        t.execute('select * from branch_details where bcode="'+d1+'"')
        if(t.fetchall()==[]):
            url='insert into  branch_details (bcode,date,bname,bcont_pr,email,phno,addr,state1,dist,reg_no,adm_no,adm_ch,cid,rec_no,cancel) value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            t.execute(url,(d1,d2,d3,d4,d5,d6,d7,d8,d9,0,0,0,0,0,0))
            if(d12.strip()==d1.strip()):
                t.execute('update state set '+d11+'='+d10+'')
            con.commit()
            print('entry success,,,,10')
        else:
            print('Already Record Available for this Branch Code!!')   
    elif(d=='cmb'):
        t.execute('select distinct bcode,bname,state1,dist from branch_details')
        rs=t.fetchall()
        bn=set()
        stat=set()
        dist=set()
        if(rs!=[]):
            print('<option selected disabled>----Select Any Branch Code----</option>')
            for a in rs:
                print('<option>'+str(a[0])+'</option>')
                bn.add(a[1])
                stat.add(a[2])
                dist.add(a[3])
            print('&&&&')
            print('<option selected disabled>----Select Any Branch Name----</option>')
            for a in bn:
                print('<option>'+str(a)+'</option>')
            print('&&&&')
            print('<option selected disabled>----Select Any State----</option>')
            for a in stat:
                print('<option>'+str(a)+'</option>')
            print('&&&&')
            print('<option selected disabled>----Select Any District----</option>')
            for a in dist:
                print('<option>'+str(a)+'</option>')
        else:
            print(0)
    
# ============================================search=======================================================
    elif d=='search':
        s1=f.getvalue('s1')
        s2=f.getvalue('s2')
        s3=f.getvalue('s3')
        s4=f.getvalue('s4')
        url='select * from branch_details where'
        if(s1!=None):
            url=url+" bcode='"+s1+"'"
        if(s2!=None and s1!=None):
            url=url+" and bname='"+s2+"'"
        if(s2!=None and s1==None):
            url=url+" bname='"+s2+"'"
        if (s3!=None and (s1!=None or s2!=None)):
            url=url+" and state1='"+s3+"'"
        if(s3!=None and s1==None and s2==None):
            url=url+" state1='"+s3+"'"
        if (s4!=None and (s1!=None or s2!=None or s3!=None)):
            url=url+" and dist='"+s4+"'"
        if(s4!=None and s1==None and s2==None and s3==None):
            url=url+" dist='"+s4+"'"
        url=url+' order by sn desc'
        t.execute(url)
        r=t.fetchall()
        if(r!=[]):
            num=0
            print('<table id="table3"><tr><th>Sn</th><th>Branch Code</th><th>Branch Name</th><th>Contact Person</th><th>Email</th><th>Phone No.</th><th>Address</th><th>State</th><th>District</th><th colspan="2" id="chk">Check</th></tr><tbody>')
            for i in r:
                num=num+1
                if(i[15]==0):
                    print('<tr><td data-label="Serial No.">'+str(num)+'  '+'</td><td data-label="Branch Code">'+str(i[1])+'  '+'</td><td data-label="Branch Name" contenteditable="true" id="x">'+str(i[3])+'  '+'</td><td data-label="Contact Person" contenteditable="true" id="x">'+str(i[4])+'  '+'</td><td data-label="Email" contenteditable="true" id="x">'+str(i[5])+'  '+'</td><td data-label="Pho_No" contenteditable="true" id="x">'+str(i[6])+'  '+'</td><td data-label="Address" contenteditable="true" id="x">'+str(i[7])+'  '+'</td><td data-label="State">'+str(i[8])+'  '+'</td><td data-label="District">'+str(i[9])+'  '+'</td><td data-label="Update"><i class="fa" id="upd" data-toggle="tooltip" title="Update">&#xf044;</i></td><td data-label="Cancel"><i class="fa" id="del" data-toggle="tooltip" title="Cancel">&#10006;</i></td></tr>')
                else:
                    print('kkkkkk')
                    print('<tr style="background:red;color:white;"><td data-label="Serial No.">'+str(num)+'  '+'</td><td data-label="Branch Code">'+str(i[1])+'  '+'</td><td data-label="Branch Name" id="x">'+str(i[3])+'  '+'</td><td data-label="Contact Person" id="x">'+str(i[4])+'  '+'</td><td data-label="Email" id="x">'+str(i[5])+'  '+'</td><td data-label="Pho_No" id="x">'+str(i[6])+'  '+'</td><td data-label="Address" id="x">'+str(i[7])+'  '+'</td><td data-label="State">'+str(i[8])+'  '+'</td><td data-label="District">'+str(i[9])+'  '+'</td><td data-label="Update"><i class="fa" data-toggle="tooltip" title="Update">&#xf044;</i></td><td data-label="Cancel"><i class="fa" data-toggle="tooltip" title="Cancel" style="color:white;">&#10006;</i></td></tr>')
            print('</tbody></table>')
        else:
            print('<table id="table3" style="font-size:2rem;font-weight:bold;background:pink;border-radius:1rem;"><tr><td align="center" style="border:none;">No Record Found!!</td></tr></table>')
# ======================================update=================================================================
    elif d=='update':
        d1=f.getvalue('s1')
        d2=f.getvalue('s2')
        d3=f.getvalue('s3')
        d4=f.getvalue('s4')
        d5=f.getvalue('s5')
        d6=f.getvalue('s6')
        d7=f.getvalue('s7')
        d8=f.getvalue('s8')
        url=("update  branch_details set  bname='"+str(d2)+"',bcont_pr='"+str(d3)+"',email='"+str(d4)+"',phno='"+str(d5)+"',addr='"+str(d6)+"',state1='"+str(d7)+"',dist='"+str(d8)+"' where bcode='"+d1+"'")
        t.execute(url)
        con.commit()
        print('Successfully Update!')
# -------------------------------------------delete for work in branch_details-------------------------------------------------------
    elif d=='delete':
        b=f.getvalue('s1')
        t.execute("update branch_details set cancel=1 where bcode='"+b+"'")
        con.commit()
        print("Successfully Cancel!&&&10")
    elif(d=='district'):
        t1=f.getvalue('t1')
        t.execute("select distr from state1 where stat='"+t1+"'")    
        rs=t.fetchall()
        if(rs!=[]):
            print('<option value="null" selected disabled>----------------Select Any District-----------------</option>')
            for a in rs:
                for i in a:
                    for b in i.split(','):
                        print('<option>'+b+'</option>')
        else:
            print("Invalid Choice!")
    elif(d=='auto_id'):
        t1=f.getvalue('t1')
        t.execute('select '+t1+' from state')
        rs=t.fetchall()
        if(rs!=[]):
            rs=rs[0][0]+1
            if(rs<10):
                print(t1.upper()+'0'+str(rs)+',,,,'+str(rs))
            elif(rs<100):
                print(t1.upper()+str(rs)+',,,,'+str(rs))
            else:
                print("End Auto!")
        else:
            print('Invalid Choice!')  
    elif d=='dash':
        t.execute('select count(recpt_no) from money_receipt')
        r1=t.fetchall()
        t.execute('select count(adm_no) from admission')
        r2=t.fetchall()
        t.execute('select count(reg_no)  from registration')
        r3=t.fetchall()
        t.execute('select count(reg_no) from book_details')
        r4=t.fetchall()
        t.execute('select count(bcode) from branch_details')
        r5=t.fetchall()
        t.execute('select count(cid) from course')
        r6=t.fetchall()
        t.execute('select count(dues_amt) from money_receipt where aform_no in (select distinct aform_no from money_receipt) and dues_amt!="0" order by recpt_no desc')
        r8=t.fetchall()
        print(r1[0][0],r2[0][0],r3[0][0],r4[0][0],r5[0][0],r6[0][0],r8[0][0],sep=',,,,,')   
    elif d=='option':
        url='select bcode,bname from branch_details'
        t.execute(url)
        print('<option selected disabled>----Select Any Branch----</option>')
        rs=t.fetchall()
        for a in rs:
            print('<option>'+a[0]+"-"+a[1]+'</option>')
    elif(d=='table'):
        d1=f.getvalue('t1')
        if(d1=='inactive'):
            t.execute('select * from signup where stat="Inactive" order by sn desc')
        else:
            t.execute('select * from signup order by sn desc')
        rs=t.fetchall()
        if(rs==[]):
            print(0)
        else:
            num=0
            t.execute('select bcode,bname from branch_details')
            rs1=t.fetchall()
            print('<table id="table3"><thead><tr><th>Sn</th><th>Username</th><th>User Id</th><th>Password</th><th>Security Question</th><th>Answer</th><th>Role</th><th>Status</th><th>Branch Name</th><th colspan="2" id="chk">Check</th></tr></thead><tbody id="myTable">')
            for a in rs:
                num=num+1
                bcode='<select id="bcode" style="text-align:center;outline: none; border: none; background: none;"><option selected disabled>----Select Any Branch----</option>'
                if(rs1!=[]):
                    for b in rs1:
                        if(str(a[8]).strip()==str(b[0]).strip()):
                            bcode=bcode+'<option selected value="'+b[0]+'">'+b[0]+'-'+b[1]+'</option>'
                        else:
                            bcode=bcode+'<option value="'+b[0]+'">'+b[0]+'-'+b[1]+'</option>'
                bcode=bcode+'</select>'
                if a[1].strip()=='Super Admin':
                    rol='<select id="role" style="text-align:center;outline: none; border: none; background: none;"><option selected>Super Admin</option><option>Admin</option><option>User</option></select>'
                elif a[1].strip()=='Admin':
                    rol='<select id="role" style="text-align:center;outline: none; border: none; background: none;"><option>Super Admin</option><option selected>Admin</option><option>User</option></select>'
                else:
                    rol='<select id="role" style="text-align:center;outline: none; border: none; background: none;"><option>Super Admin</option><option>Admin</option><option selected>User</option></select>'
               
                if(a[7].strip()=='Inactive'):
                    stat='<select id="stat" style="text-align:center;outline: none; border: none;background: none;"><option>Active</option><option selected>Inactive</option></select>'
                else:
                    stat='<select id="stat" style="text-align:center;outline: none; border: none;background: none;"><option selected>Active</option><option>Inactive</option></select>'
                print('<tr><td>'+str(num)+"  "+'</td><td data-label="username">'+str(a[2])+"  "+'</td><td data-label="user_id">'+str(a[3])+"  "+'</td><td data-label="Password">'+str(a[6])+"  "+'</td><td data-label="Security">'+str(a[4])+"  "+'</td><td data-label="Question">'+str(a[5])+"  "+'</td><td data-label="Role" readonly>'+rol+'  '+'</td><td data-label="status" readonly>'+stat+"  "+'</td><td data-label="bcode" readonly>'+bcode+"  "+'</td><td data-label="Update" style="color:blue; cursor:pointer;"><i class="fa" id="upd" data-toggle="tooltip" title="Update">&#xf044;</i></td><td data-label="Delete" style="color: red; cursor:pointer;"><i class="fa" id="del" data-toggle="tooltip" title="Cancel">&#10006;</i></td></tr>')
            print('</tbody></table>')
    elif d=='del_table':
         b1=f.getvalue('b1')
         t.execute("update signup set cancel=1 where u_id='"+str(b1)+"'")
         con.commit()
         print("successfully delete!")
    elif d=='update_table':
        d1=f.getvalue('s1')
        d2=f.getvalue('s2')
        d3=f.getvalue('s3')
        d4=f.getvalue('s4')
        url=('update signup set stat="'+d2+'", role="'+d3+'", bcode="'+d4+'" where u_id="'+d1+'"')
        t.execute(url)
        con.commit()
        print('Successfully Update!')
# ---------------------------------personal deatails works------------------------------
    elif d=='entry':
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
        t.execute('select * from profile_details where u_id="'+d1+'"')
        rs=t.fetchall()
        if(rs!=[]):
            t.execute('update profile_details set email="'+d2+'", cont_no="'+d3+'", dob="'+d4+'", gender="'+d5+'", state="'+d6+'", dist="'+d7+'", pin_code="'+d8+'", location="'+d9+'", about_yourself="'+d10+'",pic="'+d11+'" where u_id="'+d1+'" ')
            con.commit()
        else:
            url='insert into profile_details(u_id,email,cont_no,dob,gender,state,dist,pin_code,location,about_yourself,pic) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            t.execute(url,(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11))
            con.commit()
        print('Successfully Updated!&&&&10')
    elif d=='profilrun':
        d1=f.getvalue('t1')
        t.execute('select * from profile_details where u_id="'+d1+'"') 
        rs=t.fetchall()
        if(rs!=[]):
            for a in rs:
                for i in a:
                    print(str(i)+'&&')
        else:
            print(0)
except Exception as e:
    print('unsucesses',e) 
finally:
    if con.is_connected:
        con.close()
        t.close()
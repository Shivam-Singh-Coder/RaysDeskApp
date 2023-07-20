#! C:\Users\HP\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector
con=mysql.connector.connect(host='localhost', user='rays_desk', passwd='rays_desk',database='rays_desk')

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
        url='insert into  branch_details (bcode,date,bname,bcont_pr,email,phno,addr,state1,dist,reg_no,adm_no,cid,receipt_no,u_id) value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        t.execute(url,(d1,d2,d3,d4,d5,d6,d7,d8,d9,0,0,0,0,'Raj_02'))
        t.execute('update state set '+d11+'='+d10+'')
        # print(url)
        con.commit()
        print('entry success,,,,10')     
    elif(d=='cmb'):
        d1=f.getvalue('t1')
        print('<select id="s" class="s2">')
        if(d1=='br'):
            url='select distinct bcode from branch_details'
            print('<option selected disabled>----Select Branch Code----</option>')
        elif(d1=='st'):
            url='select distinct state1 from branch_details'
            print('<option selected disabled>----Select State----</option>')
        elif(d1=='dt'):
            url='select distinct dist from branch_details'
            print('<option selected disabled>----Select District----</option>')
        t.execute(url)
        rs=t.fetchall()
        if(rs!=[]):
            for a in rs:
                print('<option>'+str(a[0])+'</option>')
            print('</select>')
            # ============================================search=======================================================
    elif d=='search':
        t.execute('select * from branch_details order by sn desc')
        r=t.fetchall()
        print('<table id="table3"><tr><th id="sn">Sn</th><th>Branch code</th><th>Branch name</th><th>branch contact person</th><th>Email</th><th>Phone no</th><th>Address</th><th>State</th><th>District</th><th colspan="2" id="chk">Check</th><th id="sn"></th></tr>')
        for i in r:
            print('<tr><td id="sn"> '+str(i[0])+'  '+'</td><td data-label="bc" contenteditable="true">'+str(i[1])+'  '+'</td><td data-label="bn" contenteditable="true">'+str(i[3])+'  '+'</td><td data-label="bc_p" contenteditable="true">'+str(i[4])+'  '+'</td><td data-label="email" contenteditable="true">'+str(i[5])+'  '+'</td><td data-label="pho_no" contenteditable="true">'+str(i[6])+'  '+'</td><td data-label="Addr" contenteditable="true">'+str(i[7])+'  '+'</td><td data-label="st" contenteditable="true">'+str(i[8])+'  '+'</td><td data-label="dist" contenteditable="true" id="e">'+str(i[9])+'  '+'</td><td class="sn"></td><td data-label="Update"><i class="fa" id="upd" data-toggle="tooltip" title="Update">&#xf044;</i></td><td data-label="Delete"><i class="fa" id="del" data-toggle="tooltip" title="Delete">&#xf014;</i></td></tr>')
        print('</table>') 
        # ======================================update=================================================================
    elif d=='update':
        d1=f.getvalue('s1')
        d3=f.getvalue('s3')
        d4=f.getvalue('s4')
        d5=f.getvalue('s5')
        d6=f.getvalue('s6')
        d7=f.getvalue('s7')
        d8=f.getvalue('s8')
        d9=f.getvalue('s9')
        url=("update  branch_details set  bname='"+str(d3)+"',bcont_pr='"+str(d4)+"',email='"+str(d5)+"',phno='"+str(d6)+"',addr='"+str(d7)+"',state1='"+str(d8)+"',dist='"+str(d9)+"' where sn="+d1+"")
        t.execute(url)
        con.commit()
        print('Successfully Update!')
        # -------------------------------------------delete-------------------------------------------------------
    elif d=='delete':
        b=f.getvalue('s1')
        # print(b)
        t.execute("delete from branch_details where sn='"+b+"'")
        con.commit()
        print("successfully delete!")
    # Auto generate
    
    # elif d=='auto_search':
    #     url=('select b_id from auto')
    #     t.execute(url)
    #     rs=t.fetchall()
    #     inv=rs[0][0]+1
    #     if(inv<10):
    #         print('B00'+str(inv)+",,,,"+str(inv))
    #     elif(inv<100):
    #         print('B0'+str(inv)+",,,,"+str(inv))
    #     elif(inv<1000):
    #         print('B'+str(inv)+",,,,"+str(inv))
    #     else:
    #         print("End auto")
    elif(d=='district'):
        t1=f.getvalue('t1')
        t.execute("select distr from state1 where stat='"+t1+"'")    
        rs=t.fetchall()
        if(rs!=[]):
            print('<option value="null" selected disabled>----------------Select District-----------------</option>')
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
except Exception as e:
    
    print('unsucesses',e) 
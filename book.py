#! C:\\Users\\sunny\\AppData\\Local\Programs\\Python\\Python311\\python.exe
print('content-type:text/html\r\n\r\n')
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="rays_desk",password="rays_desk",database="rays_desk")
t=con.cursor()
f=cgi.FieldStorage()
try:
    d=f.getvalue('t')
    if d=='ent':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6')
        d7=f.getvalue('t7')
        url='insert into book_details (reg_no,sname,bname,aname,pname, issue_dt,subm_dt) values(%s,%s,%s,%s,%s,%s,%s)'
        # print(url)
        t.execute(url,(d1,d2,d3,d4,d5,d6,d7))
        con.commit()

        print('entry succes')
    elif d=='match':
        g1=f.getvalue('s1')
        t.execute('select sname from book_details where reg_no=\''+str(g1)+'\'')
        res=t.fetchall()
        if res!=[]:
          print(res[0][0])
        else:
            print(0)
    elif d=='search':
        g1=f.getvalue('t1')
        g2=f.getvalue('t2')
        ur='select * from book_details where '
        if g1=='reg_no':
            ur=ur+'reg_no=\''+str(g2)+'\''
        elif g1=='subm_dt':
            ur=ur+'subm_dt=\''+str(g2)+'\''
            # print(ur)
        elif g1=='issue_dt':
            ur=ur+'issue_dt=\''+str(g2)+'\''
        t.execute(ur)
        res=t.fetchall()
        # print(res)
        if res==[]:
          print(0)
        else:
           print('<table id="table3"><tr><th id="sn">Sn</th><th>Registration no</th><th>Student_name</th><th>Book_Number</th><th>AuthorName</th><th>Publication_Name</th><th>Issue_Name</th><th>Submission_Date</th><th>RECEIVE</th><th>BCODE</th><th colspan="2">Check</th></tr>')
        for a in res:
            print(' <tr><td id="sn"></td><td data-label="Registration no">'+str(a[0])+'  '+'</td><td data-label="Student_name"contenteditable="true">'+str(a[1])+'  '+'</td><td id="e" data-label="Book_Number"contenteditable="true">'+str(a[2])+'  '+'</td><td id="e"  data-label="AuthorName" contenteditable="true">'+str(a[3])+'  '+'</td><td id="e"  data-label="Publication_Name" contenteditable="true">'+str(a[4])+'  '+'</td><td id="e"  data-label="Issue_Date" ><input id="e"  type="date" id="da1" value="'+str(a[5])+'">'+'  '+'</td> <td data-label="Submission_Date"><input id="e"  type="date" id="da2" value="'+str(a[6])+'">'+'  '+'</td> <td data-label="RECEIVE"  ><select id="box1" ><option>'+str(a[7])+'</option><option >No</option></select >'+'  '+'</td><td data-label="BCODE"  id="e">'+str(a[8])+'  '+'</td><td data-label="Update"><i class="fa" id="upd" data-toggle="tooltip"title="Update">&#xf044;</i></td><td data-label="Delete"><i class="fa" id="del" data-toggle="tooltip"title="Delete">&#xf014;</i></td><td class="sn"></td></tr>')
        print('</table>')
    elif d=='delete':
        # print('uyg')
        b=f.getvalue('s1')
        # print(b)
        t.execute("delete from book_details where reg_no='"+b+"'")
        con.commit()
        print("successfully delete!")

    elif d=='update':
        d1=f.getvalue('s1')
        d2=f.getvalue('s2')
        d3=f.getvalue('s3')
        d4=f.getvalue('s4')
        d5=f.getvalue('s5')
        d6=f.getvalue('s6')
        d7=f.getvalue('s7')
        d8=f.getvalue('s8')
        d9=f.getvalue('s9')
        # print(d1,d2,d3,d4,d5,d6,d7,d8,d9,sep=',,,')
        # # print('ghvj')
      
        url=("update book_details set sname='"+str(d2)+"',bname='"+str(d3)+"',aname='"+str(d4)+"',pname='"+str(d5)+"',issue_dt='"+str(d6)+"',subm_dt='"+str(d7)+"',receice='"+str(d8)+"',bcode='"+str(d9)+"'where reg_no='"+str(d1)+"'")
        # print(url)
        t.execute(url)
        con.commit()
        print('Successfully Update!')
except Exception as e:
    print('unsucesses',e) 
  
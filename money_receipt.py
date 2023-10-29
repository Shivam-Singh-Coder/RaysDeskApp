#! C:\Users\HP\AppData\Local\Programs\Python\Python311\python.exe
print('contact-type:text/html\r\n\r\n')
import cgi
import mysql.connector
con=mysql.connector.connect(host='localhost', user='webrays', passwd='rayssoft',database='webrays')
t=con.cursor()
f=cgi.FieldStorage()
d=f.getvalue('k')
try:
    if d=='abcd':
        d1=f.getvalue('k1')
        d2=f.getvalue('k2') 
        d3=f.getvalue('k3')
        d4=f.getvalue('k4')
        d5=f.getvalue('k5')
        d6=f.getvalue('k6')
        d7=f.getvalue('k7')
        d8=f.getvalue('k8')
        d9=f.getvalue('k9')
        d10=f.getvalue('k10')
        url='insert into money_receipt(recpt_no,rdate,aform_no,cash,upi,cheque,dd,dues_amt,ins_date,rec_from) value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        t.execute(url,(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10))
        con.commit()
        print('Submit success')
  # ================search==========================
    elif d=='search':
        k1=f.getvalue('s1')
        k2=f.getvalue('s2')
        url="select * from money_receipt where "
        if k2!=None:
            url=url+" "+k1+"='"+k2+"'"
        t.execute(url)
        r=t.fetchall()
        if r!=[]:
            print('<table id="table3"><tr><th>Recpt_no</th><th>Rdate</th><th>AForm_no</th><th>Cas</th><th>Upi</th><th>Cheque</th><th>DD</th><th>Dues_Amt</th><th>Ins_Date</th><th>Rec_Form</th><th colspan="3">select</th></tr>')
            for a in r:
                print('<tr><td data-label="recpt_no">'+str(a[0])+'   '+'</td><td data-label="rdate">'+str(a[1])+'   '+'</td><td data-label="aform_no">'+str(a[2])+'   '+'</td><td data-label="cash" contenteditable="true" id="e">'+str(a[3])+'   '+'</td><td data-label="upi" contenteditable="true">'+str(a[4])+'   '+'</td><td data-label="cheque" contenteditable="true">'+str(a[5])+'   '+'</td><td data-label="dd" contenteditable="true">'+str(a[6])+'   '+'</td><td data-label="dues_amt" id="e">'+str(a[7])+'   '+'</td><td data-label="Amt"ins_date contenteditable="true">'+str(a[8])+'   '+'</td><td data-label="rec_form"contenteditable="true" id="e">'+str(a[9])+'   '+'</td><td><i class="fa" id="upd" data-toggle="tooltip"title="Update">&#xf044;</i></td><td><i class="fa" id="del" data-toggle="tooltip"title="Delete">&#xf014;</i></td><td data-label="Print"><i class="fa" id="prt" data-toggle="tooltip" title="Print"onclick="window.print()">&#xf02f;</i></td></tr>')
            print('</table>')
        else:
            print(0)
        
        # ===========================del=====================     
    elif d=='delete':
        b=f.getvalue('s1')
        print(b)
        t.execute("delete from money_receipt where recpt_no='"+str(b)+"'")
        con.commit()
        print("successfully delete!")    
        # ==========================update====================
    elif d=='update':
        d1=f.getvalue('s2')
        d2=f.getvalue('s3')
        d3=f.getvalue('s4')
        d4=f.getvalue('s5')
        d5=f.getvalue('s6')
        d6=f.getvalue('s7')
        d7=f.getvalue('s8')
        d8=f.getvalue('s9')
        d9=f.getvalue('s10')
        d10=f.getvalue('s11')
        # print(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10, sep=',')
        t.execute("update money_receipt set recpt_no='"+str(d1)+"',rdate='"+str(d2)+"',aform_no='"+str(d3)+"',cash='"+str(d4)+"',upi='"+str(d5)+"',cheque='"+str(d6)+"',dd='"+str(d7)+"',dues_amt='"+str(d8)+"',ins_date='"+str(d9)+"',rec_from='"+str(d10)+"' where recpt_no='"+str(d1)+"'")
        con.commit()
        print('Update successfully!')
except Exception as e:
    print('Uncess',e)
# ==========================auto===============
import datetime
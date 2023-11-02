#! C:\Users\HP\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector
con=mysql.connector.connect(host='localhost', user='webrays', passwd='rayssoft',database='webrays')
x=con.cursor()
f=cgi.FieldStorage()
try:
    jk=f.getvalue('cond')
    if(jk=='inst'):
        q2=f.getvalue('b1')
        q3=f.getvalue('b2')
        q6=f.getvalue('b5')
        q4=f.getvalue('b3')
        q5=f.getvalue('b4')
        url="insert into blogs(headline,msg,image,author,pub_date) values(%s,%s,%s,%s,%s)"
        x.execute(url,(q2,q3,q6,q4,q5))
        con.commit()
        print("Successfully Inserted"+",,,10")
    elif(jk=='inst_car'):
        q1=f.getvalue('d1')
        q2=f.getvalue('d2')
        q3=f.getvalue('d3')
        q4=f.getvalue('d4')
        q5=f.getvalue('d5')
        q6=f.getvalue('d6')
        q7=f.getvalue('d7')
        q8=f.getvalue('d8')
        url="insert into rays_carear(position,skil,mode,exp,vacency,clo_data,place,sal) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        x.execute(url,(q1,q2,q3,q4,q5,q6,q7,q8))
        con.commit()
        print("Successfully Inserted"+",,,10")
    elif(jk=='inst_vid'):
        q2=f.getvalue('d1')
        q3=f.getvalue('d2')
        url="insert into video_details(topic,url) values(%s,%s)"
        x.execute(url,(q2,q3))
        con.commit()
        print("Successfully Inserted"+",,,10")
    elif(jk=='combo'):
        x.execute("select distinct headline from blogs")
        rs=x.fetchall()
        if(rs!=[]):
            for a in rs:
                print("<option>"+a[0]+"</option>")
    elif(jk=='combo_vid'):
        x.execute("select distinct topic from video_details")
        rs=x.fetchall()
        if(rs!=[]):
            for a in rs:
                print("<option>"+a[0]+"</option>")
    elif(jk=='combo_vidser'):
        x.execute("select distinct topic from video_details")
        rs=x.fetchall()
        if(rs!=[]):
            for a in rs:
                print("<option>"+a[0]+"</option>")
            print(',,,&&@@')
        x.execute("select distinct url from video_details")
        rs=x.fetchall()
        if(rs!=[]):
            for a in rs:
                print("<option>"+a[0]+"</option>")
    elif(jk=='search'):
        opt=f.getvalue('t2')
        val=f.getvalue('t3')
        if(opt=='Blogs Topic'):
            url="select * from blogs where headline='%s'"%(val)
        elif(opt=='Publication Date'):
            url="select * from blogs where pub_date='%s'"%(val)
        x.execute(url)
        rs=x.fetchall()
        if(rs!=[]):
            for a in rs:
                if(a[3]==None):
                    b=''
                else:
                    b=a[3].decode()
                print("<tr class='tab_r'><td class='tab_c'>"+a[1]+"  "+"</td><td class='tab_c'><textarea style='resize: none;border: none;width:10rem;height:2.5rem;' id='desc' readonly >"+str(a[2])+"  "+"</textarea></td><td class='tab_c'><img class='img' alt='No Pic Available' style='width:4rem;height:2rem;' id='img1' src="+b+"></td><td class='tab_c'><input class='upld' type='file' accept='image/png, image/jpeg' value='' style='width:16rem;'></td><td class='tab_c z' contenteditable='true'>"+str(a[4])+"  "+"</td><td class='tab_c'><input class='dtt' type='date' value="+str(a[5])+"></td><td class='tab_c'><input class='rad' type='radio' name='rad'></td></tr>""")
        else:
            a=0
            print(a)
    elif jk=='search_vid':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        url='select * from video_details'
        if(d1!='op' and d2!='op1'):
            url=url+" where topic='"+d1+"' and url='"+d2+"'"
        elif(d1!='dn' and d2=='op1'):
            url=url+" where topic='"+d1+"'"
        elif(d2!=None and d1=='op'):
            url=url+" where url='"+d2+"'"     
        x.execute(url)
        rs=x.fetchall()
        if(rs!=[]):
            print('<div id="t21"><input type="button" value="Update" id="b4" class="b1"><input type="button" value="Delete" id="b5" class="b1"></div><div id="t22"><br>')
            print('<table id="t2"><thead><tr><th hidden>SN</th><th>Topic</th><th>Url</th><th id="th1">Check</th></tr></thead>')
            for i in rs:
                print('<tr><td hidden>'+str(i[0])+'   '+'</td><td id="e" contenteditable="true">'+i[1]+'   '+'</td><td id="e" contenteditable="true">'+i[2]+'   '+'</td><td id="th1"><input type="radio" name="a" id="r"></td></tr>')
            print('</table></div>')
            print(',,,')
        else:
            print("No Record Found!"+',,,'+'10')
    elif(jk=='update'):
        q=f.getvalue('t1')
        w=f.getvalue('t2')
        e=str(f.getvalue('t3'))
        r=f.getvalue('t4')
        a=f.getvalue('t5')
        url="update blogs set image='"+e+"',author='"+r+"',pub_date='"+a+"' where headline='"+q+"' and msg='"+w+"'"
        x.execute(url)
        con.commit()
        print("Successfully Updated!")
    elif(jk=='update_vid'):
        q=f.getvalue('t1')
        w=f.getvalue('t2')
        e=f.getvalue('t3')
        url="update video_details set topic='"+w+"',url='"+e+"' where sn='"+q+"'"
        x.execute(url)
        con.commit()
        print("Successfully Updated!")
    elif(jk=='delete'):
        dp=f.getvalue('t1')
        rg=f.getvalue('t2')
        url="delete from blogs where headline='"+dp+"' and msg='"+rg+"'"
        x.execute(url)
        con.commit()
        print("Successfully Deleted!")
    elif(jk=='delete_vid'):
        dp=f.getvalue('t1')
        url="delete from video_details where sn='"+dp+"'"
        x.execute(url)
        con.commit()
        print("Successfully Deleted!")
    elif(jk=='searchall'):
        url="select sn,image,headline from blogs order by sn desc limit 6"
        x.execute(url)
        rs=x.fetchall()
        if(rs!=[]):
            for a in rs:
                print('<div class="anm"><img id="sld_img" src="'+a[1].decode()+'" alt=""><br><div id="sp"><span>'+a[2]+'</span><label>'+str(a[0])+'</label></div></div>')
        else:
            a=0
            print(a)
    elif(jk=='searchrec'):
        t1=f.getvalue('t1')
        if(t1=='0'):
            url="select * from blogs order by sn desc limit 5"
            x.execute("select count(sn) from blogs order by sn desc;")
        else:
            url="select * from blogs where sn<"+t1+" order by sn desc limit 5"
            x.execute("select count(sn) from blogs where sn<"+t1+" order by sn desc;")
        rs1=x.fetchall()
        x.execute(url)
        rs=x.fetchall()
        if(rs!=[]):
            kk=0
            for a in rs:
                kk=str(a[0])
                print('<div id="p1"><div id="x"><img src="' + a[3].decode() + '" alt="Blogs Pic" id="img1"></div><div id="y"><p id="topic">' + a[1] + '</p><hr id="hr1"><p id="para">' + a[2] + '</p><input class="custom-btn btn-2" type="button" value="Read More" id="but"><label class="author" for="">Author: ' + a[4] + '</label><label class="Publish" for="">Publish Date: ' +str(a[5]) + '</label><span id="span" hidden>' +str(a[0])+ '</span></div></div><hr>')
            if(rs1[0][0]>5):
                print('<div id="btn"><button><i class="fas fa-chevron-circle-down" style="font-size:2rem;"></i>&nbsp;&nbsp;VIEW MORE</button></div>')
            print(",,,,"+kk)
            # print(len(rs))
            # for k in range(len(rs)):
            #     for i in rs[k]:
            #         print(i,',,,')
            #     print("&:;")
        else:
            a=0
            print(a)
    elif(jk=='searchvideo'):
        url="select distinct topic from video_details"
        x.execute(url)
        rs=x.fetchall()
        url="select topic,url from video_details"
        x.execute(url)
        rs1=x.fetchall()
        if(rs!=[]):
            print('<h1>VIDEO TUTORIALS</h1>')
            for a in rs:
                y=0
                print('<div id="raj"><div class="d1" ><h2><b>'+a[0]+'</b></h2><br><hr><div class="d2">')
                for i in rs1:
                    if a[0] in i[0]:
                        y=y+1
                        print('<div><iframe class="img1" src="'+i[1]+'" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>')
                print('</div></div>')
                if(y>4):
                    print('<button class="button-73" role="button" style="font-size:1.3rem;"><i class="fas fa-chevron-circle-down"></i>&nbsp;&nbsp;VIEW MORE</button></div>')
                else:
                    print('</div>')
        else:
            print("10")
    elif(jk=='blogsn'):
        t1=f.getvalue('t1')
        t2=f.getvalue('t2')
        x.execute("select sn,pub_date,image,headline from blogs where pub_date<='"+t1+"' and sn not in("+t2+") order by sn desc limit 3;")
        rs=x.fetchall()
        if(rs!=[]):
            for a in rs:
                print('<div id="bot_dv"><div id="img1"><img src="'+a[2].decode()+'" alt="" style="width: 100%;height: 100%;"></div><hr><span id="l">'+a[3]+'</span><hr><span id="dt">'+str(a[1])+'</span><span style="color:red;" hidden id="sn">'+str(a[0])+'</span></div>')
        else:
            x.execute("select sn,pub_date,image,headline from blogs where pub_date<=current_date() and sn not in("+t2+") order by sn desc limit 3;")
            rs=x.fetchall()
            if(rs!=[]):
                for a in rs:
                    print('<div id="bot_dv"><div id="img1"><img src="'+a[2].decode()+'" alt="" style="width: 100%;height: 100%;"></div><hr><span id="l">'+a[3]+'</span><hr><span id="dt">'+str(a[1])+'</span><span style="color:red;" hidden id="sn">'+str(a[0])+'</span></div>')
    else:
        sn=f.getvalue('t1')
        x.execute("select * from blogs where sn=%s"%(sn))
        rs=x.fetchall()
        if(rs!=[]):
            for a in rs:
                for i in a:
                    print(i,',,,')
        else:
            a=0
            print(a)
except Exception as e:
    print("Unsuccesss",e)
finally:
    if con.is_connected:
        con.close()
        x.close()
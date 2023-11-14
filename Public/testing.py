# #! C:\Users\sudhanshu\AppData\Local\Programs\Python\Python311\python.exe
# print('content-Type:text/html\r\n\r\n')
# import cgi
# import xlrd
# import mysql.connector
# con=mysql.connector.connect(host="localhost",user="pl",passwd="rays@1324",database="patna")
# t=con.cursor()
# book=xlrd.open_workbook('test.xls')
# sheet=book.sheet_by_name()
# url="insert into test (subject,topic,q,a,o1,o2,o3,o4) values(%s,%s,%s,%s,%s,%s)"
# for i in range(1,sheet.nrows):
#     subject='x'
#     topic='y'
#     q=sheet.cell(i,0).value
#     a=sheet.cell(i,1).value
#     o1=sheet.cell(i,2).value
#     o2=sheet.cell(i,3).value
#     o3=sheet.cell(i,4).value
#     o4=sheet.cell(i,5).value
# val=(subject,topic,q,a,o1,o2,o3,o4)
# t.execute(url,val)
# con.commit()
# print('Done!')
from datetime import date
a=date.today()
x='2023-05-10'
x=x.split('-')
b=date(int(x[0]),int(x[1]),int(x[2]))
c=(b-a).days
print((a-b).days)
# if(b>a):
#     print('hii')
# else:
#     print('huu')
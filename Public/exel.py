#! C:\Users\sudhanshu\AppData\Local\Programs\Python\Python311\python.exe
# print('content-Type:text/html\r\n\r\n')
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="pl",passwd="rays@1324",database="patna")
t=con.cursor()
import xlrd

loc=("test.xls")
l=list()
a=xlrd.open_workbook(loc)
sheet=a.sheet_by_index(0)
# sheet.cell_value(0,0)
url="insert into test (subject,topic,q,a,o1,o2,o3,o4) values(%s,%s,%s,%s,%s,%s,%s,%s)"
for i in range(1,sheet.nrows):
    subject='C'
    topic='Function'
    q=sheet.cell(i,0).value
    a=sheet.cell(i,1).value
    o1=sheet.cell(i,2).value
    o2=sheet.cell(i,3).value
    o3=sheet.cell(i,4).value
    o4=sheet.cell(i,5).value
    val=(subject,topic,q,a,o1,o2,o3,o4)
    l.append(val)
t.executemany(url,l)
con.commit()
print('hello')
# import openpyxl
# loc=("test.xlsx")
# l=list()
# a=openpyxl.load_workbook(loc)
# b=a.active
# c=b.max_row
# url="insert into test (subject,topic,q,a,o1,o2,o3,o4) values(%s,%s,%s,%s,%s,%s,%s,%s)"
# for i in range(1,c+1):
#     subject='C'
#     topic='Function'
#     q=b.cell(row=i,column=1).value
#     a=b.cell(row=i,column=2).value
#     o1=b.cell(row=i,column=3).value
#     o2=b.cell(row=i,column=4).value
#     o3=b.cell(row=i,column=5).value
#     o4=b.cell(row=i,column=6).value
#     val=(subject,topic,q,a,o1,o2,o3,o4)
#     l.append(val)
# t.executemany(url,l)
# con.commit()
# print('Ok')
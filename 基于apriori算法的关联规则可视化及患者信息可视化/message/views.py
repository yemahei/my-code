from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
import os
import csv
import json
from mylib.apriori import apriori
from mylib.loadDataSet import loadDataSet
from mylib.generateRules import generateRules
from mylib.scanD import scanD
# def index(request):
#     return render(request,"index.html")

# Create your views here.
myDat = loadDataSet()
minsupport = 0.5
M, N = apriori(myDat, minsupport)
rules = generateRules(M, N, minConf=0.7)
print(rules)
li = []
li1 = []
li2 = []
li3 = []
li4 = []
print(M)
print(N)
for key in N:
    li3.append(list(key))
    li4.append(N[key])
print(li3)
print(li4)

for i in rules:
    for j in i:
        li2.append(j)

with open('C:/Users/13768/Desktop/information.csv', 'r') as csvfile:
    x = []
    reader = csv.reader(csvfile)
    for row in reader:
        x.append(row)
    x = x[0:len(x)-6]
    print(x)

v = []
for i in x:
    y = i[0:6]
    w = i[6:len(i)]
    sum = w.count('1')
    y.insert(1,sum)
    if sum > 10:
        y.append("严重")
    elif 5 < sum <= 10:
        y.append("中度")
    else:
        y.append("轻度")
    v.append(y)
print(v)
b = v[1:70]
a = v[70:140]
c = v[140:len(v)]

with open('C:/Users/13768/Desktop/information.csv', 'r') as csvfile:
    value = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    value1 = []
    i1 = 0
    q = []
    reader = csv.reader(csvfile)
    q = [row[6:28] for row in reader]
    print(q)
    q1 = q[0]
    q2 = q[1:len(q)]
    for i in q2:
        value[0].append(i[0])
        value[1].append(i[1])
        value[2].append(i[2])
        value[3].append(i[3])
        value[4].append(i[4])
        value[5].append(i[5])
        value[6].append(i[6])
        value[7].append(i[7])
        value[8].append(i[8])
        value[9].append(i[9])
        value[10].append(i[10])
        value[11].append(i[11])
        value[12].append(i[12])
        value[13].append(i[13])
        value[14].append(i[14])
        value[15].append(i[15])
        value[16].append(i[16])
        value[17].append(i[17])
        value[18].append(i[18])
        value[19].append(i[19])
    for q3 in value:
        value1.append((q3.count('1')/217)*100)
    q4 = [{"value":value1[0],"name":q1[0]},{"value":value1[1],"name":q1[1]},{"value":value1[2],"name":q1[2]},{"value":value1[3],"name":q1[3]},{"value":value1[4],"name":q1[4]},{"value":value1[5],"name":q1[5]},{"value":value1[6],"name":q1[6]},{"value":value1[7],"name":q1[7]},{"value":value1[8],"name":q1[8]},{"value":value1[9],"name":q1[9]},{"value":value1[10],"name":q1[10]},{"value":value1[11],"name":q1[11]},{"value":value1[12],"name":q1[12]},{"value":value1[13],"name":q1[14]},{"value":value1[15],"name":q1[15]},{"value":value1[16],"name":q1[16]},{"value":value1[17],"name":q1[17]},{"value":value1[18],"name":q1[18]},{"value":value1[19],"name":q1[19]}]
with open('C:/Users/13768/Desktop/information.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    p = [row[5] for row in reader]
    print(p)
    print(p.count('教师'))












def index(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("excel")  # 获取上传的文件，如果没有文件，则默认为None
        destination = open('F:\mysite\media\myFile.name', 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
    return render(request,"index.html")
def apriori(request):
    return render(request,"apriori.html",{"list1":li2,"list3":N,"list4":M})
def login(request):
    return render(request,"login.html")
def sign(request):
    return render(request,"sign.html")
def index2(request):
    return render(request,"index2.html",{"list7":json.dumps(b),"list8":json.dumps(a),"list9":json.dumps(c),"list10":json.dumps(q1),"list11":json.dumps(q4),"list1":li2,"list12":json.dumps(li3),"list13":json.dumps(li4)})
def js(request):
    return render(request,"js.html",{"list5":json.dumps(li1),"list6":json.dumps(li)})

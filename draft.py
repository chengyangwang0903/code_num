'''from random import *
seed(63)
print("{}.{}".format(randint(1,10),randint(1,10)))
seed(64)
print("{}.{}".format(randint(1,10),randint(1,10)))
seed(65)
print("{}.{}".format(randint(1,10),randint(1,10)))

t=0
while(t!=1):
    try:
        num=eval(input("输入整数："))
        print(pow(num,2))
        t=1
    except:
        print("输入类型错误！")

weight,height=eval(input("请输入你的身高体重："))
BMI=weight/(height**2)
world,china="",""
if BMI<18.5:
    world="偏瘦"
elif 18.5<=BMI<25:
    world="正常"
else:
    world="胖"
if BMI<18.5:
    china="偏瘦"
elif 18.5<=BMI<24:
    china="正常"
else:
    china="胖"
print("国内：{1},国际：{0}".format(world,china))



s=input("请输入一行字符：")
s1,s2,s3,s4=0,0,0,0
for i in s:
    if  i.isalpha():
        s1+=1
    elif i.isdigit():
        s2+=1
    elif i in [" "]:
        s3+=1
    else:
        s4+=1
print("字母：{}，数字：{}，空格：{}，其他：{}".format(s1,s2,s3,s4))

x,y=eval(input("请输入两个整数："))
sum=x*y
while y!=0:
    t=x%y
    x=y
    y=t
print("最大公倍数：",x)
print("最小公约数：",sum//x)

for i in range(1,10):
    print((9-i)*" ",end="")
    n=i
    while n>=1:
        print(n,end="")
        n-=1
    n+=2
    while n<=i:
        print(n,end="")
        n+=1
    print((9 - i) * " ")

from datetime import datetime
s=datetime(2021,8,4,15,31,30)
s.strftime("%Y-%m-%d %H:%M:%S")
s1=datetime.now()
print("现在是{0:%H}：{0:%M}：{0:%S}".format(s1))

from turtle import *
import datetime
def drawGap():
    penup()
    fd(5)
def drawLine(draw):
    drawGap()
    pendown() if draw else penup()
    fd(40)
    right(90)
def drawDigit(d):
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    left(180)
    penup()
    fd(20)
def drawData(data):
    for i in data:
        if i==":":
            write(':',font=("Arial",40,"normal"))
            fd(40)
        elif i==";":
            write(':',font=("Arial",40,"normal"))
            fd(40)
        else:
            drawDigit(int(i))
def main():
    penup()
    fd(-300)
    pensize(5)
    drawData(datetime.datetime.now().strftime('%H:%M;%S'))
    done()
main()

from turtle import *
def koch(size,n):
    if n==0:
        fd(size)
    else:
        for angle in [0,60,-120,60]:
            left(angle)
            koch(size/3,n-1)
def main():
    speed(-10)
    penup()
    goto(-200,100)
    pendown()
    pensize(2)
    koch(400,5)
    right(120)
    koch(400,5)
    right(120)
    koch(400,5)
    done()
main()'''
# a=[4,1,8,9,3,7]
# def my_sort(a):
#     for i in range(len(a)-1):
#         for j in range(i+1,len(a)):
#             if(a[i]>a[j]):
#                 a[i],a[j]=a[j],a[i]
#     print(a)
# my_sort(a)
'''#1
num=1
for i in range(9,0,-1):
    num=(num+1)*2
print("第一天摘了{}个桃子".format(num))
#2
molecular=2
denoinator=1
num=molecular/denoinator
sum=0
for i in range(20):
    sum+=num
    temp=denoinator
    denoinator=molecular
    molecular+=temp
    num=molecular/denoinator
print("该分数序列的前20项之和为：{}".format(sum))
#3
def sum(n):
    if n==1:
        return 1
    return n*sum(n-1)
num=0
for i in range(1,21):
    num+=sum(i)
print("前20项阶乘求和为：{}".format(num))
#4
menu=["土豆","马铃薯","洋芋","洋芋"]
menu=set(menu)
menu=list(menu)
print("菜单：",menu)
#5
str="abc"
def reversal(str):
    str1=""
    for i in range(len(str)-1,-1,-1):
        str1+=str[i]
    return str1
print("str反转后：",reversal(str))
#6
a=[1,2,3,4,5,6]
sum_a=sum(map(lambda x:x+3,a[1::2]))
print("列表中偶数加三在全部相加:",sum_a)
#7
List=[-2,1,3,-6]
for i in range(0,3):
    for j in range(i,4):
        if abs(List[i])>abs(List[j]):
            t=List[i]
            List[i]=List[j]
            List[j]=t
print("按绝对值从小到大排序：",List)
#8
List1=[1,2,3,4]
List2=[5,6,7,8]
for i in range(len(List2)):
    List1.append(List2[i])
print("合并后的列表：",List1)
#9
print("lambda函数是匿名函数，当实现的函数只需要一行时使用，方便简洁。")
#10
print("元组tuple不可变,列表list和字典dict可变。")
#11
alist=[
{'name':'a','age':20},
{'name':'b','age':30},
{'name':'c','age':25}]
for i in range(0,2):
    for j in range(i,3):
        if alist[i]['age']<alist[j]['age']:
            t=alist[i]
            alist[i]=alist[j]
            alist[j]=t
print("alist按age从大到小排序：",alist)
#12
str="k:1|k1:2|k2:3|k3:4"
str_list=str.split('|')
dict={}
for i in str_list:
lambda函数python
设置登录我的关注

    key,value=i.split(':')
    dict[key]=value
print(dict)
#13
n=25
fibonacci=[]
for i in range(n):
    if i==0:
        fibonacci.append(0)
    elif i==1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
print(fibonacci)'''
'''
#读写文件（w+覆盖读写，a+追加读写，二者没有文件就会新建）
import os
path='D:/Data/test01.txt'
file_path,file_name=os.path.split(path)
print(file_path,file_name)
if not os.path.exists(file_path):
    os.makedirs(file_path)
file=open(path,"a+")
file.write("Hello world!")
file.close()
file=open(path,"r")
sentences=file.read()
file.close()
print(sentences)
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("https://tianqi.so.com/weather/101270101").read().decode("utf-8")
print(html)
print("=================================================================================================")
soup=BeautifulSoup(html,features="lxml")
ul_all=soup.find("ul")
print(ul_all)
D:\pythons's's

































































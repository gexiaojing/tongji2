1.
celsius=float(input('Enter a degree in Celsius:'))
fahrenheit=(9/5)*celsius+32
print(celsius,'Celsius is ',fahrenheit,'Fahrenheit')

2.
import math 
radius=float(input('Enter the radius:'))
length=float(input('Enter the length:'))
area=radius*radius*math.pi 
volume=area*length
print('The area is %.4f'%(area))
print('The volume is %.f'%(volume))

3.
feet=eval(input('Enter a value for feet:'))
meters=feet* 0.305
print(feet,'feet is',meters,'meters')

4.
M=float(input('Enter the amount of water in kilograms:'))
initialTemperature=float(input('Enter the initial temperature:'))
finalTemperature=float(input('Enter the final temperature:'))
Q=M*(finalTemperature-initialTemperature)*4184
print('The energy needed is',Q)

5.
balance,interest=eval(input('Enter balance and interest rate (e.g., 3 for 3%):'))
p=balance*(interest/1200)
print('The interest is %.5f'%(p))

6.
v0,v1,t=eval(input('Enter v0,v1,t:'))
a=(v1-v0)/t
print('The average acceleration is', a)

7.
money=eval(input('Enter the monthly saving amount:'))
year=0.05
intreest=0
mouth=year/12
for i in range(6):
    intreest=(money+intreest)*(1+mouth)
    print('After the sixth month,the account value is %.2f'%(intreest))


8.
number=int(input('Enter a number between 0 and 1000:'))
ge=number%10
shi=number/10%10
bai=number/10/10
print('The sum of the didits is',number)

email='1234@163.com'
password=111
    count=0
    for i in range(4):
    email1=input('请输入邮箱：')
    if '@163.com' not in email1:
        print('账号不合法') 
    password1=input('请输入密码：')
    if email1==email and password1=password:
        print("登陆成功")
    else:
        print('账号或密码错误')
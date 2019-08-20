"""
1.
n=1
def getPentagonalNumber(n):
    count=0
    for n in range(1,101):
        n=n*(3*n-1)/2
        print('%d'%n,end=' ')
        count+=1
        if count%10==0:
            print('\n')

getPentagonalNumber(n)    
2.
def sumDigits(n):
    ge=n%10
    shi=n/10%10
    bai=n/10/10%10
    sum=ge+shi+bai
    print('%d'%sum)
def start():
    n=int(input("请输入一个数："))
    sumDigits(n)
start()
3.
def displaySortedNumbers(num1,num2,num3):
    nums=[num1,num2,num3]
    nums.sort()
    print(nums)
def start():
    num1,num2,num3=eval(input("Enter three numbers:"))
    displaySortedNumbers(num1,num2,num3)

start()
4.
def futureInvestmentValue(investmentAmount,yearlyInterestRate):
    month = (float(yearlyInterestRate))/12/100
    print("year",'\t',"Future Value")
    for years in range(1,31):
        futurevalue = investmentAmount*((1+month)**(12*years)) 
        print(years,'\t','%.2f'%futurevalue)
def start():
    investmentAmount = int(input("The amount invested:"))
    yearlyInterestRate = int(input("Annual interest rate:"))
    futureInvestmentValue(investmentAmount,yearlyInterestRate)
start()

5.
def zifu():
ch1=input('>>')
ch2=input('>>')
ord1=ord(ch1)
ord12=ord(ch2)
for i in range(ord1,ord2+1):
a = chr(i)
print(a,end='')
if i%10==0:
print() 
zifu()

#def numberOfDaysInAYear(year):
    year=2010
    for year in range(2010,2020,1):
            if year%400==0 and year%4==0 and year%100!=0:
                    print(year)

7.
def distance(x1,y1,x2,y2):
        juli=((x1-x2)**2+(y1-y2)**2)**1/2
        print('%.2f'%juli)
def start():
        x1,y1=eval(input("请输入x的坐标："))
        x2,y2=eval(input("请输入y的坐标："))
        distance(x1,y1,x2,y2)
start()
"""
class Rectangle(object):
        def __init__(self,width=1,height=2):
                self.width=width
                self.height=height
        def getArea(object):
                return self.width*self.height
        def getPerimeter(object):
                return (self.width+self.height)*2

if __name__=="__main__":
        a.Rectangle()
        


 


"""
4.
def number():
    for i in range(100,1001):
        if i%5 and i%6==0:
            print(i,end=" ")


number()   

7.
res=0
for i in range(1,50001):
        res+=1/i
print(res)

def main(sum):
        sum=0
        for i in range(1,50001):
               sum+=1/i 
        print(sum)
        
main(sum)

def main(sum):
        sum=0
        for i in range(50000,0,-1):
               sum+=1/i 
        print(sum)
        
main(sum)
8.
def number():
        res=0
        for i in range(1,98,2):
                res+=i/(i+2)
        print(res)
number()
9.
def number():
        res=0
        for i in range(1,100000):
                res+=4*((-1)**(i+1)/2*i-1)
        print(res)
number()

10.
for i in range(1,10000):
        res=0
        for j in range(1,i):
                if i%j==0:
                        res+=j
        if i==res:
                print(i)
2.
xf=10000
sum=0
for i in range(1,14):
        money=xf*0.05+xf
        if i==10:
                print(money)
        if i>=10:
                sum+=money
                print(sum)
"""
n=0
while n**3<12000:
        n+=1
        print(n)




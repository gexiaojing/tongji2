1.
class Rectangle(object):
        def __init__(self,width=1,height=2):
                self.width=width
                self.height=height
        def getArea(self):
                return self.width*self.height
        def getPerimeter(self):
                return (self.width+self.height)*2
        def main(self):
                rectangle=Rectangle(4,40)
                print('宽是>>',rectangle.width)
                print('高是>>',rectangle.height)
                print('面积是>>',rectangle.getArea())
                print('周长是>>',rectangle.getPerimeter())
                jx=Rectangle(3.3,35.7)
                print('宽是>>',jx.width)
                print('高是>>',jx.height)
                print('面积是>>',jx.getArea())
                print('周长是>>',jx.getPerimeter())

if __name__=="__main__":
        a=Rectangle()
        a.main()
2.
class Account(object):
        def __init__(self,id_=0,balance=100,annualInterestRate=0):
                self._id =id_
                self._balance=balance
                self._annualInterestRate=annualInterestRate
        @property
        def id(self):
                return self._id
        @id.setter
        def id(self,new_id):
                self._id=new_id
        @property
        def balance(self):
                return self._balance
        @balance.setter
        def balance(self,new_balance):
                self._balance=new_balance
        @property
        def annualInterestRate(self):
                return self._annualInterestRate
        @annualInterestRate.setter
        def annualInterestRate(self,new_annualInterestRate):
                self._annualInterestRate=new_annualInterestRate

        def getMonthlyInterestRate(self):
                return self._annualInterestRate/12/100 
        def getMonthlyInterest(self):
                rate=self.getMonthlyInterestRate()
                res=self._balance * rate
                return res
        def withdraw(self,money):
                if self._balance>=money:
                        self._balance-=money
                        print('您以成功取出:%.2f'% money)
                        print('您的余额为：%.2f'% self._balance)
                else:
                        print('您的余额不足')
                        print('您的余额为:%.2f'% self._balance)
        def deposit(self,money):
                self._balance += money
                print('您以成功存入:%.2f'%money)
                print('您的余额为：%.2f'%self._balance)

if __name__=="__main__":
        account = Account(id_=1122,balance=20000,annualInterestRate=4.5)
        print(account.getMonthlyInterest())
        account.withdraw(3000)
3.
class Fan(object):
        def __init__(self,speed=1,on=False,radius=5,color='blue'):
                self._speed=speed
                self._on=on
                self._radius=radius
                self._color=color
        @property
        def speed(self):
                return self._speed
        @speed.setter
        def speed(self,speed1):
                self._speed=speed1
        @property
        def on(self):
                return self._on
        @on.setter
        def on(self,on1):
                self._on=on1
        @property
        def radius(self):
                return self._radius
        @radius.setter
        def radius(self,radius1):
                self._radius=radius1
        @property
        def color(self):
                return self._color
        @color.setter
        def color(self,color1):
                self._color=color1
        def main(self):
                fei=Fan(3,True,10,'yellow')
                print(fei.speed,fei.on,fei.radius,fei.color)
                san=Fan(2,False,2,'blue')
                print(san.speed,san.on,san.radius,san.color)

if __name__=="__main__":
    a=Fan()
    a.main()
4.
import math
class RegularPolygon(object):
    def __init__(self,n = 3,side = 1,x = 0,y = 0):
        self.n = n
        self.side = side
        self.x = x
        self.y = y
    @property
    def n(self):
        return self._n
    @n.setter
    def n(self, new_n):
        self._n = new_n
    @property
    def side(self):
        return self._side
    @side.setter
    def side(self, new_side):
        self._side = new_side
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, new_x):
        self._x = new_x
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, new_y):
        self._y = new_y
    def getPerimeter(self):
        return self.n * self.side
    def getArea(self):
        return self.n * self.side ** 2 / (4 * math.tan(math.pi / self.n))

if __name__ == "__main__":
    r1 = RegularPolygon()
    print("周长为：",r1.getPerimeter())
    print("面积为：",r1.getArea())

    r2 = RegularPolygon(6,4)
    print("周长为：",r2.getPerimeter())
    print("面积为：",r2.getArea())

    r3 = RegularPolygon(10,4,5.6,7.8) 
    print("周长为：",r3.getPerimeter())
    print("面积为：",r3.getArea())





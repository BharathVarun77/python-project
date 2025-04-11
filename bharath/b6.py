class date:
    def __init__(self,a,b,c,):
        self.d=a
        self.m=b
        self.y=c
    def day(self):
        print("day=",self.d)
    def month(self):
        print("month=",self.m)
    def year(self):
        print("year=",self.y)
    def monthname(self):
        month=["unknown","january","februray","march","aprial","may","june","july","august","september","october","november","December"]
        print("monthname :",month[self.m])
    def isleapyear(self):
        if(self.y%400==0)and(self.y%100==0):
            print("it is a leapyear")
        elif(self.y%4==0)and(self.y%100!=0):
            print("it is a leapyear")
        else:
            print("it is not a leapyear")
d1=date(25,10,2008)
d1.day()
d1.month()
d1.year()
d1.monthname()
d1.isleapyear()
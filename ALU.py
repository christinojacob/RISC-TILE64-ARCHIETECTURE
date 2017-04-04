class ALU:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def add(self):
        self.c=self.a+self.b
        return self.c

    def subtract(self):
        self.c=self.a-self.b
        return self.c

    def multiply(self):
        self.c=self.a*self.b
        return self.c

    def div(self):
        d=[]
        d=divmod(self.a,self.b)
        return d

    def andop(self):
        self.c=(self.a)&(self.b)
        return self.c

    def orop(self):
        self.c=(self.a)|(self.b)
        return self.c

    def xorop(self):
        self.c=(self.a)^(self.b)
        return self.c


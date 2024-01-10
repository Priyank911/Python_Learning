class Cal:
    a=20
    b=30
    def add(self,a,b):
        self.a=Cal.a
        self.b=Cal.b
        c=self.a+self.b
        print(c)
call = Cal()
call.add(Cal.a,Cal.b)

# Program Done by OC (<---Noted--->)

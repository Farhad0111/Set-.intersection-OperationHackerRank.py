class Farhad:
    def __init__(self):
        self.i=int(input())
        self.a=set(input().split())
        self.j=int(int(input()))
        self.b=set(input().split())
class Farhad1(Farhad):
    def Faru(self):
        print(len(self.a.intersection(self.b)))
farhad=Farhad1()
farhad.Faru()
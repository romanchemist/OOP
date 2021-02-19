class W:
    def X(self):
        print('W')

class A(W):
    def X(self):
        print('A')
        super().X()
        # W.X(self)    # TAK NE PRAVIL'NO!!!
class B(W):
    def X(self):
        print('B')
        super().X()
class C(A, B):
    def X(self):
        print('C')
        super().X()
        # super(A, self).X()    # propustit B
        # A.X(self)    # TAK NE PRAVIL'NO!
c = C().X()
print(C.mro())
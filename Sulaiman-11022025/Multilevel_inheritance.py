class Grandfather():
    def f_name(self):
        print("The name of the Grandfather is Micheal")

class Father():
    def m_name(self):
        print("The name of the Father is Joe")

class Child(Grandfather,Father):
    def c_name(self):
        print("The name of the child is Sebastin")

c=Child()
c.f_name()
c.m_name()
c.c_name()
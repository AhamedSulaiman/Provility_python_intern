class Father():
    def f_name(self):
        print("The name of the father is Micheal")

class Mother():
    def m_name(self):
        print("The nam of the mother is Sarah")

class Child(Father,Mother):
    def c_name(self):
        print("The name of the child is Joe")

c=Child()

c.f_name()
c.m_name()
c.c_name()
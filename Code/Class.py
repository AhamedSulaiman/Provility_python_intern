class Mark:
    def __init__(self,sub,diff,marks):
        self.sub=sub
        self.diff=diff
        self.marks=marks
    def display(self):
        print(f"I have got {self.marks} marks in {self.sub} and it is so {self.diff}")

m1=Mark("English","Hard",78)
m2=Mark("Maths","Easy",87)
m1.display()
m2.display()
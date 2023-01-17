class vehicle:
    def __init__(self,num):
        self.num=num
    def display(self):
        if(self.num==2):
            print('The vehicle is a two wheeler')
        elif(self.num ==3):
            print('The vehicle is auto')
        else:
            print('The vehicle is four wheeler')



a=vehicle(2)
a.display()
b=vehicle(4)
b.display()
c=vehicle(3)
c.display()
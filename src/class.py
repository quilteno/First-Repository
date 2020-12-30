def main():
    class Dog:
        native_pace='wangwang' #类属性

        """all dogs are here"""
        def __init__(self,name,age): #  函数定义在类里称为方法
            """
            defalut option
            """
            self.name = name
            self.age = age

        def sit(self):
            """
            simulate dog sit recive order
            """
            print(f"{self.name} is now sitting.")

        def roll_over(self):
            """
            simulate dog rolled order.
            """
            print(f"{self.name} rolled over!")
    class Cat(Dog):
        """init Cat option"""
        def __init__(self,name,age,):
            super().__init__(self,name,age,length)
            self.length = length
""""""""""""""""""""""""""""""""""""""""""""""""""""""
    my_firstdog = Dog('wangcai',6)
    my_nowdog = Dog('juanfu',4)
    print(f"my now dog is age {my_nowdog.age}.")
    my_nowdog.sit()
    my_firstdog.roll_over()





main()
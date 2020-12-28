class Dog:
    native_pace='wangwang' #类属性

    """all dogs are here"""
    def _init_(self,name,age): #  函数定义在类里称为方法
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
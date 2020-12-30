class Pet:
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

        def roll_over(self): #  打滚函数
            """
            simulate dog rolled order.
            """
            print(f"{self.name} rolled over!")
        def update_name(self,fixname):
            self.name = fixname
class Dog(Pet):
    """One of the animals"""
    def __init__(self,name,age):
        """添加了品种"""        
        super().__init__(name,age)
        self.breed = 'Null'
 

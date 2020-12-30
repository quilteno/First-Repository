from Pet import Pet, Dog

def main():
    my_firstdog = Dog('wangcai',6)
    my_nowdog = Dog('juanfu',4)
    my_firstdog.update_name('changwei')
    print(f"my fist dog is age {my_firstdog.age} now.")
    my_nowdog.sit()
    my_firstdog.roll_over()





main()
from pyPS4Controller.controller import Controller
from motors import Motor

Motor_1 = Motor(3, 5)
Motor_2 = Motor(7, 8)

#from ROADENT.App import Motor_1, Motor_2



class MyController(Controller):
    
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press(self):
       print("Forward")
       Motor_1.clockwise()
       Motor_2.clockwise()
       

    def on_up_down_arrow_release(self):
        print("Stop")
        Motor_1.stop()
        Motor_2.stop()
       
    def on_down_arrow_press(self):
        Motor_1.c_clockwise()
        Motor_2.c_clockwise()
        
    def on_right_arrow_press(self):
        print("turn right")
        Motor_2.clockwise()
        Motor_1.c_clockwise()
        
    def on_left_arrow_press(self):
        Motor_1.clockwise()
        Motor_2.c_clockwise()
    
    def on_left_right_arrow_release(self):
        Motor_1.stop()
        Motor_2.stop()


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)

controller.listen(timeout=60)

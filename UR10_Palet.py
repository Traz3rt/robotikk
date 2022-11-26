from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox
RDK = Robolink()
pose = eye()
robot = RDK.Item('UR10')

#Targets
home = RDK.Item('Home')
A_p = RDK.Item('A_P')
P_p = RDK.Item('P_P')
A_Left = RDK.Item('A_Left')
D_Left = RDK.Item('D_Left')
A_Right = RDK.Item('A_Right')
D_Right = RDK.Item('D_Right')

#Kloss
box_height = 50
box_width = 50
#Avstand mellom klosser
XShift = 35
YShift = 35 
ZShift = box_height

#wait time
w_t = 150

x_n = 2
y_n = 2
z_n = 2

def pickup():
    robot.MoveJ(A_p)
    robot.RunInstruction('rq_open()',1)
    robot.Pause(w_t)
    robot.MoveL(P_p)
    robot.RunInstruction('rq_close()',1)
    robot.Pause(w_t)
    robot.MoveL(A_p)

def place_left(x,y,z):
    '''n = number box, z = height of stack'''
    new_A = A_Left.Pose()*transl( (XShift+box_width)*x, (YShift+box_width)*y, -ZShift*z)
    new_D = D_Left.Pose()*transl( (XShift+box_width)*x, (YShift+box_width)*y, -ZShift*z)
    robot.MoveJ(new_A)
    
    robot.MoveL(new_D)
    robot.RunInstruction('rq_open()',1)
    robot.Pause(w_t)
    robot.MoveL(new_A)

def place_right(x,y,z):
    new_A = A_Right.Pose()*transl( -(XShift+box_width)*x, (YShift+box_width)*y, -ZShift*z)
    new_D = D_Right.Pose()*transl( -(XShift+box_width)*x, (YShift+box_width)*y, -ZShift*z)
    robot.MoveJ(new_A)
    
    robot.MoveL(new_D)
    robot.RunInstruction('rq_open()',1)
    robot.Pause(w_t)
    robot.MoveL(new_A)



#Program

robot.MoveJ(home)
robot.RunInstruction('rq_activate_and_wait()',1)

for z in range(z_n):
    for x in range(x_n):
        for y in range(y_n):
            pickup()
            place_right(x,y,z)

for z in range(z_n):
    for x in range(x_n):
        for y in range(y_n):
            pickup()
            place_left(x,y,z)


robot.MoveJ(home)

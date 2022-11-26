
from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox

# Link to RoboDK
sim = Robolink()
math = robomath

robot = sim.Item('H-Bot', ITEM_TYPE_ROBOT)

base = sim.Item('H-Bot Base')
robot.setPoseFrame(base)

def deg2rad(deg):
    return deg* (pi/180)

def rad2deg(rad):
    return rad*(180/pi)

def create_A_Matrix(a_i, alpha, d_i, theta):
    thetaRad = deg2rad(theta)
    alphaRad = deg2rad(alpha)

    matrix = rotz(thetaRad)*transl(0,0,d_i)*transl(a_i,0,0)*rotx(alphaRad)
    return matrix

def Oppgave3():
    thet1 = robot.Joints().list()[0]
    print(thet1)
    thet2 = robot.Joints().list()[1]
    thet3 = robot.Joints().list()[2]
    thet4 = robot.Joints().list()[3]
    thet5 = robot.Joints().list()[4]
    thet6 = robot.Joints().list()[5]

    #a_i , alpha_i, d_i, theta_i
    A1 = create_A_Matrix(0, -90, 285, thet1)
    A2 = create_A_Matrix(700, 0, 0, thet2)
    A3 = create_A_Matrix(0, -90, 0, thet3)
    A4 = create_A_Matrix(0, 90, 650, thet4)
    A5 = create_A_Matrix(0, -90, 0, thet5)
    A6 = create_A_Matrix(0, 0, 170, thet6)

    H03 = A1*A2*A3
    H06 = A4*A5*A6

    H36 = H03*H06

    return H06, H03, H36
    
def IK ():
    return

H06, H03, H36 = Oppgave3()
#print(H36)
#rPose = robot.Pose()
#print("This is robot_obj.pose() matrix\n")
#print(rPose)


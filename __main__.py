from global_status import Globals
from Cloud_Connection import Cloud
from Behaviour import Behaviour
from Robot import Robot


def check_status(globals_ob):
    if(globals_ob.Life==0):
        cloud.make_system_ready()
        robot.wake_up()
    elif(globals_ob.Life==1):
        cloud.connect_to_cloud()
        
def __init__():
    globals_ob=Globals()
    cloud=Cloud()
    behaviour=Behaviour()
    robot=Robot()
    check_status(globals_ob,cloud,robot,behaviour)

    
__init__()

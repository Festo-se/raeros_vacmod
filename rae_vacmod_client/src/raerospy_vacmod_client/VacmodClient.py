import rospy
from rae_vacmod_messages.msg import vacstate
from rae_vacmod_messages.srv import suck, release, warmup

class VacmodClient(object):
    def __init__(self):
        rospy.wait_for_service("/rae_vacmod_server/Suck")
        self.__current_vacstate = None
        rospy.Subscriber("/vacstate", vacstate, self.__vacstate_update_callback)
        self.__suck_handler = rospy.ServiceProxy("/rae_vacmod_server/Suck", suck)
        self.__release_handler = rospy.ServiceProxy("/rae_vacmod_server/Release", release)
        self.__warmup_handler = rospy.ServiceProxy("/rae_vacmod_server/Warmup", warmup)
        self.__sucked_cb = None
        self.__lost_cb = None


    def __vacstate_update_callback(self,data):
        self.__current_vacstate = data.state
        if data.state == "SUCKED" and self.__sucked_cb != None:
            self.__sucked_cb()

        if data.state == "LOST" and self.__lost_cb != None:
            self.__lost_cb()        

    def suck(self, sucked_cb=None,lost_cb=None):
        rospy.loginfo("Vacuum-Module: suck")
        self.__suck_handler()
        
        if sucked_cb:
            self.__sucked_cb = sucked_cb

        if lost_cb:
            self.__lost_cb = lost_cb
            
    
    def release(self):
        rospy.loginfo("Vacuum-Module: release")
        self.__current_vastate = "OFF"
        self.__release_handler()

    def warmup(self):
        rospy.loginfo("Vacuum-module: warmup")
        self.__warmup_handler()

    def actual_state(self):
        return self.__current_vacstate


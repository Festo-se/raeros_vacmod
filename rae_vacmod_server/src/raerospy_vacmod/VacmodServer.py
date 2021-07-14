from raepy import vacmod
import rospy
from rae_vacmod_messages.srv import suck, release
from rae_vacmod_messages.msg import vacstate

class VacmodServer(object):
    def __init__(self):
        rospy.Service("~Suck",suck, self.__suck_service_request)
        rospy.Service("~Release",release, self.__release_service_request)
        self.__statepublisher = rospy.Publisher('vacstate', vacstate, queue_size=10)

    def __suck_service_request(self,req):
        vacmod.suck(self.__sucked_handler,self.__lost_handler)
        #vacmod.suck()
        return True

    def __release_service_request(self,req):
        vacmod.release()
        return True

    def __sucked_handler(self,state):
        #print(state)
        self.__statepublisher.publish("SUCKED")

    def __lost_handler(self,state):
        #print(state)
        self.__statepublisher.publish("LOST")


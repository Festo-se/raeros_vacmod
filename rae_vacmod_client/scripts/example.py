#! /usr/bin/env python3

from raerospy_vacmod_client.VacmodClient import VacmodClient
import time
import rospy
# For callback return of vacuum state
def sucked_cb():
    print("Sucked callback was called")

def lost_cb():
    print("Lost callback was called")


if __name__ == "__main__":

    v = VacmodClient()
    


    while True:
        v.suck(sucked_cb,lost_cb)
        for _ in range(10):
            rospy.loginfo("Polling Vacstate: {}".format(v.actual_state())) # Poll the current state.
            time.sleep(1)

        v.suck()
        time.sleep(5)
        v.release() # Turns Vacuum off to release object


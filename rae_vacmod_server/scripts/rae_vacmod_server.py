#! /usr/bin/env python3

import rospy

from raerospy_vacmod import VacmodServer


if __name__ == "__main__":
    rospy.init_node("vacuum_module_server")
    VacmodServer()

    rospy.spin()
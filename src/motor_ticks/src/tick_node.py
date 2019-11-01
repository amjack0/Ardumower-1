#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16, Int32MultiArray

ticks = []

tick_publisher = rospy.Publisher("motor_ticks", Int32MultiArray, queue_size=10)
def tickcallback(tick):
    global ticks
    ticks.append(tick.data)



def assignticks():
    array = Int32MultiArray()
    global ticks
    rospy.init_node('tick_assign', anonymous=False)
    r = rospy.Rate(10)
    rospy.Subscriber("lwheel", Int16, tickcallback)
    rospy.Subscriber("rwheel", Int16, tickcallback)

    while not rospy.is_shutdown():
        array.data = ticks
        tick_publisher.publish(array)
        ticks = []
        r.sleep()

if __name__ == "__main__":
    assignticks()
    

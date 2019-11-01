#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
rospy.init_node("random_ticks")
lwheel_pub = rospy.Publisher("lwheel", Int16, queue_size=1)
rwheel_pub = rospy.Publisher("rwheel", Int16, queue_size=1)

def random_ticks():
    l, r = 0, 0
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        lwheel_pub.publish(l)
        rwheel_pub.publish(r)
        l += 1
        r += 1
        rate.sleep()
   
if __name__ == "__main__":
    random_ticks()
    

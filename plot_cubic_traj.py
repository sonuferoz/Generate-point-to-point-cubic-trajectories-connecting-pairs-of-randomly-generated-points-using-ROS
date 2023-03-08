#! /usr/bin/env python

import rospy
from ar_week5_test.msg import cubic_traj_coeffs
from std_msgs.msg import Float32

def plot_cubic_traj_callback(coeffs_msg):
    a0, a1, a2, a3=coeffs_msg.a0,coeffs_msg.a1,coeffs_msg.a2,coeffs_msg.a3
    t0=coeffs_msg.t0
    tf=coeffs_msg.tf
    
#position,velocity and acceleration published into 3 different topics
    position_pub=rospy.Publisher('position_trajectory',Float32,queue_size=10)
    velocity_pub=rospy.Publisher('velocity_trajectory',Float32,queue_size=10)
    acceleration_pub=rospy.Publisher('acceleration_trajectory',Float32,queue_size=10)
    
    rate=rospy.Rate(100) #publishing rate of 100Hz
    t=t0
    while t<=tf:
        position=a0+a1*t+a2*t**2+a3*t**3
        velocity=a1+2*a2*t+3*a3*t**2
        acceleration=2*a2+6*a3*t
        position_pub.publish(position)
        velocity_pub.publish(velocity)
        acceleration_pub.publish(acceleration)
        t+=0.01 #increment time of 0.01 secs
        rate.sleep()
        
if __name__=='__main__':
    rospy.init_node('plot_cubic_traj',anonymous=True)
    rospy.Subscriber('cubic_traj_coeffs',cubic_traj_coeffs,plot_cubic_traj_callback)
    rospy.spin()
        

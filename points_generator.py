
#! /usr/bin/env python
import rospy
import random


from ar_week5_test.msg import cubic_traj_params



#Defining constants

p_max=10
p_min=-10
v_max=10
v_min=-10

def param_generator():
    p0=random.uniform(p_min,p_max)
    pf=random.uniform(p_min,p_max)
    v0=random.uniform(v_min,v_max)
    vf=random.uniform(v_min,v_max)
    t0=0.0
    dt=random.uniform(5.0,10.0)
    tf=t0+dt
    return p0,pf,v0,vf,t0,tf
    
def main():
    rospy.init_node('points_generator',anonymous=True)
    pub=rospy.Publisher('cubic_traj_params',cubic_traj_params,queue_size=10)
    rate=rospy.Rate(0.05) #Rate for publishing every 20 secs
    while not rospy.is_shutdown():
        params=cubic_traj_params()
        p0,pf,v0,vf,t0,tf=param_generator()
        params.p0=p0
        params.pf=pf
        params.v0=v0
        params.vf=vf
        params.t0=t0
        params.tf=tf
        pub.publish(params)
        rate.sleep()
        
if __name__=='__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    


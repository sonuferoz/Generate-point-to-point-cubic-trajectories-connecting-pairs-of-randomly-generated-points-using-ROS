#! /usr/bin/env python
import rospy
from ar_week5_test.msg import cubic_traj_params,cubic_traj_coeffs
from ar_week5_test.srv import compute_cubic_traj

p0, pf, v0, vf, t0, tf=None, None, None, None ,None, None
pub_coeffs=None

def callback_params(msg):
    global p0,pf,v0,vf,t0,tf
    p0,pf,v0,vf,t0,tf=msg.p0,msg.pf,msg.v0,msg.vf,msg.t0,msg.tf
    
    
def cubic_traj_planner():
    global pub_coeffs
    rospy.init_node('cubic_traj_planner')
    rospy.Subscriber('cubic_traj_params',cubic_traj_params,callback_params)
    pub_coeffs=rospy.Publisher('cubic_traj_coeffs',cubic_traj_coeffs,
    queue_size=10)
    
    rospy.wait_for_service('compute_cubic_traj')
    compute_traj=rospy.ServiceProxy('compute_cubic_traj',compute_cubic_traj)
    
    r=rospy.Rate(1/20) #20 Hz frequency
    while not rospy.is_shutdown():
        if p0 is not None and pf is not None and v0 is not None and vf is not None and t0 is not None and tf is not None:
        
            resp=compute_traj(p0,pf,v0,vf,t0,tf)
            coeffs_msg=cubic_traj_coeffs()
            coeffs_msg.a0,coeffs_msg.a1,coeffs_msg.a2,coeffs_msg.a3=resp.a0,resp.a1,resp.a2,resp.a3
            coeffs_msg.t0,coeffs_msg.tf=t0,tf
            pub_coeffs.publish(coeffs_msg)
        r.sleep()
        
if __name__=='__main__':
    try:
        cubic_traj_planner()
    except rospy.ROSInterruptException:
        pass

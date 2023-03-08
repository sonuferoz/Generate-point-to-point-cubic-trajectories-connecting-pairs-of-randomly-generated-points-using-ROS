#! /usr/bin/env python

import rospy
from ar_week5_test.srv import compute_cubic_traj
from ar_week5_test.msg import cubic_traj_params,cubic_traj_coeffs

def compute_cubic_coeffs_service(req):
    #Extracting parameters from the service request
    p0=req.p0
    pf=req.pf
    v0=req.v0
    vf=req.vf
    t0=req.t0
    tf=req.tf
    
    #Computing the coefficients
    a0=p0
    a1=v0
    a2=3.0/(tf-t0)**2 * (pf-p0) - 2.0/(tf-t0) * v0 -1.0/(tf-t0) * vf
    a3=-2.0/(tf-t0)**3* (pf-p0) + 1.0/(tf-t0)**2 * (vf+v0)
    
    #Create and return a response message
    resp=compute_cubic_traj()
    resp.a0=a0
    resp.a1=a1
    resp.a2=a2
    resp.a3=a3
    resp.t0=t0
    resp.tf=tf
    
    return resp
    
if __name__=="__main__":
    rospy.init_node('compute_cubic_coeffs')
    #Creating the 'compute_cubic_traj' service
    s=rospy.Service('cubic_cubic_traj',compute_cubic_traj,compute_cubic_coeffs_service)
    #Spinning the node to listen for incoming service requests
    rospy.spin()

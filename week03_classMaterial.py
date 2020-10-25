jtlist = [['ik_shoulder_jnt',[0.0,0.0,0.0]],['ik_elbow_jnt',[-1.0,0.0,2.0]],['ik_wrist_jnt',[0.0,0.0,4.0]],['ik_wristEnd_jnt',[0.0,0.0,6.0]]] #data types inside squared brackets

#python gives item an index number, starts from zero. This applies to nested list.
#nested list is list inside item of a list.

for item in jtlist:
    if item != ['ik_shoulder_jnt',[0.0,0.0,0.0]]: #!=notEqual, ==Equal, <=lessThanOrEqual,>=moreThanOrEqual
        cmds.joint(n=item[0],p=item[1])
    
    
#print the length of 'jtlist'
print len(jtlist) 

#print the index number of range of length in jtlist
for i in range(len(jtlist)):
    print i
    

nums = [0,1,2,3]
for n in nums:
    if n <= 2:
        print n
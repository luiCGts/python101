#creating joint chain and fix orientation
cmds.joint(n='L_leg_JNT', p=[0,10,0])
cmds.joint(n='L_knee_JNT',p=[0,5,2])
cmds.joint('L_leg_JNT', e=True, oj='xzy')
cmds.joint(n='L_ankle_JNT',p=[0,1,0])
cmds.joint('L_knee_JNT', e=True, oj='xzy')
cmds.joint(n='L_ball_JNT',p=[0,-0.5,2])
cmds.joint('L_ankle_JNT', e=True, oj='xzy')
cmds.joint(n='L_toe_JNT',p=[0,-1,4])
cmds.joint('L_ball_JNT', e=True, oj='xzy')
cmds.joint(n='L_toe_end_JNT',p=[0,-1,5])
cmds.joint('L_toe_JNT', e=True, oj='xzy')

cmds.select(cl=1)

cmds.joint(n='L_leg_ik_JNT', p=[0,10,0])
cmds.joint(n='L_knee_ik_JNT',p=[0,5,2])
cmds.joint('L_leg_ik_JNT', e=True, oj='xzy')
cmds.joint(n='L_ankle_ik_JNT',p=[0,1,0])
cmds.joint('L_knee_ik_JNT', e=True, oj='xzy')
cmds.joint(n='L_ball_ik_JNT',p=[0,-0.5,2])
cmds.joint('L_ankle_ik_JNT', e=True, oj='xzy')
cmds.joint(n='L_toe_ik_JNT',p=[0,-1,4])
cmds.joint('L_ball_ik_JNT', e=True, oj='xzy')
cmds.joint(n='L_toe_end_ik_JNT',p=[0,-1,5])
cmds.joint('L_toe_JNT', e=True, oj='xzy')

cmds.delete('L_toe_end_JNT')
cmds.delete('L_toe_end_ik_JNT')

#duplicating ik and fk
#cmds.duplicate('L_leg_JNT')
#cmds.duplicate('L_leg_JNT')

#draw ik for legs
cmds.ikHandle(n='L_leg_ikHandle', sj='L_leg_ik_JNT', ee='L_ankle_ik_JNT', sol='ikRPsolver')
cmds.ikHandle(n='L_ball_ikHandle', sj='L_ankle_ik_JNT', ee='L_ball_ik_JNT', sol='ikSCsolver')
cmds.ikHandle(n='L_toe_ikHandle', sj='L_ball_ik_JNT', ee='L_toe_ik_JNT', sol='ikSCsolver')

#create groups for footroll
footGroups = ('L_footRoll','L_heelRoll','L_toeRoll','L_ballRoll','L_flapRoll')


for item in footGroups:
    cmds.group(n=item,empty=True,world=True)
    
#move groups to respective position
leg_pos=cmds.xform('L_leg_ik_JNT',q=True,ws=True,t=True,r=True)
ankle_pos=cmds.xform('L_ankle_ik_JNT',q=True,ws=True,t=True,r=True)
ball_pos=cmds.xform('L_ball_ik_JNT',q=True,ws=True,t=True,r=True)
toe_pos=cmds.xform('L_toe_ik_JNT',q=True,ws=True,t=True,r=True)

#create control
cmds.circle(nr=(0,1,0),n='L_foot_CTRL')
cmds.group('L_foot_CTRL',n='L_foot_CTRL_NUL')
cmds.xform('L_foot_CTRL_NUL',t=ankle_pos)

cmds.xform('L_toeRoll',ws=True,t=toe_pos,ro=toe_pos)
cmds.xform('L_ballRoll',ws=True,t=ball_pos,ro=ball_pos)
cmds.xform('L_flapRoll',ws=True,t=ball_pos,ro=ball_pos)

cmds.parent('L_heelRoll','L_footRoll')
cmds.parent('L_toeRoll','L_heelRoll')
cmds.parent('L_ballRoll','L_toeRoll')
cmds.parent('L_flapRoll','L_toeRoll')
cmds.parent('L_leg_ikHandle','L_ballRoll')
cmds.parent('L_ball_ikHandle','L_ballRoll')
cmds.parent('L_toe_ikHandle','L_flapRoll')
cmds.parent('L_footRoll','L_foot_CTRL')

#creating no flip knee ---> continue on next tab

#creating no flip knee now
cmds.spaceLocator(n='L_leg_PV_LOC')
legPos=cmds.xform('L_leg_JNT',q=True,ws=True,t=True)
cmds.xform('L_leg_PV_LOC',ws=True,t=legPos)

cmds.poleVectorConstraint('L_leg_PV_LOC','L_leg_ikHandle',weight=1)

cmds.select(cl=1)
cmds.select('L_foot_CTRL')
cmds.addAttr(shortName='Twist',longName='Twist',defaultValue=0,k=True)

cmds.shadingNode('plusMinusAverage',asUtility=True,n='L_pmaNode_legTwist')
cmds.shadingNode('multiplyDivide',asUtility=True,n='L_mdNode_legTwist')

cmds.connectAttr('L_foot_CTRL.Twist','L_mdNode_legTwist.input1X')
cmds.connectAttr('L_foot_CTRL.ry','L_mdNode_legTwist.input1Y')
cmds.connectAttr('L_leg_ik_JNT.ry','L_mdNode_legTwist.input1Z')
cmds.setAttr('L_mdNode_legTwist.input2X',-1)
cmds.setAttr('L_mdNode_legTwist.input2Y',-1)
cmds.setAttr('L_mdNode_legTwist.input2Z',-1)
cmds.connectAttr('L_mdNode_legTwist.input1X','L_pmaNode_legTwist.input1D[0]')
cmds.connectAttr('L_mdNode_legTwist.input1Y','L_pmaNode_legTwist.input1D[1]')
cmds.connectAttr('L_pmaNode_legTwist.output1D','L_leg_ikHandle.twist')

#creating stretchy IK
cmds.shadingNode('addDoubleLinear',asUtility=True,n='L_adlNode_legStretch')
cmds.shadingNode('clamp',asUtility=True,n='L_clampNode_legStretch')
cmds.shadingNode('multiplyDivide',asUtility=True,n='L_mdNode_legStretch')
cmds.shadingNode('multiplyDivide',asUtility=True,n='L_mdNode_kneeStretch')
cmds.shadingNode('multiplyDivide',asUtility=True,n='L_mdNode_ankleStretch')

cmds.select('L_foot_CTRL')
cmds.addAttr(shortName='Stretch',longName='Stretch',defaultValue=0,k=True)


hipPos=cmds.xform('L_leg_JNT',q=True,ws=True,t=True)
anklePos=cmds.xform('L_ankle_ik_JNT',q=True,ws=True,t=True)
cmds.spaceLocator(p=hipPos,n='locator1')
cmds.spaceLocator(p=anklePos,n='locator2')
disDim=cmds.distanceDimension(sp=(hipPos),ep=(anklePos))

cmds.rename('distanceDimension1','L_disDimNode_legStretch')
cmds.rename('locator1','L_legDistance_hip_LOC')
cmds.rename('locator2','L_legDistance_ankle_LOC')
cmds.parent('L_legDistance_hip_LOC','L_leg_ik_JNT')
cmds.parent('L_legDistance_ankle_LOC','L_ankle_ik_JNT')

kneeLen = cmds.getAttr('L_knee_ik_JNT.tx')
print kneeLen
ankleLen = cmds.getAttr('L_ankle_ik_JNT.tx')
print ankleLen
legLen = (kneeLen + ankleLen)
print legLen

cmds.setAttr('L_adlNode_legStretch.input2', legLen)
cmds.setAttr('L_mdNode_legStretch.input2X', legLen)
cmds.setAttr('L_mdNode_kneeStretch.input2X',kneeLen)
cmds.setAttr('L_mdNode_ankleStretch.input2X',ankleLen)

cmds.connectAttr('L_foot_CTRL.Stretch','L_adlNode_legStretch.input1')
cmds.setAttr('L_clampNode_legStretch.minR',9.85730076213)
cmds.setAttr('L_mdNode_legStretch.operation',2)

cmds.connectAttr('L_disDimNode_legStretch.distance','L_clampNode_legStretch.inputR')
cmds.connectAttr('L_adlNode_legStretch.output','L_clampNode_legStretch.maxR')

#connect the distance dimension so we always know the current length of the leg
cmds.connectAttr('L_clampNode_legStretch.outputR','L_mdNode_legStretch.input1X')
cmds.connectAttr('L_mdNode_legStretch.outputX','L_mdNode_kneeStretch.input1X')
cmds.connectAttr('L_mdNode_legStretch.outputX','L_mdNode_ankleStretch.input1X')

cmds.connectAttr('L_mdNode_kneeStretch.outputX','L_knee_ik_JNT.tx')
cmds.connectAttr('L_mdNode_ankleStretch.outputX','L_ankle_ik_JNT.tx')


#creating footroll control
cmds.select('L_foot_CTRL')
cmds.addAttr(shortName='Roll_Break',longName='Roll_Break',defaultValue=0,k=True)
cmds.addAttr(shortName='Foot_Roll',longName='Foot_Roll',defaultValue=0,k=True)

cmds.shadingNode('condition',asUtility=True,n='conNode_ballRoll')
cmds.shadingNode('condition',asUtility=True,n='conNode_negBallRoll')
cmds.shadingNode('condition',asUtility=True,n='conNode_toeRoll')
cmds.shadingNode('plusMinusAverage',asUtility=True,n='pmaNode_ballRoll')
cmds.shadingNode('plusMinusAverage',asUtility=True,n='pmaNode_toeRoll')
cmds.shadingNode('condition',asUtility=True,n='conNode_heelRoll')
cmds.setAttr('pmaNode_toeRoll.operation',2)
cmds.setAttr('conNode_toeRoll.operation',2)
cmds.setAttr('conNode_toeRoll.colorIfFalseR',0)
cmds.setAttr('conNode_toeRoll.colorIfFalseG',0)
cmds.setAttr('conNode_toeRoll.colorIfFalseB',0)
cmds.setAttr('conNode_heelRoll.operation',4)
cmds.setAttr('conNode_heelRoll.colorIfFalseR',0)
cmds.setAttr('conNode_heelRoll.colorIfFalseG',0)
cmds.setAttr('conNode_heelRoll.colorIfFalseB',0)
cmds.setAttr('pmaNode_ballRoll.operation',2)
cmds.setAttr('conNode_negBallRoll.operation',3)
cmds.setAttr('conNode_ballRoll.operation',3)

#setup toe
cmds.connectAttr('L_foot_CTRL.Foot_Roll','conNode_toeRoll.firstTerm')
cmds.connectAttr('L_foot_CTRL.Foot_Roll','conNode_toeRoll.colorIfTrueR')
cmds.connectAttr('L_foot_CTRL.Roll_Break','conNode_toeRoll.secondTerm')
cmds.connectAttr('L_foot_CTRL.Roll_Break','conNode_toeRoll.colorIfFalseR')
cmds.connectAttr('L_foot_CTRL.Roll_Break','pmaNode_toeRoll.input1D[1]')
cmds.connectAttr('conNode_toeRoll.outColorR','pmaNode_toeRoll.input1D[0]')
cmds.connectAttr('pmaNode_toeRoll.output1D','L_toeRoll.rx')

#setup heel
cmds.connectAttr('L_foot_CTRL.Foot_Roll','conNode_heelRoll.firstTerm')
cmds.connectAttr('L_foot_CTRL.Foot_Roll','conNode_heelRoll.colorIfTrueR')
cmds.connectAttr('conNode_heelRoll.outColorR','L_heelRoll.rotateX')

#setup ball
cmds.connectAttr('L_foot_CTRL.Foot_Roll','conNode_ballRoll.firstTerm')
cmds.connectAttr('L_foot_CTRL.Foot_Roll','conNode_ballRoll.colorIfTrueR')
cmds.connectAttr('L_foot_CTRL.Roll_Break','conNode_negBallRoll.secondTerm')
cmds.connectAttr('L_foot_CTRL.Roll_Break','conNode_negBallRoll.colorIfTrueR')
cmds.connectAttr('conNode_negBallRoll.outColorR','pmaNode_ballRoll.input1D[0]')
cmds.connectAttr('L_toeRoll.rx','pmaNode_ballRoll.input1D[1]')
cmds.connectAttr('pmaNode_ballRoll.output1D','L_ballRoll.rx')
cmds.connectAttr('conNode_ballRoll.outColorR','conNode_negBallRoll.firstTerm')
cmds.connectAttr('conNode_ballRoll.outColorR','conNode_negBallRoll.colorIfFalseR')

#make a toe flap
cmds.select('L_foot_CTRL')
cmds.addAttr(shortName='Toe_Flap',longName='Toe_Flap',defaultValue=0,k=True)
cmds.connectAttr('L_foot_CTRL.Toe_Flap','L_flapRoll.rx')

#pivot for bank and twist
cmds.circle(nr=(0,1.5,0),n='ctrl_footPivot')
ballPos=cmds.xform('L_ballRoll',q=True,t=True,ws=True)
cmds.xform('ctrl_footPivot', t=ballPos)

cmds.select(cl=1)


cmds.group(em=True, n='grp_ctrl_footPivot')
cmds.parent('grp_ctrl_footPivot','ctrl_footPivot')
cmds.parent('ctrl_footPivot','L_foot_CTRL')
cmds.makeIdentity(apply=True)

cmds.connectAttr('grp_ctrl_footPivot.translate','L_footRoll.rotatePivot')
cmds.xform('grp_ctrl_footPivot',t=ballPos)

cmds.select('L_foot_CTRL')
cmds.addAttr(shortName='Foot_Pivot',longName='Foot_Pivot',defaultValue=0,k=True)
cmds.addAttr(shortName='Foot_Bank',longName='Foot_Bank',defaultValue=0,k=True)
cmds.connectAttr('L_foot_CTRL.Foot_Pivot','L_footRoll.ry')
cmds.connectAttr('L_foot_CTRL.Foot_Bank','L_footRoll.rz')

cmds.joint(n='shoulder_JNT',p=(0,0,6))
cmds.joint(n='elbow_JNT',p=(-1,0,0))
cmds.joint(n='wrist_JNT',p=(0,0,-6))

cmds.select(cl=True)

cmds.joint(n='shoulder_ik_JNT',p=(0,0,6))
cmds.joint(n='elbow_ik_JNT',p=(-1,0,0))
cmds.joint(n='wrist_ik_JNT',p=(0,0,-6))
cmds.joint(n='wrist_ik_JNT_END',p=(0,0,-8))

cmds.ikHandle(n='arm_ikHandle',sj='shoulder_ik_JNT',ee='wrist_ik_JNT',p=2,w=1)

cmds.select(cl=True)

cmds.joint(n='shoulder_fk_JNT',p=(0,0,6))
cmds.joint(n='elbow_fk_JNT',p=(-1,0,0))
cmds.joint(n='wrist_fk_JNT',p=(0,0,-6))
cmds.joint(n='wrist_fk_JNT_END',p=(0,0,-8))

cmds.select(cl=True)

pos = cmds.xform('wrist_ik_JNT',q=True,t=True,ws=True)
cmds.group(em=True, name='wrist_ik_CTRL_NUL')
cmds.circle(n='wrist_ik_CTRL', nr=(0,0,1),c=(0,0,0))
cmds.parent('wrist_ik_CTRL','wrist_ik_CTRL_NUL')
cmds.xform('wrist_ik_CTRL_NUL', t=pos, ws=True)
cmds.parent('arm_ikHandle', 'wrist_ik_CTRL')

cmds.select(cl=True)

pos = cmds.xform('wrist_fk_JNT',q=True,t=True,ws=True)
cmds.group(em=True, name='wrist_fk_CTRL_NUL')
cmds.circle(n='wrist_fk_CTRL', nr=(0,0,1),c=(0,0,0))
cmds.parent('wrist_fk_CTRL','wrist_fk_CTRL_NUL')
cmds.xform('wrist_fk_CTRL_NUL',t=pos,ws=True)
cmds.parentConstraint('wrist_fk_CTRL', 'wrist_fk_JNT')


cmds.select(cl=True)

pos = cmds.xform('elbow_fk_JNT',q=True,t=True,ws=True)
cmds.group(em=True, name='elbow_fk_CTRL_NUL')
cmds.circle(n='elbow_fk_CTRL', nr=(0,0,1),c=(0,0,0))
cmds.parent('elbow_fk_CTRL','elbow_fk_CTRL_NUL')
cmds.xform('elbow_fk_CTRL_NUL',t=pos,ws=True)
cmds.parentConstraint('elbow_fk_CTRL', 'elbow_fk_JNT')

cmds.select(cl=True)

pos = cmds.xform('shoulder_fk_JNT',q=True,t=True,ws=True)
cmds.group(em=True, name='shoulder_fk_CTRL_NUL')
cmds.circle(n='shoulder_fk_CTRL', nr=(0,0,1),c=(0,0,0))
cmds.parent('shoulder_fk_CTRL','shoulder_fk_CTRL_NUL')
cmds.xform('shoulder_fk_CTRL_NUL',t=pos,ws=True)
cmds.parentConstraint('shoulder_fk_CTRL', 'shoulder_fk_JNT')

cmds.select(cl=True)

cmds.parent('wrist_fk_CTRL_NUL','elbow_fk_CTRL')
cmds.parent('elbow_fk_CTRL_NUL','shoulder_fk_CTRL')

cmds.select(cl=True)

cmds.parentConstraint('elbow_fk_JNT','elbow_ik_JNT','elbow_JNT')
cmds.parentConstraint('wrist_fk_JNT','wrist_ik_JNT','wrist_JNT')
cmds.parentConstraint('shoulder_fk_JNT','shoulder_ik_JNT','shoulder_JNT')

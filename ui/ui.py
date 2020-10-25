import maya.cmds as cmds



print "UI"

def rigarm(*args):
	print "Rig_Arm_is_Cool"


mymenu = cmds.menu('RDojo_Menu',label='LuisGoh',to=True,p='MayaWindow')
cmds.menuItem(label='Rig_arm',p=mymenu,command=rigarm)


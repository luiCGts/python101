import maya.cmds as cmds

print "Startup"

#setting unit measurement at startup


cmds.currentUnit(time='ntsc')

cmds.currentUnit('linear=cm')

import ui.ui as ui #{xx.yy} xx=folder yy=fileName #to initiate UI you need __init__.py in the same folder
reload(ui)
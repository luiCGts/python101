import os
import sys
import maya.cmds as cmds

print "In User Setup"

sys.path.append('/Users/luisgoh/Documents/GitHub/python101/python101/')
cmds.evalDeferred('import startup')
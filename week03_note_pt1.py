import maya.cmds as cmds

cmds.spaceLocator(p=(1,1,1)) #create locators with local position of 1,1,1
cmds.setAttr('locator1.tx',5) #set locator1 translateX attributes to 5
print cmds.getAttr('locator1.t') #get locator1 translate attribute info and print

//////

cmds.joint(n='joint_arm1', p=[0,0,5]) #create joint with name 'joint_arm1', position at 0,0,5

//////

shldrjnt=cmds.joint(n='joint_shoulder',p=[0.0,4.0,0.0])
print shldrjnt

print type(shldrjnt) #print the type of variable(shldrjnt), it printed out as 'unicode' object

print cmds.xform(shldrjnt,q=True,ws=True,t=True)
print cmds.getAttr('%s.jointOrient'%shldrjnt) #%s is string of variable shldrjnt, %shldrjnt is to set %string variable for former command

cmds.delete(shldrjnt)

//////

shldrjnt = cmds.joint(n='joint_shoulder',p=[0.0,4.0,0.0])
elbowjnt = cmds.joint(n='joint_elbow',p=[1.0,4.0,2.0])
wristjnt = cmds.joint(n='joint_wrist',p=[0.0,4.0,4.0])

#to make this a little bicer we will use a list.

#A list = list of items like you would take shopping.#
#To save us some typing we can make a list with all of our joint names in it.#
#In fact, we can make a list of lists so we can have a list for each joint name and position#
#We use square brackets to encapsulate each item in list.#
#That list of lists can even be saved to a variable#

jointinfo = (['joint_upperarm',[0.0,5.0,0.0]],['joint_lowerarm',[1.0,5.0,2.0]],['joint_hand',[0.0,5.0,4.0]])
print jointinfo

#so we have our list, but how do we work with it?
#for this we will call upon the power of loop

cmds.select(d=True)
for item in jointinfo:
    #//print item #print each loop variables in jointinfo
    
    #//print item[0] #print each loop variables of index0 in jointinfo // the index 0 of listed item
    #//print item[1] #print each loop variables of index1 in jointinfo // the index 1 of listem item
    
    cmds.joint(n=item[0],p=item[1]) #this creates joints, with name assigned to listed items index 0, position to listem items index 1
    
//////

#define a list of strings and assign it to the mylist variable.
mylist = ('a','b')
    
#enter a for loop and print each item in my list
for item in mylist:
    
    newvar=[]
    
    newvar.append(item)

print newvar


//////



mylist = ('a','b','c')
print mylist

myotherlist = ('1','2','3')
print myotherlist

mynestedlist = (['a','b','c'],['1','2','3'])
print mynestedlist

myemptylist = []
print myemptylist

##add mylist and myotherlist to myemptylist using append function

myemptylist.append([mylist, myotherlist])
print myemptylist[0][0][0]

///////

#Dictionaries
#declare an empty dictionary
mydictionary = {}

#add items to the dictionary under the key fruit

mydictionary['fruit']=[['apple',[1.0,0.0,0.0]],['orange',[2.0,2.0,2.0]]] #define keyword 'fruit' in a dictionary with values in list
mydictionary['veg']=[['kale',[1.0,1.0,1.0]],['carrot',[2.0,2.0,2.0]]] #define keyword 'veg' in a dictionary with values in list

for key, value in mydictionary.iteritems():
    print (key,value)

#another way to do a loop if you want to target specific index from 2 list        
for i in range(len(mydictionary)):
    print mydictionary['fruit'][i]
    print mydictionary['veg'][i]
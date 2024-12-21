'''
Use this to detect spline in your scene
you gonna have hundreds of keyframe and dozens of shots so its impossible to check...
unless you finally noticed the floaty movement after playblasting
'''

import maya.cmds as do

'this will contain the list of object with keyframe in the scene, ignoring other object without keys'
keyed_obj = []

for obj in do.ls(dag=True):
    if do.keyframe(obj, query=True):
        keyed_obj.append(obj)
        
'all object with keyframe now selected'
do.select(keyed_obj)

'run detector to find which object has spline and deselect any without'
spline_found = False

for obj in keyed_obj:
    checkforSpline = do.keyTangent(obj, query=True, inTangentType=True, outTangentType=True)
    if 'spline' in checkforSpline:
        spline_found = True 
    else:
        do.select(obj, deselect=True)



if spline_found:
    message = "Objects containing spline selected"
else:
    message = "No Spline keyTangent in this scene, congrats"

do.inViewMessage(
    amg=message,
    pos="midCenter",
    fade=True,
    fadeStayTime=1000,
    fadeOutTime=250
)

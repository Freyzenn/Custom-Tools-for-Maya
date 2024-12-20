"""
use this tool to bind a value from attribute channel to a button

"""

import maya.cmds as do

#A. list the attribute and values you want
"""
Below is a def for each button on the layout
insert object name on 'thing.  and  insert attribute name on .shape
remember to use the long names instead of nice names
then you can add any desired value after the ,

"""
def default_shape():
    do.setAttr('thing.shape', 5)

def happy_shape():
    do.setAttr('thing.shape', 4)

def sad_shape():
    do.setAttr('thing.shape', 3)

def o_shape():
    do.setAttr('thing.shape', 2)

def grin_shape():
    do.setAttr('thing.shape', 1)


#prevents tools from cloning everytime it ran
if do.window("myLayoutWindow", exists=True):
    do.deleteUI("myLayoutWindow", window=True)


#delete this if you dont need it, but if you do, this thing will perform actions whenever the tool window is closed
def on_window_close():
    do.setAttr('group2.visibility', 0)


#B. window creation
myLayoutWindow = do.window("myLayoutWindow", title="lipsync panel", closeCommand= on_window_close)

column_layout = do.columnLayout(adjustableColumn=True)
text_element = do.text(label="choose mouthshape", align="center")

do.rowLayout(nc=2)
do.columnLayout(adjustableColumn=True)
do.text(label="Posit/Happy")
do.button(label="3", command="default_shape()")
do.button(label="happy", command="happy_shape()")
do.button(label="grin", command="grin_shape()")
do.setParent("..")

do.rowLayout(nc=2)
do.columnLayout(adjustableColumn=True)
do.text(label="Nega/Sad")
do.button(label="Oo", command="o_shape()")
do.button(label="sadge", command="sad_shape()")
do.setParent("..")

do.showWindow(myLayoutWindow)



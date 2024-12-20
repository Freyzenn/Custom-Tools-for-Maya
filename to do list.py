import maya.cmds as cmds

window = cmds.window('window', width=150)

cmds.columnLayout( adjustableColumn=True )

cmds.checkBox( label='Blink' )
cmds.checkBox( label='Brow' )
cmds.checkBox( label='Eyedart' )
cmds.checkBox( label='Cek EyeDir' )
cmds.checkBox( label='Eyewhite' )
cmds.checkBox( label='animate hair' )

cmds.checkBox( label='check floaty pose' )
cmds.checkBox( label='check fingers' )
cmds.checkBox( label='offset limbs' )

cmds.checkBox( label='check for visual tangent' )
cmds.checkBox( label='Lipsync' )
cmds.checkBox( label='Smooth Poly' )
cmds.checkBox( label='Clipping envi' )

cmds.showWindow( window )
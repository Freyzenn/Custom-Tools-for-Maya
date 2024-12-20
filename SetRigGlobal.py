import maya.cmds as do

# user, please read these half-assed modification guide
# quick setup works by selecting an object, which happens in def check_for_global, and then using def activate_for_global to dial their attribute channel to 10
# to modify this tool for use with other stuff, please check the (#notes) present beside some lines below
# this code only works for global attribute, if you want it to modify other stuff, i think we can add another def below to make it so

class AutoQuickSetup:
    @classmethod
    def check_for_global(cls):
        keywords = [":FKHead_M", ":FKShoulder_R", ":FKShoulder_L"] # you may insert your own keyword here
        matching_objects = do.ls(['*' + k + '*' for k in keywords])
        objects_with_global_attr = [obj for obj in matching_objects if do.attributeQuery('Global', node=obj, exists=True)] # this filters out any object that has the keyword but doesn't have the global on the channel box
        do.select(objects_with_global_attr) # objects are now selected, remember without having the object selected first, the tools won't work
        
    @classmethod
    def activate_for_global(cls):
        selected_objects = do.ls(selection=True)
        for obj in selected_objects:
            do.setAttr(f"{obj}.Global", 10) # this will dial all global on the selected object to 10
            do.cutKey(f"{obj}.Global") # this deletes keyframe so the global stays at 10 and not moving between 10 to 0

AutoQuickSetup.check_for_global()
AutoQuickSetup.activate_for_global()

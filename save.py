from maya import cmds
import os

#'W:/Repository/File-Manager/test.ma'

def save_file(path, name):
    cmds.file( rename = os.path.join(path, name + ".ma"))
    cmds.file( save=True, type='mayaAscii', f=True )
    print("SAVING COMPLETED")

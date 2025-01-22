from maya import cmds
import os

#'W:/Repository/File-Manager/test.ma'

def save_file(path, name, prefix = None):
    if not prefix:
        prefix = "base_"
    cmds.file( rename = os.path.join(path, prefix + name + ".ma"))
    cmds.file( save=True, type='mayaAscii' )
    print("SAVING COMPLETED")

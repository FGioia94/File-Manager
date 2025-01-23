from maya import cmds
import os

def import_file(path):
    cmds.file(path, i = True)
    print("IMPORT COMPLETED")
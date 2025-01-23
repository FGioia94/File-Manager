from maya import cmds
import os

def open_file(path):
    cmds.file(path, o=True, f=True)
    print("OPENING COMPLETED")
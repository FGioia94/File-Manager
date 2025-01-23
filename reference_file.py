from maya import cmds
import os

def reference_file(path, namespace = ""):
    cmds.file(path, reference=True, namespace = namespace)
    print("REFERENCING COMPLETED")


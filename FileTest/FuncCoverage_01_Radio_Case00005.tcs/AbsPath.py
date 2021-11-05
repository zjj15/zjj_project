def getProjectPath() :
    return __file__[:__file__.find("gaea") + len("gaea")]

import sys
if not (getProjectPath() in sys.path) :
    sys.path.append(getProjectPath())
print("init " + __file__)

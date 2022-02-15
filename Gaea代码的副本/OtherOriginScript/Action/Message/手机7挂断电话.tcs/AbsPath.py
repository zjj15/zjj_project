def getGaeaPath() :
    return __file__[:__file__.find("gaea") + len("gaea")]

import sys
if not (getGaeaPath() in sys.path) :
    sys.path.append(getGaeaPath())
print("init " + __file__)

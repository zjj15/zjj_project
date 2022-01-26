from autost.api import *

try:
    assert_exists(Template(os.path.join(ST.LOG_DIR, ST.BT_device_manage)))
except:
    error("BT devices Info Check Error!")

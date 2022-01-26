from autost.api import *

try:
    assert_exists(Template(os.path.join(ST.LOG_DIR, ST.avcommon)))
except:
    error('AVCommon Keep Check Error!')
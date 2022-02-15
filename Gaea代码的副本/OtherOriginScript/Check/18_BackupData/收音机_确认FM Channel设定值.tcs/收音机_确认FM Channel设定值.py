from autost.api import *

try:
    assert_exists(Template(os.path.join(ST.LOG_DIR, ST.current_frenquency)))
except:
    error('FM Channel Check Error!')
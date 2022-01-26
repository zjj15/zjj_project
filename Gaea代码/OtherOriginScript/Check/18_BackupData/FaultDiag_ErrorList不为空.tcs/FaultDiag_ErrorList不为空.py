from autost.api import *

try:
    assert_exists(Template(os.path.join(ST.LOG_DIR, ST.error_list)))
except:
    error('Error List Check Keep Error!')
from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

# judge device name changed success
try:
    assert_exists(Template('../../Design/changed_device_name.png'),device=DEV1,threshold = 0.95)
except:
    error('setting: device name change fail!') 


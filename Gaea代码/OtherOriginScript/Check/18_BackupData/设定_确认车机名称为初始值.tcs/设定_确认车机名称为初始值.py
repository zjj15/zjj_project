from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

# judge device name changed success
try:
    assert_exists(Template('../../../Design/default_device_name.png'),device=DEV1,threshold = 0.9)
except:
    error('check device name default fail!') 

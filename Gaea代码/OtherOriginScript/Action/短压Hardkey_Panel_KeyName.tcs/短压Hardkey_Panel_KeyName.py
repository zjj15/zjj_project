from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
key_name = get_param('keyname')
key_name_lower = key_name.lower()

if 'seek_up' == key_name_lower or 'track_up' == key_name_lower:
    keyevent(WIRECTR_TRACK_UP)
elif 'seek_down' == key_name_lower or 'track_down' == key_name_lower:
    keyevent(WIRECTR_TRACK_DOWN)
elif 'vol_up'== key_name_lower:
    keyevent(WIRECTR_VOL_UP)
 
else:
    error('invalid param')



from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

if exists(Template("../../Design/BTHF_Device_Manager_focus.png"), timeout=1):
    ST.BT_device_manage = 'BT_Device_manage.png'
    snapshot(rect=[220, 298, 168, 303], filename=os.path.join(ST.LOG_DIR, ST.BT_device_manage))
else:
    ST.BT_device_manage = 'BT_Device_manage.png'
    snapshot(rect=[406, 289, 164, 318], filename=os.path.join(ST.LOG_DIR, ST.BT_device_manage))


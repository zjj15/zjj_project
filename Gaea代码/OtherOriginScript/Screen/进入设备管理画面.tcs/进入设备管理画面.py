from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
#In BTAudio View 
if exists(Template('../../Design/BT_device_manage_icon.png'), timeout=2,device=DEV1):
    touch(Template('../../Design/BT_device_manage_icon.png'), timeout=3,device=DEV1)
    try:
        assert_exists(Template('../../Design/BT_setting_selected_icon.png'),device=DEV1)
    except:
        error('Into BT device Manage error!') 
elif exists(Template('../../Design/BTHF_Device_Manager.png'), threshold = 0.95, timeout=1) or exists(Template('../../Design/BTHF_Device_Manager_focus.png'), timeout=1):
        touch_if(Template('../../Design/BTHF_Device_Manager.png'), threshold = 0.95, timeout=1)

ST.BT_device_manage = 'BTHF_Device.png'
snapshot(rect=[204, 333, 200, 280], filename=os.path.join(ST.LOG_DIR, ST.BT_device_manage))
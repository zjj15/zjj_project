from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

# set time setting off
if exists(Template('../../Design/24hour_setting_off_icon.png'), timeout=3,device=DEV1):
    touch_in(Template('../../Design/setting_off_icon.png'),Template('../../Design/24hour_setting_off_icon.png'), device=DEV1)

if exists(Template('../../Design/time_Autoset_setting_on_icon.png'), timeout=3,device=DEV1):
    touch_in(Template('../../Design/setting_on_icon.png'),Template('../../Design/time_Autoset_setting_on_icon.png'), device=DEV1)

# set time to next mintue and next day
touch([899, 532],device=DEV1)
touch([1553, 532],device=DEV1)
for i in range(3):
    if poco('确定', text='确定', timeout=1).exists():
        poco('确定', text='确定', timeout=1).click()
# 获取当前时间
ST.CurrentTime_H = int(poco(pos2=[675, 435]).get_attr('text'))
ST.CurrentTime_M = int(poco(pos2=[854, 435]).get_attr('text'))

# confirm time changed success
ST.changed_time_1 = 'changed_time_1.png'
snapshot(rect=[682, 427, 323, 56], filename=os.path.join(ST.LOG_DIR, ST.changed_time_1), device=DEV1)
ST.changed_time_2 = 'changed_time_2.png'
snapshot(rect=[1143, 427, 539, 67], filename=os.path.join(ST.LOG_DIR, ST.changed_time_2), device=DEV1)

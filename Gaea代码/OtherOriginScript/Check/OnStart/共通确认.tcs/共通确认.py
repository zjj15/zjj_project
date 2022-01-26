from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)
do_segment(Segment('../../../Common/BackHomeView.tcs'))
## 多应用画面,选择'中控设定'卡片进入,画面正常,没有卡顿现象
for i in range(3):
    if poco('关闭', text='关闭', timeout=3).exists():
        touch([1120,207])
    else:
        swipe([1266,43],[1266,650])
    if poco('中控', text='中控', timeout=3).exists():
        break
poco('中控', text='中控', timeout=3).click()
touch_if(Template('../../../Design/ShortBar_Setting_nofocus_noword.png'), timeout=2)
assert_exists(Template('../../../Design/ShortBar_Setting_focus_old_noword.png'), timeout=5)
## 连接bt和wifi确认是否正常
do_segment(Segment('../../../Screen/进入蓝牙设定画面.tcs'))
do_segment(Segment('../../../Action/设定BTSetting为ON.tcs'))
do_segment(Segment('../../../Action/WiFi_网络连接.tcs'))

## 接续usb能正确识别(可通过audio、video或picture机能确认)
do_segment(Segment('../../../Screen/迁移到USB音乐画面.tcs'))
#do_segment(Segment('../../../Action/USB_端口AllOFF.tcs'))
#poco('USB设备未连接', text='USB设备未连接', timeout=3).assert_exists()

## 随意选择hardkey和softkey进行功能确认
# IT-commander
keyevent(ITCMD_MENU)
keyevent(ITCMD_MENU)
do_segment(Segment('../../确认Home画面显示.tcs'))
keyevent(ITCMD_AUDIO)
do_segment(Segment('../../USBA_Check进入音乐画面.tcs'))
sleep(2)

# Preset switch(Integrated switch)
current_screen = snapshot(rect=[900, 138, 250, 350], device=DEV1)
for _ in range(10):
    keyevent(PRESET_SEEK_UP)
    if not exists(current_screen, timeout=2):
        break
else:
    error('HardKey:PRESET_SEEK_UP check error!')
# Steering Switch
current_screen = snapshot(rect=[900, 138, 250, 350], device=DEV1)
for _ in range(10):
    keyevent(WIRECTR_TRACK_UP)
    if not exists(current_screen, timeout=2):
        break
else:
    error('HardKey:PRESET_SEEK_UP check error!')

keyevent(WIRECTR_VOL_DOWN)
sleep(0.5)
vol_down_val = image_to_string([930, 405, 220, 100])
keyevent(WIRECTR_VOL_UP)
sleep(0.5)
vol_up_val = image_to_string([930, 405, 220, 100])
print("vol_down_val: %s,vol_up_val: %s"%(vol_down_val,vol_up_val))
if vol_down_val == vol_up_val:
    error('HardKey:WIRECTR_VOL_UP/DOWN check error!')

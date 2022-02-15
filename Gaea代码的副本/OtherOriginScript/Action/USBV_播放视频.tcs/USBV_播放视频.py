from autost.api import *

touch([607, 34])

touch_if(Template('../../Design/USBVideo_File_Button.png'), timeout=2)

touch([607, 34])

touch_if(Template('../../Design/USBVideo_Pause_Button.png'))

try:
    assert_exists(Template('../../Design/USBVideo_Play_Bar.png'))
except:
    error('USB Video Play Error!')
 
touch([607, 34])

touch(Template('../../Design/USBVideo_Play_Button.png'))

ST.usbvideo_playtime = 'usbvideo_playtime,png'
snapshot(rect=[470, 520, 81, 41], filename=os.path.join(ST.LOG_DIR, ST.usbvideo_playtime))



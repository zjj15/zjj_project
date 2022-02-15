from autost.api import *


# 进入 Pana Diag 画面
# On HOME screen page1 and in Audio off status(not in BT-HF state), 
# press STSW TEL OFF(P42Q press the tel  key) for 3 seconds or more, 
# then press STSW VOL DOWN 6 times.
# Total operation should be finished in 15 seconds.

do_segment(Segment("../../Common/BackHomeView.tcs"))    
touch_if(Template("../../Design/Home_mark_focus.png"), timeout=1, threshold=0.95)
touch_if(Template("../../Design/Home_mark_focus.png"), timeout=1, threshold=0.95)

for i in range(5):
    if not exists(Template("../../Design/Mute.png"), timeout=2):
        keyevent(PRESET_AUDIO)
    else:
        pass


keyevent(WIRECTR_TEL_OFF, duration=5)
for i in range(6):
    keyevent(WIRECTR_VOL_DOWN, delay=0)

assert_exists(Template("../../Design/Panadiag_Display_Setting.png"), threshold=0.95)
from autost.api import *

enterFaultDiagFlag=False

for _  in range(3):
    do_segment(Segment('../../Common/BackHomeView.tcs'))
    touch_if(Template('../../Design/Home_mark_focus.png'), timeout=1, threshold=0.95)
    touch_if(Template('../../Design/Home_mark_focus.png'), timeout=1, threshold=0.95)
    for i in range(5):
        if not exists(Template('../../Design/Mute.png'), timeout=2):
            keyevent(PRESET_AUDIO)
        else:
            pass
    for i in range(3):
        touch([6, 699])
    for i in range(3):
        touch([958, 705])
    for i in range(3):
        touch([1901, 702])
 
    if exists(Template('../../Design/FaultDiag_Screen.png'), timeout=10) or exists(Template('../../Design/FaultDiag_Screen_noT.png'), timeout=10):
        enterFaultDiagFlag=True
        break


if not enterFaultDiagFlag:
    error("IntoFaultDiag Error!")

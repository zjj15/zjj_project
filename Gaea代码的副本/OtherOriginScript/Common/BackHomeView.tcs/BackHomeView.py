from autost.api import *

count = 1
while exists(Template('../../Design/FaultDiag_Back.png'), timeout=1):
    touch_if(Template('../../Design/FaultDiag_Back.png'), timeout=1)
    count+=1
    if count > 5:
        break

try:
    touch([682, 39])
except:
    # 车机重启后,adb还没有连接上设备
    print('error: device "GFEDCBA0987654321" not found')
    sleep(10)

for i in range(5):
    if exists(Template('../../Design/Home_Page1_Bar.png'), timeout=2):
        break
    elif exists(Template('../../Design/加油智慧_仅仅路过btn.png'), timeout=1):
        touch(Template('../../Design/加油智慧_仅仅路过btn.png'), timeout=2)
    elif exists(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1):
         touch(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
    #elif poco('关闭通知', text='关闭通知', timeout=1).exists():
    #    poco('关闭通知', text='关闭通知').click()
    else:
        keyevent(ITCMD_MENU)
        keyevent(ITCMD_MENU)


assert_exists(Template('../../Design/Home_Page1_Bar.png'), timeout=5)
#error('Error:[BackHomeView][step][threshold]')
 

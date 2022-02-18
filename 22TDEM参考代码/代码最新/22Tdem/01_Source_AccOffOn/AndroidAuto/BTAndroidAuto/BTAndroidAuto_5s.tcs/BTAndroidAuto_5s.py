from autost.api import *

DEV1 = ST.DEV1
checkImage = Template('')
errType = 'acc_AndroidAuto_5s_error'

def check(on_sleep):
    if exists(checkImage, threshold=ST.allSource_threshold, timeout=10, device=DEV1):
        pass
    else:
        error(errType)
    sleep(on_sleep)

def playAndroidAuto():
    global checkImage
    touch(Template("pic/菜单按钮.png"), threshold=ST.allSource_threshold)
    touch(Template('pic/AndroidAuto图标.png'), threshold=ST.allSource_threshold, device=DEV1)
    if exists(Template('pic/AA_连接弹框.png'), threshold=ST.allSource_threshold, device=DEV1):
        #touch 配对手机
        touch([471, 438], device=DEV1)
        do_segment(Segment('../AA_BTConnect.tcs'))
        sleep(5)
        if exists(Template('pic/AA_连接成功.png'), threshold=ST.allSource_threshold, device=DEV1):
            print('AA_连接成功')
    else:
        print('AA已连接')
    checkImage = snapshot(rect=ST.eare_devices3, device=DEV1)
    

for i in range(2):
    keyevent(HOME, device=DEV1)
   
playAndroidAuto()
#重置重启睡眠时间
ST.acc_off_sleep_time = ST.acc_off_sleep_start
#重启
do_segment(Segment("../../../common/reStart.tcs"))
#确认复归
check(ST.source_on_sleep_start)

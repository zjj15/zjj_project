from autost.api import *
retryTimes=20

sendCAN(MICU_BCM.C_IG1.phys,1.0, interval=0.1, device=ST.DEV1)
sendCAN(MICU_BCM.C_BACKLTSW.phys,1.0, interval=0.1, device=ST.DEV1)
 
# 判断当前画面是camera正常显示的摄像头画面内容。(有引导线，无引导线)
for i in range(retryTimes):
    if exists(Template("pic/BackCamera_Normal.png"),threshold = ST.backCamera_threshold, timeout = 1, device=ST.DEV2):
        break
    else:
        sleep(1)
 
    if i + 1 == retryTimes:
        error('Rev ON Error')

sendCAN(MICU_BCM.C_BACKLTSW.phys,0.0, interval=0.1, device=ST.DEV1)
 
# 判断camera画面正常退出(没有camera画面，没有camera黑屏画面，前台复归场合，Home key押下可以回到Home)
for i in range(retryTimes):
    if exists(Template("pic/BackCamera_Normal.png"),threshold = ST.backCamera_threshold, timeout = 1, device=ST.DEV2):
        sleep(1)
    elif exists(Template("pic/BackCamera_Black.png"),threshold = ST.backCamera_threshold, timeout = 1, device=ST.DEV1):
        sleep(1)
    else:
        break
 
    if i + 1 == retryTimes:
        error('rev off error')

from autost.api import *

import os
import cv2
import numpy as np

#snapshot_screen = os.path.join(ST.LOG_DIR, "snapshot.png")
#snapshot(rect=[867, 300, 186, 186], filename=snapshot_screen)
#snapshot_pic = snapshot(rect=[867, 300, 186, 186])
#img = cv2.imread(snapshot_screen)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print(np.mean(gray))
try:
    poco('爱奇艺账号登录', text='爱奇艺账号登录', timeout=60).assert_exists()
    poco('打开爱奇艺手机APP扫描二维码登录', text='打开爱奇艺手机APP扫描二维码登录').assert_exists()
finally:
    for _ in range(2):
        if poco('爱奇艺账号登录', text='爱奇艺账号登录', timeout=5).exists():
            do_segment(Segment("../../Action/iQIYI_登录二维码画面close键押下.tcs"))

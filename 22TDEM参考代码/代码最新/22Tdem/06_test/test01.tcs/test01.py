from autost.api import *
DEV1 = ST.DEV1
'''
keyevent(HOME)
def playAM():
    if exists(Template('pic/Tuner未播放.png'), timeout=3, threshold=0.9) or exists(Template('pic/Tuner播放中.png'), timeout=3, threshold=0.9):
        #进入Tuner
        touch([991, 384])
        #不论是不是AM在播放，都点击AM图标让AM播放
        touch([141, 571])
        #确认AM播放中
        assert_exists(Template('pic/AM_ON.png'))
 
snapshot(touch([36, 603])touch([32, 535])touch([183, 537])touch([188, 607]))
32,188,630,535
checkImage = snapshot(rect=ST.eare_tuner, device=DEV1)
 
 snapshot(rect=[76, 556, 66, 33])


#fm1
touch([284, 564])
snapshot(rect=[220, 541, 110, 50])


#fm2
touch([444, 569])
snapshot(rect=[425, 556, 80, 37])
    if exists(Template('pic/Tuner未播放.png'), timeout=3, threshold=0.9) or exists(Template('pic/Tuner播放中.png'), timeout=3, threshold=0.9):
        #进入Tuner
        touch([991, 384])
        #不论是不是FM1在播放，都让AM播放
        touch([284, 564])


checkImage = snapshot(rect=ST.eare_tuner, device=DEV1)



snapshot(rect=[213, 148, 352, 88]
)
[1388, 106, 460, 584]
snapshot(rect=None)
snapshot(rect=[767, 106, 449, 553])
rev_on()
rev_off()
exists(Template('pic/capture_20220218150414973868.png'))

'''
usb_off(2)



















from autost.api import *

ST.DEV1 = '22TDEM:///?stream_method=camera'
ST.DEV2 = '22TDEM:///?stream_method=camera'#如果更换为HDMI方式建议将DEV2修改为HDMI的url
ST.DEV3 = 'Hab21m://127.0.0.1:5037/RQ8MA026H9F'
ST.Phone1_name='Hab21m'


#系统的启动时间，上限值
ST.system_startUp_Time = 60

##截屏匹配区域定义

#tuner
ST.eare_tuner=[271, 168, 75, 71]
#usb audio
ST.eare_devices1=[774, 106, 465, 392]#full of softbar
#bt,ipod
ST.eare_devices2=[450, 588, 386, 83]
#androidauto
ST.eare_devices3=[1011, 612, 229, 87]
#carplay
ST.eare_devices4=[21, 603, 93, 96]
#usb video
ST.eare_usb_video=[13, 635, 1897, 76]


##匹配度
#除camera外所有图片匹配度
ST.allSource_threshold=0.5

#backCamera匹配度
ST.backCamera_threshold = 0.5


############# acc off on 相关默认值设置 #############
#reStart.py：重启休眠时间：acc off~on，调用reStart.py之前需要重置
ST.acc_off_sleep_time = 5

#acc off之后,等待时间起点 
ST.acc_off_sleep_start = 5

#Source播放中，等待时间起点
ST.source_on_sleep_start = 30

#fm1,acc off/on 时间递增起点
ST.fm1 = 0

#fm,2acc off/on 时间递增起点
ST.fm2 = 0

#am,acc off/on 时间递增起点
ST.am = 0
#bt,acc off/on 时间递增起点
ST.bt = 0

#usbAudio,acc off/on 时间递增起点
ST.usbAudio = 0

#usbVideo,acc off/on 时间递增起点
ST.usbVideo = 0

#ipod,acc off/on 时间递增起点
ST.ipod = 0

#ACC Off On case:sleep时间递增case执行完一个时间切片所需次数，acc off[6,35], acc on[31,60]
ST.testTimes = 30 #[2,+]
############# acc off on 相关默认值设置 end #############

############# source切换相关默认值设置 start #############

#任意两个Source切换执行一次的切换次数
ST.touchTimes = 20
############# source切换相关默认值设置 end #############

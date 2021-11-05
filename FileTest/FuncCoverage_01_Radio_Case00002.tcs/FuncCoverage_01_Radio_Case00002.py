from autost.api import *
import AbsPath

from Common.InfraLibAPI import *

readScriptsTable()
#前置条件
#1、短压Hardkey Panel_Audio
keyevent(AUDIO)

#2、等待3秒
sleep(3)



#手顺
#1、在Home画面上点击电台卡片
clickPicture("Home画面", ['电台卡片.png', '电台卡片_2.png'], ignore_bg = True, threshold = 0.95)

#2、在导航栏上点击收音机按钮
clickPicture("导航栏", ['收音机按钮_选中.png', '收音机按钮_非选中_1.png', '收音机按钮_非选中_2.png', '收音机按钮_非选中_3.png'], ignore_bg = True, threshold = 0.95)



#期待结果
#1、在状态栏上确认FM图标是显示状态
assertPicture("状态栏", ['FM图标_选中.png', 'FM图标_非选中.png'], timeout=3)



#复归状态手顺


#确认是否有异常
checkException()

from autost.api import *
import AbsPath

from Common.InfraLibAPI import *

readScriptsTable()
#前置条件
#1、进入FM基本播放画面
transToScreen("FM基本播放画面")

#2、FM调频到98_5频道
doScriptByConditions([["别名", "FM调频到98_5频道"]])



#手顺
#1、进入在线电台画面
transToScreen("在线电台画面")

#2、进入FM基本播放画面
transToScreen("FM基本播放画面")



#期待结果
#1、在状态栏上确认FM图标是显示状态
assertPicture("状态栏", ['FM图标_选中.png', 'FM图标_非选中.png'], timeout=3)

#2、在FM基本播放画面上确认98_5MHZ是显示状态
assertPicture("FM基本播放画面", ['98_5MHZ.png'], timeout=3)



#复归状态手顺


#确认是否有异常
checkException()

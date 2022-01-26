from autost.api import *

if exists(Template('../../Design/OnlineVideo_BitStreamQualit_Off_icon.png'), timeout=2):
    touch([1479, 546])
elif exists(Template('../../Design/OnlineVideo_BitStreamQualit_On_icon.png'), timeout=2):
    touch([1438, 540])
else:
    error('iQIYI_拖动进度条至快结束:不在视频播放状态')


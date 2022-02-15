from autost.api import *


if exists(Template('../../Design/OnlineVideo_VIP视频试看6分钟提示.png'), timeout=10,threshold = 0.88) or exists(Template('../../Design/OnlineVideo_VIP视频提示登录.png'), timeout=10,threshold = 0.88):
    pass
else:
    error('iQIYI_试看6分钟提示 error')

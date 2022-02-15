from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'


weatherList = ["爆表","良","其它","轻度","严重","优","中度","重度"]

poco('空气质量').exists()
weatherQuality = poco(pos2 = [1235, 401]).get_attr('name')

if weatherQuality in weatherList:
    pass
else:
    error('wrong weather quality')

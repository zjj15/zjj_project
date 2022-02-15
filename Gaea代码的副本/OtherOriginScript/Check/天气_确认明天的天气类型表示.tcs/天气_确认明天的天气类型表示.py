from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'


weatherList = ["晴","多云","阴","阵雨","雷阵雨","雷阵雨伴有冰雹","雨夹雪","小雨","中雨","大雨","暴雨","小雪","中雪","大雪","暴雪","雾","沙尘暴","浮尘","扬沙","霾","冰粒","少云","尘卷风","雷暴"]

weatherQuality = poco(pos2 = [1420, 237]).get_attr('name')

if weatherQuality in weatherList:
    pass
else:
    error('wrong tomorrow weather type')

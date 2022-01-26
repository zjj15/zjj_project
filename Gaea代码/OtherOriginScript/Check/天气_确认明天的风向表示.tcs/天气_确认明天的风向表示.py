from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'


weatherList = ["北风","东北风","东风","东南风","南风","微风","西北风","西风","西南风","旋转风"]

poco(pos2 = [1420, 272]).exists()
wind = poco(pos2 = [1420, 272]).get_attr('text')

if (wind.split(' ', 1)[0]) in weatherList:
    print(wind.split(' ', 1)[0])
    pass
else:
    error('wrong wind display')

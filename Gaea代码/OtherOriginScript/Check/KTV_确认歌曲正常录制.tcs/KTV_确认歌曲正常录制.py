from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

print('__脚本名称: ' + __file__)

poco('com.changba.sd:id/playing_background', pos2=[1539, 150]).click()

poco('正在录音', text='正在录音',pos2=[579, 534]).exists()



from autost.api import *
DEV1 = ST.DEV1

do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/Radio_Card.png'), [1788, 332], DIR_LEFT, device=DEV1)

touch(Template('../../Design/Radio_Card.png'), device=DEV1)
try:
    #poco('智行电台', text='智行电台', timeout=4).click()
    poco('android.widget.ImageView', pos=(0.0390625, 0.3972222222222222)).click()
except:
    touch_if(Template('../../Design/Radio_Nissan_button.png'), timeout =2,threshold = 0.9)
    touch_if(Template('../../Design/Radio_ximalaya_button.png'), timeout =2,threshold = 0.9)
sleep(5)
## 日产电台
if poco(text='允许喜马拉雅访问您设备上的照片、媒体内容和文件吗？').exists():
    poco(text='允许').click()
    poco(text='允许').click()
    poco(text='允许').click()
touch_if(Template('../../Design/Radio_Nissan_同意条款.png'), timeout =3,threshold = 0.88)
touch_if(Template('../../Design/Radio_Nissan_开始使用.png'), timeout =1,threshold = 0.88)
## 喜马拉雅 20210608
if poco('取消登录', text='取消登录', timeout=3).exists():
    poco('取消登录', text='取消登录').click()
if poco('同意并不再提醒', text='同意并不再提醒', timeout=3).exists():
    poco('同意并不再提醒', text='同意并不再提醒').click()

## check
## 日产电台
if exists(Template('../../Design/Radio_Nissan_button_focus.png'), timeout=2):
    pass
## 喜马拉雅 20210608
elif exists(Template('../../Design/Radio_ximalaya_button_focus.png')):
    pass
else:
    error('IntoNissanRadio Error!')

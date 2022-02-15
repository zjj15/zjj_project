from autost.api import *

try:    
    if exists(Template('../../Design/个人中心_登录失败tips.png'), threshold=0.95, timeout=5):
        pass
    else:
        poco(text='登录').assert_exists()
except:
    error(__file__+' error')
finally:
    if poco('android.widget.ImageView',pos2=[1526, 441], timeout=2).exists():
        poco('android.widget.ImageView',pos2=[1526, 441]).click()
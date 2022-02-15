from autost.api import *

while exists(Template('../../Design/AudioBooks_back_icon.png'), timeout=3, threshold=0.93):
    touch_if(Template('../../Design/AudioBooks_back_icon.png'), timeout=3, threshold=0.93)

touch_if(Template('../../Design/AudioBooks_search_cancel_button.png'),timeout=3)
poco('我的', text='我的').click()
poco('下载', text='下载').click()
if poco('正在下载', text='正在下载').exists():
    poco('正在下载', text='正在下载').click()
    poco('全部删除', text='全部删除').click()
    touch_if(Template('../../Design/AudioBooks_back_icon.png'), timeout=3, threshold=0.93)
#touch_if(Template('../../Design/AudioBooks_search_result_xianni.png'), timeout=3, threshold=0.93)
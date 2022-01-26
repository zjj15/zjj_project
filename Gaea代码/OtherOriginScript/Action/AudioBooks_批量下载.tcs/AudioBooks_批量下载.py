from autost.api import *

if not exists(Template('../../Design/AudioBooks_下载btn.png')):
    print('该书没有下载功能')
    pass
else:
    poco(name='批量下载', pos2=[1038, 199]).click()
    poco(name='确定', pos2=[794, 499]).click()

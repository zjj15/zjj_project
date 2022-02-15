from autost.api import * 

print('__脚本名称: ' + __file__)

if exists(Template('../../Design/Statusbar_Navi_1.png'), timeout=1, threshold=0.90):
    pass
elif exists(Template('../../Design/Statusbar_Navi_2.png'), timeout=1, threshold=0.90):
    pass
else:
    keyevent(ITCMD_MENU)
    keyevent(ITCMD_MENU)
    poco('GPS定位中…', text='GPS定位中…').click()
    sleep(2)


if exists(Template('../../Design/Navi_naving_km.png'), threshold=0.88) or exists(Template('../../Design/Navi_naving_m.png'), threshold=0.88):
    pass
elif exists(Template('../../Design/Navi_naving_后_夜.png'), threshold=0.88) or exists(Template('../../Design/Navi_naving_后.png'), threshold=0.88):
    pass
else:
    error('NAVI_确认导航中画面 Check Error!')

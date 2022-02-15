from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
for _ in range(10):
    flick([238, 667], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)
    touch_if(Template('../../../../CoverageTest/FuncCoverage/18_BackupData/Design/otherSetting_icon.png'), timeout=2,device=DEV1)
    touch_if(Template('../../../../CoverageTest/FuncCoverage/18_BackupData/Design/otherSetting_English_icon.png'), timeout=2,device=DEV1)
    if (exists(Template('../../../../CoverageTest/FuncCoverage/18_BackupData/Design/otherSetting_selected_English_icon.png'), timeout=2,device=DEV1)) or exists(Template('../../../../CoverageTest/FuncCoverage/18_BackupData/Design/otherSetting_selected_icon.png'),device=DEV1, timeout=2):
        break
else:
    error('IntoOtherSetting error!')

flick([1026, 214], DIR_DOWN, step=1, speed=SPEED_NORMAL,device=DEV1)

if(exists(Template('../../../../CoverageTest/FuncCoverage/18_BackupData/Design/languageSetting_icon.png'),device=DEV1, timeout=2))or (assert_exists(Template('../../../../CoverageTest/FuncCoverage/18_BackupData/Design/languageSetting_English_icon.png'), timeout=2,device=DEV1)):
    pass
else:
    error('IntoLanguageSetting error!')

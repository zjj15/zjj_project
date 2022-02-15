from autost.api import *

count = 1
while exists(Template('../../Design/FaultDiag_Back.png'), timeout=2):
    touch_if(Template('../../Design/FaultDiag_Back.png'), timeout=2)
    count+=1
    if count > 5:
        break

touch([682, 39])
for i in range(5):
    if not exists(Template('../../Design/Home_science_theme_Page1_Bar.png'), timeout=2):
        keyevent(ITCMD_MENU)
        keyevent(ITCMD_MENU)
    else:
        break

assert_exists(Template('../../Design/Home_science_theme_Page1_Bar.png'), timeout=2)
#error('Error:[BackHomeView][step][threshold]')
 

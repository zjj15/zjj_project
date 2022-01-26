from autost.api import *
touch_if(Template("../../Design/OnlineVideo_Login_cancel.png"), timeout=1)
if exists(Template('../../Design/OnlineVideo_Resolution_Standard.png'), timeout=2):
    pass
else:
    if exists(Template('../../Design/OnlineVideo_Resolution_720P.png'), timeout=2):
        touch(Template('../../Design/OnlineVideo_Resolution_720P.png'))
    elif exists(Template('../../Design/OnlineVideo_Resolution_High.png'), timeout=2):
        touch(Template('../../Design/OnlineVideo_Resolution_High.png'))
    
    touch_in(Template('../../Design/OnlineVideo_ResScreen_Check.png'), Template('../../Design/OnlineVideo_ResScreen_Standard.png'))
    
sleep(5)
try:
    assert_exists(Template('../../Design/OnlineVideo_Resolution_Standard.png'))
except:
    error('OnlineVideo Resolution Setup Standard Error!')

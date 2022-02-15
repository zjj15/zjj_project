from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
touch_if(Template('../../Design/OnlineVideo_PlayScreen_return.png'),timeout=1, threshold=0.95)
touch_if(Template('../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=3)
#确认video type：推荐/VIP特选/电视剧/综艺/电影/动漫/儿童
if poco(text='推荐').exists():
    poco(text='推荐').click()
poco('com.iauto.onlinevideo:id/ChannelRecommendTitleList').assert_exists()
assert_exists(Template('../../Design/OnlineVideo_recommend_list.png'))

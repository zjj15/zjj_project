from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
touch_if(Template("../../Design/OnlineVideo_Login_cancel.png"), timeout=1)
key_name = get_param('tabname')
if key_name:
    key_name_lower = key_name
else:
    key_name_lower = ''

try:
    assert True == poco(key_name_lower, text=key_name_lower).get_attr('selected')
    if '推荐' == key_name_lower:
        poco('com.iauto.onlinevideo:id/ChannelRecommendList').assert_exists()
    elif 'VIP专区' == key_name_lower:
        poco('com.iauto.onlinevideo:id/ChannelVIPList').assert_exists()
    elif '电视剧' == key_name_lower:
        poco('com.iauto.onlinevideo:id/ChannelTVList').assert_exists()
    elif '综艺' == key_name_lower:
        poco('com.iauto.onlinevideo:id/ChannelVarietyList').assert_exists()
    elif '电影' == key_name_lower:
        poco('com.iauto.onlinevideo:id/ChannelMovieList').assert_exists()
    elif '动漫' == key_name_lower:
        poco('com.iauto.onlinevideo:id/ChannelAnimeList').assert_exists()
    elif '少儿' == key_name_lower:
        poco('com.iauto.onlinevideo:id/ChannelChildPagerList').assert_exists()
    else:
        error('invalid param')    
except:
    error('Tab：%s check error'%key_name)

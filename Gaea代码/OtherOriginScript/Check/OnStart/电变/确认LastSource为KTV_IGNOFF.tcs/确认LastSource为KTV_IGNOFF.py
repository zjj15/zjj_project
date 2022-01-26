from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

# case suffix: 0007, 0008, 0009
try:
    assert_exists(Template('../../../../Design/statusbar_ktv.png'), threshold=0.90, device=DEV1)
    assert_exists(Template("../../../../Design/KTV_playing_btn.png"), threshold=0.90, device=DEV1)
    poco('为了您的驾驶安全，请勿在车辆行驶过程中K歌。', text='为了您的驾驶安全，请勿在车辆行驶过程中K歌。', timeout=2).assert_not_exists()
    poco('安全提示', text='安全提示', timeout=2).assert_not_exists()
except:
    error('__脚本名称: ' + __file__+ 'Check error')

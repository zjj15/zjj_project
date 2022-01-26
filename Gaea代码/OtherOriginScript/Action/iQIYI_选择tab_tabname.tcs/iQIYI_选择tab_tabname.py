from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

touch_if(Template('../../Design/OnlineVideo_PlayScreen_return.png'), timeout=1)
sleep(1)
for i in range(5):
    if poco('加载中', text='加载中', timeout=1).exists():
        sleep(2)
    else:
        break

snp_cur_screen = snapshot(rect=[231, 281, 1400, 360])
key_name = get_param('tabname')
print('key_name: ',key_name)
has_been_selected = False
if key_name:
    has_been_selected = poco(key_name, text=key_name).get_attr('selected')
else:
    error('invalid param')

if not has_been_selected:
    poco(key_name, text=key_name).click()
    for i in range(5):
        if poco('加载中', text='加载中', timeout=1).exists():
            sleep(2)
        else:
            break
    assert_not_exists(snp_cur_screen, timeout=3)
else:
    assert_exists(snp_cur_screen, timeout=3)

for i in range(3):
    if exists(Template('../../Design/OnlineVideo_加载失败提示.png'),threshold = 0.95, timeout = 1):
        touch([454, 437])
        sleep(5)
    else:
        break

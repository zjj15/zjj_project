from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

if poco('我的收藏', text='我的收藏', timeout=1.5).exists():
    pass
else:
    for _ in range(3):
        if poco('我的收藏', text='我的收藏', timeout=1.5).exists():
            break
        else:
            touch_if(Template("../../Design/OnlineVideo_return_icon.png"), timeout=2, device=DEV1)
            touch_if(Template("../../Design/OnlineVideo_Center.png"), timeout=2, device=DEV1)

poco('我的收藏', text='我的收藏').click()

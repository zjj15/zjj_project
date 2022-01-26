from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'


touch_if(Template('../../Design/OnlineVideo_return_icon.png'), timeout=2, device=DEV1)
touch(Template('../../Design/OnlineVideo_InputBox_Srch.png'), threshold=0.92, timeout=2, device=DEV1)


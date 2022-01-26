from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

# favorite onlinevideo
for _ in range(2):
    touch_if(Template('../../Design/onlinevideo_not_favorite_icon.png'), timeout=2, device=DEV1)
    sleep(1)
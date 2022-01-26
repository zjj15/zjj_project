from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
touch_if(Template("../../Design/OnlineVideo_Login_cancel.png"), timeout=1)
touch([483, 497],device=DEV1)
try:
    wait_for_appearance(Template('../../Design/OnlineVideo_Playing_icon.png'), timeout=30,device=DEV1)
except:
    error('OnlineVideo display fail!')


# favorite onlinevideo
sleep(2)
touch_if(Template('../../Design/onlinevideo_not_favorite_icon.png'),device=DEV1)
sleep(2)
touch(Template('../../Design/OnlineVideo_return_icon.png'),device=DEV1)

# enter onlinevideo myfavorite
touch(Template('../../Design/OnlineVideo_Center.png'),device=DEV1)
touch_if(Template('../../Design/onlinevideo_my_favorite_not_select_icon.png'), timeout=3,device=DEV1)

ST.OnlineVideo_favourite = 'OnlineVideo_favourite.png'
snapshot(rect=[216, 270, 716, 319], filename=os.path.join(ST.LOG_DIR, ST.OnlineVideo_favourite), device=DEV1)

from autost.api import *

touch(Template("../../../Design/iPodScreen_ListButton.png"))

touch_if(Template("../../../Design/iPodList_Playlist_nofocus.png"), timeout=3)

touch(Template("../../../Design/iPodPlayList_ListButton.png"))

try:
    assert_exists(Template('../../../Design/iPodList_PlayList_empty.png'))
except:
    error('iPod Play List Check I Error!')
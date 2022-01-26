from autost.api import *

touch(Template('../../Design/iPodScreen_ListButton.png'))

touch_if(Template('../../Design/iPodList_Playlist_nofocus.png'), timeout=3)

touch(Template('../../Design/iPodPlayList_ListButton.png'))

ST.ipod_playlist = 'ipod_playlist.png'
snapshot(rect=[387, 213, 954, 498], filename=os.path.join(ST.LOG_DIR, ST.ipod_playlist))


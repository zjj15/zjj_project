from autost.api import *

if poco('音乐', text='音乐', timeout=2).exists():
    do_segment(Segment('../../Common/BackHomeView.tcs'))

cur_song_name = poco(className='android.widget.TextView', pos2=[540, 406] ).get_attr('text')
cur_song_artist = poco(className='android.widget.TextView', pos2=[540, 362] ).get_attr('text')

if cur_song_name == '' or cur_song_artist=='':
    error('expect song info is Null！！！')
else:
    print('cur_song_name: '+cur_song_name)
    print('cur_song_artist: '+cur_song_artist)

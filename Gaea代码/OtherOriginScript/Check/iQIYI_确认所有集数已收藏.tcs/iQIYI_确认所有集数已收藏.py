from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

tar_poco = poco(className='android.widget.TextView', pos2=[1600, 214]).get_attr('text')
print(tar_poco)
list_series_num = tar_poco.split('-')
print(list_series_num)

for num in range(int(list_series_num[1])):
    cur_series = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
    if num == 0:
        first_series = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
    elif cur_series == first_series:
        break
    else:
        print('first_series:%s, cur_series:%s'%(first_series,cur_series))
    do_segment(Segment('../../Action/iQIYI_播放下一个视频.tcs'))
    if exists(Template('../../Design/onlinevideo_favorite_icon.png'),device=DEV1):
        continue
    else:
        print('first_series:%s, cur_series:%s'%(first_series,cur_series))
        error(__file__+' error')

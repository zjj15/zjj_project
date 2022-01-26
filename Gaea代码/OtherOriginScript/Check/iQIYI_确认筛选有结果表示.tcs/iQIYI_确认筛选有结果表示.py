from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'GAEA_Camera:///'
print('__脚本名称: ' + __file__)

tab_name = get_param('tabname')
print('tab_name: %s,'%(tab_name))

tv_filter_list = ['排序', '专区', '地区', '类型', '年代']
varity_filter_list = ['排序', '专区', '地区', '类型', '年代']
movie_filter_list = ['排序', '专区', '地区', '类型', '规格' ,'年代']
animation_filter_list = ['排序', '专区', '地区', '版本', '风格']
children_filter_list = ['排序', '专区', '语种', '年龄段', '类型' ,'地区']

dict_tab_filter_list ={
"电视剧":tv_filter_list,
"综艺":varity_filter_list,
"电影":movie_filter_list,
"动漫":animation_filter_list,
"少儿":children_filter_list
}

check_list = dict_tab_filter_list[tab_name]
len_check_list = len(check_list)

for k in check_list:
    if poco(k, text=k, timeout=1.5).exists():
        continue
    else:
        swipe([270,570],[270,330])
        sleep(1)
        poco(k, text=k, timeout=1.5).assert_exists()

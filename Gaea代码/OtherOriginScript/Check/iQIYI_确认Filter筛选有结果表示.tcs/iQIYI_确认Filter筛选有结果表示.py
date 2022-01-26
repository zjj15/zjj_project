from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'GAEA_Camera:///'
print('__脚本名称: ' + __file__)


num_filter_conditon = get_param('filternum')
print('filternum:%s'%(num_filter_conditon))

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

tv_dict_filter_item = {
"排序":["最近热播","最近更新"],
"专区":["全部","4K","1080P","VIP"],
"地区":["全部","内地","香港","韩国"],
"类型":["全部","自制","古装","言情"],
"年代":["全部","2021","2020","2019"]
}

varity_dict_filter_item = {
"排序":["最近热播","最近更新"],
"专区":["全部","4K","VIP","免费"],
"地区":["全部","内地","港台","日韩"],
"类型":["全部"," 播报"," 访谈"," 搞笑"],
"年代":["全部","2020","2019","2018"]
}

movie_dict_filter_item = {
"排序":["最近热播","最近更新"],
"专区":["全部","4K","1080P","VIP"],
"地区":["全部","华语","香港","美国"],
"类型":["全部","喜剧","爱情","动作"],
"规格":["全部","巨制","院线","独播"],
"年代":["全部","2021","2020","2019"]
}

animation_dict_filter_item = {
"排序":["最近热播","最近更新"],
"专区":["全部","VIP","免费"],
"地区":["全部","国漫","日漫","韩国"],
"版本":["全部","动画","特摄","布袋戏"],
"风格":["全部","搞笑","热血","催泪"],
}

children_dict_filter_item =  {
"排序":["最近热播","最近更新"],
"专区":["全部","VIP","免费"],
"语种":["全部","英语","普通话","日语"],
"年龄段":["0-3岁","4-6岁","7-10岁"],
"类型":["全部","电影","有声绘本","儿童"],
"地区":["全部","欧美","大陆","港台"]
}

snp_cur_screen = snapshot(rect=[771, 281, 1050, 360])
filter_list_from_tabName = None
item_list_to_filter_from_tabName = None
if poco('电视剧', text='电视剧', selected=True, timeout=2).exists():
    filter_list_from_tabName = dict_tab_filter_list["电视剧"]
    item_list_to_filter_from_tabName = tv_dict_filter_item
elif poco('综艺', text='综艺', selected=True, timeout=2).exists():
    filter_list_from_tabName = dict_tab_filter_list["综艺"]
    item_list_to_filter_from_tabName = varity_dict_filter_item
elif poco('电影', text='电影', selected=True, timeout=2).exists():
    filter_list_from_tabName = dict_tab_filter_list["电影"]
    item_list_to_filter_from_tabName = movie_dict_filter_item
elif poco('动漫', text='动漫', selected=True, timeout=2).exists():
    filter_list_from_tabName = dict_tab_filter_list["动漫"]
    item_list_to_filter_from_tabName = animation_dict_filter_item
elif poco('少儿', text='少儿', selected=True, timeout=2).exists():
    filter_list_from_tabName = dict_tab_filter_list["少儿"]
    item_list_to_filter_from_tabName = children_dict_filter_item
else:
    print('tab_to_filter is None!')


if num_filter_conditon:
    for num in range(num_filter_conditon):
        cur_filter = filter_list_from_tabName[num]
        item_to_filter = item_list_to_filter_from_tabName[cur_filter]
        text_to_filter = item_to_filter[1]
        if 5 == num:
            swipe([270,570],[270,330])
            sleep(1)
        if 5 > num:
            swipe([270,570],[270,630])
            sleep(1)
        isSelected= poco(className='android.widget.TextView', text=text_to_filter, package='com.iauto.onlinevideo').get_attr('selected')
        poco(text=text_to_filter, package='com.iauto.onlinevideo').click()
        if isSelected == True:
            text_to_filter = item_to_filter[0]
            print('isSelected1:', text_to_filter)
            poco(text=text_to_filter, package='com.iauto.onlinevideo').click()
        else:
            print('isSelected2:', text_to_filter)
            poco(text=text_to_filter, package='com.iauto.onlinevideo').click()
    sleep(10)
else:
    error('unknown situation')

if num_filter_conditon is None:
    pass
else:
    assert_not_exists(snp_cur_screen)

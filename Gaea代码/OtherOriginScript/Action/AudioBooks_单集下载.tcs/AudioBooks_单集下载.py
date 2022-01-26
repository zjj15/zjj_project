from autost.api import *
#点击的位置有问题，点击了删除
#需要修改AudioBooks_下载btn

#poco(className='android.widget.ImageView', pos2=[1170, 464] ).click()
if not exists(Template('../../Design/AudioBooks_下载btn.png')):
    print('该书没有下载功能')
    pass
touch_if(Template('../../Design/AudioBooks_下载btn.png'), timeout=3)



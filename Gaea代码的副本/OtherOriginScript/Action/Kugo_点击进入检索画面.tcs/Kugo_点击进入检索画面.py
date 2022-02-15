from autost.api import *

#搜索画面
if poco('com.kugou.android.auto:id/arg', className='android.widget.EditText').exists():
    poco(text='取消').click()
#搜索按钮存在则点击
if poco('com.kugou.android.auto:id/arg', pos=(0.15520833333333334, 0.24583333333333332), index=2).exists():
    poco('com.kugou.android.auto:id/arg', pos=(0.15520833333333334, 0.24583333333333332), index=2).click()
else:
    #点击列表
    touch_if(Template('../../Design/Kugo_return_button.png'), timeout=3)
    #点击列表
    if poco('com.kugou.android.auto:id/arg', pos=(0.10833333333333334, 0.24583333333333332)).exists():
        poco('com.kugou.android.auto:id/arg', pos=(0.10833333333333334, 0.24583333333333332)).click()
    #点击返回按钮
    if poco('com.kugou.android.auto:id/arg', pos=(0.15520833333333334, 0.24583333333333332), index=1).exists():
        poco('com.kugou.android.auto:id/arg', pos=(0.15520833333333334, 0.24583333333333332), index=1).click()
    poco('com.kugou.android.auto:id/arg', pos=(0.15520833333333334, 0.24583333333333332)).click()


touch(Template('../../Design/Kugo_Input_box.png'))

try:
    assert_exists(Template('../../Design/IME_BTPhone_keyboard_icon.png'))
except:
    error('KTV enter search screen Error!')

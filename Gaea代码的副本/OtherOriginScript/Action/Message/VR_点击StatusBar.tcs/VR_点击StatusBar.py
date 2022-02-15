from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'


#do_segment(Segment('../../Common/BackHomeView.tcs'))
touch(Template('../../../Design/statusBar_VR_icon.png'),device=DEV1)

#try:
#    assert_exists(Template('../../../../Design/VR_title.png'),device=DEV1,timeout=3)
#except:
#    error('VR：open error !')

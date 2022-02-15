from autost.api import *

touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)

do_segment(Segment('../../Action/iQIYI_选择tab_tabname.tcs'), tabname='推荐')

do_segment(Segment('../iQIYI_确认VIP角标表示.tcs'))
do_segment(Segment('../iQIYI_确认自制角标表示.tcs'))
do_segment(Segment('../iQIYI_确认独播角标表示.tcs'))


from autost.api import *

do_segment(Segment('../../Common/BackHomeView_science_Theme.tcs'))

try:
    assert_exists(Template('../../Design/Home_science_theme_Page1_Bar.png'),timeout=5)
    assert_exists(Template('../../Design/Home_science_theme_Music_Card.png'),timeout=5)
except:
    error('not science theme')
from autost.api import *

try:
    assert_exists(Template('../../Design/Home_Page1_Bar.png'),timeout=5)
    assert_exists(Template('../../Design/Music_Card.png'),timeout=5)
except:
    error('not default theme')


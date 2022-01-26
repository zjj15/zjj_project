from autost.api import *

try:
    assert_exists(Template('../../Design/OnlineVideo_Card.png'))
except:
    error('OnlineVideo Card Check!')

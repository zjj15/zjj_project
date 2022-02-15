from autost.api import *

sleep(10)

try:
   assert_exists(Template('../../../Design/Home_OnlineMusic_Play.png'))
except:
    error('Online Music Card Check Error!')
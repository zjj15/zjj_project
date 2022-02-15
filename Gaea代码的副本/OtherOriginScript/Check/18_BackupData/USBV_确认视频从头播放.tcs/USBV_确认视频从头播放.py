from autost.api import *

touch([607, 34])

touch_if(Template("../../../Design/USBVideo_File_Button.png"), timeout=2)

try:
    assert_exists(Template('pic/capture_20210208174311959763.png'))
except:
    error('USB Video Play Time init Check Error!')
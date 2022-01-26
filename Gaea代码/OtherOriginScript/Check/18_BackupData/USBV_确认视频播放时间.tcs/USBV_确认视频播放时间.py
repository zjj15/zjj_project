from autost.api import *

touch([607, 34])

try:
    assert_exists(Template(os.path.join(ST.LOG_DIR, ST.ST.usbvideo_playtime)))
except:
    error('USB Video Play Time Keep Check Error!')
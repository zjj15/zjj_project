from autost.api import *

try:
    assert_exists(Template(os.path.join(ST.LOG_DIR, ST.usbaudio_playinfo)))
except:
    error('USB Audio Play Info Keep Check Error!')
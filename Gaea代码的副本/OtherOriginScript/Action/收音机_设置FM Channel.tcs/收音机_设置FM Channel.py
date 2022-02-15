from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'


touch(Template('../../Design/radio_add_frenquency_button.png'), timeout=3,device=DEV1)
ST.current_frenquency = 'current_frenquency.png'
snapshot(rect=[810, 223, 373, 95], filename=os.path.join(ST.LOG_DIR, ST.current_frenquency))
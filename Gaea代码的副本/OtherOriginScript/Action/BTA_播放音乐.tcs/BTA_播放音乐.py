from autost.api import *

for i in range(3):
    touch_if(Template('../../Design/USBAudio_PauseButton.png'), timeout=2)
    if exists(Template('../../Design/USBAudio_PlayBar.png'), timeout=2):
        break
else:
    error('BTAudio Play Error!s')